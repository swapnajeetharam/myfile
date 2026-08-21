import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIOS": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}


def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        if value in suffixes:
            print('its valid category file',{category} )
            return category
    return "MISC"

# test out the pickDirectory() function
print(pickDirectory('.jpg'))


def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            print(item.name)
            continue
        filepath=Path(item)
        filetype=filepath.suffix.lower()
        #filetype=path(item).suffix()
        directory=pickDirectory(filetype)
        directorypath=Path(directory)
        if directorypath.is_dir()!= True:
            directorypath.mkdir()
        filepath.rename(directorypath.joinpath(filepath))

organizeDirectory()
            
        
        