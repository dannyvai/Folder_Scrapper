PICTURE_EXT = \
[
    'jpeg',
    'jpg',
    'jpe',
    'jif',
    'jfif',
    'jfi',
    'gif',
    'png'
]

MUSIC_EXT = \
[
    'mp3',
    'wav',
    'ogg',
    'midi'
]


def is_picture(file_ext):
    return file_ext.lower() in PICTURE_EXT

def is_music(file_ext):
    return file_ext.lower() in MUSIC_EXT
 
def is_mp3(file_ext):
    return file_ext.lower() == 'mp3'
