import os.path

a_dir = os.getcwd()
a_dir = a_dir.replace('codigos', '')

def armazenar(dest):
    from game import player_data, itens
    dados = [player_data, itens]
    with open(f'{a_dir}/saves/{dest}', 'w') as v:
        v.write(str(dados[0]))
        v.write('\n')
        v.write(str(dados[1]))


player_data_leitura = []
idata_leitura = []
diferenca_tempo = 0
loja_leitura = []
multiplicador_prestigio_leitura = 0
version_leitura = 0
tempo_sessao_leitura = 0
admin_mode_leitura = False
banco_leitura = 0
tela_cheia_leitura = 'False'
background_leitura = ''
admin_password_leitura = ''


def leitura(dest):
    global admin_password_leitura
    global player_data_leitura
    global tela_cheia_leitura
    global admin_mode_leitura
    global idata_leitura
    global diferenca_tempo
    global background_leitura
    global loja_leitura
    global multiplicador_prestigio_leitura
    global tempo_sessao_leitura
    global version_leitura
    global banco_leitura
    ler = open(f'{a_dir}/saves/{dest}', 'r')
    linhas = ler.readlines()
    linhaslen = len(linhas)
    n = 1
    for x in linhas:
        x=x.replace('{','')
        x = x.replace('}', '')
        x = x.replace('[', '')
        x = x.replace(']', '')
        x = x.replace(':', '')
        x = x.replace(',', '')
        x = x.replace('\'', '')
        tes = x.split()
        if n == 1:
            player = tes
        elif n == 2:
            itens = tes
        elif n == 3:
            data = tes
        elif n == 4:
            loja = tes
        elif n == 5:
            multiplicador_prestigio_leitura = tes
        elif n == 6 and linhaslen >= 6:
            version_leitura = float(tes[0])
        elif n == 7 and linhaslen >= 7:
            tempo_sessao_leitura = int(tes[0])
        elif n == 8 and linhaslen >= 8:
            admin_mode_leitura = tes[1]
            admin_password_leitura = tes[3]
            print('[Sistema] Admin_mode= '+admin_mode_leitura)
        elif n == 9 and linhaslen >= 9:
            banco_leitura = tes[1]
        elif n == 10 and linhaslen >= 10:
            tela_cheia_leitura = tes[1]
        elif n == 11 and linhaslen >= 11:
            background_leitura = tes[1]
        n+=1
    if len(linhas)>0:
        player_data_leitura={'nome': player[1], 'din': int(player[3]), 'ouro': float(player[5]), 'barraco': int(player[7])
                             , 'apartamento': int(player[9]), 'casa': int(player[11]), 'loja': int(player[13]),
                             'condominio': int(player[15]), 'bairro': int(player[17]), 'município': int(player[19])
                             , 'cidade': int(player[21]), 'estado': int(player[23]), 'país': int(player[25]),
                             'banco': int(player[27]), 'quartel': int(player[29]), 'batalhão': int(player[31]),
                             'brigada': int(player[33]), 'aeroporto militar': int(player[36]),
                             'arsenal nuclear': int(player[39])}
        for cons in range(0, 121, 12):
            i = {itens[cons]:itens[cons+1],itens[cons+2]:int(itens[cons+3]),itens[cons+4]:int(itens[cons+5]),
            itens[cons+6]:int(itens[cons+7]),itens[cons+8]:int(itens[cons+9]),
            itens[cons+10]:int(itens[cons+11])}
            idata_leitura.append(i)
        dia = int(data[0])
        hora = int(data[3])
        minuto = int(data[4])
        segundo = int(data[5])
        from .datas import data_atual as data_anterior
        data_anterior = str(data_anterior)
        data_anterior = data_anterior.replace('[','')
        data_anterior = data_anterior.replace(']', '')
        data_anterior = data_anterior.replace('"', '')
        data_anterior = data_anterior.replace(',', '')
        data_anterior = data_anterior.replace('\'', '')
        data_anterior = data_anterior.split()
        dia_anterior = int(data_anterior[0])
        hora_anterior = int(data_anterior[3])
        minuto_anterior = int(data_anterior[4])
        segundo_anterior = int(data_anterior[5])
        tempo_atual=(86400*dia)+(3600*hora)+(60*minuto)+segundo
        tempo_anterior = (86400 * dia_anterior) + (3600 * hora_anterior) + (60 * minuto_anterior) + segundo_anterior
        diferenca_tempo = tempo_atual-tempo_anterior
        if diferenca_tempo<0:
            diferenca_tempo*=-1
        if diferenca_tempo>86400:
            diferenca_tempo=86400



        loja_leitura=[]
        l1={loja[0]:loja[1]+' '+loja[2],'preço':int(loja[4]),'qtd':int(loja[13])}
        l2={'nome':loja[15]+' '+loja[16],'preço':int(loja[18]),'qtd':int(loja[30])}
        l3={'nome':loja[32]+' '+loja[33]+' '+loja[34],'preço':int(loja[36]),'qtd':int(loja[48])}
        l4={'nome':loja[50],'preço':int(loja[52]),'qtd':int(loja[67])}
        l5 = {'nome': loja[69]+' '+loja[70], 'preço': int(loja[72]), 'qtd': int(loja[84])}
        loja_leitura.append(l1)
        loja_leitura.append(l2)
        loja_leitura.append(l3)
        loja_leitura.append(l4)
        loja_leitura.append(l5)
        multiplicador_prestigio_leitura=float(multiplicador_prestigio_leitura[0])


with open(f'{a_dir}/outros/destino.txt', 'r') as arq:
    desti = arq.readlines()[0]
leitura(desti)
