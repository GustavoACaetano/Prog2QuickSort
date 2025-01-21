import pickle


def menu():
    print('---------------------------------- O melhor programa de ordenação! ----------------------------------')
    print('')


def leArquivoBin(nomeArquivo):
    if (os.path.isfile(".bin")):
        with open('.bin', 'rb') as arq:
            jogadores = pickle.load(arq)


def main():
    

    return 0


if __name__ == "__main__":
    main()