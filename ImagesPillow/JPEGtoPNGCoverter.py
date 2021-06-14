import sys
from PIL import Image
from pathlib import Path

# grab first and second argument
Folder = sys.argv[1]

newFolder = sys.argv[2]

# check if the folder exists , if not created
newPath = Path(newFolder)
if not newPath.is_dir():
    newPath.mkdir(mode=0o777, parents=False, exist_ok=False)
# loop into pokedex, convert images to png
# save to the new folders
pokedex_path = Path(Folder)
for x in pokedex_path.iterdir():
    img = Image.open(x)
    clean_name = x.stem
    img.save(f'{newPath}/{clean_name}.png', 'png')




