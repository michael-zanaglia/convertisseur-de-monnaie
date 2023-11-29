from forex_python.converter import CurrencyRates
import re
c = CurrencyRates()
# Je cree une liste des devise afin de verifier si je les rentre correctement.
de = c.get_rates("EUR")
ld = list(de.keys())
ld.append("EUR")

# J'affiche le taux de change actuel de la devise souhaité.
def my_currency(wanted, have) :
    dict_c = c.get_rate(have, wanted)
    print(f"Le taux entre votre devise et le {wanted} est : {dict_c}.")

# Je convertis une somme dans une autre devise.
def change(j, l) :
    while True :
            value_h = input("Quelle devise possedez vous ?\n").upper()
            if value_h not in l :
                print("Introuvable, reessayez.")
            else :
                break
    while True :
            value_w = input("Quelle devise souhaitez vous observer aujourd'hui ?\n").upper()
            if value_w not in l :
                print("Introuvable, reessayez.")
            else :
                break
    value_h = re.sub(r'\s', '', value_h)
    value_w = re.sub(r'\s', '', value_w)
    while True :
        yn = input(f"Souhaitez-vous convertir une somme entre {value_h} et {value_w} ?(y/n)\n").lower()
        if yn == "y" :
            while True :
                try :
                    money = input(f"Entrez un montant en {value_h} :\n")
                    money = float(re.sub(r'\s', '', money))
                    break
                except ValueError :
                    print("Montant invalide, etes vous sur de n'avoir rentré que des chiffres ?")
            fi = c.convert(value_h, value_w, money)
            j.append(fi)
            fichier = open("historic.txt", "a")
            fichier.write(f"{(value_h, money)} => {(value_w, fi)}")
            fichier.close()
            print(f"{money} {value_h} en {value_w} fait {fi : .2f} {value_w}.")
        elif yn == "n" :
            break 
        else :
            print("Entrez une réponse valide.")

# Voir l'historique des taux de changes.
def history(x) :
    if not x :
        print("Aucun historique à ce jour.\n")
    else :
        print("Historique :\n")
        fichier = open("historic.txt", "r")
        for line in fichier :
            print(line)
        fichier.close()
    print("")

def add() :
    print("\nAjout non fait :(\n")
     
    
    
        
# ---------------------------- MENU ---------------------------            
print("Bonjour,\nMenu Principal :\n 1. Pour observer le taux actuel entre deux devises\n 2. Convertir une somme\n 3. Observer l'historique\n 4. Ajouter une devise\n 5. Quitter")
count = 0
cle = []
while True :
    if count == 1 :
        print("Menu Principal :\n 1. Pour observer le taux actuel entre deux devises\n 2. Convertir une somme\n 3. Observer l'historique\n 4. Ajouter une devise\n 5. Quitter")
    try :
        r = int(input("Entrez le chiffre correspondant à votre demande : "))
    except ValueError :
        print("Entrée invalide.\n")
    if r < 1 or r > 5 :
        print("Veuillez entrer un chiffre entre 1 et 5 inclus.")
        count = 1
        continue
    elif r == 1 :
        while True :
            w = input("Quelle devise souhaitez vous observer aujourd'hui ?\n").upper()
            if w not in ld :
                print("Introuvable, reessayez.\n")
            else :
                break
        while True :
            h = input("Quelle devise possedez vous ?\n").upper()
            if h not in ld :
                print("Introuvable, reessayez.\n")
            else :
                break
        h = re.sub(r'\s', '', h)
        w = re.sub(r'\s', '', w)
        my_currency(w, h)
        count = 1
    elif r == 2 :
        change(cle, ld)
        count = 1
    elif r == 3 :
        history(cle)
        count = 1
    elif r == 4 :
        add()
        count = 1
    elif r == 5 :
        print("Merci, à bientot !")
        break        
