from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from script.constantes_sistema import *
from script.analise_fundos import *
import pandas as pd
from threading import *

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
        lista_fiis=[
            'ABCP11'
            ,'AFCR11'
            ,'AFHI11'
            ,'AFOF11'
            ,'AIEC11'
            ,'ALMI11'
            ,'ALZR11'
            ,'ANCR11B'
            ,'APTO11'
            ,'ARCT11'
            ,'ARRI11'
            ,'ATSA11'
            ,'BARI11'
            ,'BBFI11B'
            ,'BBFO11'
            ,'BBPO11'
            ,'BBRC11'
            ,'BBVJ11'
            ,'BCFF11'
            ,'BCIA11'
            ,'BCRI11'
            ,'BICE11'
            ,'BICR11'
            ,'BLCP11'
            ,'BLMC11'
            ,'BLMG11'
            ,'BLMO11'
            ,'BLMR11'
            ,'BMLC11'
            ,'BMLC11'
            ,'BNFS11'
            ,'BPFF11'
            ,'BPML11'
            ,'BRCO11'
            ,'BRCR11'
            ,'BREV11'
            ,'BRLA11'
            ,'BTAL11'
            ,'BTCR11'
            ,'BTLG11'
            ,'BTRA11'
            ,'BTWR11'
            ,'BVAR11'
            ,'CACR11'
            ,'CARE11'
            ,'CBOP11'
            ,'CCRF11'
            ,'CEOC11'
            ,'CNES11'
            ,'CORM11'
            ,'CPFF11'
            ,'CPTS11'
            ,'CRFF11'
            ,'CTXT11'
            ,'CVBI11'
            ,'CXCE11B'
            ,'CXCO11'
            ,'CXRI11'
            ,'CXTL11'
            ,'DEVA11'
            ,'DMAC11'
            ,'DOMC11'
            ,'DOVL11B'
            ,'DRIT11B'
            ,'DVFF11'
            ,'EDFO11B'
            ,'EDGA11'
            ,'ELDO11B'
            ,'EQIN11'
            ,'EQIR11'
            ,'ERCR11'
            ,'EURO11'
            ,'EVBI11'
            ,'FAED11'
            ,'FAMB11B'
            ,'FATN11'
            ,'FCFL11'
            ,'FEXC11'
            ,'FFCI11'
            ,'FIGS11'
            ,'FIIB11'
            ,'FIIP11B'
            ,'FISC11'
            ,'FLCR11'
            ,'FLMA11'
            ,'FLRP11'
            ,'FMOF11'
            ,'FPAB11'
            ,'FPNG11'
            ,'FVBI11'
            ,'FVPQ11'
            ,'GALG11'
            ,'GCFF11'
            ,'GCRI11'
            ,'GESE11B'
            ,'GGRC11'
            ,'GRLV11'
            ,'GTLG11'
            ,'GTWR11'
            ,'HAAA11'
            ,'HABT11'
            ,'HBRH11'
            ,'HBTT11'
            ,'HCHG11'
            ,'HCRI11'
            ,'HCTR11'
            ,'HFOF11'
            ,'HGBS11'
            ,'HGCR11'
            ,'HGFF11'
            ,'HGIC11'
            ,'HGLG11'
            ,'HGPO11'
            ,'HGRE11'
            ,'HGRU11'
            ,'HLOG11'
            ,'HMOC11'
            ,'HOSI11'
            ,'HPDP11'
            ,'HRDF11'
            ,'HREC11'
            ,'HSAF11'
            ,'HSLG11'
            ,'HSML11'
            ,'HSRE11'
            ,'HTMX11'
            ,'HUSC11'
            ,'IBCR11'
            ,'IBFF11'
            ,'IDFI11'
            ,'IFID11'
            ,'IFIE11'
            ,'IRDM11'
            ,'IRIM11'
            ,'ITIP11'
            ,'ITIT11'
            ,'JFLL11'
            ,'JPPA11'
            ,'JRDM11'
            ,'JSRE11'
            ,'KEVE11'
            ,'KFOF11'
            ,'KINP11'
            ,'KISU11'
            ,'KNCR11'
            ,'KNHY11'
            ,'KNIP11'
            ,'KNRE11'
            ,'KNRI11'
            ,'KNSC11'
            ,'LASC11'
            ,'LFTT11'
            ,'LGCP11'
            ,'LUGG11'
            ,'LVBI11'
            ,'MALL11'
            ,'MATV11'
            ,'MAXR11'
            ,'MBRF11'
            ,'MCCI11'
            ,'MCHF11'
            ,'MCHY11'
            ,'MFAI11'
            ,'MFII11'
            ,'MGCR11'
            ,'MGFF11'
            ,'MGHT11'
            ,'MGLG11'
            ,'MORC11'
            ,'MORE11'
            ,'MXRF11'
            ,'NAVT11'
            ,'NCHB11'
            ,'NEWL11'
            ,'NEWU11'
            ,'NSLU11'
            ,'NVHO11'
            ,'ONEF11'
            ,'ORPD11'
            ,'OUFF11'
            ,'OUJP11'
            ,'OULG11'
            ,'OURE11'
            ,'PATC11'
            ,'PATL11'
            ,'PLCR11'
            ,'PLOG11'
            ,'PLRI11'
            ,'PORD11'
            ,'PQAG11'
            ,'PQDP11'
            ,'PRSV11'
            ,'PVBI11'
            ,'QAGR11'
            ,'QAMI11'
            ,'QIFF11'
            ,'QIRI11'
            ,'QMFF11'
            ,'RBBV11'
            ,'RBCO11'
            ,'RBDS11'
            ,'RBED11'
            ,'RBFF11'
            ,'RBGS11'
            ,'RBHG11'
            ,'RBHY11'
            ,'RBIV11'
            ,'RBLG11'
            ,'RBRD11'
            ,'RBRF11'
            ,'RBRL11'
            ,'RBRP11'
            ,'RBRR11'
            ,'RBRS11'
            ,'RBRY11'
            ,'RBTS11'
            ,'RBVA11'
            ,'RBVO11'
            ,'RCFF11'
            ,'RCRB11'
            ,'RDES11'
            ,'RDPD11'
            ,'RECR11'
            ,'RECT11'
            ,'RECX11'
            ,'RELG11'
            ,'RFOF11'
            ,'RMAI11'
            ,'RNDP11'
            ,'RNGO11'
            ,'RRCI11'
            ,'RSPD11'
            ,'RVBI11'
            ,'RZAK11'
            ,'RZTR11'
            ,'SADI11'
            ,'SAIC11B'
            ,'SARE11'
            ,'SCPF11'
            ,'SDIL11'
            ,'SDIP11'
            ,'SEQR11'
            ,'SHDP11B'
            ,'SHPH11'
            ,'SNCI11'
            ,'SNFF11'
            ,'SPTW11'
            ,'SRVD11'
            ,'STRX11'
            ,'TBOF11'
            ,'TEPP11'
            ,'TGAR11'
            ,'THRA11'
            ,'TORD11'
            ,'TRNT11'
            ,'TRXF11'
            ,'TRXL11'
            ,'UBSR11'
            ,'URPR11'
            ,'VCJR11'
            ,'VCRR11'
            ,'VERE11'
            ,'VGHF11'
            ,'VGIP11'
            ,'VGIR11'
            ,'VIFI11'
            ,'VILG11'
            ,'VINO11'
            ,'VISC11'
            ,'VIUR11'
            ,'VLOL11'
            ,'VOTS11'
            ,'VRTA11'
            ,'VSHO11'
            ,'VSLH11'
            ,'VTLT11'
            ,'VVPR11'
            ,'VXXV11'
            ,'WPLZ11'
            ,'WTSP11B'
            ,'XPCI11'
            ,'XPCM11'
            ,'XPHT11'
            ,'XPIN11'
            ,'XPLG11'
            ,'XPML11'
            ,'XPPR11'
            ,'XPSF11'
            ,'XTED11'
            ,'YCHY11']
        
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