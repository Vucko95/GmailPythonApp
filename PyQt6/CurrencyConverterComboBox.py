from PyQt6.QtWidgets import QApplication, QWidget,  QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests


def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    return rate


def show_currenct():
    input_text = float(text.text())
    in_cur = in_combo.currentText()
    target_cur = target_combo.currentText()
    rate = get_currency(in_cur, target_cur)
    output_currency_value = round(rate * input_text, 2)
    output_value_msg = f'{input_text} {in_cur}  is {output_currency_value}  {target_cur}'
    output_label.setText(output_value_msg)


app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency converter')
layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)


btn = QPushButton('USD to EUR Convert')
layout.addWidget(btn)
btn.clicked.connect(show_currenct)


in_combo = QComboBox()
curenncies = ['USD', 'EUR', 'GBP']
in_combo.addItems(curenncies)
layout.addWidget(in_combo)


target_combo = QComboBox()
target_combo.addItems(curenncies)
layout.addWidget(target_combo)


output_label = QLabel('')
layout.addWidget(output_label)

# output_label2 = QLabel('')
# layout.addWidget(output_label2)

window.setLayout(layout)
window.show()
app.exec()
