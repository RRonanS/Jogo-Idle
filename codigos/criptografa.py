class criptografia():
    def __init__(self, arquivo):
        with open(arquivo, 'r') as leitura:
            linhas = leitura.readlines()
            try: key = int(linhas[0])
            except: key = None
        self.key = key
        letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z']
        numeros = [x for x in range(0, 9)]
        self.numeros = numeros
        self.letras = letras
        self.arquivo = arquivo
    def gerarkey(self):
        from random import randint
        key = randint(5,12)
        return key
    def transforme(self, u, k):
        if u.isnumeric():
            u = (int(u))
            for c in range(k):
                if c%2 == 0:
                    u += c
                elif (u - c) >0:
                    u -= c
                else: u *= c
            u = bin(u)
            return u
        else:
            if u == ' ': return ' '
            letras = self.letras
            pos = letras.index(u)
            pos *= k
            while pos > len(letras):
                if (pos-(k+1)) < 0:
                    if (pos - 1) > 0:pos -= 1
                pos -= (k+1)
            return letras[pos]

    def escrita(self, lista_items):
        key = self.gerarkey()
        numeros = self.numeros
        letras = self.letras
        arquivo = self.arquivo
        cont2 = 0
        for item in lista_items:
            item_list = list(item)
            cont = 0
            for unidade in item_list:
                item_list[cont] = self.transforme(unidade, key)
                cont += 1
            lista_items[cont2] = ''.join(item_list)
            cont2 += 1
        with open(arquivo, 'w') as arq:
            arq.write(str(key))
            arq.write('\n')
            for item in lista_items:
                arq.write(item)
                arq.write('\n')
    def leitura(self):
        arquivo = self.arquivo
        key = self.key
        with open(arquivo, 'r') as leitura:
            linhas = leitura.readlines()
        linhas = linhas[1::]
        cont2 = 0
        for item in linhas:
            item_list = list(item)
            cont = 0
            for unidade in item_list:
                item_list[cont] = self.destransforme(unidade, key)
                cont += 1
            linhas[cont2] = ''.join(item_list)
            cont2 += 1
        print(linhas)
    def destransforme(self, u, k):
        pass



classe = criptografia('testes.txt')
classe.leitura()
#classe.escrita(['eae mano blz a senha e','123456'])

