#juego basado en HXH
#descripcion:Gon Freecss es un niño de 12 años
#que desea convertirse en un cazador como su padre
#Durante el examen, enfrenta 3 pruebas clave:

#en esta prueba, en el camino gon enfreta a otro cazador, que le impedira
#pasar la primera prueba

#elige una opcion para ayudar a Gon a pasar la prueba
opcion = input("Que opcion eliges? (NEGOCIAR/PELEAR/PEDIR_AYUDA):").strip().upper()

if opcion == "NEGOCIAR":
    print("\nbuena eleccion, el cazador acepta tu propuesta y te deja pasar.")
    # elegiste negociar, evitas el combate y pasas la prueba

elif opcion == "PELEAR":
    print("\nEl cazador 'hisoka' te derrota facilmente, no puedes pasar. Fin del juego ")
    exit()
    # omg decidiste pelear, te dieron mas coñazos que a saco e boxeo, y pierdes tt
    
elif opcion == "PEDIR_AYUDA":
    print("\ntu gran amigo killua te ayuda a derrotar al malvado hisoka, pasas la prueba.")
    
    # nuestro lindo angelito te ayuda a derrotar a ese hermoso hisoka, y pasas la prueba (merecido)
else:
    print("\nNo elegiste una opción válida. Te quedas paralizado y el cazador te derrota. Fin del juego.")
    exit()
    # por que elegirias una opcion que no esta? molleja

#Gon enfrenta su segunda prueba, esta vez no se encuentra solo, sino
#junto a su amigo Killua, quien siempre le acompaña 

#en esta prueba, Gon y Killua se encuentran en un bosque
#deben llegar al campamento base, antes de que anochezca
#este esta dividido en 3 caminos, elige el correcto para llegar al destino

opcion2 = input("Elige un camino (IZQUIERDA/CENTRO/DERECHA): ").strip().upper()

if opcion2 == "IZQUIERDA":
    #en este camino gon y killua se encuentran con una manada de lobos
    #y los lobos se los comen, rip
    print("\nGon y Killua fueron devorados por unos lobos malvados. Fin del juego.")
    print("tonto")
    exit()

elif opcion2 == "CENTRO":
    #un camino lleno de trampas!!!
    #Gon y killua caen en arenas movedizas, pero logran salir
    print("\nGon y Killua logran salir de las arenas movedizas, pero llegan tarde al campamento. Fin del juego. ")
    exit()

elif opcion2 == "DERECHA":
    #era el camino correcto, llegan al campamento base
    print("\nGon y Killua llegan al campamento base. Felcidades, han pasado la prueba.")
else:
    #no eligieron una opcion valida, se quedan perdidos en el bosque
    print("\nNo elegiste un camino válido. Te pierdes en el bosque y no llegas al campamento. Fin del juego.")
    print("como te vas a quedar quieto en un bosque ????????")
    exit()  

#Gon y Killua enfrenta su ultima prueba, deben enfrentarse nada mas y nada menos
#que al cazador mas hermoso de todos, CHROLLO 
#en esta prueba, deben elegir entre 3 armas para derrotarlo
 
 # lista de armas 
armas = ["ESPADA", "CAÑA_PESCA", "YOYOS"]

gon = input(f"elige una arma para gon de las siguientes {armas}: ").strip().upper()
#esto es para remover el arma elegida para gon 'listas'
if gon in armas:
    armas.remove(gon)  
else:
    print(" Gon eligió un arma no válida.")
    exit()

kill = input(f"elige un arma de las siguientd para killua {armas}: ").strip().upper()
#aqui supongo que vas a elegir un arma valida 

if gon == "ESPADA" and kill == "YOYOS":
    print("\nGon saca su espada con diamantes y la blande, killua saca sus super yoyos y derrotan al papasito de chrollo.")  
     #profe es que soy muy fan de kill y chrollo

elif gon == "CAÑA_PESCA" and kill == "ESPADA":    
    print("\nGon saca su antigua caña de pescar, killua su espada, pero esto no es sufienes y son derrotados por chrollo.")
     #suelta la caña miamor, por favor
    exit()

elif gon == "YOYOS" and kill == "CAÑA_PESCA":
    print("\nChrollo derrota a Gon y Killua. Fin del juego")
    #amigo, es al contrario, no viste como usa esos yoyos kill?
    exit()

elif gon == "ESPADA" and kill == "CAÑA_PESCA":
    print("\nLos super amigos no logran superar a chrollo, son derrotados. Fin del juego")
    exit()

elif gon == "CAÑA_PESCA" and kill == "YOYOS":
    print("\nDerrotan a Chrollo y lo hacen papilla. EASY PEASY ;) ")
    #la combinacion perfecta

elif gon == "YOYOS" and kill == "ESPADA":
    print("\nChrollo derrota a Gon y Killua. Fin del juego")
    exit()
else:
    print("\nGon y Killua no eligieron armas válidas. Fin del juego.")
    exit()

print("\nFelicidades, ayudaste a gon y kill a convertirse en cazadores ")
print("y derrotar al hermoso chrollo. ")

# chanchan chaaan, bonus tragico para no olvidar los traumas
print("\nEl momento más difícil... Gon y Kill deben separarse. TT")
print("Después de vencer a papiChrollo, han terminado el examen. Cada cazador debe tomar su propio camino.")

veryhard = input("¿Qué debe hacer Gon? (DESPEDIRSE/QUEDARSE/HUIR): ").strip().upper()

if veryhard == "DESPEDIRSE":
    print("\n'Gracias por todo', dice Gon. Kill sonríe entre lagrimas.")
    print("Se despiden... kill con el corazon roto y gon llorando a mares, pero sigue adelante.")
    #pinchegon
elif veryhard == "QUEDARSE":
    print("\nGon, eres la luz. A veces, brillas tan intensamente que tengo que mirar hacia otro lado")
    print("Pero aun asi, puedo quedarme a tu lado?")
    #frase ICONIC mi corazon hizo crack
    print("Gon responde: 'Siempre serás mi amigo, Killua'.")
    print("se abrazan pero saben que deben seguir cada uno su camino.")
    #fak mi corazon
elif veryhard == "HUIR":
    print("\nGon huye para evitar la despedida. Killua lo busca, pero nunca lo encuentra.")
    print("sin decir adiós, ambos siguen su camino y queda ese vacío eterno en sus corazones </3")
else:
    print("\nOpción no válida.LOS SEPARASTEEEE. Fin del juego.")
    #MAL AHII 
#bueno, ojala te guste, hasta llore y todo
#ojala este bueno, sino me muero