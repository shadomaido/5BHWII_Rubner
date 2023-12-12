#herangehensweise an Programmierübung

#firma
#liste von Personen

#person
    #name
    #vorname
    #gender
    #alter

#Mitarbeiter erben von person
    #Abteilung

#Abteilungsleiter erbt von mitarbeiter
class Gender:
    def __init__(self, isBiologicalFemale):
        self.IsBiologicalFemale = isBiologicalFemale

class Abteilung:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Rechnungswesen(Abteilung):
    def __init__(self, name):
        super().__init__(name)


class Vertrieb(Abteilung):
    def __init__(self, name):
        super().__init__(name)

class Verkauf(Abteilung):
    def __init__(self, name):
        super().__init__(name)

class Person:
    def __init__(self,name , age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Mitarbeiter(Person):
    def __init__(self, abteilung, name, age, gender):
        self.abteilung = abteilung
        super(Mitarbeiter, self).__init__(name,age,gender)

class Abteilungsleiter(Mitarbeiter):
    def __init__(self, abteilung, name, age, gender):
        super(Abteilungsleiter,self).__init__(abteilung, name,age,gender,)



class Firma:
    def __init__(self):
        self.personen = []

    def add_person(self, person):
        self.personen.append(person)

    def list_Personen(self):
        for person in self.personen:
            print(person.name)

    def list_Mitarbeiter(self):
        listMitarbeiter = []
        for person in self.personen:
            if isinstance(person, Mitarbeiter):
                listMitarbeiter.append(person)
        return listMitarbeiter

    def list_Abteilungsleiter(self):
        listAbteilungsleiter = []
        for person in self.personen:
            if isinstance(person, Abteilungsleiter):
                listAbteilungsleiter.append(person)
        return listAbteilungsleiter

    def list_departments(self):
        list_departments = set()
        for person in self.personen:
            if isinstance(person, Mitarbeiter):
                if not person.abteilung.name in list_departments:
                    list_departments.add(person.abteilung.name)
        return list_departments

    def count_mitarbeiter(self):
        return len(self.list_Mitarbeiter())

    def count_abteilungsleiter(self):
        return len(self.list_Abteilungsleiter())

    def count_departments(self):
        return len(self.list_departments())

    def find_size_of_department(self, department):
        count = 0
        for person in self.personen:
            if isinstance(person, Mitarbeiter):
                if person.abteilung.name == department:
                    count += 1
        return count

    def find_largest_of_all_departments(self):
        largest = 0
        departmentname = ""
        for department in self.list_departments():
            size = self.find_size_of_department(department)
            if size > largest:
                largest = size
                departmentname = department
        return departmentname

    def percentage_is_female(self):
        count = 0
        for person in self.personen:
            if person.gender.IsBiologicalFemale:
                count +=1
        return count / len(self.personen)*100













