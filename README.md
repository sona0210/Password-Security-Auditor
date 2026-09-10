# Password Security Auditor

## About the Project

Password Security Auditor is a simple Python project made to check how strong a password is.

The program asks the user to enter a password and checks different things like its length, uppercase and lowercase letters, numbers, and special characters. Based on these checks, it gives a security score out of 100.

It also checks for some common passwords, repeated characters, and simple patterns like `1234` or `abcd`.

## Features

- Checks password length
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters
- Gives a password score out of 100
- Shows a simple security meter
- Gives suggestions for improving the password
- Detects commonly used passwords
- Detects repeated characters
- Detects simple sequential patterns
- Calculates a final score after risk deductions
- Shows the final security level

## How It Works

First, the user enters a password. The password is taken using Python's `getpass` module so that it is not directly displayed while typing.

The program then checks five basic requirements:

1. Password should have at least 8 characters.
2. It should contain an uppercase letter.
3. It should contain a lowercase letter.
4. It should contain a number.
5. It should contain a special character.

Each requirement gives 20 points, so the maximum basic score is 100.

After that, the program checks for some additional risks such as common passwords, repeated characters, and predictable sequences. Some points are deducted if these risks are found.

Finally, the program displays the final score and tells whether the password is Weak, Moderate, or Strong.

## Technologies Used

- Python
- getpass module
- Functions
- Lists
- Dictionaries
- If-else statements
- For loops
- String methods

## How to Run

1. Make sure Python is installed on your computer.
2. Open this project folder in VS Code.
3. Open the terminal.
4. Run the following command:
```bash
    python password_audicator.py
```    
5.Enter your password when the program asks for it.
6.Check the security analysis and final score.

## Author

Sonali Shivaji Bonde
BTech CSE – Cyber Forensic & Information Security
