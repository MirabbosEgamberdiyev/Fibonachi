from typing import Any


class Talaba:
    def __init__(self, firstname: str, lastname: str, tyil: int, phone_number) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.tyil = tyil
        self.phone_number = phone_number
    
    def get_info(self):
        return f"Ism: {self.firstname}, Familiya: {self.lastname}, Tug'ilgan yili: {self.tyil}, Telefon raqami: {self.phone_number}"
    
    def __eq__(self, other: object) -> bool:
        return self.tyil == other.tyil
    
    def __delattr__(self, name: str) -> None:
        if name == "tyil":
            print("Tug'ilgan yil atributi o'chirildi.")
            self.tyil = None
        else:
            super().__delattr__(name)
    
    def __call__(self) -> None:
        print("Talaba sinfi chaqirildi.")
        print(self.firstname)
    
    def __format__(self, new_number: str) -> str:
        if new_number == self.phone_number:
            return self.phone_number
        else:
            return new_number


talaba1 = Talaba("Mirabbos", "Egamberdiyev", 2001, "+998 88 999 64 99")
talaba2 = Talaba("Abdullo", "Oripov", 2007, "+998 94 276 80 54")
print("New Number : {}".format(talaba1.__format__("+998 88 999 65 88")))




# print(talaba1.tyil == talaba2.tyil)
# del talaba1.tyil
# print(talaba1.tyil)
# talaba1()
# print(talaba1.__class__)
# print(dir(talaba1))
# print(talaba1.__dict__)
    