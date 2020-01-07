import os, glob, shutil

dl = "D:\\Downloads"
os.chdir(dl)
dlfiles = glob.glob("D:\\Downloads\\*")
folderslist = ['Executables', 'Documents', 'Images', 'Torrents', 'Compressed', 'Misc.']
EXext = ['.exe', '.msi']
DOCext = ['.docx', '.pptx', '.pdf']
IMAGEext = ['.png', '.jpg', '.jpeg']
TORRENText = ['.torrent']
COMPRESSEDext = ['.zip', '.rar', '.7z',]

exeDetect = glob.glob('*.exe') + glob.glob('*.msi')
docDetect = glob.glob('*.docx') + glob.glob('*.pdf') + glob.glob('*.pptx') + glob.glob('*.xlsx') 
imageDetect = glob.glob('*.png') + glob.glob('*.jpg') + glob.glob('*.jpeg')
torrentDetect = glob.glob('*.torrent')
compressedDetect = glob.glob('*.zip') + glob.glob('*.rar') + glob.glob('*.7z')

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
