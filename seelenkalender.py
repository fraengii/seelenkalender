import datetime

##"Please enter the year"
print("Bitte gebe die Jahreszahl ein:")
Jahr = input()
print("Du suchst nach dem Datum des Oster-Sonntags im Jahr",Jahr)
X = int(Jahr)
##Following formulas comming from the wikipedia article https://de.wikipedia.org/wiki/Gau%C3%9Fsche_Osterformel#Eine_erg.C3.A4nzte_Osterformel
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
##The easter formulas maybe amount a date greater then 31 (e.g. March 32. = April 1. etc.) 
if os > 31:
    april = os - 31
    print("Ostersonntag ist der",april,"te April!",Jahr)
    tag = april
    mon = 4
else:
        print("Ostersonntag ist der",os,"te März!",Jahr)
        tag = os
        mon = 3
##
ersterTag = tag + 1
t1 = "Die erste Woche beginnt mit dem Datum "
t2 = "."
tgesamt = t1 + str(ersterTag) + t2 + str(mon) + t2 + str(Jahr)
print(tgesamt)
##
KW = datetime.date(int(Jahr), int(mon), int(ersterTag)).isocalendar()[1]
print('Die Kalenderwoche:', KW)
