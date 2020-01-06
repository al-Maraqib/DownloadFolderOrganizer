import os, glob, shutil

dl = "D:\\Downloads"
os.chdir(dl)
dlfiles = glob.glob("D:\\Downloads\\*")
folderslist = ['Executeables', 'Documents', 'Images', 'Torrents', 'Compressed', 'Misc.']
EXext = ['.exe', '.msi']
DOCext = ['.docx', '.pptx', '.pdf']
IMAGEext = ['.png', '.jpg', '.jpeg']
TORRENText = ['.torrent']
COMPRESSEDext = ['.zip', '.rar', '.7z',]

exeDetect = glob.glob('*.exe') + glob.glob('*.msi')
docDetect = glob.glob('*.exe') + glob.glob('*.msi')
imageDetect = glob.glob('*.exe') + glob.glob('*.msi')
torrentDetect = glob.glob('*.exe') + glob.glob('*.msi')
compressedDetect = glob.glob('*.zip') + glob.glob('*.rar') + glob.glob('*.7z')

for folder in folderslist:
    if not os.path.exists(os.path.join(dl,str(folder))):
        os.makedirs(os.path.join(dl,str(folder)))

print("Current files and Directories in '% s':" % dl)
print(dlfiles)

for files in exeDetect:
    print(files)
    shutil.move(files,(os.path.join(dl,"Executeables")))
