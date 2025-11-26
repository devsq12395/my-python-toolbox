import os
from PIL import Image

ROOT_DIR = os.path.abspath(os.curdir)

EXT_FROM = [".jpg", ".jpeg"]
EXT_TO = ".png"

def get_extension (_filePath):
    for i in EXT_FROM:
        _ext = _filePath.endswith (i)
        print i
        if _ext == True:
            return i
    return ""

def rename_all ():
    for file in os.listdir(ROOT_DIR):
        _ext = get_extension (file)
        if (_ext != ""):
            print (file)
            image = Image.open(file)
            
            fileNew = image.convert ('RGB')
            fileNew.save (image.filename.replace (_ext, EXT_TO))
            print (fileNew)
        
rename_all ()