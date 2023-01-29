import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

page = requests.get('https://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find("table", class_="mfd-currency-table")
output = []
output1 = []
new_output=[]

for row in table.findAll("tr"):
    new_row = []
    for cell in row.findAll(["td", "th"]):
        for sup in cell.findAll('sup'):
            sup.extract()
        new_row.append(cell.get_text().strip())
    output1.append(new_row[1::2])
    output.append(new_row)

for i in range(len(output1)):
    for j in range(len(output1[i])):
        new_output.append(output1[i][j])

new_output.pop(0)
result = list(map(float, new_output))
result = list(reversed(result))

for i in range(len(output)):
    for j in range(len(output[i])):
        print(output[i][j], end = ' ')
    print()
plt.plot(result)
plt.show()