"""
Feito por:

Davi Henrique Comério
Gustavo Alves Caetano
João Pedro Zamborlini Barcellos

"""


import pickle
import os


def menu() -> None:
    """ Imprime o título """ 
    print('\n---------------------------------- O melhor programa de ordenação! ----------------------------------\n')


def read_file_bin(nome_arquivo: str) -> dict:
    """ Lê um arquivo binário e retorna o dicionário de alunos. """
    if file_exists(nome_arquivo):
        with open(f"{nome_arquivo}.bin", 'rb') as arquivo:
            return pickle.load(arquivo)
    else:
        return read_file_bin(read_file_name())


def file_exists(nome_arquivo: str) -> bool:
    """ Verifica se o arquivo existe. """
    return os.path.isfile(f"{nome_arquivo}.bin")


def read_file_name() -> str:
    """ Solicita ao usuário o nome do arquivo binário. """
    return input('Insira um nome de arquivo .bin existente nesta pasta: ')

def salvar_saida(ordenados: list, alunos: dict) -> None:
    """ Salva o arquivo de saída conforme especificação. """
    with open("saida.txt", "w") as f:
        limite_bonus = 5
        quinta_nota = calcular_nota_final(alunos[ordenados[limite_bonus - 1]])
        quinto_tempo = alunos[ordenados[limite_bonus - 1]][5]

        # Verifica se há empates no quinto lugar
        repetir = True
        i = limite_bonus
        while repetir and i < len(ordenados):
            nota_final = calcular_nota_final(alunos[ordenados[i]])
            tempo = alunos[ordenados[i]][5]
            if nota_final == quinta_nota and tempo == quinto_tempo:
                limite_bonus += 1
            else:
                repetir = False
            i += 1

        # Aplica o bônus e salva no arquivo
        for i, matricula in enumerate(ordenados):
            nome, *notas, tempo = alunos[matricula]
            nota_final = somar_notas(notas)

            # Aplica o bônus apenas para os primeiros `limite_bonus` alunos com nota máxima
            if i < limite_bonus and nota_final == 40:
                nota_final += 2

            f.write(f"{nome} {nota_final}\n")


def somar_notas(notas: list) -> int:
    """ Soma as notas da lista. """
    return notas[0] + notas[1] + notas[2] + notas[3]


def calcular_nota_final(aluno: list) -> int:
    """ Calcula a nota total do aluno. """
    return aluno[1] + aluno[2] + aluno[3] + aluno[4]


def quicksort(matriculas: list, alunos: dict, low: int, high: int) -> None:
    """ Implementação recursiva do QuickSort para ordenar a lista de matrículas. """
    if low < high:
        pi = partition(matriculas, alunos, low, high)
        quicksort(matriculas, alunos, low, pi - 1)
        quicksort(matriculas, alunos, pi + 1, high)


def partition(matriculas: list, alunos: dict, low: int, high: int) -> int:
    """ Particionamento do QuickSort seguindo os critérios de ordenação do professor. """
    pivot = matriculas[high]
    pivot_data = alunos[pivot]
    pivot_nota = calcular_nota_final(pivot_data)
    pivot_tempo = pivot_data[5]
    pivot_nome = pivot_data[0]
    pivot_matricula = pivot

    i = low - 1
    for j in range(low, high):
        aluno_data = alunos[matriculas[j]]
        aluno_nota = calcular_nota_final(aluno_data)
        aluno_tempo = aluno_data[5]
        aluno_nome = aluno_data[0]
        aluno_matricula = matriculas[j]

        if (nota_maior(aluno_nota, pivot_nota)) or \
        (desempate_por_tempo(aluno_nota, pivot_nota, aluno_tempo, pivot_tempo)) or \
        (desempate_por_nome(aluno_nota, pivot_nota, aluno_tempo, pivot_tempo, aluno_nome, pivot_nome)) or \
        (desempate_por_matricula(aluno_nota, pivot_nota, aluno_tempo, pivot_tempo, aluno_nome, pivot_nome, aluno_matricula, pivot_matricula)):
            i += 1
            matriculas[i], matriculas[j] = matriculas[j], matriculas[i]

    matriculas[i + 1], matriculas[high] = matriculas[high], matriculas[i + 1]
    return i + 1


def nota_maior(aluno_nota: int, pivot_nota: int) -> bool:
    """ Verificação de nota maior. """
    return (aluno_nota > pivot_nota)


def desempate_por_tempo(aluno_nota: int, pivot_nota: int, aluno_tempo: int, pivot_tempo: int) -> bool:
    """ Verificação de desempate por tempo. """
    return (aluno_nota == pivot_nota and aluno_tempo < pivot_tempo)


def desempate_por_nome(aluno_nota: int, pivot_nota: int, aluno_tempo: int, pivot_tempo: int, aluno_nome: str, pivot_nome: str):
    """ Verificação de desempate por nome. """
    return (aluno_nota == pivot_nota and aluno_tempo == pivot_tempo and aluno_nome < pivot_nome)


def desempate_por_matricula(aluno_nota: int, pivot_nota: int, aluno_tempo: int, 
    pivot_tempo: int, aluno_nome: str, pivot_nome: str, aluno_matricula: str, pivot_matricula: str):
    """ Verificação de desempate por matrícula. """
    return (aluno_nota == pivot_nota and aluno_tempo == pivot_tempo and aluno_nome == pivot_nome and aluno_matricula < pivot_matricula)


def main() -> None:
    # Display do menuzinho
    menu()

    # Leitura do arquivo bin
    dict_arquivo = read_file_bin(read_file_name())
    
    # Criação da lista só de matrículas
    matriculas = list(dict_arquivo.keys())

    # Ordenação recursiva com QuickSort
    quicksort(matriculas, dict_arquivo, 0, len(matriculas) - 1)

    # Salvando no arquivo de saída
    salvar_saida(matriculas, dict_arquivo)

    # Acabou
    print("Processamento concluído. Arquivo 'saida.txt' gerado com sucesso!")


if __name__ == "__main__":
    main()
    