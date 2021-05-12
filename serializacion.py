import pickle

lista_nombres=["Pedro","Ana","María","Isabel"]
fichero_binario=open("fichero_binario_lista_nombres","wb")
pickle.dump(lista_nombres,fichero_binario)
fichero_binario.close()
del (fichero_binario)


#Vamos a leer del fichero_binario_lista_nombres
fichero=open("fichero_binario_lista_nombres","rb")
lista=pickle.load(fichero)

print(lista)
fichero.close()
del (fichero)