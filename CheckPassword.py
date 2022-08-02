from CheckEnglishWords import checkEnglishWords
from checkCharectorsinPassword import checkCharectorsinPassword
import fileinput
import os

def CheckPassword(password = "", folderPath = 'filesAfterInput'):
    if(not checkEnglishWords(password=password)):
        print("Password is not Secure")
        return False

    if not checkCharectorsinPassword(password=password):
        print("Password is not Secure")
        return False
    
    password_length = len(password)

    n = 1
    d = 1
    for i in range(1, password_length + 1):

        path = os.path.join(folderPath, 'XCombined', str(int(i)) + '.txt')
        # fX = open(os.path.join(folderPath, 'XCombined', str(i), '.txt'), "w")
        total_lines = 0
        with open(path, 'r') as fp:
            total_lines = len(fp.readlines())
        
        count = 0
        with fileinput.input(files=(path)) as f:
            for line in f:
                if line[:-1] == password[0:i]:
                    count += 1
        if (count == 0):
            count = 1
        n *= float(count)
        d *= float(total_lines) / 300
        # print(p)
        # p *= float(count) / float(total_lines)
    if (n / d > .2):
        print("Password is not Secure")
        return False
    return True
