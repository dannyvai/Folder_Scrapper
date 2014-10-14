#MP3 tag reader
import eyeD3
import shutil

def foreach_file_do(filepath,filename,file_ext):
    print filepath
    return

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