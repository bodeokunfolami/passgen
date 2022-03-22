import string
import random

class PasswordGenerator:

    def __init__(self, length, numbers, symbols, save):
        self.length = length
        self.numbers = numbers
        self.symbols = symbols
        self.save = save
    

    def create_password(self):
        chars = string.ascii_letters

        if self.numbers:
            chars += string.digits
        if self.symbols:
            chars += string.punctuation
        
        return self.generate_password(chars)
    
    def generate_password(self, chars):
        while True:
            password = ''.join(random.choice(chars) for i in range(self.length))
            if self.numbers and sum(char.isdigit() for char in password) >= 3:
                break
            elif not self.numbers:
                break

        return password
    
    def save_password(self, password):
        with open('passwords.txt', 'a') as file:
            file.write(password)
            file.write('\n')