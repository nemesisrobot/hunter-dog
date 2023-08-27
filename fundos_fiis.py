from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from script.constantes_sistema import *
from script.analise_fundos import *
import pandas as pd
from threading import *
from script.base import *

class ProcessCollector(Thread):
    def __init__(self, statuscollector):
        Thread.__init__(self)
        self.statuscollector= statuscollector

    #metodo para escrever no csv
    def escreve(self, arquivo,dados):
        arquivo.write(dados+'\n')
    
    #metodo para fechar csv
    def fechar_arquivo(self,arquivo):
        arquivo.close()
    
    #metodo para gerar arquivo csv
    def gera_csv(self):
        return open('base_fiis.csv','w')
    
    def run(self):
        #pegando todos os fiis
        select = FiisCad('base.db')
        lista_fiis=select.selectFiis()
        
        colunas_csv=""
        fiis_html = BeautifulSoup(urlopen(Request('{}'.format(URL_FUNDS_EXPLORER),headers = HEADER)), 'html.parser')
        html_puro_fiis = fiis_html.findAll("span",{"class":"symbol"})
        for fiis in html_puro_fiis:
            lista_fiis.append(fiis.getText())
            #definindo colunas dos fis
        colunas_csv = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format("FII","Cotação","Empresa","Data Atualização","Segmento",\
                                                  "Div. Yield","Dividendo/cota","Cap Rate","Vacância Média",\
                                                 "P/VP","Qtd Imoveis","Qtd Cotas","liquidez")

        

        
    

        #gerando CSV
        arquivo = self.gera_csv()

            #escrevendo colunas
        self.escreve(arquivo,colunas_csv)

        #contador
        CONTADOR=1

        print("----------------------------------------------------------")
        print("|                Iniciando Hunter Dog!!!!!!              |")
        print("----------------------------------------------------------")

        for fii in lista_fiis:
            #pegando pagina do fiis
            print("Coleta de dados em : {}%".format(round((CONTADOR/len(lista_fiis))*100),1))
            self.statuscollector["text"]="Status: Coleta de dados em {}%".format(round((CONTADOR/len(lista_fiis))*100),1)
    

            try:
                dados = Request('{}{}'.format(URL_FUNDAMENTUS,fii),headers = HEADER)
                resposta= urlopen(dados)
                lista_dados = []

                #fazendo parser de dados
                html = BeautifulSoup(resposta, 'html.parser')
                grid_dados = html.findAll('span')

                for dado in grid_dados:
                    if '?' not in dado.getText():
                        #print(dado.getText())
                        lista_dados.append(dado.getText())

                #escrevendo conteudo
                conteudo_arquivo = '{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(lista_dados[2]\
                                        ,lista_dados[4]\
                                        ,(lista_dados[6]).replace(',','.')\
                                        ,lista_dados[8]\
                                        ,lista_dados[14]\
                                        ,((lista_dados[40]).replace(',','.')).replace('%','')\
                                        ,(lista_dados[42]).replace(',','.')\
                                        ,(((lista_dados[94]).replace(',','.')).replace('%','')).replace('-','0')\
                                        ,(((lista_dados[100]).replace(',','.')).replace('%','')).replace('-','0')\
                                        ,lista_dados[46].replace(',','.')\
                                        ,lista_dados[90]\
                                        ,lista_dados[24]\
                                        ,lista_dados[20].replace('.',''))

                self.escreve(arquivo,conteudo_arquivo)
            except HTTPError:
                print("Erro"+HTTPError.reason)
            except IndexError:
                print("Erro na extração deda do FIIs {}".format(fii))

            CONTADOR=CONTADOR+1


        #fechando escrita no arquivo
        self.fechar_arquivo(arquivo)
        self.statuscollector["text"]="Status:Concluido"

        

#prth = Process()
#prth.start()

class ProcessReports(Thread):

    def __init__(self, vacancia=None, pvpmin=None,pvpmax=None,liquidez=None,statuscolector=None):
        Thread.__init__(self)
        self.vacancia = vacancia
        self.pvpmin = pvpmin
        self.pvpmax = pvpmax
        self.liquidez = liquidez
        self.statuscollector=statuscolector

    def run(self):
        regras = FundosRegras(self.vacancia,self.pvpmin,self.pvpmax,self.liquidez,self.statuscollector)
        regras.aplica_regas_gera_realtorio(CarregarDados.carrega_dados("base_fiis.csv","|","ISO-8859-1"))

#pa = ProcessReports(10,1.02,1.04,150000)
#pa.start()

class DataBaseCreate(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        print("Gerando base!")
        basedt = GenerateBase()
        print("Dropando base de dados!")
        basedt.drop_base("base.db")
        print("Gerando tabela")
        basedt.create_connection("base.db")
        print("Fazendo Carga de dados")
        basedt.load_datas("base.db")