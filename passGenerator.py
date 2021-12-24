import pyperclip
import random
def generatePass():
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    nos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spChar = ['@', '#', '!', '$', '&']
    capital_no = random.randint(8, 12)
    small_no = random.randint(4, 8)
    nos_no = random.randint(2, 4)
    sp_no = random.randint(2, 4)
    capitals = [random.choice(capital) for _ in range(capital_no)]
    smalls = [random.choice(small) for _ in range(small_no)]
    numbers = [random.choice(nos) for _ in range(nos_no)]
    sps = [random.choice(spChar) for _ in range(sp_no)]
    password_str = capitals + smalls + numbers + sps
    random.shuffle(password_str)
    passwordGen = ''
    for i in password_str:
        passwordGen += i
    password_entry.delete(0, tk.END)
    password_entry.insert(0, passwordGen)
    pyperclip.copy(passwordGen)
