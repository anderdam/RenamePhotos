import os

origem = os.chdir("C:\\Users\\adapp\\Desktop\\DigitalizacaoDeFotos\\teste")

i = 1000

for foto in os.listdir(origem):
    new_file_name = f"foto{i}.jpg"
    os.rename(foto, new_file_name)
    i += 1
