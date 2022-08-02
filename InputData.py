"""
This program inputs the passwords and outputs a set of files in the format 
"""


import fileinput
from loadEnglishWords import putWordsInFile
import os


def inputSimple(folderPath = 'filesAfterInput', filePath = 'words.txt'):
    words_by_length_X_Split = {}
    words_by_length_X_Combined = {}
    words_by_length_Y = {}


    with fileinput.input(files=(filePath)) as f:
        for raw_line in f:
            line = raw_line.lower()
            if (len(line)) == 1:
                pass
            else:
                line_length = len(line)
                newX = list()
                for i in range(line_length - 2):
                    newX.append(line[i])
                if line_length in words_by_length_X_Split.keys():
                    words_by_length_X_Split[line_length].append(newX)
                    words_by_length_X_Combined[line_length].append(line[0:line_length - 2])
                    words_by_length_Y[line_length].append(line[(line_length - 2)])
                else:
                    words_by_length_X_Split[line_length] = [newX]
                    words_by_length_X_Combined[line_length] = [line[0:line_length - 2]]

                    words_by_length_Y[line_length] = [line[line_length - 2]]


    for p in ['XCombined', 'XSplit', 'y']:
        dir = os.path.join(folderPath, p)
        if not os.path.exists(dir):
            os.mkdir(dir)


    for key, value in words_by_length_X_Combined.items():
        fX = open(os.path.join(folderPath, 'XCombined', str(key) + '.txt'), "w")
        for word in value:
            fX.write(word + '\n')
        fX.close()

    for key, value in words_by_length_X_Split.items():
        fXSplit = open(os.path.join(folderPath, 'XSplit', str(key) + '.txt'), "w")
        for word in value:
            for let in word:
                fXSplit.write(let + ' ')
            fXSplit.write('\n')
        fXSplit.close()

    for key, value in words_by_length_Y.items():
        fy = open(os.path.join(folderPath, 'y', str(key) + '.txt'), "w")
        for let in value:
            fy.write(let + '\n')
        fy.close()


def inputComplicated(folderPath = 'filesAfterInput', filePath = 'words.txt'):
    words_by_length_X_Split = {}
    words_by_length_X_Combined = {}
    words_by_length_Y = {}


    with fileinput.input(files=(filePath)) as f:
        for raw_line in f:
            line = raw_line.lower()
            if (len(line)) == 1:
                pass
            else:
                line_length = len(line)
                line = line[0:line_length - 2]
                while(line_length > 1):
                    newX = list()
                    for i in range(line_length - 2):
                        newX.append(line[i])
                    if line_length in words_by_length_X_Split.keys():
                        words_by_length_X_Split[line_length].append(newX)
                        words_by_length_X_Combined[line_length].append(line[0:line_length - 1])
                        if (line_length > 2):
                            words_by_length_Y[line_length].append(line[-1])
                    else:
                        words_by_length_X_Split[line_length] = [newX]
                        words_by_length_X_Combined[line_length] = [line[0:line_length - 1]]
                        if (line_length > 2):
                            words_by_length_Y[line_length] = [line[-1]]

                    line = line[0:line_length - 2]
                    line_length = len(line)



    for p in ['XCombined', 'XSplit', 'y']:
        dir = os.path.join(folderPath, p)
        if not os.path.exists(dir):
            os.mkdir(dir)


    for key, value in words_by_length_X_Combined.items():
        m = key - 1
        fX = open(os.path.join(folderPath, 'XCombined', str(m) + '.txt'), "w")
        for word in value:
            fX.write(word + '\n')
        fX.close()

    for key, value in words_by_length_X_Split.items():
        m = key - 1
        fXSplit = open(os.path.join(folderPath, 'XSplit', str(m) + '.txt'), "w")
        for word in value:
            for let in word:
                fXSplit.write(let + ' ')
            fXSplit.write('\n')
        fXSplit.close()

    for key, value in words_by_length_Y.items():
        m = key - 1
        fy = open(os.path.join(folderPath, 'y', str(m) + '.txt'), "w")
        for let in value:
            fy.write(let + '\n')
        fy.close()