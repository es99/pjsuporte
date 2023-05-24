import csv
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('usuarios')

linhas_dict = []

def limpa_cpf(cpf):
    cpf_limpo = ''
    for c in cpf:
        if (c != '.') and (c != '-'):
            cpf_limpo += c
    return cpf_limpo

with open('usuarios_infopublic.csv') as arquivo:
    arquivo_reader = csv.reader(arquivo)
    for row in arquivo_reader:
        row[0] = limpa_cpf(row[0])
        linhas_dict.append(row)

for row in linhas_dict:
    table.put_item(
        Item={
            'cpf': row[0],
            'nome': row[1],
            'tel': row[2],
            'rg': row[3],
            'email': row[4],
            'senha_ts': row[5],
            'senha_sistema': row[6],
            'data_cadastro': row[7]
        }
    )
