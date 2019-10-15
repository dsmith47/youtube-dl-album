from mutagen.easyid3 import EasyID3
import os
import sys

dir_name = "output/"
ARTIST = sys.argv[1]
ALBUM = sys.argv[2]
DISCNUM = sys.argv[3]
#TRACKNUM = sys.argv[4]
GENRE = sys.argv[4]
DATE = sys.argv[5]

for file_name in os.listdir(dir_name):
  pathname = os.path.join(dir_name, file_name)
  if not os.path.isfile(pathname): continue

  metatag = EasyID3(pathname)
  metatag['artist'] = ARTIST
  metatag['album'] = ALBUM
  metatag['albumartist'] = ARTIST
  metatag['discnumber'] = DISCNUM
  #metatag'tracknumber'] = TRACKNUM
  metatag['genre'] = GENRE
  metatag['date'] = DATE

  metatag.save()
  print(metatag)
