ime = input("Unesi ime datoteke:  ")
dat = open(ime, "w")

# unos u datotekuls

while True:
    while True:
        tekst = input("Unesite rečenicu : ")
        if len(tekst) < 20:
            break
    dat.write(tekst + "\n")
    odg = input("Želite li nastaviti s unosom: D/N")
    if odg.upper() == "N":
        break
dat.close()

# citanje

dat = open(ime, "r")
samoglasnici = "aeiou"

for linija in dat:
    linija = linija[:-1]

    nova = ""
    for slovo in linija:
        if slovo.lower() in samoglasnici:
            nova = nova + slovo + "*"

        else:

            nova = nova + slovo

        print(linija, ":", nova)
dat.close()
