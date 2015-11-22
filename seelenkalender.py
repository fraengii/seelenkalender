print("Bitte gebe die Jahreszahl ein:")
X = input()
print("Du suchst nach dem Datum des Oster-Sonntags im Jahr",X)
X = int(X)
k = X // 100
m = 15 + (3*k + 3) // 4 - (8*k +13) // 25
s = 2 - (3*k +3) // 4
a = X % 19
d = (19*a + m) % 30
r = (d + a // 11) // 29
og = 21 + d - r
sz = 7 - (X + X // 4 + s) % 7
oe = 7 - (og - sz) % 7
os = og + oe
if os > 31:
    april = os - 31
    print("Ostersonntag ist der",april,"te April!")
else:
        print("Ostersonntag ist der",os,"te März!")
