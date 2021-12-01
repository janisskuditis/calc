#kvadratviedajumu kalkulators  ax2 + bx + c = 0
#Autors: Jānis
#Izstrades datums: 08.11.2021
#Apreķina kvadratviedajumu pec lietotaja a,b,c vērtībām
import math as m
#TO-DO
a = int(input("ievadi a vērtību"))
b = int(input("ievadi b vērtību"))
c = int(input("ievadi c vērtību"))
print(type(a))
#TO-DO
if a==0:
    print("ERROR 404")
d = (b ** 2) - (4 * a * c)
print(d)
#TO-DO
if d < 0:
    print("d = is less-or-equal than 0")
    exit(0)
else:
    x_1 = (-b * m.sqrt-(d))/2 * a
    x_2 = (-b * m.sqrt+(d))/2 * a
    print('This is result')