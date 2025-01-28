"""
Feito por:

- Davi Henrique Comério
- Gustavo Alves Caetano
- João Pedro Zamborlini Barcellos
"""

import pickle
import os


def menu() -> None:
    print('---------------------------------- O melhor programa de ordenação! ----------------------------------')
    print('')


def read_file_bin(nome_arquivo: str):
    if (file_exists(nome_arquivo)):
        with open(f"{nome_arquivo}.bin", 'rb') as arquivo:
            alunos = pickle.load(arquivo)
    else:
        read_file_bin(read_file_name())
    return alunos


def file_exists(nome_arquivo: str):
    return os.path.isfile(f"{nome_arquivo}.bin")


def read_file_name():
    return input('Insira um nome de arquivo .bin existente nesta pasta: ')


def main():
    dict_arquivo = read_file_bin(read_file_name())
    matriculas = list(dict_arquivo.keys())
    print(matriculas)






    return 0


if __name__ == "__main__":
    main()
