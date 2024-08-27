#1-
A = (10)
B = (20)
print (A, B)
A= B
B= A
print (A, B)
#2-
#3-A)sim B)não C)não
#5-
A = int(input ("digite um valor: "))
print(A-1)
#6-
A = int(input ("digite um valorda altura: "))
B= int(input ("digite um valorda lado: "))
print("a largura do terreno é de", A*B)
#7-
A = int(input ("digite quantos dias voce tem de vida: "))
B = int(input ("digite quantos meses voce tem de vida: "))
C= int(input ("digite quantos anos voce tem de vida: "))
if 12>=B:
   print ((365*C) + (30*B) + A, "dias vividos")
else:
      print("valor acima do limite de meses em uma ano")
#8-
A = float(input ("digite quantos eleitores tem no municipio: "))
B = float(input ("digite quantos brancos: "))
C = float(input ("digite quantos nulos: "))
D= (A-(B+C))
print ("são validos: " ,D)
print ("são nulos: ", C)
print ("são brancos: ", B)
print ("são validos: ", (D*100)/A,"%")
print ("sao nulos ", C*100/A,"%")
print ("são brancos: ", B*100/A, "%")
#9-
salario = float(input ("Informe seu salario mensal: "))
reajuste= float(input ("Informe o reajuste: "))
new_salario=((reajuste/100)*salario)+salario
print ("seu novo salario :",new_salario)
