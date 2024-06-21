"""Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al
usuario jugar piedra, papel o tijeras contra la computadora."""""

import random

print("Ingrese su eleccion: ")
usuario = input("piedra, papel o tijera ? ")
usuario = usuario.lower()

while usuario not in ['piedra','papel','tijera']:
    print('Su eleccion no es valida, vuelva a ingresarlo')
    usuario = input("piedra, papel o tijera ? ")
    usuario = usuario.lower()

print("Usted ha elegido: ",usuario)
computadora = random.choice([1, 2, 3])

if computadora == 1:
    compu = "piedra"
elif computadora == 2:
    compu = "papel"
else: 
    compu = "tijera"
print("La computadora eligio: ",compu)

# Determinar el ganador
if usuario == compu:
    print("¡Es un empate!")
elif (usuario == 'piedra' and compu == 'tijera' or usuario == 'papel' and compu == 'piedra' or usuario == 'tijera' and compu == 'papel'):
    print("¡USTED ES EL GANADOR!")
else:
    print("¡Mejor suerte la proxima,yo gano :) !")


