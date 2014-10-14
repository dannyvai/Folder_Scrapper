import os 
import sys # argv

debug = True

#TODO add to config
base_folder = "/home/ubuser/tmp"
base_music_folder = base_folder + "/music"

sys.path.insert(1,os.getcwd()+"/scripts_per_file")
sys.path.insert(1,os.getcwd()+"/")

#########################
#	Util		#
#########################
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


#########################
#	Helpers	       #
#########################

def foreach_file_do(filepath,filename,file_ext):
    global debug,base_music_folder
        
    for script_filename in os.listdir(os.getcwd()+'/scripts_per_file'):
        if script_filename[0] != '_' :
            exec('import %s'  % script_filename)
            eval(script_filename+'.foreach_file_do("%s","%s","%s")'%(filepath,filename,file_ext))
    
def scan_folder(folder_path,n_dirs,n_files,file_ext_dict):

	for filename in os.listdir(folder_path): 
		filepath = folder_path +"/" + filename

           #Directory
		if os.path.isdir(filepath):
			n_dirs,n_files,file_exts = scan_folder(filepath,n_dirs,n_files,file_ext_dict)

			n_dirs = n_dirs + 1
           #File
		else :

			name_parts = filename.split('.')
			file_ext = name_parts[-1]

			foreach_file_do(filepath,filename,file_ext)

               
			if file_ext_dict.has_key(file_ext):
				file_ext_dict[file_ext]['n_files'] = file_ext_dict[file_ext]['n_files'] + 1
				file_ext_dict[file_ext]['total_size'] = file_ext_dict[file_ext]['total_size'] + os.path.getsize(filepath)
                #new extension
			else:
				file_ext_dict[file_ext] = {'n_files': 1,'total_size':os.path.getsize(filepath) }

			n_files = n_files + 1

	return n_dirs,n_files,file_ext_dict


#########################
#	main		       #
#########################
def main(argv):

	if len(sys.argv) < 2 :
		sys.stderr.write('Usage: sys.argv[0]  folder \n')
		exit(-1)


	search_path = sys.argv[1]
	if not os.path.exists(search_path) :
		sys.stderr.write('Error sys.argv[1] doesn\'t exist ')
	
 
	file_ext_dict = {}
	n_dirs,n_files,file_ext_dict = scan_folder(search_path,0,0,file_ext_dict)
 
	print "Number of Dirs : ",n_dirs
	print "Number of Files : " ,n_files

if __name__ == "__main__":
   main(sys.argv[1:])