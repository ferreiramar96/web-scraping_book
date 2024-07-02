import csv

csvFile = open('teste.csv', 'w+')

try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))

finally:
    csvFile.close()

'''Um lembrete como precaução: a criação de arquivos em Python é
razoavelmente à prova de balas. Se test.csv ainda não existir, Python criará
o arquivo (mas não o diretório) automaticamente. Se já existir, o arquivo
test.csv será sobrescrito com os novos dados.'''