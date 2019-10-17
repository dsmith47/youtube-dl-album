from mutagen.easyid3 import EasyID3
import os
import sys
import time

dir_name = "output/"

def file_last_edit(file_name):
  return os.path.getctime(os.path.join(dir_name, file_name))

ARTIST = sys.argv[1]
ALBUM = sys.argv[2]
DISCNUM = sys.argv[3]
GENRE = sys.argv[4]
DATE = sys.argv[5][-4:]

file_names = sorted(os.listdir(dir_name), key=file_last_edit)

DIR_SIZE = len(file_names)
index = 1

for file_name in file_names:
  pathname = os.path.join(dir_name, file_name)
  if not os.path.isfile(pathname): continue

  metatag = EasyID3(pathname)
  metatag['title'] = file_name[:-4] # File Name sans path extension
                                    # TODO: replace with a regex
                                    # procssing out the last 
                                    # .-delimited characters (in case
                                    # it is non-existent or not 3
                                    # chars long)
  metatag['artist'] = ARTIST
  metatag['album'] = ALBUM
  metatag['albumartist'] = ARTIST
  metatag['discnumber'] = DISCNUM
  metatag['genre'] = GENRE
  metatag['date'] = DATE
  metatag['tracknumber'] = str(index) + "/" + str(DIR_SIZE)

  metatag.save()
  print(metatag)
  time.sleep(1)
  index += 1
