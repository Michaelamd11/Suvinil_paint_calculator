"""
Programa que checa Login e usuário, projetinho paeee
"""
from typing import Set, Union, List

import emoji

print('=' * 30)
print(emoji.emojize('HELLO WORD!!! :snake:'))
print('=' * 30)

nome = input('Digite seu nome: \n')
idade = input('Qual sua idade? \n')

while not idade.isdigit():
    print('Digite apenas números')
    idade = input('Digite a idade novamente: \n')
else:
    print(emoji.emojize(f'Seja bem vindo(a) {nome.title()}. :star-struck:'))

lista_usr = {'michael', 'omiichael', 'mlalmeida', 'ithaiz', 'thinska', 'thizinha', 'thins', 'thaiz'}

print('escolha um nome de usuário, \nusuário esse que você irá acessar o sistema.\n')
user = input()

while user in lista_usr:
    user = input('nome de usuário já em uso, \npor favor escolha outro.\n')
else:
    print(emoji.emojize('Usuário valido. :check_mark_button:'))

senha = input('Escolha  uma senha com no minimo 8 caracteres\n')
len(senha)

while len(senha) < 8:
    senha = input('Atenção!!! a senha deve ter no minimo 8 caracteres \nEscolha uma nova senha.\n')
    len(senha)
else:
    print(emoji.emojize('Usuário criado! =) :fire: :thumbs_up:'))

print('=' * 90)

print('Faça o Login no sistema SUVINIL')

usr_d = input('Digite o usuário:\n')
senha_d = input('Digite a senha:\n')

if senha_d != senha or usr_d != user:
    print('Máximo de 8 tentativas')

tenta = 1
logado = 0

while senha_d != senha or usr_d != user:
    print('usuário ou senha incorretos!!!\n')
    if tenta >= 8:
        print(emoji.emojize('Seu IP foi bloqueado por muitas tentativas incorretas :face_with_head-bandage:\n'
                            'tente novamente mais tarde ou contate o Suporte pelo fone:\n'
                            ' :telephone:(11) 2545-0079'))
        break
    else:
        usr_d = input('Digite o usuário novamente:\n')
        senha_d = input('Digite a senha novamente:\n')
        tenta += 1
else:
    print(emoji.emojize(f'Bem vindo ao sistema \nvocê está logado como o usuário: {user} :check_mark:'))
    logado = 1

if logado == 1:
    print('=' * 30)
    print('SUVINIL, A MARCA QUE PINTA COMO EU PINTO! \n calculadora de consumo de tinta.')
    altura = float(input('Digite em metros a altura da parede (EX: 2.30):\n'))
    comprimento = float(input('Digite em metros o Comprimento da parede (EX: 5.30):\n'))
    area = float(altura * comprimento)
    print('Sua parede tem uma area de {:.3f}².'.format(area))
    print('=' * 5)

    print('Agora escolha a tinta SUVINIL que vai utilizar na sua parede.')
    print('Temos: \n 1. SUVINIL Dense \n 2. SUVINIL Plus. \n 3. SUVINIL MAX 2.0 \n 4. SUVINIL Basic')
    tinta = input('Escolha o numero da opção\n')


list_tinta: List[Union[int, str]] = [1, '1', 2, ' 2', 3, '3', 4, '4']

while not tinta.isdigit():
    print('Digite apenas números')
    tinta = input('Escolha o numero da opção\n')

while tinta not in list_tinta:
    print('Ops! não temos essa opção, Para seguir é necessário selecionar uma opção existente. \n'
          'Ex: para tinta  ¨3. SUVINIL MAX 2.0¨, digite 3 e em seguida pressione enter.\n')
    print('1. SUVINIL Dense \n2. SUVINIL Plus. \n3. SUVINIL MAX 2.0 \n4. SUVINIL Basic')
    tinta = input('Escolha o numero da opção:\n')
    while not tinta.isdigit():
        print('Digite apenas números')
        tinta = input('Escolha o numero da opção\n')
else:
    print(f'Você escolheu a opção {tinta}')
    confirm = input('Aperte enter se escolheu a opção desejada,\n'
                    'caso queira escolher novamente, digite não e pressione enter para voltar.\n')
    while confirm != '':
        print('1. SUVINIL Dense \n2. SUVINIL Plus. \n3. SUVINIL MAX 2.0 \n4. SUVINIL Basic')
        tinta = input('Escolha o numero da opção:\n')
        print(f'Você escolheu a opção {tinta}')
        confirm = input('pressione enter no seu teclado se escolheu a opção desejada,\n'
                        'caso queira escolher novamente, digite não e pressione enter para voltar.\n')
        while tinta not in list_tinta:
            print('ATENÇÃO escolha uma opção existente e digite APENAS O NUMERO da OPÇÃO !!!!!!')
            tinta = input('Escolha o numero da opção\n')
            print(f'Você escolheu a opção {tinta}')
            confirm = input('pressione enter no seu teclado se escolheu a opção desejada,\n'
                            'caso queira escolher novamente, digite não e pressione enter para voltar.\n')

    if tinta == '1':
        print('Boa escolha, as tintas SUVINIL Dense, Possuem uma boa qualidade e firmeza, '
              'Material robusto para seus trabalhos.')
    elif tinta == '2':
        print('Boa, as tintas SUVINIL Plus, Vem com uma camada extra de verniz para melhorar o brilho e durabilidade')
    elif tinta == '3':
        print('Muito boa escola !!!, as tintas SUVINIL MAX 2.0, possui a mais alta tecnologia, alem de deixar aquele '
              'acabamento de primeira.')
    elif tinta == '4':
        print('Ótima escolha, a tinta SUVINIL Basic e a melhor pedida pra quem quer economizar')

    if tinta == '1':
        tint_esc = str('SUVINIL Dense')
    if tinta == '2':
        tint_esc = str("SUVINIL Plus")
    if tinta == '3':
        tint_esc = str('SUVINIL MAX 2.0')
    if tinta == '4':
        tint_esc = str('SUVINIL Basic')

    if tinta == '1' :
        ar_tin_esc = float(2 ** 2)
    elif tinta == '2':
        ar_tin_esc = float(3 ** 2)
    elif tinta == '3' :
        ar_tin_esc = float(4 ** 2)
    elif tinta == '4':
        ar_tin_esc = float(1 ** 2)

    litro = float(area / ar_tin_esc)
    q_lata = float(litro / 12)

    if q_lata >= 1.0:
        latas = float(litro / 12)
    else:
        latas = int(1)

    print('Calculando...\n \n OK, com a área de {:.3f}² e utilizando a tinta {} , que cobre uma área de {}²\n'
          'Você irá utilizar o total de {:.2f} litro(s) de tinta.'.format(area, tint_esc, ar_tin_esc, litro))
    print('Aconselhamos a compra de {} Lata(s) (12 Litros) da tinta {}'.format(latas, tint_esc))

print('=' * 50)
