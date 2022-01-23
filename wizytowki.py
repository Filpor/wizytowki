from faker import Faker
fake=Faker()
class person:
    def __init__(self,name,company,job,email):
        self.name=name
        self.company=company
        self.job=job
        self.email=email
        #Variables
        self._dlugosc=len(self.name)
    def contact(self):
        print("Kontaktuje się z", self.name , self.job , self.email )
    @property
    def dlugosc(self):
        return len(self.name)
person1=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())
person2=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())
person3=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())
person4=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())
person5=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())

print(person4.name)
print(person4._dlugosc)


