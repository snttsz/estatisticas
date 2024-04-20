import pandas
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

class Estatisticas():

    def __init__(self) -> None:

        """ 
            Dataframe com todos os dados
        """
        self.dataframe = pandas.read_csv("Estatistica-uso-de-internet-2010.csv")

        """ 
            Dataframe para guardar os totais de cada região
        """
        self.brasil = pandas.DataFrame()

        """ 
            Dataframes para guardar os totais por estado de cada região

            Ex: self.norte contém as linhas e colunas associadas ao estado do Acre, 
            Amazonas, Roraima, Pará, etc...
        """
        self.norte = pandas.DataFrame()
        self.nordeste = pandas.DataFrame()
        self.sudeste = pandas.DataFrame()
        self.sul = pandas.DataFrame()
        self.centro_oeste = pandas.DataFrame()

        self.dividir_dataframes()

    def dividir_dataframes(self):
        """ 
            Divide o dataframe principal em sub-dataframes.
        """

        primeira_coluna = self.dataframe["Grandes Regiões, Unidades da Federação e Regiões Metropolitanas"]

        """ 
            Indice de cada região para iterar por cada uma e adicionar cada estado
            em sua respectiva região.
        """
        indice_norte = self.dataframe.index[primeira_coluna == "Norte"].tolist()[0]
        indice_nordeste = self.dataframe.index[primeira_coluna == "Nordeste"].tolist()[0]
        indice_sudeste = self.dataframe.index[primeira_coluna == "Sudeste"].tolist()[0]
        indice_sul = self.dataframe.index[primeira_coluna == "Sul"].tolist()[0]
        indice_centro_oeste = self.dataframe.index[primeira_coluna == "Centro-Oeste"].tolist()[0]

        """ 
            Lista para adicionar as linhas do estado associadao a cada região
        """
        estados_regiao_norte = []
        estados_regiao_nordeste = []
        estados_regiao_sul = []
        estados_regiao_sudeste = []
        estados_regiao_centro_oeste = []
        brasil = []

        for indice, linha in self.dataframe.iterrows():

            if indice > indice_norte and indice < indice_nordeste:
                estados_regiao_norte.append(linha)
            
            elif indice > indice_nordeste and indice < indice_sudeste:
                estados_regiao_nordeste.append(linha)
            
            elif indice > indice_sudeste and indice < indice_sul:
                estados_regiao_sudeste.append(linha)
            
            elif indice > indice_sul and indice < indice_centro_oeste:
                estados_regiao_sul.append(linha)

            elif indice > indice_centro_oeste:
                estados_regiao_centro_oeste.append(linha) 
            
            elif linha["Grandes Regiões, Unidades da Federação e Regiões Metropolitanas"] != "Brasil":
                brasil.append(linha)

        """ 
            Adicionando as listas como linhas dentro dos sub-dataframes
        """
        self.norte = pandas.DataFrame(estados_regiao_norte, columns = self.dataframe.columns)
        self.nordeste = pandas.DataFrame(estados_regiao_nordeste, columns = self.dataframe.columns)
        self.sudeste = pandas.DataFrame(estados_regiao_sudeste, columns = self.dataframe.columns)
        self.sul = pandas.DataFrame(estados_regiao_sul, columns = self.dataframe.columns)
        self.centro_oeste = pandas.DataFrame(estados_regiao_centro_oeste, columns = self.dataframe.columns)
        self.brasil = pandas.DataFrame(brasil, columns = self.dataframe.columns)

    def getMedia(self, dataframe: pandas.DataFrame, coluna) -> float:

        return dataframe[coluna].mean()

    def getMediana(self, dataframe: pandas.DataFrame, coluna) -> float:
        
        return dataframe[coluna].median()

    def getModa(self, dataframe: pandas.DataFrame, coluna) -> float:
        
        return dataframe[coluna].mode()

    def getDesvioPadrao(self, dataframe: pandas.DataFrame, coluna) -> float:
        
        return dataframe[coluna].std()
    
    def getVariancia(self, dataframe: pandas.DataFrame, coluna) -> float:
        
        return dataframe[coluna].var()
    
estatisticas = Estatisticas()

""" 
    Exemplo de uso 
"""
# nome_coluna1 = estatisticas.dataframe.columns[1]
# nome_coluna2 = estatisticas.dataframe.columns[2]
# nome_coluna3 = estatisticas.dataframe.columns[3]

# print(f"Media coluna 1 -> {estatisticas.getMedia(dataframe = estatisticas.norte, coluna = nome_coluna1)}")
# print(f"Media coluna 2 -> {estatisticas.getMedia(dataframe = estatisticas.norte, coluna = nome_coluna2)}")
# print(f"Media coluna 3 -> {estatisticas.getMedia(dataframe = estatisticas.norte, coluna = nome_coluna3)}")

dados_regioes = {
    "Norte": estatisticas.norte,
    "Nordeste" : estatisticas.nordeste,
    "Sudeste" : estatisticas.sudeste,
    "Sul" : estatisticas.sul,
    "Centro Oeste" : estatisticas.centro_oeste
}

def gerar_media_de_participantes_da_pesquisa():
    
    nome_coluna = estatisticas.dataframe.columns[1]
    
    # Calcula a media e desvio padrão
    regioes = list(dados_regioes.keys())
    medias = [dados[nome_coluna].mean() for dados in dados_regioes.values()]
    
    # Plota no grafico
    plt.figure(figsize=(14, 8))
    barras = plt.bar(regioes, medias, capsize=5)
    plt.xlabel('Região')
    plt.ylabel('Média de pessoas (por 1000 pessoas)')
    plt.title('Média de pessoas de 10 anos ou mais de idade que utilizaram a Internet para o estudo por região do país')
    plt.xticks(rotation=45)
    
    # Define referências no eixo y
    max_mediana = max(medias)
    referencias_y = range(0, int(max_mediana) + 1000, 1000)
    plt.yticks(referencias_y)
    
    # Adiciona referencias para as barras
    for barra in barras:
        yval = barra.get_height()
        plt.axhline(y=yval, color='gray', linestyle='--', linewidth=0.5, zorder = 0)
        plt.text(barra.get_x() + barra.get_width()/2, yval + 0.2, round(yval), ha='center', va='bottom')
    
    plt.show()


def gerar_moda_de_participantes_da_pesquisa():
    
    nome_coluna = estatisticas.dataframe.columns[1]
    
    # Calcula a moda
    regioes = list(dados_regioes.keys())
    modas = [dados[nome_coluna].mode().iloc[0] for dados in dados_regioes.values()]
    
    # Plota no grafico
    plt.figure(figsize=(14, 8))
    barras = plt.bar(regioes, modas, capsize=5, color="green")
    plt.xlabel('Região')
    plt.ylabel('Moda da quantidade de pessoas (por 1000 pessoas)')
    plt.title('Moda da quantidade de pessoas de 10 anos ou mais de idade que utilizaram a Internet para o estudo por região do país')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Define referências no eixo y
    max_mediana = max(modas)
    referencias_y = range(0, int(max_mediana) + 1000, 1000)
    plt.yticks(referencias_y)
    
    # Adiciona referencias para as barras
    for barra in barras:
        yval = barra.get_height()
        plt.axhline(y=yval, color='gray', linestyle='--', linewidth=0.5, zorder = 0)
        plt.text(barra.get_x() + barra.get_width()/2, yval + 0.2, round(yval), ha='center', va='bottom')
    
    plt.show()
    

def gerar_mediana_de_participantes_da_pesquisa():
    nome_coluna = estatisticas.dataframe.columns[1]
    
    # Calcula a mediana
    regioes = list(dados_regioes.keys())
    medianas = [dados[nome_coluna].median() for dados in dados_regioes.values()]
    
    # Plota no grafico
    plt.figure(figsize=(14, 8))
    barras = plt.bar(regioes, medianas, capsize=5, color="purple")
    plt.xlabel('Região')
    plt.ylabel('Mediana da quantidade de pessoas (por 1000 pessoas)')
    plt.title('Mediana da quantidade de pessoas de 10 anos ou mais de idade que utilizaram a Internet para o estudo por região do país')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Define referências no eixo y
    max_mediana = max(medianas)
    referencias_y = range(0, int(max_mediana) + 1000, 1000)
    plt.yticks(referencias_y)
    
    # Adiciona referencias para as barras
    for barra in barras:
        yval = barra.get_height()
        plt.axhline(y=yval, color='gray', linestyle='--', linewidth=0.5, zorder = 0)
        plt.text(barra.get_x() + barra.get_width()/2, yval + 0.2, round(yval), ha='center', va='bottom')
    
    plt.show()


def gerar_histograma():

    #Obtendo dataframe
    dataFrame = estatisticas.brasil

    #Obtendo os intervalos do eixo x  
    grupos_eixo_x = dataFrame.keys()[2:]

    for index, row in dataFrame.iterrows():

        dados = row.values
        nome_regiao = dados[0]
        plt.figure(num=f"Histograma da Região {nome_regiao}", figsize=(14, 8))

        plt.title(f"Histograma da Região {nome_regiao} \n")
        plt.bar(grupos_eixo_x, dados[2:], capsize=5, color="purple")
        plt.xlabel("\nGrupos de anos de estudo Sem instrução")
        plt.ylabel("Quantidade de usuários", labelpad=20)

        plt.show()

def gerar_poligono_frequencia():

 # Obtendo dataframe
    dataFrame = estatisticas.brasil

    # Obtendo os intervalos do eixo x
    grupos_eixo_x = dataFrame.keys()[2:]

    for index, row in dataFrame.iterrows():

        dados = row.values
        nome_regiao = dados[0]
        plt.figure(num=f"Polígono de frequência absoluta da Região {nome_regiao}", figsize=(14, 8))

        plt.title(f"Polígono de frequência absoluta da Região {nome_regiao} \n")
        plt.bar(grupos_eixo_x, dados[2:], capsize=5, color="purple")
        plt.xlabel("\nGrupos de anos de estudo Sem instrução")
        plt.ylabel("Quantidade de usuários", labelpad=20)

        # Plotar polígono de frequência
        plt.plot(grupos_eixo_x, dados[2:], marker='o', linestyle='-')

        plt.show()

def gerar_poligono_frequencia_acumulada():

 # Obtendo dataframe
    dataFrame = estatisticas.brasil

    # Obtendo os intervalos do eixo x
    grupos_eixo_x = dataFrame.keys()[2:]

    for index, row in dataFrame.iterrows():

        dados = row.values
        nome_regiao = dados[0]

        plt.figure(num=f"Polígono de frequência acumulada da Região {nome_regiao}", figsize=(14, 8))
        plt.title(f"Polígono de frequência acumulada da Região {nome_regiao} \n")

        # Calculando frequências acumuladas
        frequencias = dados[2:]
        frequencias_acumuladas = np.cumsum(frequencias)

        plt.bar(grupos_eixo_x, frequencias, capsize=5, color="purple")
        plt.xlabel("\nGrupos de anos de estudo Sem instrução")
        plt.ylabel("Quantidade de usuários", labelpad=20)

        # Plotar polígono de frequência
        plt.plot(grupos_eixo_x, frequencias_acumuladas, marker='o', linestyle='-')

        plt.show()


if __name__ == "__main__":

    #gerar_media_de_participantes_da_pesquisa()
    #gerar_moda_de_participantes_da_pesquisa()
    #gerar_mediana_de_participantes_da_pesquisa()
    gerar_poligono_frequencia_acumulada()