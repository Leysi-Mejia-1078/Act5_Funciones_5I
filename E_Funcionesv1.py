print("Manejo de funciones V1")
def hola_mundo():
    print("Hola aquí estoy dentro de la función")

def mensa(msg):
    print(msg)

def EscribeNC(nombre, apellido):
    print(nombre,apellido)
    print(f"Tu nombre completo es {nombre} {apellido}")

def suma2numeros(n1,n2):
    s=n1+n2
    return f"La suma de {n1} y de {n2} es de: ",s

# Llamado a la funcion
hola_mundo()
mensa("Hola WhatsApp") # Llama a mensa como un parametro
mensa("El profe me sorprendió enciando mensajes") # LLama a mensa con un parametro
EscribeNC("Leysi", "Mejia")
print("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))
