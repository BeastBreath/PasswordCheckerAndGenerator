# Password Checker and Generator
Nividh Singh

### About

This program analyses many passwords to find patterns and generate more secure passwords. This program can also be used to check security of a password. The program uses the patterns in the password files to simuate a more efficient brute force attack. The program calculates how secure a password is if hacked using the patterns found. 

### Motivation

In today's world, two of the biggest problems in cybersecurity are brute force attacks and [social engineering](https://www.imperva.com/learn/application-security/social-engineering-attack/#:~:text=Social%20engineering%20is%20the%20term,or%20giving%20away%20sensitive%20information). The goal of this program is to find patterns in passwords. By finding patterns, this program can find weak passwords that traditional password checkers don't identify.  

### Contribution

For contributions, please use pull requests on Github. Please see [Contributing](Contributing.md) for more information and next steps

### Download the Data

The data that this program uses is too big to store in a repository, so its stored on external storage locations. The passwords that this program is trained on is from [Rockyou2021.txt](https://github.com/ohmybahgosh/RockYou2021.txt). This is the method I used to download the data: 

---

>## AnonFiles.com Download Links:
>##### Command To Extract:  `7za e RockYou2021.txt.7z.001`
>#### **Part 1:**  rockyou2021.txt.7z.001  
>**Size:** 9GB  
>**Link:**  https://anonfiles.com/Da41k3c9y9/rockyou2021.txt.7z_001  
>
>#### **Part 2:**  rockyou2021.txt.7z.002  
>**Size:** 4.64GB
>**Link:**  https://anonfiles.com/pfd4ra0fu9/rockyou2021.txt.7z_002
---
If this isn't working, or you want to download it from a different file hosting site, please visit: [Rockyou2021.txt](https://github.com/ohmybahgosh/RockYou2021.txt)

### Requirements

1. You will need to install [Python](https://www.python.org/) 3.10 on your machine.

2. The next version of the program also uses tensorflow and keras

```bash
python3 -m pip install -r requirements.txt
```

### Usage

To install the repository, clone it from github with the following command

	$ git clone https://github.com/BeastBreath/PasswordCheckerAndGenerator

After cloning, run main.py to start the program. Running main.py will give you 4 options:

```
Create a Secure Password
Check a Password
Train Program
End Program
```

##### Create a Secure Password
This function creates a password thats more secure than a randomly generated password. It uses the patterns found in the data and finds statistically less probable passwords. This function also checks this new password to make sure that it is secure against the program to make sure that it is robust.

##### Check a Password
This function checks a password against the patterns that the program found to make sure the password is secure. This function also runs some other checks on the password, including some traditional ones and some new ones to make sure that the password isn't susceptible to an attack.

##### Train Program
Train program takes in a file and finds patterns in the passwords. 

##### End Program
This ends the program

### License
This work is made available under the "GNU General Public License v3.0". Please see the file [LICENSE](LICENSE) in this distribution for license terms.


### Acknowledgements

Thanks to my mentor Professor Shih-Lien Lu for helping me and guiding me through this project and to the [Institute for Computing in Research] (https://computinginresearch.org/) for the support for this project.
