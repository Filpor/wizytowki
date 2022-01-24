from faker import Faker
fake=Faker()
class BaseContact:
    def __init__(self,name,email,phone):
        self.name=name
        self.phone=phone
        self.email=email
        self._label_len=len(self.name)
    def __str__(self):
        return f'{self.name} , {self.phone} , {self.email}'
    def contact(self):
        return (f"Wybieram numer {self.phone} I dzownię do {self.name} ")
    @property
    def label_len(self):
        return len(self.name)

class BusinesContact(BaseContact):
    def __init__(self,job,company,BusinesPhone,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.job=job
        self.company=company
        self.BusinesPhone=BusinesPhone
    def __str__(self):
        return f'{self.name}, {self.job}, {self.company} , {self.BusinesPhone} , {self.email}, {self.phone}'
    def contact(self):
        return (f"Wybieram numer {self.BusinesPhone} I dzownię do {self.name} ")

def create_contacts(a,b):
    if a==1:
        for contact in range(0,b):
            contact=BaseContact(name=fake.name(), phone=fake.phone_number(), email=fake.email())
            print(contact)
    elif a==2:
        for contact in range (0,b):
            contact=BusinesContact(name=fake.name(), phone=fake.phone_number(), email=fake.email(),job=fake.job(),company=fake.company(), BusinesPhone=fake.phone_number())
            print(contact)
    else:
        print("zły parametr")
        exit(1)
   
if __name__ == '__main__':
    print("Rodzaj wizytówki która ma zostać utworzona (1-BaseContact 2-BuisnessContact):")
    a=int(input())
    print("Ilość wizytówek do utworzenia")
    b=int(input())
    create_contacts(a,b)
