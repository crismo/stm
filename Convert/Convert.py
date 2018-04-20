import os
import getopt
import sys
from PIL import Image

Possible = [(2048, 1536), (2048, 1406)]

def findScale(n):
    x, y = 2732, 2048
    x2, y2 = Possible[n]

    return (x2/x,y2/y)

def resizeImages(scale, path, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)

    for root, folder, files in os.walk(path):
        for file in files:
            pathJoined = os.path.join(root, file)
            Img = Image.open(pathJoined)
            newWidth = int(Img.width*scale[0])
            newHeight = int(Img.height*scale[1])
            Img = Img.resize((newWidth, newHeight), Image.ANTIALIAS)
            Img.save(os.path.join(dest, file))


def reSizeTxtCoords(scale, path, dest):
    newLines = []
    with open(path, mode='r') as r:
        lines = r.readlines()
        for line in lines:
            if line.__contains__('Handling') or line.__contains__('Drag'):
                splitted = line.split(',')
                if line.__contains__('DragAlternativ'):
                    currentX = int(splitted[len(splitted)-5])
                    currentY = int(splitted[len(splitted)-4])
                    currentWidth = int(splitted[len(splitted)-3])
                    currentHeight = int(splitted[len(splitted)-2])
                    allBefore = splitted[:len(splitted)-5]
                    newLine = "".join(allBefore[0:1])
                    for split in allBefore[1:]:
                        newLine += "," + split
                    newX = str(int(currentX*scale[0]))
                    newY = str(int(currentY*scale[1]))
                    newWidth = str(int(currentWidth*scale[0]))
                    newHeight = str(int(currentHeight*scale[1]))
                    newLine+=","+newX+","+newY+","+newWidth+","+newHeight+","+splitted[len(splitted)-1]
                    newLines.append(newLine)
                else:
                    currentX = int(splitted[len(splitted)-2])
                    currentY = int(splitted[len(splitted)-1].split('\n')[0])
                    allBefore = splitted[:len(splitted) - 2]
                    newX = str(int(currentX * scale[0]))
                    newY = str(int(currentY * scale[1]))
                    newLine = "".join(allBefore[0:1])
                    for split in allBefore[1:]:
                        newLine +=","+split
                    newLine+=","+newX+","+newY+"\n"
                    newLines.append(newLine)
            else:
                newLines.append(line)
    with open(dest, mode='w') as w:
        w.writelines(newLines)

def run(n, pathOrgFile, pathOrgImg, pathNewFile, pathNewImg):
    scale = findScale(n)
    reSizeTxtCoords(scale, pathOrgFile, pathNewFile)
    resizeImages(scale, pathOrgImg, pathNewImg)


def main(argv):
    orgTxtFile = ''
    orgImages = ''
    newTxtFile = ''
    newImages = ''
    n = 0
    try:
        opts, args = getopt.getopt(argv,"h:n:iF:iI:oF:oI:",["nummer","iFile=","iImg=", "oFile=", "oImg="])
    except getopt.GetoptError as e:
        print('Convert.py --nummer <index> --iFIle <orgFile> --iImg <orgImages> --oFile <newFile> --oImg <newImages>')
        print(e)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('Convert.py --nummer <index> --iFIle <orgFile> --iImg <orgImages> --oFile <newFile> --oImg <newImages>')
            sys.exit()
        elif opt in ("-iF", "--iFile"):
            orgTxtFile = arg
        elif opt in ("-iI", "--iImg"):
            orgImages = arg
        elif opt in ("-oF", "--oFile"):
            newTxtFile = arg
        elif opt in ("-oI", "--oImg"):
            newImages = arg
        elif opt in ("-n", "--number"):
            n = int(arg)
    print(n)
    print(orgTxtFile)
    print(orgImages)
    print(newImages)
    print(newTxtFile)
    run(n, orgTxtFile, orgImages, newTxtFile, newImages)
if __name__ == '__main__':
    main(sys.argv[1:])
    #run(0,  'C:/Users/Atle/Downloads/Testing/programOld.txt','C:/Users/Atle/Downloads/Testing/imgOld',
            #'C:/Users/Atle/Downloads/Testing/program.txt', 'C:/Users/Atle/Downloads/Testing/img')