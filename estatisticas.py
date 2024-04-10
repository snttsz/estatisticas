import pandas

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
nome_coluna1 = estatisticas.dataframe.columns[1]
nome_coluna2 = estatisticas.dataframe.columns[2]
nome_coluna3 = estatisticas.dataframe.columns[3]

print(f"Media coluna 1 -> {estatisticas.getMedia(dataframe = estatisticas.norte, coluna = nome_coluna1)}")
print(f"Media coluna 2 -> {estatisticas.getMedia(dataframe = estatisticas.norte, coluna = nome_coluna2)}")
print(f"Media coluna 3 -> {estatisticas.getMedia(dataframe = estatisticas.norte, coluna = nome_coluna3)}")





