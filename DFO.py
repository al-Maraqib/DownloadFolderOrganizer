import os, glob, shutil
from config import *

os.chdir(dl)
dlfiles = glob.glob("%s\\*" %dl)


exeDetect = []
docDetect = []
imageDetect = []
torrentDetect = []
compressedDetect = []

for extension in EXEext:
    exeDetect.extend(glob.glob(dl + "\\%s" %(extension)))
for extension in DOCext:
    docDetect.extend(glob.glob(dl + "\\%s" %(extension)))
for extension in IMAGEext:
    imageDetect.extend(glob.glob(dl + "\\%s" %(extension)))
for extension in TORRENText:
    torrentDetect.extend(glob.glob(dl + "\\%s" %(extension)))
for extension in COMPRESSEDext:
    compressedDetect.extend(glob.glob(dl + "\\%s" %(extension)))


for folder in folderslist:
    if not os.path.exists(os.path.join(dl,str(folder))):
        os.makedirs(os.path.join(dl,str(folder)))

print("Current files and Directories in '% s':" % dl)
print(dlfiles)

for files in exeDetect:
    print("An executable was detected: %s" %files)
    shutil.move(files,(os.path.join(dl,"Executables")))

for files in docDetect:
    print("A document was detected: %s" %files)
    shutil.move(files,(os.path.join(dl,"Documents")))

for files in imageDetect:
    print("An image was detected: %s" %files)
    shutil.move(files,(os.path.join(dl,"Images")))

for files in torrentDetect:
        print("A torrent was detected: %s" %files)
        shutil.move(files,(os.path.join(dl,"Torrents")))

for files in compressedDetect:
    print("A compressed file was detected: %s" %files)
    shutil.move(files,(os.path.join(dl,"Compressed")))
