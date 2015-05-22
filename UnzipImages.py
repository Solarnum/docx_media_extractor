import zipfile, sys, shutil, os
from os import path

if len(sys.argv) > 2:
    dir_path = sys.argv[2]
else:
    dir_path = "images"
if not os.path.isdir(dir_path):
    os.mkdir(dir_path)
mZipfile = zipfile.ZipFile(sys.argv[1])
for member in mZipfile.namelist():
    if member.startswith('word/media'):
        filename = path.basename(member)
        source = mZipfile.open(member)
        target = file(path.join(dir_path, filename), "wb")
        with source, target:
            shutil.copyfileobj(source, target)
