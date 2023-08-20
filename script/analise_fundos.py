#Autor:Diego Lopes da Silva
#Data:21/09/2021
#Descrição:Script para tratar dados e aplica regras em cima dos fundos imobiliarios

import pandas as pd
import numpy as np

#classe para carregar dados
class CarregarDados:

    @staticmethod
    def carrega_dados(path, separador, tipo_encode):
        print("|-------------------------|")
        print(">> Carregando base de dados")
        print("|-------------------------|")
        base =pd.read_csv(path,sep=separador,encoding=tipo_encode)
        base.columns=["fii","cotacao","empresa","data","segmento","div_yield","dividendo_cota","cap_rate","vacancia","p_vp","Qtd Imoveis","Nº de Cotas","liquidez"]
        return base

#classe de regras
class FundosRegras:

    def __init__(self,vacancia,minpvp,maxpvp,liquidez,statuscollector):
        self.vacancia = vacancia
        self.minpvp = minpvp
        self.maxpvp = maxpvp
        self.liquidez = liquidez
        self.statuscollector = statuscollector

    def aplica_regas_gera_realtorio(self, dados):
        self.statuscollector["text"]="Status:Analisando Dados"
        #pegando segmentos para analise de fiis e gerando sub bases para analise
        segmentos = dados["segmento"].unique()
        
        lista_fiis = []
        for tipo_segmento in segmentos:
            lista_fiis.append(dados.query("segmento=='{}'".format(tipo_segmento)))

        print("----------------------------------")
        print("|        Fazendo Analises        |")
        print("----------------------------------")

        #aplicando regras e gerando relatorios
        for dados in lista_fiis:
            dados = dados.query(f"vacancia < {self.vacancia}")
            dados = dados.query(f"liquidez > {self.liquidez}")
            dados = dados.query(f"p_vp >= {self.minpvp} and p_vp <={self.maxpvp}")
            
            print("Gerando relatório de do seguimento: {}".format(dados['segmento'].unique()))
            dados.columns=["fii","cotacao","empresa","data","segmento","dividend_yield %","valor_dividendo_cota","cap_rate %","vacancia %","P/VP","Qtd Imoveis","Nº de Cotas","liquidez"]
            dados.to_excel("export_lista_fiis_investimentos{}.xlsx".format(dados['segmento'].unique()))
        
        self.statuscollector["text"]="Status:Concluido"

