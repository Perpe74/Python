import xml.sax

class CurrencyHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata = ""

    def startElement(self, tag, attributes):
        self.currentdata = tag

    def characters(self, content):
        if self.currentdata == "nazwa_waluty":
            print("currency name is ", content)
        elif self.currentdata == "kod_waluty":
            print("currency code is ", content)
        elif self.currentdata == "kurs_kupna":
            print("buying rate is ", content)
        elif self.currentdata == "kurs_sprzedazy":
            print("selling rate is ", content)

    def endElement(self, tag):
        self.currentdata = ""


parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = CurrencyHandler()
parser.setContentHandler(Handler)
parser.parse("kursy.xml")