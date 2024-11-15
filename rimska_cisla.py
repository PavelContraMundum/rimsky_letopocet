def preved_arabsky_letopocet_na_rimsky(rok):
    vysledek = []
    if type(rok) == int and rok > 0 and rok < 9999:
        rad = 1
        while rok > 0:
            zbytek = rok % 10
            rok = rok // 10
            if zbytek != 0:
                vysledek.append(vrat_rimske_cislo(zbytek, rad))
            rad = rad * 10
        vysledek.reverse()
        return ''.join(vysledek)  # Převést list na řetězec
    else:
        return "chyba"

def vrat_rimske_cislo(hodnota, rad):
    rimske_cislo = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    cislo = hodnota * rad
    rimske = ""
    for klic in sorted(rimske_cislo.keys(), reverse=True):
        while cislo >= klic:
            rimske += rimske_cislo[klic]
            cislo -= klic
    return rimske



zadany_rok = int(input("Zadejte rok: "))

print(f"{zadany_rok} na rimske cislo je: " + preved_arabsky_letopocet_na_rimsky(zadany_rok))
