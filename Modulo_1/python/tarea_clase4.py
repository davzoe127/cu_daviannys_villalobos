#ejercicios de diccionario

mi_diccionario ={
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Ingenieria"

}
#imprime el valor de "carrera"
print("carrera:", mi_diccionario["carrera"])


#contrar frecuencia de letras
palabra = "banana"
frecuencia = {}

for letra in palabra:
    if letra in frecuencia:
        frecuencia[letra] += 1
    else:
        frecuencia[letra] = 1

print(frecuencia)

#actualizar valores

precios = {
    "manzana": 0.5,
    "banana": 0.3, 

}
#cambio de banana de 0.3 a 0.4
precios["banana"] = 0.4  
print("\nluego de la modificacion del precio:", precios)

#iterar sobre claves y valores
capitales ={
    "francia": "paris",
    "italia": "roma",
    "españa": "madrid",
}

for pais, capital in capitales.items():
    print(f"La capital de {pais} es {capital}")
