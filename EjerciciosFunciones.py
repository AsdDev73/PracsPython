#3. Crea una función que dados dos números mostrará todos los números que hay entre ellos.
"""
n=5
m=65

def nMedio(n,m):

    if (n>m):
        for x in range(m+1,n-1):
            print(x, end=" ")
    elif(m>n):
        for x in range(n+1,m-1):
            print(x, end=" ")
    else:
        print("Los numero son iguales")

nMedio(n,m)
"""
#3 En este ejercicio, escribirá una función que determine si la contraseña es buena o no.
#Definiremos una buena contraseña para que sea una que tenga al menos 8 caracteres y contenga al menos una letra mayúscula, al menos 
#una letra minúscula y al menos un número. el usuario e informa si es bueno o no.

def buenaContra(contrasena):
    if len(contrasena) < 8:
       print("No tiene 8 caracteres")
    
    for caracter in contrasena:
        if caracter.isupper():
            mayuscula = True
        elif caracter.islower():
            minuscula = True
        elif caracter.isdigit():
            numero = True
    
    return mayuscula and minuscula and numero


contra = input("Ingrese su contraseña: ")

buenaContra(contra)
