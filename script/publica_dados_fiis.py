#Autor:Diego Silva
#Data:02/09/2021
#Descrição: classe para fazer post de dados no web service

#classe para compor post de dads
from os import link
from typing import Dict
import requests as rq
import json as js

#classe para publicar dados
class PublicaDados:

    '''
        Criando properties para configuração de 
        login e senha de acesso ao web service
    '''

    def __init__(self) -> None:
        self._login = None
        self._senha = None

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login=login


    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha=senha


    '''
        criando métodos para interagir com o post de dados para o web service
    '''
    @staticmethod
    def cabecalho() ->Dict:
        return {'content-type':'application/json'}

    def executa_post(self, host,port,service,payload,cabecalho) -> Dict:
        link = 'http://{}:{}/{}'.format(host,str(port),service)
        resposta="Erro com a conexão"
        try:
            resposta = rq.post(url=link, data=js.dumps(payload), auth=(self._login,self._senha),headers=cabecalho)
            resposta.json
        except:
            print("Erro")
            
        return resposta


    def executa_delete(self, host,port,service) -> Dict:
        link = 'http://{}:{}/{}'.format(host,str(port),service) 
        resposta="Erro com a conexão"
        try:
            resposta = rq.delete(url=link, auth=(self._login,self._senha))
            resposta.json
        except:
            print("Erro")

        return resposta


#classe para compor json de payload de dados
class MontaJsonFiis:

    @staticmethod
    def compor_json_envio(lista_dados):
        return { "nome":"{}".format(lista_dados[2]),\
            "cotacao":"{}".format(lista_dados[4]),\
            "empresa":"{}".format((lista_dados[6]).replace(',','.')),\
            "data":"{}".format(lista_dados[8]),\
            "segmento":"{}".format(lista_dados[14]),\
            "dividend yield %":"{}".format(((lista_dados[40]).replace(',','.')).replace('%','')),\
            "valor dividendo cota":"{}".format((lista_dados[42]).replace(',','.')),\
            "cap rate %":"{}".format((((lista_dados[94]).replace(',','.')).replace('%','')).replace('-','0')),\
            "vacancia %":"{}".format((((lista_dados[100]).replace(',','.')).replace('%','')).replace('-','0')),\
            "P/VP":"{}".format(lista_dados[46].replace(',','.')),\
            "Qtd Imoveis":"{}".format(lista_dados[90]),\
            "Nº de Cotas":"{}".format(lista_dados[24].replace('.','')),\
            "liquidez":"{}".format(lista_dados[20].replace('.',''))\
            }

