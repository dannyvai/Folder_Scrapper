
picture_extentions = ['jpeg','jpg','gif','png']

music_extentions = ['mp3','wav','ogg','midi']


def is_picture(file_ext):
	return file_ext in picture_extentions

def is_music(file_ext):
	return file_ext in music_extentions