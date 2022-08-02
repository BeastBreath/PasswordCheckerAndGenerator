from InputData import inputComplicated
from GeneratePassword import createSecurePassword, generatePassword
from CheckPassword import CheckPassword
import time

#def createSecurePassword(folderPath = 'filesAfterInput', length = 20, randomness = 10):
#def inputComplicated(folderPath = 'filesAfterInput', filePath = 'words.txt'):
#def CheckPassword(password = "helsp", folderPath = 'filesAfterInput'):

def main():
    inputComplicated()
    while(True):
        print("What do you want to do?")
        print("1. Create a Secure Password")
        print("2. Check a Password")
        print("3. Train Program")
        print("4. End Program")
        user_input = input()
        if user_input not in ['1', '2', '3', '4']:
            print("Please enter a valid number")
            continue
        elif user_input == '1':
            length = int(input("Enter Length: "))
            while (length < 12):
                length = int(input("Enter bigger Length (atleast 12): "))
            print("Password: ", end="")
            print(createSecurePassword(cases=50, length=length, printProgress=True))
        
        elif user_input == '2':
            inputPassword = input("Enter Password: ").lower()
            if(CheckPassword(password=inputPassword)):
                print("You have a secure password")
            
        
        elif user_input == '3':
            passwordFile = input("Enter a file of passwords: ")
            inputComplicated(filePath=passwordFile)
            print("Trained on: " + passwordFile)
        
        elif user_input == '4':
            break
        time.sleep(1)
        print()
            
main()