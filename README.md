# Random Password Generator

## Description

This project is a command-line tool designed to generate random passwords with customizable length and complexity. The main goal is to provide users with a simple yet effective way to create secure passwords that can resist brute-force attacks and guessing. The tool allows users to specify various requirements for the password, such as the inclusion of uppercase letters, lowercase letters, digits, and special characters. This ensures that the generated passwords are strong and meet the specific needs of different security contexts.

## Features

- **Customizable Length:** Users can specify the desired length of the password.
- **Uppercase Letters:** Option to include uppercase alphabetic characters (A-Z).
- **Lowercase Letters:** Option to include lowercase alphabetic characters (a-z).
- **Digits:** Option to include numeric characters (0-9).
- **Special Characters:** Option to include special characters (e.g., !, @, #, $, etc.).

### Steps

Run the password_generator.py script with the following command-line arguments to generate passwords:

-l or --length (required): Specifies the length of the password.
-u or --use_upper: Include uppercase letters in the password.
-lw or --use_lower: Include lowercase letters in the password.
-d or --use_digits: Include digits in the password.
-s or --use_special: Include special characters in the password.

####Generate a password of length 8 with only lowercase letters and digits:

python password_generator.py -l 8 -lw -d

##Example Output

####When you run the command:
python password_generator.py -l 12 -u -lw -d -s

####You will get an output similar to:
Generated Password: A1b2C3d4!E5f
