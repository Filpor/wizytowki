from faker import Faker
fake=Faker()
class person:
    def __init__(self,name,company,job,email):
        self.name=name
        self.company=company
        self.job=job
        self.email=email
person1=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())
person2=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())
person3=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())
person4=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())
person5=person(name=fake.name(),company=fake.company(),job=fake.job(),email=fake.email())
new_list=[person1,person2,person3,person4,person5]
by_name=sorted(new_list, key=lambda person: person.name)
by_email=sorted(new_list, key=lambda person: person.email)


