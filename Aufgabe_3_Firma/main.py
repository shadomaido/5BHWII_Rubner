import Firma

if __name__ == '__main__':

    female = Firma.Gender(True)
    male = Firma.Gender(False)
    firma = Firma.Firma()
    rechnungswesen = Firma.Rechnungswesen("Rechnungswesen")
    vertrieb = Firma.Vertrieb("Vertrieb")
    verkauf = Firma.Verkauf("Verkauf")


    firma.add_person(Firma.Person("Ian", 19, Firma.Gender(False)))
    firma.add_person(Firma.Mitarbeiter(rechnungswesen, "JOJO", 19, Firma.Gender(False)))
    firma.add_person(Firma.Mitarbeiter(rechnungswesen, "Dani", 19, Firma.Gender(False)))
    firma.add_person(Firma.Abteilungsleiter(vertrieb, "July", 19, Firma.Gender(True)))
    firma.add_person(Firma.Mitarbeiter(verkauf, "Eva", 19, Firma.Gender(True)))
    firma.add_person(Firma.Abteilungsleiter(verkauf, "Pati", 19, Firma.Gender(False)))

    print("Mitarbeiter: " + str(firma.count_mitarbeiter()))
    print("Abteilungsleiter: " + str(firma.count_abteilungsleiter()))
    print("Departments: " + str(firma.count_departments()))
    print("Largest Department: " + firma.find_largest_of_all_departments())
    print("percentage is Female: " + str(firma.percentage_is_female()))
