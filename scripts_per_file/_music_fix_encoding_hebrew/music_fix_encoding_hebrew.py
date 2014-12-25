#MP3 tag reader

import eyeD3

import file_ext_util
import util

DEBUG = False

def print_debug(string):
    global debug
    if DEBUG:
        print string

def foreach_file_do(filepath, filename, file_ext,private_data):
    print_debug(filepath)
    if file_ext_util.is_mp3(file_ext):
        tag = eyeD3.Tag()
        tag.link(filepath)

        if tag is not None:

            artist_name = util.from_gibrish_to_hebrew_fix(tag.getArtist())
            if artist_name and  artist_name != tag.getArtist():
                 #TODO fix this

                print_debug(artist_name.encode('utf-8'))
                print_debug(map(ord, list(artist_name.encode('utf-8'))))
                tag.setArtist(artist_name.encode('utf-8'))
                tag.update()


            if artist_name is not None:
                album_name = util.from_gibrish_to_hebrew_fix(tag.getAlbum())
                if album_name is None:
                    album_name = ""
                if album_name != tag.getAlbum():
                    #TODO fix this                     
                    print_debug(album_name)
                    tag.setAlbum(album_name)
                    tag.update()
    return private_data