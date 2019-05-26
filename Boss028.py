import random
from time import sleep

nPC = random.randint(0, 5)
print('Jogo da advinhação !')

print('O computador(eu) pensei em um numero entre 0 e 5')
nUser = int(input('Usuario, Digite um numero de 0 á 5: '))

print('PROCESSANDO...')
sleep(3)

if nPC == nUser:
    print('Parabens usuario, voce venceu!')
else:
    print('Voce perdeu usuario, Eu pensei no numero: {}'.format(nPC))
print('Fim do jogo')

input('Fim da aplicação, pressioneENTER para continuar... ')
