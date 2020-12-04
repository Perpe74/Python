# Funkcja sprawdzajaca czy podane haslo jest prawidlowe
def sprawdz_poprawnosc(prawidlowy_kod, wprowadzony_kod):
    if wprowadzony_kod == prawidlowy_kod:
        print("Poprawne haslo!")
    else:
        print("Haslo jest niepoprawne!")


# Ustawianie stalego prawidlowego hasla
prawidlowy_kod = input("Prosze ustaw haslo dla zamka")

# Wprowadzanie hasla by odblokowac zamek
wprowadzony_kod = input("Prosze wprowadz haslo")

#Sprawdzanie czy haslo jest poprawne
sprawdz_poprawnosc(prawidlowy_kod, wprowadzony_kod)