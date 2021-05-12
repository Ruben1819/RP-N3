# Módulo para trabajar con CSV
import csv

# Clase de trabajo
class  Contacto:
    def __init__(self,USUARIO, NOMBRE, CORREO):
        self.USUARIO = USUARIO
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO

    def getNombre(self):
        return self.NOMBRE

    def __del__(self):
        print('Destructor llamado, Objeto contatos destruido (libera memoria del objeto).')
# Elaboro la lista de trabajo
Contactos = []

# Abrimos CSV y cargamos datos, usando separador |
# Se cargan en una lista de obetos (Contactos)
with open('contactos.csv', newline='') as archivo_csv:
    #lector_csv = csv.reader(archivo_csv, delimiter='|')
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    for e in lector_csv:
        Contactos.append(Contacto(e[0],e[1],e[2]))

# Podemos barrer Contactos, leyendo propiedades.
#print("Usuario              Nombre                        Correo")
for oe in Contactos:
    #print(oe.USUARIO)
    #print(oe.NOMBRE)
    #print(oe.CORREO)
    print(oe.USUARIO,"  ",oe.NOMBRE,"   ",oe.CORREO,"\n")

jose=Contacto("Maestro","José","Correo")
print("Destruir ojeto Jose")
del jose
#print(jose.getNombre())
#print(jose.NOMBRE)
# Aquí podría capturar nuevos datos, que agregaría a un objeto de tipo Contacto
# y ese objeto, podría cargarlo a la colección, y al final, pasar a un CSV.
