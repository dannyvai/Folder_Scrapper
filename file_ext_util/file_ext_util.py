
picture_extentions = ['jpeg','jpg','jpe','jif','jfif','jfi','gif','png']

music_extentions = ['mp3','wav','ogg','midi']


def is_picture(file_ext):
	return file_ext in picture_extentions

def is_music(file_ext):
	return file_ext in music_extentions
 
def is_mp3(file_ext):
    return file_ext == "mp3"