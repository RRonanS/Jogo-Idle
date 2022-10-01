from PIL import Image

'''nomes = ['casa', 'loja', 'condominio', 'bairro', 'municipio', 'cidade', 'estado', 'pais']
for nome in nomes:
    barraco = Image.open(f'fonte/{nome}.png')
    barraco = barraco.resize((32, 32))
    barraco.save(f'{nome}.png')'''

nome = 'arsenal nuclear'
barraco = Image.open(f'fonte/{nome}.png')
barraco = barraco.resize((32, 32))
barraco.save(f'{nome}.png')