import requests


class BuscaEndereco:
    def __init__(self, cep):
        self.link = f'https://viacep.com.br/ws/{cep}/json/'
        self.requisicao = requests.get(self.link)
        self.dic_requisicao = self.requisicao.json()
        self.uf = self.dic_requisicao['uf']
        self.rua = self.dic_requisicao['logradouro']
        self.cidade = self.dic_requisicao['localidade']
        self.bairro = self.dic_requisicao['bairro']

    def pesquisa(self):
        print(f'Uf: {self.uf}\nCidade: {self.cidade}\nBairro: {self.bairro}\nRua: {self.rua} ')

    def informacoes_completa(self):
        return self.dic_requisicao


class BuscaCep:
    def __init__(self,uf ,cidade, logradouro):
        self.link = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'
        self.requisicao = requests.get(self.link)
        self.dic_requisicao = self.requisicao.json()


    def mostrar_cep(self):
        for cep in self.dic_requisicao:
            print(cep['cep'])



cep2 = BuscaCep('AM', 'Manaus', 'Rua Kamakura')
cep2.mostrar_cep()
