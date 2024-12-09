#nome= input('Qual e o seu nome:')
#print('Prazer em te conhecer {}!'.format(nome))
#print('Prazer em te conhecer {:20}!'.format(nome))
#print('Prazer em te conhecer {:>20}!'.format(nome))
#print('Prazer em te conhecer {:=^10}!'.format(nome))


#Operadores aritimeticos
#n1 = int(input('Digite o primeiro numero:'))
#n2 = int(input('Digite o segundo numero:'))
#s = n1 + n2
#sub = n1 - n2
#m = n1 * n2
#di = n1 / n2
#p = n1 ** n2
#print('A soma é: {} ,  a subtração é: {}, \n a multiplicação é: {:.2f} e a divisão e: {:.2f}'.format(s, sub, di, m), end= ' >>> ')
#print('E por ultimo sua potencia é: {}'.format(p))




#5
#a =int(input('Digite um numero:'))
#ant = a - 1
#s = a + 1
#print('O antecessor desse numero é:{} e o seu sucessor é: {}'.format(ant, s))
# ou pode ser feito assim:
#print('Analisando o valor inserido {}, O antecessor desse numero é:{} e o seu sucessor é: {}'.format(a, (a-1), (a+1) ))


#6
#n = int(input('Digite um numero:'))
#m = n*2
#m1 = n*3
#di = n**(1/2)
#print('O dobro do numero digitado é: {}, o triplo é: {} e sua raiz quadrada é: {}'.format(m, m1, di))



#7
#n1 = float(input('Digite sua primeira nota:'))
#n2 = float(input('Digite sua segunda nota:'))
#n3 = float(input('Digite sua terceira nota:'))
#n4 = float(input('Digite sua quarta nota:' ))

#s = n1 + n2 + n3 + n4
#d = s // 4
#print('Sua media e: {:.1f}'.format(d))


#8

#metros = float(input('Digite o valor em metros:'))
#cm= metros*100
#mil = metros*1000
#print("o valor correposde á:{} centimetros e á {} milimetros".format(cm, mil))



#9
n = int(input('Digite um numero:'))
m = n*1, n*2, n*3, n*4, n*5, n*6, n*7, n*8, n*9, n*10
print('O resultado que procura é: {}'.format(m))
print('-'* 12)
print('{} * {:2} ={}'.format(n, 1, n*1))
print('{} * {:2} ={}'.format(n, 2, n*2))
print('{} * {:2} ={}'.format(n, 3, n*3))
print('{} * {:2} ={}'.format(n, 4, n*4))
print('{} * {:2} ={}'.format(n, 5, n*5))
print('{} * {:2} ={}'.format(n, 6, n*6))
print('{} * {:2} ={}'.format(n, 7, n*7))
print('{} * {:2} ={}'.format(n, 8, n*8))
print('{} * {:2} ={}'.format(n, 9, n*9))
print('{} * {:2} ={}'.format(n, 10, n*10))
print('-'* 12)



#10
#r= float(input('Quanto você tem na carteira?R$'))
#dolar = r/3.27
#print('O valor que você possui {:.2f}R$, pode ser comprado {:.2f} dólares'.format(r, dolar))



#11
#a=float(input('Digite a altura em metros:'))
#l=float(input('Digite a largura em metros:'))
#m = a*l
#tinta= m/2
#print('A altura é {} e a larhura sendo {}, então sua area é: {}'.format(a, l, m))
#print('A quantidade da tinta vai ser: {}'.format(tinta))



#12
#p=int(input('Digite o preço:R$'))
#novo= p-(p*5/100)
#print('O produto que custava R${:.2f}, após o desconto ficará R${:.2f}'.format(p, novo))


#13
#salario =float(input('Digite o seu salario:R$'))
#aumento= salario + (salario*15/100)
#print('Você ganhava {:.2f}R$, agora o seu novo salario após o aumento é de:R${:.2f}'.format(salario, aumento))


#14
#c=float(input('Digite a temperatura em C°:'))
#f= ((9*c)/5+32)
#print('O grau em Celsius{}, corresponde á {} fahrenheit'.format(c, f))


#15
dias = int(input('Quantos dias o carro ficou alugado?')) 
km = float(input('Quantos km o carro está?'))        
pago = (dias * 60) + (km * 0.15)
print('O total a ser pago é R${}'.format(pago))