from faker import Faker
fake=Faker()
class BaseContact:
    def __init__(self,name,email,phone):
        self.name=name
        self.phone=phone
        self.email=email
        #Variables
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
    def contact(self):
        return (f"Wybieram numer {self.BusinesPhone} I dzownię do {self.name} ")
contact1=BaseContact(name=fake.name(), phone=fake.phone_number(), email=fake.email())
contact2=BusinesContact(name=fake.name(), phone=fake.phone_number(), email=fake.email(),job=fake.job(),company=fake.company(), BusinesPhone=123456789)

print(contact2)