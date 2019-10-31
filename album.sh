ARTIST=""
ALBUM=""
DISCNUM=""
GENRE=""
DATE=""
URL=""
REGEX=""

while [[ $# -gt 0 ]]; do
  key=$1
  case $key in
    --artist)
      ARTIST="$2"
      shift
      shift
    ;;
    --album)
      ALBUM="$2"
      shift
      shift
    ;;
    --disc)
      DISCNUM="$2"
      shift
      shift
    ;;
    --genre)
      GENRE="$2"
      shift
      shift
    ;;
    --date)
      DATE="$2"
      shift
      shift
    ;;
    --url)
      URL="$2"
      shift
      shift
    ;;
    --regex)
      REGEX="$2"
      shift
      shift
    ;;
  esac
done

if [ -z "$ARTIST" ]; then
  read -p "[METADATA] Enter Artist Name: " ARTIST
fi	

if [ -z "$ALBUM" ]; then
  read -p "[METADATA] Enter Album Name: " ALBUM
fi	

if [ -z "$DISCNUM" ]; then
  read -p "[METADATA] Enter Disc Index (\$number/\$total): " DISCNUM 
fi	

if [ -z "$GENRE" ]; then
  read -p "[METADATA] Enter the Genre to sort album under: " GENRE
fi	

if [ -z "$DATE" ]; then
  read -p "[METADATA] Enter Album Release Date: " DATE
fi	

if [ -z "$URL" ]; then
  read -p "[METADATA] Enter Playlist URL: " URL
fi	

youtube-dl \
  --ignore-errors \
  --extract-audio \
  --audio-format mp3 \
  -o "output/%(title)s.%(ext)s" \
  "$URL"

python3 metadata.py3 \
  "$ARTIST" \
  "$ALBUM" \
  "$DISCNUM" \
  "$DATE" \
  "$GENRE" \
  "$REGEX"
