from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

#dados para requisição
header = {
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

url = "https://www.fundamentus.com.br/detalhes.php?papel="

#lista de fiis
lista_fiis = ['ATSA11','ABCP11','AFCR11','AFHI11','AFOF11','AIEC11','ALMI11','ALZR11','ANCR11B','ARFI11B','ARRI11','ATCR11']
lista_fiis.append('BARI11')
lista_fiis.append('BBFI11B')
lista_fiis.append('BBFO11')
lista_fiis.append('BBIM11')
lista_fiis.append('BBPO11')
lista_fiis.append('BBRC11')
lista_fiis.append('BCFF11')
lista_fiis.append('BCIA11')
lista_fiis.append('BCRI11')
lista_fiis.append('BICE11')
lista_fiis.append('BICR11')
lista_fiis.append('BLCP11')
lista_fiis.append('BLMC11')
lista_fiis.append('BLMG11')

#definindo colunas dos fis
colunas_csv = '{}|{}|{}|{}|{}|{}|{}|{}|{}'.format("FII","Cotação","Empresa","Data Atualização","Segmento",\
                                                  "Div. Yield","Dividendo/cota","Cap Rate","Vacância Média")

#metodo para gerar arquivo csv
def gera_csv():
    return open('base_fiis.csv','w')

#metodo para escrever no csv
def escreve(arquivo,dados):
    arquivo.write(dados+'\n')

#metodo para fechar csv
def fechar_arquivo(arquivo):
    arquivo.close()
    

#gerando CSV
arquivo = gera_csv()

#escrevendo colunas
escreve(arquivo,colunas_csv)

#contador
CONTADOR=1

print("----------------------------------------------------------")
print("|                Iniciando Hunter Dog!!!!!!              |")
print("----------------------------------------------------------")

for fii in lista_fiis:
    #pegando pagina do fiis
    print("Coleta de dados em : {}%".format(round((CONTADOR/len(lista_fiis))*100),1))
    

    try:
        dados = Request('{}{}'.format(url,fii),headers = header)
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
        conteudo_arquivo = '{}|{}|{}|{}|{}|{}|{}|{}|{}'.format(lista_dados[2]\
                             ,lista_dados[4]\
                             ,(lista_dados[6]).replace(',','.')\
                             ,lista_dados[8]\
                             ,lista_dados[14]\
                             ,((lista_dados[40]).replace(',','.')).replace('%','')\
                             ,(lista_dados[42]).replace(',','.')\
                             ,(((lista_dados[94]).replace(',','.')).replace('%','')).replace('-','0')\
                             ,((lista_dados[100]).replace(',','.')).replace('%','')).replace('-','0')

        escreve(arquivo,conteudo_arquivo)
    except HTTPError:
        print("Erro"+HTTPError.reason)
    except IndexError:
        print("Erro na extração deda do FIIs {}".format(fii))

    CONTADOR=CONTADOR+1




#fechando escrita no arquivo
fechar_arquivo(arquivo)



