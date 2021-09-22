#Autor:Diego Lopes da Silva
#Data:21/09/2021
#Descrição:Script para tratar dados e aplica regras em cima dos fundos imobiliarios

import pandas as pd

#classe para carregar dados
class CarregarDados:

    @staticmethod
    def carrega_dados(path, separador, tipo_encode):
        print("|-------------------------|")
        print(">> Carregando base de dados")
        print("|-------------------------|")
        base =pd.read_csv(path,sep=separador,encoding=tipo_encode)
        base.columns=["fii","cotacao","empresa","data","segmento","div_yield","dividendo_cota","cap_rate","vacancia"]
        return base

#classe de regras
class FundosRegras:

    def aplica_regas_gera_realtorio(self, dados):
        #pegando segmentos para analise de fiis e gerando sub bases para analise
        segmentos = dados["segmento"].unique()
        
        lista_fiis = []
        for tipo_segmento in segmentos:
            lista_fiis.append(dados.query("segmento=='{}'".format(tipo_segmento)))

        #aplicando regras e gerando relatorios
        for dados in lista_fiis:
            dados = dados.query("vacancia < 2")
            dados = dados.query("div_yield > 1 and cap_rate > 1")
            dados.columns=["fii","cotacao","empresa","data","segmento","div_yield %","dividendo_cota %","cap_rate %","vacancia %"]
            dados.to_excel("export_lista_fiis_investimentos{}.xlsx".format(dados['segmento'].unique()))

