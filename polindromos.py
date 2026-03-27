def polidromos (textos):
     textos = textos.lower().replace(" ", "")
     i = 0 
     j = len(textos) - 1 

     while i < j:
          if textos[i] != textos[j]:
               return False 
          i += 1
          j -= 1
     return True
     
while True:
    palabra = input(" introduce una palabra ( ´salir´ para salir del programa )): ")

    if palabra.lower()== "salir": 
        print("saliendo del programa")
        break
          
    if  polidromos(palabra):
          print("en un polidromo") 
    else: 
       print(" no es un polidromo")