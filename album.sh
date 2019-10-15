youtube-dl \
  --ignore-errors \
  --extract-audio \
  --audio-format mp3 \
  -o "output/%(title)s.%(ext)s" \
  "$6"

python3 metadata.py3 "$1" "$2" "$3" "$4" "$5"
