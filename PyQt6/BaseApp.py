from PyQt6.QtWidgets import QApplication, QWidget,  QVBoxLayout, QLabel, QPushButton, QLineEdit
from bs4 import BeautifulSoup
import requests


def get_currency(in_currency='USD', out_currency='EUR'):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    return rate


def get_currency2(in_currency='USD', out_currency='GBP'):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    return rate


def show_currenct():
    input_text = float(text.text())
    rate = get_currency()
    output_currency_value = rate * input_text
    output_label.setText(str(output_currency_value))


def show_currency_2():
    input_text2 = float(text.text())
    rate = get_currency2()
    output_currency_value = rate * input_text2
    output_label2.setText(str(output_currency_value))


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency converter')
layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)
text2 = QLineEdit()
layout.addWidget(text2)

btn = QPushButton('USD to EUR Convert')
layout.addWidget(btn)
btn.clicked.connect(show_currenct)


btn2 = QPushButton('USD to GPD Convert')
layout.addWidget(btn2)
btn2.clicked.connect(show_currency_2)


output_label = QLabel('')
layout.addWidget(output_label)

output_label2 = QLabel('')
layout.addWidget(output_label2)

window.setLayout(layout)
window.show()
app.exec()
