import math
import keyword


nazwy_funkcji_math = [nazwa for nazwa in dir(math) if callable(getattr(math, nazwa))]
print("Funkcje w module math:", nazwy_funkcji_math)

nazwy_funkcji_tuple = [nazwa for nazwa in dir(tuple) if callable(getattr(tuple, nazwa))]
print("Funkcje w module tuple:", nazwy_funkcji_tuple)

nazwy_funkcji_keyword = [nazwa for nazwa in dir(keyword) if callable(getattr(keyword, nazwa))]
print("Funkcje w module keyword:", nazwy_funkcji_keyword)
