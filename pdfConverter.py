from fpdf import FPDF
pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()
pdf.image('bird.jpg', w=100, h=100)
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt="This is a Bird", align='C', border=2)
pdf.output('test.pdf')
