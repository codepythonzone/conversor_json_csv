import json
import csv

def json_para_csv(arquivo_json, arquivo_csv):
	with open(arquivo_json, 'r') as json_file:
		dados = json.load(json_file)

		with open(arquivo_csv, 'w', newline='') as csv_file:
			escritor_csv = csv.writer(csv_file)

			cabecalho= dados[0].keys()
			escritor_csv.writerow(cabecalho)

			for linha in dados:
				escritor_csv.writerow(linha.values())

arquivo_json = 'exemplo.json'
arquivo_csv = 'saida.csv'

json_para_csv(arquivo_json,arquivo_csv)