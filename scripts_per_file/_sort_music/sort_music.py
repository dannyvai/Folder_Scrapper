#MP3 tag reader
import os
import eyeD3
import shutil

import file_ext_util
import util

def foreach_file_do(filepath,filename,file_ext,private_data):
    print filepath
    return private_data

    if file_ext_util.is_mp3(file_ext):
        tag = eyeD3.Tag()
        tag.link(filepath)

        if tag is not None:
            artist_name = util.from_gibrish_to_hebrew_fix(tag.getArtist())
            if artist_name and  artist_name != tag.getArtist():
                pass
             
            if artist_name is not None:
                album_name = util.from_gibrish_to_hebrew_fix(tag.getAlbum())
                if album_name is None:
                    album_name = ""
                artist_folder = base_music_folder+"/"+artist_name
                album_folder = artist_folder + "/" + album_name
                if not os.path.exists(artist_folder):
                    os.makedirs(album_folder)
                if not os.path.exists(album_folder):
                    os.makedirs(album_folder)
                shutil.copy(filepath,album_folder.encode('utf-8'))
    return private_data
