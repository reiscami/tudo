#nome = str(input('Qual é o seu nome?'))
#if nome == 'Camille':
    #print('Que nome lindo você tem, casa-se comigo!')
#elif nome == 'Maria' and nome == 'João':
    #print('O seu nome e muito popular aqui no Brasil.')
#else:
    #print('Gostei do seu nome!')
    #print('tenha um otimo dia {}{}{}!!!'.format('\033[1;33m', nome, '\033[m'))


#36
'''casa = float(input('Qual o valor do imovel que deseja comprar:'))
salario = float(input('Qual é o seu salário:'))
anos = int(input('Em quantos anos pretende pagar:'))
prestação = casa / (anos * 12)
minimo = salario * 30/100
print('Para pagar o imovel de R${} em {} anos a prestação ficara de R${}'.format(casa, anos, prestação))
if prestação <= minimo:
    print('O em prestimo foi APROVADO com sucesso')
else:
    print('NÃO fo aprovado')'''


#37

n = int(input('Digite um numero:'))
print(''' Escolha para qual base quer converter:
[1]Binário
[2]Octal
[3]Hexadecimal''')
opção = int(input('Qual sua escolha?'))
if opção == 1:
   print('O valor {} convertido para \033[33mBINÁRIO\033[m é: {}'.format(n, bin(n)))
elif opção == 2:
   print('O valor {} conertido para \033[36mOCTAL\033[m é: {}'.format(n, oct(n)))
elif opção == 3:
   print('O valor {} convertido para \033[31mHEXADECIMAL\033[m é: {}'.format(n, hex(n)))
else:
   print('\033[1;31;40mOPÇÃO INVAÍDA\033[m')

#38
'''a = int(input('Primeiro valor:'))
b =int(input('Segundo valor:'))
if a > b:
    print('O primeiro valor é maior')
elif a < b:
    print('O segundo valor é maior')
else:
    print('Os dois valores sao iguais')'''


#39
'''from datetime import date
print('\033[1;32;40mAlistamento Militar\033[m')
atual = date.today().year
nasc = int(input('Informe seu ano de nascimento:'))
idade = atual - nasc
print(f'Você nasceu em {nasc} e tem {idade} anos.')

if idade == 18:
    print('Já pode se alistar!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam \033[4m{saldo} anos \033[m.')
    ano = atual + saldo
    print(f'Seu alistamento será {ano}')
else:
    saldo = idade - 18
    print(f'Você deveria ter se alistado á \033[4m{saldo} anos\033[m.')
    ano = atual - saldo
    print(f'eu alistamento foi em \033[4m{ano}\033[m')'''


#40
'''n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
if media <=5:
    print(f'Com a primeira nota {n1} e a segunda {n2} a média do aluno é de {media}. Está \033[1;31mREPROVADO\033[m')
elif media >=5 and media <=7:
    print(f'Com a primeira nota {n1} e a segunda nota {n2}, sua média é {media}. Está de \033[4mRECUPERAÇÃO\033[m')
elif media >=7:
    print('O aluno está \033[1;34mAPROVADO\033[m')'''


#41
'''from datetime import date
atual = date.today().year
nasc =int(input('Digite a data de nascimento do atleta:')).strip()
idade = atual - nasc
print(f'Você nasceu em {nasc} e tem {idade} anos.')
if idade <=9:
    print(f'O atleta com {idade} anos é um nadador \033[33mMIRIM\033[m')
elif idade <=14:
    print(f'O atleta com {idade} é considerado um nadador \033[32mINFANTIL\033[m')
elif idade <=19:
    print(f'O atleta com a {idade} anos é considerado nadador \033[36mJUNIOR\033[m')
elif idade <=25:
    print(f'O atleta com {idade} anos é considerado nadador \033[35mSÊNIOR\033[m')
else:
    print(f'O atleta com a {idade} é considerado nadador \033[34mMASTER\033[m')'''



#42
'''from time import sleep
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

if r1 == r2 == r3:
    print('Os segmentos formam um triângulo \033[1;31mEQUILÁTERO\033[m')
elif r1 != r2 != r3 != r1:
    print('Os segmentos formam um triângulo \033[1;31mESCALENO\033[m')
else:
    print('Os segmentos podem formar um triângulo \033[1;31mISOSCÉLES\033[m')'''



#43
'''peso = float(input('Digite o seu peso:'))
alt = float(input('Digite a sua altura:'))

imc = peso / (alt**2)
print('Seu imc é:', imc)

if imc <16.9:
    print(f'Está Muito abaixo do peso')
elif imc >17 and imc <=18.4:
    print(f'Está abaixo do peso ideal')
elif imc >18.5 and imc <=24.9:
    print(f' Seu peso está proporcional aos seus dados')
elif imc >25 and imc <=29.9:
    print('Acima do peso')
elif imc >30 and imc <=34.9:
    print('Obesidade grau 1')
elif imc >35 and imc <=40:
    print('Obesidade grau 2')
else:
    print('Procure um médico!')'''



#44
#compras = float(input('Digite o valor das compras:R$'))
#print('{:=^40}'.format(' Formas de Pagamento '))
#print('''[1] á vista (dinheiro ou cheque)
#[2]á vista no Debito
#[3] 2x no cartão
#[4] 3x ou mais no cartão''')

'''opção = int(input('Qual é a opção?'))
if opção == 1:
    total = compras - (compras * 10/100 )
    print(f'Sua compra de {compras} saíra por {total}')
elif opção == 2:
    total = compras - (compras * 5/100)
    print(f'Sua compra de {compras} saíra por {total}')
elif opção == 3:
    total = compras 
    parcela = compras / 2
    print(f'Sua compra será parcelada em 2x. A primeira parcela será de {parcela}')
elif opção == 4:
    total = compras + (compras *20/100)
    parc= int(input('Quantas parcelas?'))
    parcela = total / parc
    print(f'Sua compra será parcelada em {parc}x e o valor da primeira parcela será de R${parcela}')
    print(f'Sua compra de {compras} vai acabar custando {total}, por causa do JUROS de 20%')
else:
    total = 0
    print('\033[1;31mOPÇÃO INVALÍDA\033[m. Tente novamente.')'''



#45
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)
print('''Suas opções:
[0]Pedra
[1]Papel
[2]Tesoura''')
jogador =int(input('Qual sua escolha?'))
print('>'*24)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('<'*24)

if computador == 0:
    if jogador == 0:
       print('\033[7;31mEMPATE\033[')
    
    elif jogador == 1:
       print('O JOGADOR VENCEU!')

    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
    else:
       print('\033[31mJOGADA INVALÍDA\033[m')

elif computador == 1:
    if jogador ==0:
       print('O COMPUTADOR VENCEU!')
    
    elif jogador == 1:
       print('\033[7;31mEMPATE\033[m')

    elif jogador == 2:
       print('O JOGADOR VENCEU!')
       
    else:
      print('\033[31mJOGADA INVALÍDA\033[31m')

elif computador == 2:
    if jogador == 0:
       print('O JOGADOR VENCEU!')
    
    elif jogador == 1:
       print('O COMPUTADOR VENCEU!')
    
    elif jogador == 2:
       print('\033[7;31mEMPATE\033[m')
    
    else:
     print('\033[31mJOGADA IVALÍDA\033[m')



