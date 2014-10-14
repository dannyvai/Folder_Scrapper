import os 
import sys # argv
import file_ext_util

#Picture face recog
import face_detect.face_detect

#MP3 tag reader
import eyeD3
import shutil

debug = True

base_folder = "./tmp"
base_music_folder = base_folder + "/music"

locale_fixes_count = 0
#########################
#	Util		#
#########################
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def from_gibrish_to_hebrew_fix(string):
    global locale_fixes_count
    
    if string is None or len(string) == 0:
          return (None)
      
    if ord(string[0]) < 128: #english
		return (string)
    if ord(string[0]) < 255: #gibrish
           locale_fixes_count = locale_fixes_count + 1
           return (string.encode('cp1252').decode('cp1255',errors='replace'))
	#if ord(str[0]) > 256 : #unicode already

#########################
#	Helpers	       #
#########################

def foreach_file_do(filepath,filename,file_ext):
    global debug,base_music_folder
 
#	if file_ext_util.is_picture(file_ext):
#		if face_detect.face_detect.find_faces(filepath,debug) :
#			print filepath
 

    if file_ext_util.is_mp3(file_ext):
         tag = eyeD3.Tag()
         tag.link(filepath)

         if tag is not None:

             artist_name = from_gibrish_to_hebrew_fix(tag.getArtist())
             if artist_name and  artist_name != tag.getArtist() : 
                 #TODO fix this
                 #print artist_name
                 #tag.setArtist(artist_name.encode('utf-8'))
                 #tag.update()
                 pass
             
             if artist_name is not None:
                 album_name = from_gibrish_to_hebrew_fix(tag.getAlbum())
                 if album_name is None:
                     album_name = ""
                 if album_name != tag.getAlbum() :
                     #TODO fix this                     
                     #print album_name
                     #tag.setAlbum(album_name)
                     #tag.update()
                     pass
                 artist_folder = base_music_folder+"/"+artist_name
                 album_folder = base_music_folder+"/"+artist_name + "/" + album_name
                 if not os.path.exists(artist_folder):
                     os.makedirs(album_folder)
                 if not os.path.exists(album_folder):
                     os.makedirs(album_folder)
                 #print album_folder
                 #print map(ord,album_folder)
                 #print filepath
                 shutil.copy(filepath,album_folder.encode('utf-8'))
                 
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
	print "Locale fixes : " ,locale_fixes_count

if __name__ == "__main__":
   main(sys.argv[1:])