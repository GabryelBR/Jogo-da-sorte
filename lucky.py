import random
import time
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nVou pensar em um número de 0 a 10 tente advinhar !\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
n = int(input('Digite o número: '))
ia = random.choice([0,1,2,3,4,5,6,7,8,9,10])
cont = 1
while n != ia:
    n = int(input('\033[1;31mVocê errou\033[m, digite novamente: '))
    cont = cont + 1
time.sleep(1)
print('\033[1;32mVocê acertou\033[m, mas precisou tentar {} vezes para conseguir.'.format(cont))
