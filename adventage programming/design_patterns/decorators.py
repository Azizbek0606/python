import datetime
from abc import ABC, abstractmethod


class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class SendMessage(MessageSender):
    def send(self):
        return "Hello World!"

class Decorator:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def decorate(self):
        return self.sender.send()

class MessageAddTime(Decorator):
    def send(self):
        now = datetime.datetime.now()
        return self.sender.send() + f", {now}"

class MessageEncrypt(Decorator):
    def send(self):
        message = self.sender.send()
        encrypted_message = encrypt(message)
        return encrypted_message


message = SendMessage()
encrypted_message = MessageEncrypt(message)
print(encrypted_message.send())


# dictionary
crypt = {
    "a": "100",
    "b": "101",
    "c": "102",
    "d": "103",
    "e": "104",
    "f": "105",
    "g": "106",
    "h": "107",
    "i": "108",
    "j": "109",
    "k": "110",
    "l": "111",
    "m": "112",
    "n": "113",
    "o": "114",
    "p": "115",
    "q": "116",
    "r": "117",
    "s": "118",
    "t": "119",
    "u": "120",
    "v": "121",
    "w": "122",
    "x": "123",
    "y": "124",
    "z": "125",
    "0": "200",
    "1": "201",
    "2": "202",
    "3": "203",
    "4": "204",
    "5": "205",
    "6": "206",
    "7": "207",
    "8": "208",
    "9": "209",
}
inv_crypt = {v: k for k, v in crypt.items()}

# encrypt function
def encrypt(word):
    encrypted = ''
    for char in word:
        if char in crypt:
            encrypted += crypt[char]
        else:
            encrypted += char
    return encrypted

# decrypt function
def decrypt(code):
    ind = 0
    decrypted = ''
    while ind < len(code):
        if code[ind: ind + 3] in inv_crypt:
            decrypted += inv_crypt[code[ind: ind + 3]]
            ind += 3
        else:
            decrypted += code[ind]
            ind += 1
    return decrypted