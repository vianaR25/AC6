#1
import random
contador_1 = 0
contador_2 = 0
contador_3 = 0
contador_4 = 0
contador_5 = 0
contador_6 = 0
for _ in range(100):
    
    resultado = random.randint(1, 6)

    
    if resultado == 1:
        contador_1 += 1
    elif resultado == 2:
        contador_2 += 1
    elif resultado == 3:
        contador_3 += 1
    elif resultado == 4:
        contador_4 += 1
    elif resultado == 5:
        contador_5 += 1
    elif resultado == 6:
        contador_6 += 1


print(f'Número 1: {contador_1} vezes')
print(f'Número 2: {contador_2} vezes')
print(f'Número 3: {contador_3} vezes')
print(f'Número 4: {contador_4} vezes')
print(f'Número 5: {contador_5} vezes')
print(f'Número 6: {contador_6} vezes')


#2 
import json


def ler_dados():
    nome = input("Nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        return None
    matricula = input("Matrícula do aluno: ")
    email = input("E-mail do aluno: ")
    return {"nome": nome, "matrícula": matricula, "e-mail": email}


dados_alu = {}


while True:
    aluno = ler_dados()
    if aluno is None:
        break
    matricula = aluno["matrícula"]
    dados_alu[matricula] = aluno


with open("alunos.json", "w") as arquivo_json:
    json.dump(dados_alu, arquivo_json, indent=4)

print("Dados dos alunos foram salvos no arquivo 'alunos.json'.")




#3
from datetime import datetime

def formatar_data(data_str):
    try:
        
        data = datetime.strptime(data_str, '%d/%m/%Y')

       
        meses_por_extenso = [
            "janeiro", "fevereiro", "março", "abril",
            "maio", "junho", "julho", "agosto",
            "setembro", "outubro", "novembro", "dezembro"
        ]

        
        data_formatada = data.strftime(f'%-d de {meses_por_extenso[data.month - 1]} de %Y')

        return data_formatada

    except ValueError:
        return None

data_input = input("Digite uma data no formato DD/MM/AAAA: ")
data_formatada = formatar_data(data_input)

if data_formatada:
    print(f'Data formatada: {data_formatada}')
else:
    print('Data inválida. Certifique-se de usar o formato DD/MM/AAAA.')



