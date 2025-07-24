# -*- coding: utf-8 -*-
"""
Name:tariffs.py

Un estudiante llevó a cabo un programa que calculó el coste de
envío de un minorista online para el cliente. El programa basaría el
coste de envío en el total del carrito y el país de residencia del cliente en
cuestión.

La tabla de abajo muestra los detalles de los gastos de envío:
Pais         Total      Precio de envio
 USA         <$50           Free
           $50 - $99         $10
          $100 - $249        $25
            >$250            $50
 
 AU          <$50            $10
          $50 - $99          $20
          $100-$249          $50
            >$250           $100
          
 CA          <$50            $5
          $50 -$99           $15
          $100 - $249        $30
             >$250           $75

 UK          <$50            $20
          $50 - $99          $25
          $100 - $249        $55
             >$250           $110
 
"""

mapeo_opciones = {
                1: "USA",
                2: "AU",
                3: "CA",
                4: "UK"}    # cada opción seleccionada lleva a un país diferente

shipping = {"USA":[0, 10, 25, 30],
            "AU":[10, 20, 50, 100],
            "CA":[5, 15, 30, 75],
            "UK":[20, 25, 55, 110]} # conjunto clave - valor: país - gasto añadido

subtotal = -1

while subtotal <= 0:
    subtotal = float(input("Introduzca precio del producto (en euros): "))

opcion_envio = int(input("Seleccione país de envío: 1-USA, 2-AU, 3-CA, 4-UK: "))

while opcion_envio not in mapeo_opciones.keys():
    print("Opción inválida. Por favor, vuelva a intentarlo.")   # Comprobar que se escoge correctamente el país
    opcion_envio = int(input("Seleccione país de envío: 1-USA, 2-AU, 3-CA, 4-UK: "))
    
clave_pais = mapeo_opciones.get(opcion_envio)   # Obtener el país mediante valores del 1º diccionario según la clave opción
tarifas = shipping[clave_pais] # Obtener la lista de valores añadidos del país seleccionado con diccionario

# Suma de los gastos de envío añadidos a partir del subtotal de la venta
if subtotal < 50:
    costo_envio = tarifas[0]
elif subtotal < 100:
    costo_envio = tarifas[1]
elif subtotal < 250:
    costo_envio = tarifas[2]
else:
    costo_envio = tarifas[3]
    
total = subtotal + costo_envio

print(f"Total: {total} €")

    


