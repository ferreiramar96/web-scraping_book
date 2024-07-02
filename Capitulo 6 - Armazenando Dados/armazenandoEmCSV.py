import csv
import requests
from bs4 import BeautifulSoup

html = requests.get('http://en.wikipedia.org/wiki/''Comparison_of_text_editors')
bs = BeautifulSoup(html.content, 'html.parser')
# A tabela principal de comparação é atualmente a primeira tabela da página
table = bs.findAll('table',{'class':'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('editors.csv', 'wt+')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
    for cell in row.findAll(['td', 'th']):
        csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()