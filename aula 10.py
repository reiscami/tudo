'''nome = str(input('Qual é o seu nome?'))
if nome == 'Camille':
  print('Que nome bonito você tem')
else:
  print('Amei o seu nome.')
print('Bom dia, Tenha um otimo dia, {}'.format(nome))'''

#n1= float(input('digite a primeira nota:'))
#n2=float(input('digite a segunda nota:'))
#n3= float(input('digite a terceira nota:'))
#n4=float(input('digite a quarta nota:'))
#m = (n1+ n2 + n3 + n4) / 4
#print('A sua media é: {}'.format(m))
#if m>=6.0:
    #print('Parabens, vocé nao ficou de recuperação')
#else:
    #print('Sua nota esta baixa, se esforce!')
#print('Parabens' if m>=6 else'Estude mais!')




#28
#from random import randint
#from time import sleep faz o computador esperar
#computador = randint(0,5)  #Faz o computador sortear
#computador= str(input('Eu vou pensar em um numero....PENSEI, tente adivinhar'))
#jogador = int(input('Eu acho que voce pensou nesse numero:'))
#print('Processando seu palpite.......')
#sleep(3)
#if jogador == computador:
    #print('PARABENS, dessa vez você venceu!')
#else:
    #print('PARABENS para mim, eu venci!')

'''n = int(input('escolha um numero entre 1 e 5:'))
lista = [1, 2, 3, 4, 5]
escolhido = random.choice(lista)
print('O numero escolhido foi: {}'.format(escolhido))
if n == escolhido:
    print('Você acertou!')
else:
    print('Você errou!')'''


#29
'''velocidade = int (input('velocidade que o veiculo estava: '))
if velocidade >80:
    print ('vc foi multado')
    multa = velocidade - 80
    valor = multa * 7
    print('vc foi multado em R$ ', valor)
else:
    print('vc nao foi multado, tenha um bom dia!')'''


#30
'''n = int(input('Digite um numero:'))
if n % 2==0:
    print('O numero {} e par'.format(n))
else:
    print('O numero {} é ímpar:'.format(n))'''


#31
'''viagem = int(input('Digite a distancia da sua viagem em km:'))
custo1 = viagem * 0.50
custo2 = viagem * 0.45
if viagem <=200:
    print('Sua viagem custará:{}'.format(custo1))
elif viagem >200:
    print('A sua viagem custará:', custo2)'''


#32
#from datetime import date
'''ano = int(input('Qual ano queres saber se e bissexto? ou apenas digite 0 para saber o ano que você está'))
if ano == 0:
   ano = date.today().year
if ano % 4==0 and % 100!=0 or ano % 400 ==0:
    print('{} é bissexto'.format(ano))
else:
    print('Não é bissexto')'''


#33
'''a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c 
print('O menor numero é: {}'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>b and b>c:
    maior = c
print('O maior numero é: {}'.format(maior))'''



#34
'''salario = float(input('informe o seu salário:'))
if salario <=1.250:
    novo = salario + (salario *15/100)
else:
    novo = salario + (salario *10/100)
print('Quem ganhava {}, agora passa a ganhar {}'.format(salario, novo))'''

#35

from time import sleep
print('<'*20)
sleep(1)
print('Analisador de triangulos, Teste já')
sleep(1)
print('>'*20)
sleep(1)
r1= float(input('Primeiro segmento:'))
r2= float(input('Segundo segmento:'))
r3= float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM formar um triangulo!') 
else:
    print('Os segmentos NÃO podem formar um triangulo')
