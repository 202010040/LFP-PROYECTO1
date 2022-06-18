archivo = open (r"C:\Users\Compu Fire\Documents\LFP\PROYECTO 1\fuente.sc", 'r', encoding="utf8")
contenido = (archivo.read())
i = 0
for c in contenido:
    print (i, c)
    i +=1