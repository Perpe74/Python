import os

ilosc_plikow = len(os.listdir("/dev"))

print(f"Liczba plikow w katalogu: {ilosc_plikow}")