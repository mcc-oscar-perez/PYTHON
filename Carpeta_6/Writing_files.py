#%%
# Abrimos archivo en modo solo lectura 
# Open the file in read-only mode

mi_archivo = open('Prueba.txt','r')
mi_archivo.close()


#%%

# Abrimos el archivo en modo escritura "w" el cual reemplaza o crea un contenido nuevo con el texto que deseemos imprimir 
# Open the file in write mode "w"  which replaces or creates new content with the text we want to print

mi_archivo = open('Prueba1.txt','w')

mi_archivo.write('''soy el nuevo texto. Ahora podemos 
escribir con saltos de linea colocando 
3 comillas simples''')

mi_archivo.close()

# %%

# Escribir un archivo pero ahora con writelines 
# Write a file but now with writlines

mi_archivo = open('Prueba1.txt','w')

mi_archivo.writelines(['uno','dos','tres','cuatro'])

# print(mi_archivo.read())


mi_archivo.close()
# %%
# Abrir el archivo y escribir pero desde la parte final del mismo con "a"
# Open the file and write but from the end of it with "a"

mi_archivo = open('Prueba1.txt', 'a')
mi_archivo.write(" Bienvenido nuevo texto ")


mi_archivo.close()

# %%
# Ejercicios practicos extra
# Exetra practical exercises 

# 1

archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

# 2 

archivo = open("mi_archivo.txt","a") 

archivo.write("Nuevo inicio de sesión")

archivo.close()

archivo = open("mi_archivo.txt","r")
print(archivo.read())



# 3 

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registro.txt","a")
for item in registro_ultima_sesion:
    registro.writelines(item +'\t')

registro.close()
registro = open("registro.txt","r")
print(registro.read())