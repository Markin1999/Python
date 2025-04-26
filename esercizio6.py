# 1. Crea una classe base chiamata Veicolo
#    - Attributi PRIVATI: marca, modello
#    - Costruttore (__init__) per inizializzare marca e modello
#    - Metodi getter e setter per marca e modello
#    - Metodo info() che stampa: "Veicolo: [marca] [modello]"

class Veicolo:
    def __init__(self, marca, modello):
        self.__marca = marca 
        self.__modello = modello
    
    def get_marca(self):
        return self.__marca

    def set_marca(self, nuova_Marca):
       self.__marca = nuova_Marca
       
    def get_modello(self):
        return self.__modello

    def set_modello(self, nuova_Modello):
       self.__modello = nuova_Modello
       
    def info (self):
        print(f"Veicolo: {self.__modello} {self.__marca}")

    

        

# 2. Crea una classe Auto che eredita da Veicolo
#    - Nuovo attributo privato: posti
#    - Costruttore che riceve anche i posti (usa super() per marca e modello)
#    - Getter e setter per posti
#    - Override del metodo info() per stampare: "Veicolo: [marca] [modello] - Posti: [posti]"

class Auto(Veicolo):
    def __init__(self, marca, modello, posti):
        super().__init__(marca, modello)
        self.__posti = posti
        
    def get_posti(self):
        return self.__posti
        
    def set_posti(self, nuoviPosti):
        self.__posti = nuoviPosti
            
    def info(self):
        print(f"Veicolo: {self.get_modello()} {self.get_marca()} {self.__posti}")
            
            
        
        



# 3. Crea una classe Moto che eredita da Veicolo
#    - Nuovo attributo privato: cilindrata
#    - Costruttore che riceve anche la cilindrata (usa super())
#    - Getter e setter per cilindrata
#    - Override del metodo info() per stampare: "Veicolo: [marca] [modello] - Cilindrata: [cilindrata] cc"

class Moto(Veicolo):
    def __init__(self, marca, modello, cilindrata):
        super().__init__(marca, modello)
        self.__cilindrata = cilindrata
        
    def get_cilindrata(self):
            return self.__posti
        
    def set_cilindrata(self, nuovaCilindrata):
            self.__posti = nuovaCilindrata
        
    def info(self):
        print(f"Veicolo: {self.get_modello()} {self.get_marca()} {self.__cilindrata}")
        
    pass  # qui scrivi il codice della classe


# 4. Istanzia un oggetto Auto e uno Moto con dati a tua scelta
#    - Chiama il metodo info() per entrambi

a = Auto("Fiat", "Panda", 4)
a.info()
m = Moto("honda", "shadow", 2500)
m.info()

# Esempio (da completare con i tuoi dati):
# auto1 = Auto("Fiat", "Panda", 4)
# auto1.info()

# moto1 = Moto("Yamaha", "R6", 600)
# moto1.info()
