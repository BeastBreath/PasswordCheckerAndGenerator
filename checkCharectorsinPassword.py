

def checkCharectorsinPassword(password = ""):
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
                break

        if not found:
            return False
    return True