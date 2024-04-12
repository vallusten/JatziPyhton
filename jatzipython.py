import random
noppa = random.randint(1, 6)
nopat = []

def heitto():
    for n in range(1, 6):
        nopat.append(random.randint(1, 6))

tuloslista = [ykkoset := 0, kakkoset := 0, kolmoset := 0, neloset := 0, vitoset := 0, kutoset := 0]
tuloslista2 = [kolmesamaa := 0, neljasamaa := 0, tayskasi := 0, pienisuora := 0, isosuora := 0, jatzi := 0, sattuma := 0]

def vertailu(x):
    return len(x) != len(set(x))

def vertailu2(x):
    if len(set(x)) == 2:
        numerot = {}
        for n in x:
            if n in numerot:
                numerot[n] += 1
            else:
                numerot[n] = 1
        for number, count in numerot.items():
            if count >= 4:
                return False
            else:
                return True


counter = 0

for kierros in range(1, 7):
    loop = True
    vastaus = input('Heitä?:')
    if vastaus == 'k':
        heitto()
        print(f'Heittosi silmäluvut ovat', nopat)
        for tavoite in range(5, 0, -1):
            for numero in range(6, 0, -1):
                for noppa in nopat:
                    if noppa == numero:
                        counter += 1
                        continue
                    else:
                        continue
                if counter >= tavoite and tuloslista[numero - 1] == 0:
                    tuloslista[numero - 1] = (counter * numero)
                    loop = False
                    break
                else:
                    counter = 0
                    continue
            if not loop:
                break
        print(f'Tilanteesi', tuloslista)
        nopat = []
    else:
        print('lopetit pelin')
        break
summa = 0
for n in tuloslista:
    summa += n
if summa >= 60:
    bonus = 25
else:
    bonus = 0
valisumma = summa + bonus
print(valisumma, 'ja', summa, 'ja', bonus)
    
for kierros in range(1, 7):
    loop = True
    vastaus = input('Heitä?:')
    if vastaus == 'k':
        heitto()
        print(f'Heittosi silmäluvut ovat', nopat)
        counter = 0
        if vertailu(nopat):
            if vertailu2(nopat):
                tk = 0
                for n in nopat:
                    tk += n
                tuloslista2[2] = tk
                break
            else:
                for tavoite in range(5, 0, -1):
                    counter = 0
                    for numero in range(6, 0, -1):
                        for noppa in nopat:
                            if noppa == numero:
                                counter += 1
                                continue
                            else:
                                continue
                        if counter >= tavoite:
                            if tavoite == 5:
                                tuloslista2[5] = 50
                                loop = False
                                break
                            elif tavoite == 4:
                                tuloslista2[1] = (numero * 4)
                                loop = False
                                break
                            elif tavoite == 3:
                                tuloslista2[0] = (numero * 3)
                                loop = False
                                break
                            else:
                                sattumasumma = 0
                                for n in nopat:
                                    sattumasumma += n
                                if tuloslista2[6] == 0:
                                    tuloslista2[6] = sattumasumma
                                    loop = False
                                    break 
                                else:
                                    continue
                        else:
                            counter = 0
                            continue
                    if loop == False:
                        break
        else:
            suora = 0
            for n in nopat:
                suora += n
            if suora == 20:
                tuloslista2[4] = 20
            elif suora == 15:
                tuloslista2[3] = 15
        nopat = []
        print(f'Tilanteesi', tuloslista2)
    else:
        print('lopetit pelin')
        break


for n in tuloslista2:
    valisumma += n
print(f'Tuloksesi on', valisumma)