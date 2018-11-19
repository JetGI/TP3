def main():
    f= open("textosimple","w+")
    #con "w" abrimos para escribir en un archivo y si no existe lo crea
    #con "+" abrira un archivo para leerlo y escribir actualizandolo

    for i in range(10):
        f.write("Esta es la linea %d\r\n" % (i+1))
    #con esa serie de caracteres indicamos que hasta 10 lineas lea una a una y muestre su numero
    f.close()

    #Abrimos el archivo anterior y leemos el contenido
    f=open("textosimple", "r")
    if f.mode == 'r': 
        contents =f.read()
        print (contents)

if __name__== "__main__":
  main()