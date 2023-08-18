def ZbrojZnamenki(broj):
    suma = 0
    while (broj > 0):
        z = broj % 10
        suma = suma + z
        broj = broj//10
    return suma


ime = input("Unesi ime datoteke:  ")
dat = open(ime, "w")

while True:
    broj = int(input("Unesi broj:  "))
    if broj != 0:
        dat.write(str(broj)+"\n")
    else:
        break
dat.close()

dat = open(ime, "r")
for linija in dat:
    linija = int(linija)
    s = ZbrojZnamenki(linija)
    if s % 2 == 0:
        print("Zbroj znamenki broja", linija, "je paran broj")
    else:
        print("Zbroj znamenki broja", linija, "je neparan broj")

dat.close()
