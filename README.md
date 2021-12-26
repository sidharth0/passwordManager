
# Password Managing Software

This software is quite useful to manage our personal login/password credentials. We generally use web browsers to automatically save our passwords which have higher possibility of getting hacked. Moreover sometime we have to share our PC and other users can automatically login to our personal websites due to saved credentials. With the help of this software we can avoid the use of web browsers to save our paswords.

## Features
### Sign Up
There is feature to create an account in the software. The account is created locally using SQLITE3 databasemanagement. The user credentials are saved in the database. Thus if there are multiple users each user can create an indivisual account. Each account is connected to a randomly generated key saved in database which is required to access the stored credentials of each user. 
### Login
When a user logs in he can access his indivisually saved credentials for different websites. These saved credentials are also encryped and cannot be read unless the user key is known.
### Password Generator
There is a password generator feature available with the software. It is advisable to use such passwords as these are difficult to guess.
### Search 
Once the credentials are entered by the user. The software provides the user with the option to search from the list of saved passwords.
### Added Security
The user can make the software even more secure by removing the saved password file after use from the software directory. The user can paste the saved password file only when he wants to use the software. The user can further increase the security by removing the database file from the software directory. It is the database file which contains the key for decrypting the saved passwords.
