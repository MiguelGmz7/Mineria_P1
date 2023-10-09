import math
import numpy as np
import pandas as pd
import os
class Bayes:
    def __init__(self):
        self.frequency = {}
        self.verisim = {}
    
    def compute_frequency(self, data): # toda la serie de pasos para sacar la tabla de frecuencia
        self.group(data)
        self.mean_std('sepal-length')
        self.laplace('sepal-width', tuple=('≥3.2', '<2.8', '2.8-3.2'))
        self.mean_std('petal-length')
        self.laplace('petal-width', tuple=('<0.8','≥1.6','0.8-1.6'))
        #return self.frequency


    def group(self, data): # realiza tabla de frecuencia de los datos (tanto continuos como discretos)
        
        for column_name in data:
            self.frequency[column_name] = {}
            self.frequency[column_name]['Iris-setosa'] = {}
            self.frequency[column_name]['Iris-virginica'] = {}
            self.frequency[column_name]['Iris-versicolor'] = {}
            if column_name == 'iris':
                self.frequency[column_name]['Iris-setosa'][0] = 0
                self.frequency[column_name]['Iris-virginica'][0] = 0 
                self.frequency[column_name]['Iris-versicolor'][0] = 0
            x = 0
            y = 0
            z = 0
        
            for index, row in data.iterrows():

                if data.iloc[index]['iris'] == 'Iris-setosa': # llenamos la columna de iris setosa
                    x += 1
                    if column_name == 'sepal-length':
                        self.frequency[column_name]['Iris-setosa'][x] = data.iloc[index]['sepal-length']

                    if column_name == 'sepal-width':
                        value = data.iloc[index]['sepal-width']
                        if value not in self.frequency[column_name]['Iris-setosa']:
                            self.frequency[column_name]['Iris-setosa'][value] = 1
                        else:
                            self.frequency[column_name]['Iris-setosa'][value] += 1

                    if column_name == 'petal-length':
                        self.frequency[column_name]['Iris-setosa'][x] = data.iloc[index]['petal-length']    
                    
                    if column_name == 'petal-width':
                        value = data.iloc[index]['petal-width']
                        if value not in self.frequency[column_name]['Iris-setosa']:
                            self.frequency[column_name]['Iris-setosa'][value] = 1
                        else:
                            self.frequency[column_name]['Iris-setosa'][value] += 1
                        
                if data.iloc[index]['iris'] == 'Iris-virginica': # columna de iris virginica
                    y += 1
                    if column_name == 'sepal-length':
                        self.frequency[column_name]['Iris-virginica'][y] = data.iloc[index]['sepal-length']

                    if column_name == 'sepal-width':
                        value = data.iloc[index]['sepal-width']
                        if value not in self.frequency[column_name]['Iris-virginica']:
                            self.frequency[column_name]['Iris-virginica'][value] = 1
                        else:
                            self.frequency[column_name]['Iris-virginica'][value] += 1
                    
                    if column_name == 'petal-length':
                        self.frequency[column_name]['Iris-virginica'][y] = data.iloc[index]['petal-length']

                    if column_name == 'petal-width':
                        value = data.iloc[index]['petal-width']
                        if value not in self.frequency[column_name]['Iris-virginica']:
                            self.frequency[column_name]['Iris-virginica'][value] = 1
                        else:
                            self.frequency[column_name]['Iris-virginica'][value] += 1

                
                if data.iloc[index]['iris'] == 'Iris-versicolor':
                    z += 1
                    if column_name == 'sepal-length':
                        self.frequency[column_name]['Iris-versicolor'][z] = data.iloc[index]['sepal-length']
                    
                    if column_name == 'sepal-width':
                        value = data.iloc[index]['sepal-width']
                        if value not in self.frequency[column_name]['Iris-versicolor']:
                            self.frequency[column_name]['Iris-versicolor'][value] = 1
                        else:
                            self.frequency[column_name]['Iris-versicolor'][value] += 1
                    
                    if column_name == 'petal-length':
                        self.frequency[column_name]['Iris-versicolor'][z] = data.iloc[index]['petal-length']
                    
                    if column_name == 'petal-width':
                        value = data.iloc[index]['petal-width']
                        if value not in self.frequency[column_name]['Iris-versicolor']:
                            self.frequency[column_name]['Iris-versicolor'][value] = 1
                        else:
                            self.frequency[column_name]['Iris-versicolor'][value] += 1
                    
                if column_name == 'iris':
                    value = data.iloc[index]['iris']
                    if value == 'Iris-setosa':
                        self.frequency['iris']['Iris-setosa'][0] += 1

                    if value == 'Iris-virginica':
                        self.frequency['iris']['Iris-virginica'][0] += 1

                    if value == 'Iris-versicolor':
                        self.frequency['iris']['Iris-versicolor'][0] += 1
    
        #return self.frequency
        

    def laplace(self,column_name,tuple): # realiza correccion laplaceana para datos continuos
    # ejeplo tuple = ('≥3.2', '<2.8', '2.8-3.2')
        for key in self.frequency[column_name]:
            for i in tuple:
                if i not in self.frequency[column_name][key]:
                    self.frequency[column_name][key][i] = 1
                else: 
                    self.frequency[column_name][key][i] += 1
    
    def mean_std(self, colum_name): # realiza media y desviacion de datos continuos
        
        # for values in self.frequency['sepal-length']['Iris-setosa'].values():
        for key in self.frequency[colum_name]:
            my_list = []
            for value in self.frequency[colum_name][key].values():
                my_list.append(value)
            
            my_array = np.array(my_list)
            self.frequency[colum_name][key]['m'] = my_array.mean()
            self.frequency[colum_name][key]['d'] = my_array.std()
    
    def compute_verisimilitude(self): # tabla de verosimilitud para datos discretos
        columns = ('sepal-width','petal-width', 'iris')
        total = self.frequency['iris']['Iris-setosa'][0] + self.frequency['iris']['Iris-virginica'][0] + self.frequency['iris']['Iris-versicolor'][0]
        for colum_name in columns:
            self.verisim = self.frequency
            for key1 in self.verisim[colum_name]:
                count = 0
                for value in self.verisim[colum_name][key1].values():
                    count += value

                for key2 in self.verisim[colum_name][key1]:
                    self.verisim[colum_name][key1][key2] = self.frequency[colum_name][key1][key2] / count

                if colum_name == 'iris':
                    self.verisim[colum_name][key1][0] = (self.frequency[colum_name][key1][0] / total) / 2

        #return self.verisim

        # for colum_name in columns:
        # self.frequency['iris']['Iris-setosa'][0] = 5 / 15
        # self.frequency['iris']['Iris-virginica'][0] = 5 / 15 # aun no se como resolver
        # self.frequency['iris']['Iris-versicolor'][0] = 5 / 15
        #return self.verisim
            
    def dataframe(self, data):
        #df_verisim = pd.DataFrame.from_dict(self.verisim['sepal-width'], columns = ['Iris-setosa', 'Iris-Virginica', 'Iris-versicolor'])
        count = 0
        win = 0
        y_true = []
        y_pred = []
        ace = False
        for index, row in data.iterrows():
            count += 1
            instance = {}
            instance['Iris-setosa'] = []
            instance['Iris-virginica'] = []
            instance['Iris-versicolor'] = []
            for column_name in data:
                for key in instance:
                    if column_name ==  'sepal-length' or column_name == 'petal-length':
                        x = data.iloc[index][column_name]
                        m = self.verisim[column_name][key]['m']
                        d = self.verisim[column_name][key]['d']
                        densidad = (np.pi*d) * np.exp(-0.5*((x-m)/d)**2)
                        instance[key].append(densidad)
                    
                    if column_name == 'sepal-width':
                        if data.iloc[index][column_name] == '≥3.2':
                            v = self.verisim[column_name][key]['≥3.2']
                            instance[key].append(v)

                        if data.iloc[index][column_name] == '<2.8':
                            v = self.verisim[column_name][key]['<2.8']
                            instance[key].append(v)
                        
                        if data.iloc[index][column_name] == '2.8-3.2':
                            v = self.verisim[column_name][key]['2.8-3.2']
                            instance[key].append(v)
                    
                    if column_name == 'petal-width':
                        if data.iloc[index][column_name] == '<0.8':
                            v = self.verisim[column_name][key]['<0.8']
                            instance[key].append(v)

                        if data.iloc[index][column_name] == '≥1.6':
                            v = self.verisim[column_name][key]['≥1.6']
                            instance[key].append(v)
                        
                        if data.iloc[index][column_name] == '0.8-1.6':
                            v = self.verisim[column_name][key]['0.8-1.6']
                            instance[key].append(v)
                    
                    if column_name == 'iris':
                            v = self.verisim[column_name][key][0]
                            instance[key].append(v)

            print("--------------------------------------------------------------")
            #results = []
            comp = {}
            for key in instance: # la multiplicacion de cada clase
                result = 1
                for x in instance[key]:
                    result = result * x
                    #results.append(result)
                    comp[key] = result
            total = 0
            for key in comp: # el total
                total += comp[key]
            for key in comp:
                comp[key] = comp[key] / total
            
            r = comp.values()
 
            # Convert object to a list
            dt = list(r)
            
            # Convert list to an array
            numpyArray = np.array(dt)
            max = numpyArray.max()
            
            for key in comp:
                if max == comp[key]:
                    prediccion = key
            
            if prediccion == data.iloc[index]['iris']:
                win += 1
                ace = True
            y_true.append(data.iloc[index]['iris'])
            y_pred.append(prediccion)

            if ace == True:
                print(f"{count}: Prediccion: {prediccion} Realidad: {data.iloc[index]['iris']} Acierto?: Verdadero")
                ace = False
            else:
                print(f"{count}: Prediccion: {prediccion} Realidad: {data.iloc[index]['iris']} Acierto?: Falso")

        accuracy = win / count
        self.matriz_confusion(np.array(y_true), np.array(y_pred))
        print(f"Acuracy: {accuracy}")

    def multiplylist(key, instance):
        result = 1
        for x in instance[key]:
            result = result * x
        return result
    
    def print_tables(self,str):

        #frequencia 
            for key1 in self.frequency:
                print(str) 
                print("{:<20} {:<20} {:<20}".format('index', key1, 'Clase'))
        
                # print each data item.
                for key2 in self.frequency[key1]:
                        for key3 in self.frequency[key1][key2]:
                            print("{:<20} {:<20} {:<20}".format(key3, self.frequency[key1][key2][key3], key2))
                        
                        print("----------------------------------------------------------------------")
                input("presione una tecla....")
                os.system("cls")
            #print("----------------------------------------------------------------------")

    def matriz_confusion(self, y_true, y_pred):
        