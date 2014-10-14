#Picture face reco
import face_detect
import file_ext_util

debug = False

def foreach_file_do(filepath,filename,file_ext):
	global debug
	if file_ext_util.is_picture(file_ext):
		if face_detect.face_detect.find_faces(filepath,debug) :
			print filepath