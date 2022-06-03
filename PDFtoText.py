import fitz

with fitz.open("Malayan Tiger.pdf") as pdf:
    for page in pdf:
        print(page.get_text())
