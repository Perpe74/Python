import xml.dom

DOM = xml.dom.minidom.parse("kursy.xml")
collection = DOM.documentElement

kursy = collection.getElementsByTagName("pozycja")

for pozycja in kursy:
   nazwa_waluty = pozycja.getElementsByTagName("nazwa_waluty")[0]
   print("currency name is ", nazwa_waluty.childNodes[0].data)
   kod_waluty = pozycja.getElementsByTagName("kod_waluty")[0]
   print("currency code is ", kod_waluty.childNodes[0].data)
   kurs_kupna = pozycja.getElementsByTagName("kurs_kupna")[0]
   print("buying rate is ", kurs_kupna.childNodes[0].data)
   kurs_sprzedazy = pozycja.getElementsByTagName("kurs_sprzedazy")[0]
   print("selling rate is ", kurs_sprzedazy.childNodes[0].data)
