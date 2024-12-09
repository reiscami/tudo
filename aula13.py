'''for c in range(1,10):
    print('oi')
print('Fim')'''


#for c in range (6, 0, -1): #conta para trás
    #print(c)


#for c in range (0, 7, 2): #contou de dois em dois
    #print(c)

#n = int(input('Digite um numero:'))
#for c in range (0, n+1):
    #print(c)


#i = int(input('Inicio:'))
#f = int(input('Fim:'))
#p = int(input('Passo:'))
#for c in range(i, f+1, p):
    #print(c)


#46
'''from time import sleep
for i in range (10, -1, -1):
    sleep(1)
    print(i)
print('\033[1;31mFOGOS\033[m')'''


#47
'''for i in range (0, 52, 2):
    print(i, end=' ')'''


#48
'''soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
       soma+= i
       cont += 1
print(f'A soma de todos os valores solicitados {cont} é {soma}')'''


#49

'''n =  int(input('Digite um número:'))
for i in range (0,11):
   print('{} * {:2} ={}'.format(n, i, n*i))''' #o i foi colocado para que o numero que o usuario digitou seja executado 10 vezes, um por um, assim formando a tabuada
  
    
#50
'''soma = 0
cont = 0
for c in range (1, 7):
  n = int(input('Digite {} valor:'.format(c)))
  if n  % 2 == 0:
    soma += n
    cont  += 1
print('Voce informou {} PARES, e a soma deles é: {}'.format(cont,soma))'''

#51
n = int(input('Digite o primeiro termo:'))
n2 = int(input('Digite a razão:'))
décimo =  n + (10 - 1) * n2
for c in range  (n, décimo+n2,n2):
    print(c, end= '-')  #o range foi colocado para que o programa execute de 1 a

