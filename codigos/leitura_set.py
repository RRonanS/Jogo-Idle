import os.path

print('[Sistema] Carregando arquivo settings')
a_dir = os.getcwd().replace('codigos', '')
with open(f'{a_dir}/outros/settings.txt', 'r') as arq:
    linhas = arq.readlines()
temp = linhas[0].split()
try:
    size = int(temp[2].replace(',', '')), int(temp[3])
except:
    print(f'{temp} é um formato inválido, settings.txt linha 1\n usando default 600, 400')
    size = 600, 400
temp = linhas[1].split()
version = float(temp[2])

