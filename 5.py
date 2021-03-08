import string
import secrets


class Phone:
    number = ''.join(secrets.choice(string.digits) for i in range(11))


class Samsung(Phone):
    os = "android"
    brand = "Samsung"


class Apple(Phone):
    os = "IOS"
    brand = "Apple"


print(Samsung.brand, Samsung.os, Phone.number)
print(Apple.brand, Apple.os, Phone.number)
