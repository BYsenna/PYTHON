import random
import time
import os
import sys


def func_Escrever_Texto(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.004)


def func_menu_principal():
    print("\033[44;30;10m :*** Menu do Game ***\033[m")
    time.sleep(0.5)
    texto = "São essas as opções...\n"
    func_Escrever_Texto(texto)
    texto = "Opção 01 - Mentalista \n"
    func_Escrever_Texto(texto)


def func_menu_Jogo():
    opcao = int(input("Escolha:  "))
    if (opcao == 1):
        print('OPÇÃO JOGO DO MENTALISTA')
        x = func_randomizador()
        numero = 0
        func_mentalista(x, numero)
    elif (opcao == 2):
        print('OPÇÃO INVALIDA')
        func_menu_Jogo(x, numero)
    else:
        func_menu_principal()
        func_menu_Jogo()


def func_titulo():
    print('(((      Bem vindo ao Gamer da Sorte     )))')
    print('     Você está preparado para iniciarmos?...')
    texto = ('Pressione ENTER....')
    func_Escrever_Texto(texto)
    input()
    texto = "Entendi.. então iremos começar...\n"
    func_Escrever_Texto(texto)


def func_randomizador():
    numero_gerado = random.randint(1, 100)
    return numero_gerado


def func_mentalista(x, numero):
    while True:
        chute = int(input('Chute um numero de 0 a 100: '))
        if (chute > 100 or chute < 0):
            print("OPÇÃO INVALIDA..")
        elif (chute > x):
            print('Numero pensado: {}'.format(x))
            print('O numero {} que você digitou e Maior que o numero pensado..'.format(chute))
        elif (chute < x):
            print('Numero pensado: {}'.format(x))
            print('O numero {} que você digitou e Menor que o numero pensado..'.format(chute))
        elif (chute == x):
            print('Numero pensado: {}'.format(x))
            print('Parabéns.. você acertou.. ')
            print('O numero pensado foi {}'.format(chute))
            opcao = str(input('Ainda deseja jogar....(S/N): '))
            if opcao.lower() == 's':
                print('Parabéns.. Reiniciando jogo..')
                time.sleep(2)
                x = func_randomizador()
                numero = 0
                func_mentalista(x, numero)
                return ()
            elif opcao.lower() == 'n':
                texto = "(S) Exit, (M) Menu..."
                func_Escrever_Texto(texto)
                xcod = str(input("..: ")).lower()
                if (xcod == 's'):
                    print('Parabéns, Finalizando o Jogo!!..')
                    sys.exit()
                    break
                if (xcod == 'm'):
                    x = func_randomizador()
                    numero = 0
                    func_mentalista(x, numero)

func_titulo()
func_menu_principal()
func_menu_Jogo()