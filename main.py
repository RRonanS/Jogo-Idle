import PySimpleGUI as sg
from os import listdir
import os.path

a_dir = os.getcwd()

def set_destino(dest):
    if '.txt' not in dest:
        dest += '.txt'
    with open(f'../outros/destino.txt', 'w') as arq:
        arq.write(dest)


nome_jogo = 'Jogo Idle'
size = 400, 300
width, height = size
button_size = 8, 1
text_font = 'arial', 18
text_font2 = 'arial', 13
bc = 'dark blue'

layout = [
    [sg.Text(f'{nome_jogo}', font=text_font, background_color=bc, size=button_size)],
    [sg.Button('Novo jogo', font=text_font, key='jogar', size=button_size)],
    [sg.Button('Carregar partida', font=text_font, key='carregar', size=button_size)],
    [sg.Button('Sair', key='sair', font=text_font, size=button_size)]]

escolha_nome = [[sg.Text('Como deseja salvar o jogo:', font=text_font), sg.Input('', key='save_name', font=text_font2)],
                [sg.Button('Jogar', key='iniciar', font=text_font), sg.Button('Voltar', key='voltar', font=text_font)],
                [sg.Text('Erro, nome de arquivo vazio ou inválido', key='text_erro', visible=False)]]

disponiveis = [[sg.Text('Saves disponíveis:', font=text_font, background_color=bc)]]
for x in listdir('../saves'):
    nome = x
    disponiveis.append([sg.Button(f'{nome}', key=f'carregar_{nome}', font=text_font)])
disponiveis.append([sg.Button('Voltar', key='voltar2', font=text_font)])

layoutself = [[sg.Frame('', layout, element_justification='c', key='menu', border_width=2, font=text_font,
                        size=(width, height), background_color=bc),
               sg.Frame('', escolha_nome, element_justification='c', key='escolha_nome', background_color=bc,
                        font=text_font, visible=False),
               sg.Frame('', disponiveis, element_justification='c', key='escolha_carregar', background_color=bc,
                        font=text_font, visible=False)
               ]]

window = sg.Window('Menu', layoutself)

run = False
while True:
    event, values = window.read()
    print(event, values)
    if event is None or event == 'sair':
        break
    elif event == 'jogar':
        window.Element('escolha_nome').update(visible=True)
        window.Element('menu').update(visible=False)
    elif event == 'carregar':
        window.Element('escolha_carregar').update(visible=True)
        window.Element('menu').update(visible=False)
    elif 'voltar' in event:
        window.Element('escolha_nome').update(visible=False)
        window.Element('escolha_carregar').update(visible=False)
        window.Element('menu').update(visible=True)
    elif event == 'iniciar':
        save = values['save_name']
        if len(save) != 0:
            set_destino(save)
            run = True
            break
        else:
            window.Element('text_erro').update(visible=True)
    elif 'carregar' in event:
        dest = event.replace('carregar_', '')
        set_destino(dest)
        run = True
        break

window.close()
if run:
    print('Executando o jogo...')
    import codigos.game
    '''try:
        import codigos.game
    except Exception as e:
        print(f'Ocorreu um erro ao executar o jogo\n{e}')'''
