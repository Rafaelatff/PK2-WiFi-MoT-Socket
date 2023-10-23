
filename1 = "teste.txt"

print ("Arquivo gerado (irá aparecer na IDLE shell): %s" % filename1)
arquivo = open(filename1, 'w')

print ('Mensagem à ser salva no arquivo! Hello World',file=arquivo)

arquivo.close()
