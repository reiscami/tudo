'''frase = '            curso em Vídeo Python'
print(frase[3:16:2])'''

'''frase = 'Curso em Vídeo amor'''
'''print(frase.count('P'))'''
'''print(frase.upper().count('O'))'''
'''print(len(frase))'''
'''print(frase.strip())'''
'''print(frase.replace('Curso', 'Aula'))'''
'''print('Curso' in frase)'''
'''print(frase.capitalize())'''
'''print(frase.title())'''
'''print(''.join(frase))'''
''''print('Posição: {}'.format(frase.find('a')))'''


'''frase = 'Curso em Vídeo'
dividido = frase.split()
print(dividido[2][3])'''




#22
n = str(input('Digite o seu nome completo:')).strip()
print('Carregando as informações....')
print('O seu nome maiusculo é: {}'.format(n.upper()))
print('O seu nome misnusculo é: {}'.format(n.lower()))
print('O seu nome tem ao todo {} letras'.format((len(n) -n.count(' '))))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))


#23
'''num = int(input('Digite um numero entre 0 e 9999:'))
n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 & 10
print('Analisando o numero {}...'.format(num))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m)) '''  


#24
'''cid = str(input('Em qual cidade que você nasceu?')).strip()
print( cid [:5].upper() == 'SANTO')'''


#25
'''nome = str(input('Digite o seu nome completo?')).strip().upper()
print('Tem Silva ? {}'.format('SILVA' in nome))'''

#26
'''frase = str(input('Digite uma frase:')).strip()  
print('A letra "A" aparece: {}'.format(frase.count('a')))
print('A letra "A" aparece pela 1º vez na posição:{}'.format(frase.find('a')+1)) 
print('A letra "A" aparece pela ultima vez na posição:{}'.format(frase.rfind('a')+1))'''


#27
'''nome = str(input('Qual é o seu nome?')).strip().split()
print('Prazer em te conhcer {}!'.format(nome)) 
print('O seu primeiro nome é: {}'.format(nome[0])) 
print('E o seu ultimo nome é: {}'.format(nome[-1]))'''
