from math import exp

# Obliczanie odsetek "ciągłych" dla procentu składanego

p = 100 # kapitał początkowy
r = .20 # roczna stopa oprocentowania
t = 2.0 # czas, liczba lat

a = p * exp(r * t)
print(a)