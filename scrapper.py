import os 
import sys # argv
import urllib2
import re
import time #sleep

import file_ext_util
import face_detect.face_detect


#########################
#	Util		#
#########################
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def print_dict(d):
	for val in d:
		print isinstance(val,dict)
		if isinstance(val,dict):
			print_dict(val)
		else :
			for key in d.keys():
				print key,d[key]

#########################
#	Helpers		#
#########################

def foreach_file_do(filepath,filename,file_ext):
	
	if file_ext_util.is_picture(file_ext):
		if face_detect.face_detect.find_faces(filepath) :
			print filepath

def scan_folder(folder_path,n_dirs,n_files,file_ext_dict):
	for filename in os.listdir(folder_path): 
		filepath = folder_path +"/" + filename
		if os.path.isdir(filepath):
			#print "Dir name :: " + filename
			n_dirs,n_files,file_exts = scan_folder(filepath,n_dirs,n_files,file_ext_dict)
			n_dirs = n_dirs + 1
		else :
			#print "Raw filename :: " + filename
			name_parts = filename.split('.')
			file_ext = name_parts[-1]

			if file_ext_dict.has_key(file_ext):
				file_ext_dict[file_ext]['n_files'] = file_ext_dict[file_ext]['n_files'] + 1
				file_ext_dict[file_ext]['total_size'] = file_ext_dict[file_ext]['total_size'] + os.path.getsize(filepath)
			else:
				file_ext_dict[file_ext] = {'n_files': 1,'total_size':os.path.getsize(filepath) }
			n_files = n_files + 1

			foreach_file_do(filepath,filename,file_ext)

	return n_dirs,n_files,file_ext_dict


#########################
#	main		#
#########################
def main(argv):
	if len(sys.argv) < 2 :
		sys.stderr.write('Usage: sys.argv[0]  folder \n')
		exit(-1)

	file_dict = {}	
	search_path = sys.argv[1]

	if not os.path.exists(search_path) :
		sys.stderr.write('Error sys.argv[1] doesn\'t exist ')
	
	file_ext_dict = {}

	n_dirs,n_files,file_ext_dict = scan_folder(search_path,0,0,file_ext_dict)
	print "Number of Dirs : ",n_dirs
	print "Number of Files : " ,n_files
	#print_dict(file_ext_dict)
	#print file_ext_dict


if __name__ == "__main__":
   main(sys.argv[1:])