"""
This function generates a password. The key idea of this is that 
"""
import fileinput
import os
import random
from CheckPassword import CheckPassword
from checkCharectorsinPassword import checkCharectorsinPassword

def createSecurePassword(cases = 10000, folderPath = 'filesAfterInput', length = 20, randomness = 10, printProgress=True):
    
    while(not checkParameters(cases=cases, folderPath = 'filesAfterInput', length = length, randomness = randomness, printProgress=printProgress)):
        if (randomness < 25):
            print("Changing Randomness to: " + str(randomness))
            randomness += 1
            continue
        print("Password length does not generate a secure password")
        length = int(input("New Length: "))
        # randomness = int(input("New Randomness: "))
    
    return generatePassword(folderPath = 'filesAfterInput', length = length, randomness = randomness)

def findNKey(d, i):
    c = 0
    for k in d.keys():
        if c==i:
            return k
        else:
            c += 1

def generatePassword(folderPath = 'filesAfterInput', length = 20, randomness = 10):

    alpha_numeric_charectors = "QAZWSXEDCRFVTGBYHNUJMIKOLPqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678900123456789!@#$%^&*()_+=-~`{}][:;?/>.<,\"\'"

    if length < 1:
        print("Please Input Valid length for password")
        return 1
    


    password = ''
    # firstLetterFile = open(os.path.join(folderPath, 'XCombined', str(key) + '.txt'), "w")
    with fileinput.input(files=(os.path.join(folderPath, 'XCombined', '1.txt'))) as f:
        freq = {}
        for line in f:
            line = line[:-1]
            if line in freq.keys():
                freq[line] += 1
            else:
                freq[line] = 1

        dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        random_number = len(freq) - random.randint(1,randomness)
        if findNKey(freq, random_number) == None or random.randint(0,1) == 0:
            random_charector = alpha_numeric_charectors[random.randint(0,len(alpha_numeric_charectors) - 1)]
            password += random_charector
        else:
            password = password + findNKey(freq, random_number)

    for i in range(2, min(11, length + 1)):
        path = os.path.join(folderPath, 'XCombined', str(i) + '.txt')
        X = list()
        with fileinput.input(files=(path)) as f:
            for line in f:
                X.append(line[:-1])
        path = os.path.join(folderPath, 'y', str(i) + '.txt')
        y = list()
        with fileinput.input(files=(path)) as f:
            for line in f:
                y.append(line[:-1])
        
        freq = {}
        for i in range(len(X)):
            if X[i] == password:
                if y[i] in freq.keys():
                    freq[y[i]] += 1
                else:
                    freq[y[i]] = 1

        dict(sorted(freq.items(), key=lambda item: item[1]))
        random_number = len(freq) - random.randint(1,randomness)
        if findNKey(freq, random_number) == None or random.randint(0,1) == 0:
            random_charector = alpha_numeric_charectors[random.randint(0,len(alpha_numeric_charectors) - 1)]
            password += random_charector
        else:
            password = password + findNKey(freq, random_number)
    
    for i in range(10, length + 1):
        random_charector = alpha_numeric_charectors[random.randint(0,len(alpha_numeric_charectors) - 1)]
        password += random_charector



    lowerCase = 'qwertyuioplkjhgfdsazxcvbnm'
    upperCase = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
    specialCharectors = '!@#$%^&*()~`\"\';:<,>.?/+=_-'
    numbers = '1234567890'
    groups = [lowerCase, upperCase, specialCharectors, numbers]
    for s in groups:
        found = False
        for i in range(len(s)):
            if s[i] in password:
                found = True
                continue
        
        if not found:
            randomSpot = random.randint(0,len(password) - 1)
            password = password[:randomSpot] + s[random.randint(0,len(s) - 1)] + password[randomSpot:]
    
    return password


# This function tests the password generator 
def checkParameters(cases = 10000, folderPath = 'filesAfterInput', length = 20, randomness = 10, printProgress=True):
    # print(length)
    # print(randomness)
    passwordsGenerated = list()
    for i in range(cases):
        if printProgress and i % (cases/100) == 0:
            print(str(100 * i/cases) + '%')
        newPassword = generatePassword(folderPath = 'filesAfterInput', length = length, randomness = randomness)
        if newPassword in passwordsGenerated or not CheckPassword(password=newPassword):
            return False
        passwordsGenerated.append(newPassword)
    return True

# createSecurePassword(length=2, randomness=1)

# p = generatePassword()
# print(p)
