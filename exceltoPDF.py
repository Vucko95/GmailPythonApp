import pandas
import json
from fpdf import FPDF


data = pandas.read_excel('data.xlsx')
for index, row in data.iterrows():
    # print(row['name'])
    animal_text = row['name']
    # print(row)
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=f'{animal_text}',  ln=1)

    for column in data.columns[1:]:
        title = column.title()
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=100, h=25, txt=f'{title}')
        pdf.set_font(family='Times', style='B', size=8)
        pdf.cell(w=100, h=25, txt=row[column],  ln=1)

    pdf.output(f'{animal_text}.pdf')
