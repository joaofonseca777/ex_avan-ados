#1-
A = 10
B = 20
print (A, B)
C=A
A = B
B = C
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
#11-
quant_car = float(input("quantos carros voce vendeu? "))
venda = float(input("quantas o valor das vendas que voce fez? "))
sal = float(input("qual seu salario fixo? "))
gan_ven = (5/100)*venda
sal_fin =sal+700
print("voce ganhou pela venda deste carro:", gan_ven)
print("sua remuneração será de: ", sal_fin+gan_ven)
#12-
far = float(input("quantos a atual temperatura em F? "))
cel=(far-32)/9
cel2=cel*5
cel_fin = "{:,.1f}".format(cel2)
print("a temperatura em celsius é: ", cel_fin )
#13-
n1 = float(input("informe a primeira nota: "))
n2 = float(input("informe a segunda nota: "))
n3 = float(input("informe a terceira nota: "))
media=((n1*2)+(n2*3)+(n3*5))/10
media_fin = "{:,.1f}".format(media)
print("sua nota final é : ", media_fin)
#14-
valor= float(input("informe um valor: "))
if 10 == valor:
    print("é 10!")
elif valor>=11:
    print("maior que 10!")
else:
   print("é menor que 10!")
   #15-
   valor= float(input("informe um valor: "))
if valor>= 0:
    print(valor, "é Positivo")

else :
    print(valor, "é negativo! ")
#16-
maca= float(input("informe um valor: "))
if maca<= 12:
    valor=maca*1.30
    print( "vai custar", valor)
else :
    valor=maca*1
    print( "vai custar ", valor)
    #17-
    
val1=float(input("insira um valor: "))
val2=float(input("insira outro valor: "))
soma=(val1+val2)/2  
if soma<=5.9:
        print("reporvado")
else: 
        print ("aprovado")
    #18-
    ano_atual=int(input("qual ano estamos? "))
ano_nasc=int(input("qual o ano do seu nascimento?"))
if (ano_atual-ano_nasc)>= 16:
   
    print( "voce pode votar")
else :
    
    print( "voce nao pode votar" )
    #19-val1=int(input("insira um valor: "))
val2=int(input("insira outro valor: "))

while True:
   
    if (val1 == val2):
        print ("________________________")
        print ("ERRADO TENTE DE NOVO!!!")
        print ("________________________")
        val1=int(input("insira um valor: "))
        val2=int(input("insira outro valor: "))
        continue
    elif (val1 >val2):
        print ("o primeiro é maior")
        break
    else:
        print("o segundo é maior")
        break
