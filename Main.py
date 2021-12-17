import random
import time
import os
import sys
import collections

def func_texto_print(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.004)

def func_menu_info():
    print("\033[40;156;60m \t\t\t*** Menu do Game ***")
    print(""
        "((Bem vindo ao jogo adivinhe o número.))\n\033[m"
        "Acabei de pensar em um número entre 1 e 100. "
        "Tente descobrir esse número.\n"
        "Digite EXIT para parar de jogar.",
    )
    time.sleep(1)
    texto="..................................\n"
    func_texto_print(texto)

def func_new_game():
    jogar_novamente = input("Jogar novamente? ")

    if jogar_novamente.strip().lower() in ["s", "si", "sim"]:
        return

    print("Até a próxima!")
    sys.exit()

def func_new_info():
    print(
        "Legal! Acabei de pensar em outro número entre 1 e 100.\n"
        "Tente adivinhar, ou digite sair para finalizar o jogo.\n"
    )

def func_exit(opcao):
    if opcao.strip().lower() == "exit":
        print("\033[7;30;90m *** !OBRIGADO POR JOGAR, ATÉ UMA PROXIMA! ***\033[m")
        sys.exit()

def func_str_number(opcao):
    try:
        opcao = int(opcao)
        return opcao
    except ValueError:
        return None

def checar_palpite_correto(opcao, número_aleatório):
    if opcao > número_aleatório:
        ('O numero {} e Maior que o numero pensado..'.format(opcao))
    elif opcao < número_aleatório:
        print('O numero {} e Menor que o numero pensado..'.format(opcao))
    else:
        print("Parabéns! Você acertou!\n")
        return True
    return False

def func_mentalista():
    func_menu_info()
    número_aleatório = random.randint(1, 100)

    while True:
        opcao = input("Digite um número entre 1 e 100: ")
        func_exit(opcao)

        opcao = func_str_number(opcao)
        if opcao is None:
            print("Erro: Você deve digitar um número! Tente novamente.\n")
            continue

        if 1 <= opcao <= 100:
           opcao_correta = checar_palpite_correto(opcao, número_aleatório)
        else:
            print("Erro: O número deve estar entre 1 e 100! Tente novamente.\n")
            continue

        if opcao_correta:
            func_new_game()
            func_new_info()
            número_aleatório = random.randint(1, 100)

func_mentalista()