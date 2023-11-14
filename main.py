import random

class PassGen:
    def displayMessage(self):
        passLength = int(input("[+] Введите длину пароля для генерации: "))
        numOfPasswords = int(input("[+] Введите количество паролей для генерации: "))
        print("[+] Будет сгенерировано паролей:", numOfPasswords)
        print()
        filename = input("[+] Введите имя файла для записи: ")
        with open(filename, 'w') as outFile:
            for k in range(numOfPasswords):
                password = self.passGenerator(passLength)
                outFile.write(password + '\n')
        print("[+] Пароль был успешно записан в", filename)

    def passGenerator(self, passLength):
        password = ''
        numOfNumbers, numOfUpperCase, numOfLowerCase = self.numOfChars(passLength)
        for i in range(numOfNumbers):
            password += chr(random.randint(48, 57))
        for i in range(numOfNumbers, numOfNumbers + numOfUpperCase):
            password += chr(random.randint(65, 90))
        for i in range(numOfNumbers + numOfUpperCase, passLength):
            password += chr(random.randint(97, 122))
        password = ''.join(random.sample(password, len(password)))
        return password

    def numOfChars(self, passLength):
        numOfLowerCase = random.randint(0, passLength)
        charRandEnd = passLength - numOfLowerCase
        numOfUpperCase = random.randint(0, charRandEnd)
        numOfNumbers = passLength - numOfLowerCase - numOfUpperCase
        return numOfNumbers, numOfUpperCase, numOfLowerCase

passGen = PassGen()
passGen.displayMessage()
