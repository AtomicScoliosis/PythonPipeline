#!/usr/bin/python
import sys
import os
import fnmatch
import tarfile

def findFiles(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result
    
def untar(tarFile):
    tarLoc = os.path.dirname(tarFile)
    print("tars located at: " + tarLoc)
    print(tarFile)
    tarSrm = tarfile.open(tarFile)
    tarSrm.extractall(tarLoc)
    tarSrm.close
    
def findAjlLoc(tarFile):
    dirName = os.path.splitext(tarFile)
    dirName = os.path.splitext(dirName[0])
    ajlFiles = findFiles('*.ajl', dirName[0])
    if ajlFiles:
        print(ajlFiles)
        return os.path.dirname(ajlFiles[0])
    else: 
        print("no ajls found")
    
def processTar(tarFile):
    print("found tar: " + tarFile)
    untar(tarFile)
        
    #findajls
    ajlLoc = findAjlLoc(tarFile) 
    if ajlLoc:
        os.chdir(ajlLoc)
        print("AJL DIRECTORY:")
        # here is where you would run csv generation instead of listing
        print(os.listdir())
      
        #back up one for mana
        os.chdir('..')
        print('do mana here:')
        print(os.listdir())
        os.chdir(hsvRunDir)
    else: 
        print("no ajl found")
#hsvRunDir = os.path.dirname(sys.argv[1])
hsvRunDir = sys.argv[1]
print("Working Directory: " + hsvRunDir)

runsInDir = os.listdir(hsvRunDir)
for runDir in runsInDir:
    
    #check to see if already in completed list
    print('unpacking in run: ' + runDir)
    runDirLoc = os.path.join(hsvRunDir, runDir)
    
    # Discover relevant Tars per run Directory
    #find srm tar
    srmTar = findFiles('*srmsvr*', runDirLoc)
    bmTar = findFiles('*bmsvr1*', runDirLoc)
    rstmTar = findFiles('*bmsvr7*', runDirLoc)
    
    
    #untar if not empty
    if srmTar:
        processTar(srmTar[0])
    else:
        print("no tar found for SRM")
    if bmTar:
        processTar(bmTar[0])
    else:
        print("no tar found for BM")    
    if rstmTar:
        processTar(rstmTar[0])
    else:
        print("no tar found for BM")