import os
from PIL import Image

ROOT_DIR = os.path.abspath(os.curdir)

EXT_FROM = [".png", ".jpg"]
EXT_TO = [".jpg", ".png"]

def get_extension (_filepath, _ind):
    _ext = _filepath.endswith (EXT_FROM [_ind])
    if _ext == True:
        return EXT_FROM [_ind]
    return ""

def rename_all (_ind):
    for file in os.listdir(ROOT_DIR):
        _ext = get_extension (file, _ind)
        if (_ext != ""):
            print (file)
            image = Image.open(file)
            
            fileNew = image.convert ('RGB')
            fileNew.save (image.filename.replace (_ext, EXT_TO [_ind]))
            print (fileNew)
        
rename_all (0)
rename_all (1)