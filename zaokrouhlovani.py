import math
import sys
print(sys.argv)
cislo = float(sys.argv[1])
a = str(cislo)
b = a.split(".")
c = b[1] 
d = int(c[0])
if d >= 5:
    novecislo = math.ceil(cislo)
    
else: 
    novecislo = math.floor(cislo)
print(f"Zaokrouhlení: {novecislo}") 
