import PySimpleGUI as sg
import os.path
from codigos.leitura_set import size, version
from PIL import Image
# Arrumar para reiniciar tudo sem precisar fechar o jogo
# No modo desenvolvedor, botão para reler o txt
# Reajustar codigo usando classes
# Exército custar população
a_dir = os.getcwd()

with open(f'{a_dir}/outros/destino.txt', 'r') as arq:
    dest = arq.readlines()[0]

if os.path.exists(f'{a_dir}/saves/{dest}'):
    pass
else:
    print(f'[Sistema] {dest} não foi encontrado, criando arquivo')
    file = open(f'{a_dir}/saves/{dest}', 'w')
    file.write('')

width, height = size
tela_cheia = 'False'
admin_password = '000000'
passwords = ['666666', '123968', '997788']
print(f'[Sistema] Versão: {version}')
tempo_sessao = 0
multiplicador_prestigio = 0.000025
banco = 0
admin_mode = 'False'
background = 'black'
cores={'verde': 'green', 'preto': 'black', 'roxo': 'purple', 'vermelho': 'red'}
print('[Sistema] Iniciando')


def limpartxt():
    with open(f'{a_dir}/saves/{dest}', 'w') as v:
        v.write('')


player_data = {'nome':'nda','din':40,'ouro':0,
               'barraco':0,'apartamento':0,'casa':0,'loja':0,'condominio':0,'bairro':0,'município':0
               ,'cidade':0,'estado':0,'país':0,'banco':0
               ,'quartel':0,'batalhão':0,'brigada':0,'aeroporto militar':0,'arsenal nuclear':0}
i1 = {'nome':'barraco','preço':40,'inflacao':0,'lucro':3,'melhoria':10000,'nivel':0,'preço_base':40,'lucro_base':2,'melhoria_base':10000}
i2 = {'nome':'apartamento','preço':2000,'inflacao':0,'lucro':10,'melhoria':50000,'nivel':0,'preço_base':2000,'lucro_base':8,'melhoria_base':50000}
i3 = {'nome':'casa','preço':24000,'inflacao':0,'lucro':110,'melhoria':600000,'nivel':0,'preço_base':24000,'lucro_base':100,'melhoria_base':600000}
i4 = {'nome':'loja','preço':180000,'inflacao':0,'lucro':780,'melhoria':4500000,'nivel':0,'preço_base':180000,'lucro_base':750,'melhoria_base':4500000}
i5 = {'nome':'condominio','preço':900000,'inflacao':0,'lucro':3900,'melhoria':22500000,'nivel':0,'preço_base':900000,'lucro_base':3750,'melhoria_base':10000}
i6 = {'nome':'bairro','preço':10000000,'inflacao':0,'lucro':40000,'melhoria':250000000,'nivel':0,'preço_base':10000000,'lucro_base':40000,'melhoria_base':22500000}
i7 = {'nome':'município','preço':85000000,'inflacao':0,'lucro':280000,'melhoria':2125000000,'nivel':0,'preço_base':85000000,'lucro_base':280000,'melhoria_base':2125000000}
i8 = {'nome':'cidade','preço':500000000,'inflacao':0,'lucro':1000000,'melhoria':12500000000,'nivel':0,'preço_base':500000000,'lucro_base':1000000,'melhoria_base':12500000000}
i9 = {'nome':'estado','preço':2000000000,'inflacao':0,'lucro':3000000,'melhoria':50000000000,'nivel':0,'preço_base':2000000000,'lucro_base':3000000,'melhoria_base':50000000000}
i10 = {'nome':'país','preço':1000000000000,'inflacao':0,'lucro':12000000,'melhoria':25000000000000,'nivel':0,'preço_base':1000000000000,'lucro_base':12000000,'melhoria_base':25000000000000}
i11 = {'nome':'banco','preço':10000000000000,'inflacao':0,'lucro':1,'melhoria':50000000000000,'nivel':0,'preço_base':10000000000000,'lucro_base':1,'melhoria_base':50000000000000}
itens = []
itens.append(i1)
itens.append(i2)
itens.append(i3)
itens.append(i4)
itens.append(i5)
itens.append(i6)
itens.append(i7)
itens.append(i8)
itens.append(i9)
itens.append(i10)
itens.append(i11)
itens_backup=itens

niveis = {0:'melhorado',1:'gigante',2:'super',3:'Deluxe',4:'Ultra',5:'Mega'}
loja = []
l1 = {'nome':'dinheiro inicial','preço':2000,'efeito':'aumenta em 200% o dinheiro inicial','qtd':0}
l2 = {'nome':'lucro geral','preço':5000,'efeito':'aumenta em 50% o lucro de todas as propriedades','qtd':0}
l3 = {'nome':'ganho de ouro','preço':5000,'efeito':'aumenta em 10% o ganho de ouro após ascender','qtd':0}
l4 = {'nome':'banco','preço':30000,'efeito':'libera a compra da propriedade banco com dinheiro e que gera ouro','qtd':0}
l5 = {'nome':'upgrades barateados','preço':3000,'efeito':'diminui em 20% o custo de todos os upgrades','qtd':0}
loja.append(l1)
loja.append(l2)
loja.append(l3)
loja.append(l4)
loja.append(l5)

exercito=[]
e1 = {'nome':'quartel','preço':100000,'poder':1000,'manutençao':1000,'inflacao':0}
e2 = {'nome':'batalhão','preço':5000000,'poder':50000,'manutençao':40000,'inflacao':0}
e3 = {'nome':'brigada','preço':100000000,'poder':1000000,'manutençao':750000,'inflacao':0}
e4 = {'nome':'aeroporto militar','preço':2000000000,'poder':20000000,'manutençao':15000000,'inflacao':0}
e5 = {'nome':'arsenal nuclear','preço':1000000000000,'poder':10000000000,'manutençao':5000000000,'inflacao':0}
exercito.append(e1)
exercito.append(e2)
exercito.append(e3)
exercito.append(e4)
exercito.append(e5)


ler = open(f'{a_dir}/saves/{dest}', 'r')
linhas = ler.readlines()
mostra = ler.read()
print('[Sistema] Verificando dados')
if len(linhas)!=0:
    print('[Sistema] Save encontrado, baixando dados')
    from codigos.armazenamento import player_data_leitura,idata_leitura,loja_leitura,multiplicador_prestigio_leitura,tempo_sessao_leitura,admin_mode_leitura,banco_leitura,tela_cheia_leitura
    from codigos.armazenamento import background_leitura, admin_password_leitura
    background = background_leitura
    player_data = player_data_leitura
    itens = idata_leitura
    banco = int(banco_leitura)
    multiplicador_prestigio = multiplicador_prestigio_leitura
    tempo_sessao = tempo_sessao_leitura
    admin_mode = admin_mode_leitura
    tela_cheia = tela_cheia_leitura
    admin_password = admin_password_leitura
    for x in loja:
        for y in loja_leitura:
            if x['nome'] == y['nome']:
                x['preço'] = y['preço']
                x['qtd'] = y['qtd']
    from codigos.armazenamento import version_leitura
    if version > version_leitura:
        print('[Sistema] Nova versão de jogo detectada, atualizaremos seus dados, '
              'verifique as notas de atualziação para saber mais')
        sg.Popup(f'Seu jogo foi atualizado para a versão {version} , veja as novidades nas notas de atualização')
else:
    print('[Sistema] Nenhum save encontrado, começando do zero!')


def gera_tela():
    print('[Sistema] plano de fundo:', background)
    t_f = 'arial', 15
    t_f2 = 'arial', 13
    t_f3 = 'arial', 12
    t_fg = 'arial', 18
    b_s = 1, 1
    b_s2 = 11, 2
    b_s3 = 5, 1
    b_s4 = 8, 1
    b_c = 'black'

    tela_exercito = []
    for coisa in exercito:
        ver = True
        nome = coisa['nome']
        tela_exercito += [[sg.Image(f'{a_dir}/imagens/{nome}.png', tooltip=f'{nome}'),
                           sg.Button('Comprar', key='comprar'+nome,
                                     tooltip='Gasta '+str(coisa['manutençao'])+'/s', visible=ver, font=t_f3, size=b_s4),
                            sg.Text(' '*12, key='preço'+nome, visible=ver, text_color='light green', font=t_f3)]]
        tela_exercito += [[sg.Text('Atual: ', visible=ver, key='atualtxt'+nome, font=t_f3),
                           sg.Text(' '*11, key='atual_'+nome, visible=ver, font=t_f3)]]
    tela_exercito += [[sg.Text('Poder militar: ', font=t_f2), sg.Text(' '*20, key='podermilitar', font=t_f2)]]
    tela_banco = [
        [sg.Text('10% do valor escolhido será guardado e protegido mesmo após resetar\nCusta 1000 de ouro.',
                 text_color='yellow', font=t_f2)],
        [sg.Text('Valor guardado:', font=t_f3), sg.Text(' '*30, key='guardado', font=t_f3)],
        [sg.Input('Valor para guardar', key='depositar_valor', font=t_f3),
         sg.Button('Guardar', key='guardar', font=t_f2),
         sg.Button('Retirar', key='retirar', font=t_f2)],
        [sg.Button('10%', font=t_f2), sg.Button('25%', font=t_f2),
         sg.Button('50%', font=t_f2), sg.Button('100%', font=t_f2)],
        [sg.Text('Erro, valor inválido ou dinheiro insuficiente', key='guardarerro', text_color='red',
                 visible=False, font=t_f3),
         sg.Text('Operação realizada com sucesso!', key='guardarsucesso', text_color='green', visible=False, font=t_f3)]
    ]
    tela_principal = [
        [sg.Image(f'{a_dir}/imagens/dinheiro.png'), sg.Text(' '*15, key='din', text_color='light green', font=t_f)
            , sg.Image(f'{a_dir}/imagens/ouro.png'), sg.Text(' '*15, key='ouro', text_color='yellow', font=t_f)
            , sg.Image(f'{a_dir}/imagens/populacao.png'), sg.Text(' '*20, key='pop', text_color='red', font=t_f),
         sg.Button(':', key='optionsclick', size=b_s, font=t_f),
         sg.Button('+', key='somarouro', visible=True, button_color='yellow',size=b_s),
         sg.Button('+', key='somardin', visible=True, button_color='light green', size=b_s)]]
    tela_comprar=[[], []]
    lista = [[] for i in range(10)]
    num = 0
    x = 0
    y = 1
    cont = 0
    for item in itens:
        num += 1
        ver = True
        if item['nome'] == 'banco':
            pass
        else:
            nome = item['nome']
            lista[x].append(sg.Image(f'{a_dir}/imagens/{nome}.png', key=f'img_{nome}'))
            lista[x] += sg.Button(nome.capitalize(), key='comprar'+nome, button_color='black',
                                  tooltip='Produz '+str(item['lucro'])+'/s', visible=ver, font=t_f2),\
                        sg.Text(' '*20, key='preço'+nome, visible=ver, text_color='light green', font=t_f2)
            lista[y] += sg.Text('Atual: ', visible=ver, key='atualtxt'+nome, font=t_f3),\
                        sg.Text(' '*11, key='atual_'+nome, visible=ver, font=t_f3)
            cont += 1
            if cont % 2 == 0 and cont != 0:
                x += 2
                y += 2
    tela_comprar += lista

    l_hora = [[sg.Text('Dinheiro:', font=t_f2, text_color='light green'), sg.Text(' '*15, key='lucroseg', font=t_f3),
             sg.Text('Ouro:', font=t_f2, text_color='yellow'), sg.Text(' '*15, key='ouroseg', font=t_f3)]]

    l_options = [[sg.Button('Propriedades', key='propriedades', button_color=b_c, font=t_fg,),
                sg.Button('Exército', key='mostrarexercito', button_color=b_c, font=t_fg),
                sg.Button('Upgrade',key='upgrade', button_color=b_c, font=t_fg),
                sg.Button('Ascenção', key='ascencao', button_color=b_c, font=t_fg),
                sg.Button('Loja', key='abrirloja', button_color=b_c, font=t_fg),
                sg.Button('Banco', key='abrirbanco', button_color=b_c, font=t_fg)]]
    l_menuopcoes = [[sg.Button('Reiniciar jogo', key='reset', size=b_s2, font=t_f3)],
                  [sg.Button('Confirmar', key='resetconfirmar', visible=False, button_color='red', font=t_f3),
                   sg.Button('Cancelar', key='resetcancelar', visible=False,button_color='red', font=t_f3)]
                  , [sg.Checkbox('Tela cheia', key='telacheia', enable_events=True, size=b_s2, font=t_f3)]
                  , [sg.Text('Plano de fundo:', font=t_f3)],
                  [sg.Button('Vermelho', key='vermelho', button_color='red', size=b_s4),
                   sg.Button('Preto', key='preto', button_color='black', size=b_s4)
                   , sg.Button('Roxo', key='roxo', button_color='purple', size=b_s4),
                   sg.Button('Verde', key='verde', button_color='green', size=b_s4)]
                  , [sg.Text('Discord do dev: RRonan#3260', font=t_f3)],
                  [sg.Text('Tempo total de jogo:', font=t_f3),sg.Text(' ' * 100, key='exibirtempojogo', font=t_f3)],
                  [sg.Text('Vesão do jogo: '+str(version)+' beta', font=t_f2)]]
    l_mult = [[sg.Button('1x', size=b_s3, font=t_f3),
               sg.Button('10x', size=b_s3, font=t_f3), sg.Button('100x', size=b_s3, font=t_f3),
               sg.Button('1000x', size=b_s3, font=t_f3), sg.Text('1x       ', key='mult', size=b_s3, font=t_f3)]]

    l_upgrade = []
    g_cont = 0
    grupamento = []
    for item in itens:
        grupamento.append(sg.Button(item['nome']+' melhorado', button_color='black', key=item['nome']+'melhoriatext',
                                    font=t_f2))
        grupamento.append(sg.Text(' '*12, key=item['nome']+'melhoradocusto', text_color='light green', font=t_f3))
        if g_cont == 1:
            l_upgrade.append(grupamento)
            grupamento = []
            g_cont = 0
        else:
            g_cont += 1
    if grupamento:
        l_upgrade.append(grupamento)
    l_upgrade.append([sg.Text('* Cada melhoria duplica o ganho proveniente da propriedade', font=t_f3)])

    l_ascencao=[[sg.Button('Ascender', key='prestigio', size=b_s2, font=t_f3),
                 sg.Text(' '*100, key='ouroganhar', font=t_f3)],
                [sg.Button('Confirmar', key='asconfirmar', button_color='red', visible=False,),
                 sg.Button('Cancelar', key='ascancelar', button_color='red', visible=False)]]
    l_loja=[]
    for coisa in loja:
        l_loja += [[sg.Button(coisa['nome'], tooltip=coisa['efeito'], button_color='yellow',
                              key='loja'+str(coisa['nome']), font=t_f2, size=b_s4),
                    sg.Text(str(coisa['preço'])+' ouro',
                            text_color='yellow', key=coisa['nome']+'preço', font=t_f3)]]
    l_loja += [[sg.Button('banco'.capitalize(), key='comprar' + 'banco', button_color='black',
                          tooltip='Produz ' + '1' + '/s', visible=False, font=t_f2, size=b_s4),
                  sg.Text(' ' * 12, key='preço' + 'banco', visible=False, text_color='light green', font=t_f3)]]
    l_loja += [
        [sg.Text('Atual: ', visible=False, key='atualtxt' + 'banco', font=t_f3),
         sg.Text(' ' * 11, key='atual_' + 'banco', visible=False, font=t_f3)]]
    print('[Sistema] Criando layout')
    layout = [[sg.Frame('',tela_principal, element_justification='center', visible=True, size=(width, 35))],
            [sg.Frame('', l_upgrade, element_justification='left', visible=False, key='upgradescreen'),
            sg.Frame('',tela_comprar, element_justification='center', key='comprarscreen', visible=True,
                     size=(width, height*0.53)),
            sg.Frame('',l_menuopcoes,key='options',visible=False,element_justification='ce'),
            sg.Frame('',l_ascencao,key='ascender',visible=False,element_justification='ce'),
            sg.Frame('',tela_exercito,key='telaexercito',visible=False,element_justification='ce'),
            sg.Frame('', tela_banco, key='telabanco', visible=False, element_justification='left'),
            sg.Frame('', l_loja, key='loja', visible=False, element_justification='ce')],
            [sg.Frame('', l_hora,element_justification='center', visible=True, key='dinseg', size=(width//2, 48)),
             sg.Frame('', l_mult, element_justification='center', visible=True, key='lmult', size=(width//2, 48))],
            [sg.Frame('', l_options, element_justification='center', key='barradeopçoes', visible=True)]]

    layout = [[sg.Frame('', layout, size=size, element_justification='c')]]
    window = sg.Window('Idle', layout, finalize=True, element_justification='ce',
                       background_color=background, size=size)
    if tela_cheia in 'True':
        window.maximize()
    print('[Sistema] tela cheia = ', tela_cheia)
    return window


window = gera_tela()

print('[Sistema] definindo variáveis')
tempo=0
lseg=0
qtd_pessoas=0
prestigio_a_ganhar=0
ouro_produzido=0
mult=1
podermilitar_exiba=0
cooldown=0
p_f = 'bold', 15


def eventos():
    from random import randint,choice
    chance=randint(1, 300)
    if chance>=299:
        print('[Evento] aconteceu um evento')
        evento=randint(1,6)
        if evento==1 or evento==2 or evento==3:
            print('[Evento] do tipo desastre')
            valor=int(player_data['din']*(randint(1,15)/10))
            if valor<0:
                valor=valor*-1
            sg.popup(f'Aconteceu um desastre natural você irá desembolsar {exiba(valor)} para reparos', font=p_f)
            player_data['din']-=valor
        elif evento==4 or evento==6:
            print('[Evento] do tipo dinheiro')
            valor=int(player_data['din']*(randint(1,300))/10)
            if valor<0:
                valor=valor*-1
            sg.Popup(f'Você encontrou {exiba(valor)} de dinheiro num barraco abandonado', font=p_f)
            player_data['din']+=valor
        elif evento==5:
            print('[Evento] do tipo escritura')
            escolha=choice(itens)['nome']
            while escolha=='país':
                escolha = choice(itens)['nome']
            while escolha=='banco':
                escolha = choice(itens)['nome']
            sg.popup(f'Você achou uma escritura de {escolha} que agora será seu(sua)', font=p_f)
            player_data[escolha]+=1


def exiba(num):
    resultado=''
    if num<0:
        num=num*-1
    add=7
    if num>=1000:
        resultado=str('{:.2f}'.format(num/1000))+'K'
    if num<1000:
        resultado=num
    if num>=1000000:
        resultado=str('{:.2f}'.format(num/1000000))+'M'
    if num>=1000000000:
        resultado=str('{:.2f}'.format(num/1000000000))+'B'
    if num >= 1000000000000:
        resultado = str('{:.2f}'.format(num / 1000000000000)) + 'T'
    if num >= 1000000000000000:
        resultado = str('{:.2f}'.format(num / 1000000000000000)) + 'Q'
    if num>=10000000000000000:
        while num>=10000000000000000:
            num=num/10
            add+=1
        resultado=(str(exiba(num)) + '^'+str(add))
    return resultado


def pessoas():
    global qtd_pessoas
    qtd_pessoas=((player_data['barraco']*2)+(player_data['apartamento']*3)+(player_data['condominio']*200)
                 +(player_data['bairro']*2500)+(player_data['município']*10000)+(player_data['cidade']*100000)
                 +(player_data['estado']*1000000+player_data['país']*15000000))
    return qtd_pessoas


def lucro(*arg):
    lucro=0
    produz_ouro=0
    for item in itens:
        if item['nome']=='banco': produz_ouro+=player_data['banco']*0.1
        else:
            lucro+=player_data[item['nome']]*item['lucro']
    for item in exercito:
        lucro+=(-(player_data[item['nome']]*item['manutençao']))
    if False not in arg:
        player_data['din']+=lucro
    global ouro_produzido
    ouro_produzido= produz_ouro
    if False not in arg:
        player_data['ouro']+=produz_ouro
    global lseg
    lseg=lucro


def atualizar(*arg):
    lucro(arg)
    eventos()
    window.Element('pop').update(exiba(pessoas()))
    window.Element('exibirtempojogo').update(segundosparastr(tempo_sessao))
    if player_data['país']>0:
        ataques(0)
    if l4['qtd']!=0:
        window.Element('comprarbanco').update(visible=True)
        window.Element('lojabanco').update(visible=False)
        window.Element('bancopreço').update(visible=False)
        window.Element('preçobanco').update(visible=True)
        window.Element('atualtxtbanco').update(visible=True)
        window.Element('atual_banco').update(visible=True)
    global mult
    global lseg
    for item in itens:
        while item['inflacao']!=0:
            item['preço']=int(item['preço']+0.5*item['preço'])
            item['inflacao']-=1
        if player_data['din']>=(int(item['preço']+(mult-1)*0.5*item['preço'])):
            window.Element('comprar'+item['nome']).update(button_color='green')
        if player_data['din']<(int(item['preço']+(mult-1)*0.5*item['preço'])):
            window.Element('comprar'+item['nome']).update(button_color='black')
        if item['nivel']>=len(niveis)-1:
            window.Element(item['nome']+'melhoriatext').update(button_color='red')
        else:
            if player_data['din']<item['melhoria']:
                window.Element(item['nome']+'melhoriatext').update(button_color='black')
            if player_data['din']>=item['melhoria']:
                window.Element(item['nome']+'melhoriatext').update(button_color='green')
    for coisa in loja:
        if player_data['ouro']>=coisa['preço']:
            window.Element('loja'+str(coisa['nome'])).update(button_color='green')
        else:
            window.Element('loja' + str(coisa['nome'])).update(button_color='black')
        window.Element(coisa['nome'] + 'preço').update(str(exiba(coisa['preço'])) + ' ouro')
    if player_data['din']>0:
        window.Element('din').update(str(exiba(player_data['din'])))
    else:
        window.Element('din').update('-'+str(exiba(player_data['din'])))
    if lseg>=0:
        window.Element('lucroseg').update(str(exiba(lseg))+'/s')
    else:
        window.Element('lucroseg').update('-'+str(exiba(lseg)) + '/s')
    window.Element('ouro').update(exiba(int(player_data['ouro'])))
    window.Element('ouroseg').update(str(ouro_produzido)+'/s')
    for item in itens:
        window.Element('preço'+item['nome']).update(exiba(item['preço']))
        window.Element('atual_'+item['nome']).update(player_data[item['nome']])
        window.Element(item['nome']+'melhoradocusto').update(exiba(item['melhoria']))
    prestigio_a_ganhar = lseg * multiplicador_prestigio
    if prestigio_a_ganhar<=0:
        prestigio_a_ganhar=0
    window.Element('ouroganhar').update('Reiniciar tudo para ganhar '+str(exiba((int(prestigio_a_ganhar))))+' ouro')
    podermilitar=0
    for coisa in exercito:
        nome=coisa['nome']
        podermilitar+=coisa['poder']*player_data[nome]
        while coisa['inflacao']!=0:
            coisa['preço']=int(coisa['preço']+0.5*coisa['preço'])
            coisa['inflacao']-=1
        if player_data['din']>=(int(coisa['preço']+(mult-1)*0.5*coisa['preço'])):
            window.Element('comprar'+coisa['nome']).update(button_color='green')
        if player_data['din']<(int(coisa['preço']+(mult-1)*0.5*coisa['preço'])):
            window.Element('comprar'+coisa['nome']).update(button_color='black')
        window.Element('preço' + coisa['nome']).update(exiba(coisa['preço']))
        window.Element('atual_' + coisa['nome']).update(player_data[coisa['nome']])
        window.Element('podermilitar').update(exiba(podermilitar))
        global podermilitar_exiba
        podermilitar_exiba=podermilitar


def compra(item,mult):
    global tempo
    for i in itens:
        if item==i['nome'] and player_data['din']>=i['preço']*mult:
            if item == 'país' and player_data['país'] == 0:
                sg.popup('Agora você é dono de um país, muitos irão cobiçar suas riquezas'
                         ', certifique-se de manter seu poder militar alto na aba exército')
            player_data['din']-=i['preço']*mult
            player_data[item]+=mult
            i['inflacao']+=mult
            nome=i['nome']
            preco=i['preço']
            print('')
            print(f'{nome} comprado no instante {tempo} por {preco}')
            print('')
            atualizar(False)
    for coisa in exercito:
        if item==coisa['nome'] and player_data['din']>=coisa['preço']*mult:
            player_data['din']-=coisa['preço']*mult
            player_data[item]+=mult
            coisa['inflacao']+=mult
            nome=coisa['nome']
            preco=coisa['preço']
            print('')
            print(f'{nome} comprado no instante {tempo} por {preco}')
            print('')
            atualizar()


def upgrade(nome):
    global tempo
    for item in itens:
        if nome==item['nome'] and player_data['din']>=item['melhoria'] and item['nivel']<len(niveis)-1:
            nome=item['nome']
            print('')
            print(f'{nome} recebeu upgrade no instante {tempo}'.upper())
            print('')
            player_data['din']-=item['melhoria']
            item['nivel']+=1
            item['lucro']=item['lucro']+item['lucro']
            item['melhoria']=item['melhoria']*10
            window.Element('comprar' + item['nome']).set_tooltip('Produz '+str(exiba(item['lucro']))+'/s')
            window.Element(item['nome']+'melhoradocusto').update(item['melhoria'])
            window.Element(item['nome']+'melhoriatext').update(item['nome']+' '+niveis[item['nivel']])
            atualizar()


def armazenar():
    for i in itens:
        if 'preço_base' in i and 'lucro_base' in i and 'melhoria_base' in i:
            i.pop('preço_base')
            i.pop('lucro_base')
            i.pop('melhoria_base')
    dados=[player_data,itens,loja]
    with open(f'{a_dir}/saves/{dest}', 'w') as v:
        v.write(str(dados[0]))
        v.write('\n')
        v.write(str(dados[1]))
        from codigos.datas import data_atual
        v.write('\n')
        v.write(str(data_atual))
        v.write('\n')
        v.write(str(dados[2]))
        v.write('\n')
        v.write(str(multiplicador_prestigio))
        v.write('\n')
        v.write(str(version))
        v.write('\n')
        v.write(str(tempo_sessao))
        v.write('\n')
        v.write('admin_mode: '+str(admin_mode)+' Pass: '+str(admin_password))
        v.write('\n')
        v.write('Banco: '+str(banco))
        v.write('\n')
        v.write('Tela_cheia: '+tela_cheia)
        v.write('\n')
        v.write('Plano_de_fundo: '+background)
        print('')
        print('[Sistema] JOGO SALVO COM SUCESSO')
        print('')


def relogin():
    print('[Sistema] carregando relogin')
    lucro()
    txt=''
    ser_atacado=False
    from codigos.armazenamento import diferenca_tempo
    if diferenca_tempo>86400:
        diferenca_tempo=86400
    global lseg
    offline_din=diferenca_tempo*lseg
    ouro_offline=ouro_produzido*diferenca_tempo
    print(f'GANHA {offline_din} OFFLINE POR {diferenca_tempo} SEGUNDOS OFFLINE')
    player_data['din']+=offline_din
    player_data['ouro']+=ouro_offline
    if player_data['país']>=1:
        from random import randint
        random=randint(0,diferenca_tempo)
        if random>=diferenca_tempo//1.5 and diferenca_tempo>=600:
            ser_atacado=True
            txt='. Seu país foi atacado enquanto você estava offline, veja o relatório a seguir...'
    if offline_din>0 and ouro_offline==0:
        sg.Popup(f'Recebeu {exiba(offline_din)} por {segundosparastr(diferenca_tempo)} offline'+txt,
                 background_color='dark red',button_color='green',text_color='yellow', font=p_f)
    elif offline_din>0 and ouro_offline>0:
        sg.Popup(f'Recebeu {exiba(int(ouro_offline))} de ouro e {exiba(offline_din)} de dinheiro por {segundosparastr(diferenca_tempo)} offline'+txt,
                 background_color='dark red', button_color='green', text_color='yellow', font=p_f)
    if ser_atacado==True:  ataques((randint(9950,10000)))


def segundosparastr(seg):
    hora=0
    minuto=0
    while seg>=3600:
        seg-=3600
        hora+=1
    while seg>=60:
        minuto+=1
        seg-=60
    string = ''
    if hora>0 and minuto>0:
        string = f'{hora} horas {minuto} minutos e {seg} segundos'
    elif hora==0 and minuto>0:
        string = f'{minuto} minutos e {seg} segundos'
    else:
        string = f'{seg} segundos'
    return string


def prestigio():
    global player_data,player_data_backup,itens,prestigio_a_ganhar
    prestigio_ganho=lseg*multiplicador_prestigio
    ouro=player_data['ouro']
    if lseg<=0:
        prestigio_ganho=0
        prestigio_a_ganhar=0
    for coisa in player_data:
        if coisa=='nome':
            pass
        else:
            player_data[coisa]=0
    for coisa in itens_backup:
        for coisa2 in itens:
            if coisa['nome']==coisa2['nome']:
                coisa2['preço']=coisa['preço_base']
                coisa2['lucro'] = coisa['lucro_base']
                coisa2['melhoria'] = coisa['melhoria_base']
                coisa2['nivel']=0
    player_data['ouro']+=int(prestigio_ganho)+ouro
    prestigio_a_ganhar=prestigio_ganho
    x=l1['qtd']
    din=40
    while x!=0:
        x-=1
        din=din*3
    player_data['din']=din
    atualizarvaloresloja()
    print('PRESTIGIO ACONTECEU')
    print('')
    atualizar()


def comprarloja(item,custo):
    global bonus_lucro_geral
    if player_data['ouro']>=custo:
        player_data['ouro']-=custo
        for coisa in loja:
            if coisa['nome']==item:
                coisa['qtd']+=1
                sg.Popup('Compra efetuada com sucesso')
                coisa['preço']=int(coisa['preço']*3)
                print(f'{item} comprado na loja no instante {tempo}')
                print('')
        atualizarvaloresloja()
        atualizar()
    else:
        sg.Popup('Ouro insuficiente')


def atualizarvaloresloja():
    global multiplicador_prestigio
    for i in itens:
        i['lucro']=int((i['lucro']*(1+0.5*l2['qtd'])))
        i['melhoria']=int(i['melhoria']-(0.2*i['melhoria']*l5['qtd']))
        window.Element('comprar' + i['nome']).set_tooltip('Produz ' + str(exiba(i['lucro'])) + '/s')
        multiplicador_prestigio= multiplicador_prestigio*(1+0.005*l3['qtd'])
        print('Valores da loja atualizados')
        print('')


def ataques(x):
    from random import randint
    random=randint(1,10000)
    if x>0: random=x
    if random>=9950:
        print(f'PAÍS ATACADO NO INSTANTE {tempo}')
        inimigo_poder=(random-9950)*(lseg//120)
        resultado=''
        if podermilitar_exiba<inimigo_poder:
            resultado='derrota'
        else:
            resultado='vitória'
            ganho=int(inimigo_poder*200)
            player_data['din']+=ganho
            resultado+=f', ganhou: {exiba(ganho)} de dinheiro'
            ganhar_ouro=randint(1,100)
            if ganhar_ouro>=90:
                ouro=randint(10,500)
                resultado+=f' e {ouro} de ouro.'
                player_data['ouro']+=ouro
        if resultado=='derrota':
            prerand=randint(60,300)
            prejuizo=int(lseg*prerand)
            perder_estruturas=randint(1,10)
            resultado += ', prejuízo: '
            resultado += f'{exiba(prejuizo)} de dinheiro'
            player_data['din'] -= prejuizo
            if perder_estruturas>=8:
                prejuizo_barraco=int(player_data['barraco']*0.2)
                prejuizo_apartamento = int(player_data['apartamento'] * 0.15)
                prejuizo_casa= int(player_data['casa']*0.1)
                prejuizo_loja= int(player_data['loja']*0.05)
                if prejuizo_barraco>=1:
                    resultado+=f', {prejuizo_barraco} barracos'
                    player_data['barraco']-=prejuizo_barraco
                    while prejuizo_barraco>0:
                        i1['preço']=int(i1['preço']*0.8)
                        prejuizo_barraco-=1
                if prejuizo_apartamento>=1:
                    resultado+=f', {prejuizo_apartamento} apartamentos'
                    player_data['apartamento']-=prejuizo_apartamento
                    while prejuizo_apartamento>0:
                        i2['preço']=int(i2['preço']*0.8)
                        prejuizo_apartamento-=1
                if prejuizo_casa>=1:
                    resultado+=f', {prejuizo_casa} casas'
                    player_data['casa']-=prejuizo_casa
                    while prejuizo_casa>0:
                        i3['preço']=int(i3['preço']*0.8)
                        prejuizo_casa-=1
                if prejuizo_loja>=1:
                    resultado+=f', {prejuizo_loja} lojas'
                    player_data['loja']-=prejuizo_loja
                    while prejuizo_barraco>0:
                        i4['preço']=int(i4['preço']*0.8)
                        prejuizo_loja-=1
        if inimigo_poder>0:
            sg.Popup(f'Seu país foi atacado por um tropa de {exiba(inimigo_poder)} poder,'
                     f' resultado: {resultado}', font=p_f)
            atualizar()
        print(f'Resultado do ataque: {resultado}')


def guardar(ato):
    global banco
    global cooldown
    valor=(window.Element('depositar_valor').get())
    if valor.isdigit():
        valor=int(valor)
    else:
        valor=0
    if player_data['din']>=valor and ato=='guardar' and player_data['ouro']>=1000:
        window.Element('guardarerro').update(visible=False)
        window.Element('guardarsucesso').update(visible=True)
        banco+=valor//10
        player_data['din']-=valor
        player_data['ouro']-=1000
        window.Element('depositar_valor').update('0')
        print('[Sistema] Deposito de dinheiro ocorreu no instante',tempo)
    elif ato=='retirar' and banco>=valor:
        player_data['din']+=valor
        banco-=valor
        window.Element('guardarerro').update(visible=False)
        window.Element('guardarsucesso').update(visible=True)
        window.Element('depositar_valor').update('0')
        print('[Sistema] Retirada de dinheiro no instante',tempo)
    else:
        if player_data['ouro']<1000:
            window.Element('guardarerro').update('Erro, ouro insuficiente')
        elif player_data['din']<valor:
            window.Element('guardarerro').update('Erro, dinheiro insuficiente')
        window.Element('guardarerro').update(visible=True)
        window.Element('guardarsucesso').update(visible=False)
    cooldown=0
    window.Element('guardado').update(exiba(banco))
    atualizar()


# Atenção: Novos elementos na tela devem ser adicionados na lista da função
def fecha_todos(excecoes):
    elementos = ['upgradescreen', 'comprarscreen', 'options', 'ascender',
                 'telaexercito', 'telabanco', 'loja', 'dinseg', 'lmult' ]#,'barradeopçoes']
    for item in elementos:
        if item not in excecoes:
            window.Element(item).update(visible=False)
        else:
            window.Element(item).update(visible=True)


for coisa in exercito:
    window.Element('comprar'+coisa['nome']).set_tooltip('gasta '+str(exiba(coisa['manutençao']))+'/s')
print('[Exercito] Atualizando tooltips')
for i in itens:
    window.Element('comprar'+i['nome']).set_tooltip('Produz '+str(exiba(i['lucro']))+'/s')
print('[Propriedades] Atualizando tooltips')
if admin_mode=='True':
    if admin_password in passwords:
        window.Element('somardin').update(visible=True)
        window.Element('somarouro').update(visible=True)
        print('[Sistema] Passe de administrador aceito')
    else:
        print('[Sistema] Passe de administrador invalido')
        window.Element('somardin').update(visible=False)
        window.Element('somarouro').update(visible=False)
else:
    window.Element('somardin').update(visible=False)
    window.Element('somarouro').update(visible=False)
window.Element('guardado').update(exiba(banco))

relogin()
mult=1
atualizar()
print('[Sistema] atualizando dados')

while True:
    event,values= window.read(timeout=1000,timeout_key='atualizar')
    tempo_sessao+=1
    cooldown+=1
    if tempo%60==0 and tempo!=0:
        print('[Sistema] Salvando automaticamente...')
        armazenar()
    if event==None or 'None' in event:
        armazenar()
        break
    elif event=='telacheia':
        if tela_cheia=='False':
            tela_cheia='True'
            sg.popup('Feche o jogo para ativar a tela cheia', font=p_f)
        else:
            tela_cheia='False'
            sg.popup('Feche o jogo para desativar a tela cheia', font=p_f)
        print('[Sistema] configuração de jogo modificada')
    elif event in cores:
        background=cores[event]
        print('[Sistema] Background mudado para',background)
        sg.popup('Feche o jogo para mudar a cor do plano de fundo', font=p_f)
    elif event=='atualizar':
        tempo += 1
        atualizar()
    else:
        for item in itens:
            if 'comprar'+item['nome']==event:
                compra(item['nome'],mult)
            if item['nome']+'melhoriatext'==event:
                upgrade(item['nome'])
        for item in exercito:
            if 'comprar'+item['nome']==event:
                compra(item['nome'],mult)
    if event=='upgrade':
        fecha_todos(['upgradescreen','dinseg'])
    if event=='abrirbanco':
        fecha_todos(['telabanco'])
    elif event=='propriedades':
        fecha_todos(['dinseg', 'lmult', 'comprarscreen'])
    elif event=='1x' or event=='10x' or event=='100x' or event=='1000x':
        mult=int(event.replace('x',''))
        window.Element('mult').update(str(mult)+'x')
    elif event=='optionsclick':
        fecha_todos(['options'])
    elif event=='reset':
        window.Element('resetconfirmar').update(visible=True)
        window.Element('resetcancelar').update(visible=True)
    elif event=='resetconfirmar':
        limpartxt()
        sg.popup('Reiniciando o jogo para aplicar a mudança')
        break
    elif event == 'resetcancelar':
        window.Element('resetconfirmar').update(visible=False)
        window.Element('resetcancelar').update(visible=False)
    elif event=='ascencao':
        fecha_todos(['ascender'])
    elif event=='prestigio':
        window.Element('asconfirmar').update(visible=True)
        window.Element('ascancelar').update(visible=True)
    elif event=='asconfirmar':
        prestigio()
    elif event=='ascancelar':
        window.Element('asconfirmar').update(visible=False)
        window.Element('ascancelar').update(visible=False)
    elif event=='abrirloja':
        fecha_todos(['loja','lseg'])
    else:
        for coisa in loja:
            if event=='loja'+str(coisa['nome']):
                comprarloja(coisa['nome'],coisa['preço'])
    if event=='mostrarexercito' and player_data['país']>=1:
        fecha_todos(['dinseg','lmult','telaexercito'])
    elif event=='mostrarexercito' and player_data['país']==0:
        sg.Popup('Para acessar o exército você precisa ser dono de um país', font=p_f)
    if event=='somardin':
        player_data['din']+=10000000000000*mult
        atualizar()
    if event=='somarouro':
        player_data['ouro']+=100000*mult
        atualizar()
    if event=='guardar' and cooldown>=5:
        guardar('guardar')
    elif event=='retirar' and cooldown>=5:
        guardar('retirar')
    if event=='10%':
        window.Element('depositar_valor').update(int(player_data['din']*0.1))
    if event=='25%':
        window.Element('depositar_valor').update(int(player_data['din']*0.25))
    if event=='50%':
        window.Element('depositar_valor').update(int(player_data['din']*0.5))
    if event=='100%':
        window.Element('depositar_valor').update(player_data['din'])


window.close()
