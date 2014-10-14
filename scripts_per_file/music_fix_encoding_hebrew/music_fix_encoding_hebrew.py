#MP3 tag reader
import eyeD3
import file_ext_util


def from_gibrish_to_hebrew_fix(string):
    
    if string is None or len(string) == 0:
          return (None)
      
    if ord(string[0]) < 128: #english
		return (string)
    if ord(string[0]) < 255: #gibrish
           return (string.encode('cp1252').decode('cp1255',errors='replace'))
	#if ord(str[0]) > 256 : #unicode already


def foreach_file_do(filepath,filename,file_ext):
    print filepath
    if file_ext_util.is_mp3(file_ext):
         tag = eyeD3.Tag()
         tag.link(filepath)

         if tag is not None:

             artist_name = from_gibrish_to_hebrew_fix(tag.getArtist())
             if artist_name and  artist_name != tag.getArtist() : 
                 #TODO fix this

                 print artist_name.encode('utf-8')
                 print map(ord,list(artist_name.encode('utf-8')))
                 tag.setArtist(artist_name.encode('utf-8'))
                 tag.update()
                 
             
             if artist_name is not None:
                 album_name = from_gibrish_to_hebrew_fix(tag.getAlbum())
                 if album_name is None:
                     album_name = ""
                 if album_name != tag.getAlbum() :
                     #TODO fix this                     
                     print album_name
                     tag.setAlbum(album_name)
                     tag.update()