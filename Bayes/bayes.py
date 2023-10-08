import pandas
import numpy as np
class Bayes:
    def __init__(self):
        self.frequency = {}
        self.verisim = {}
    
    def compute_frequency(self, data):
        self.group(data)
        self.mean_std('sepal-length')
        self.laplace('sepal-width', tuple=('≥3.2', '<2.8', '2.8-3.2'))
        self.mean_std('petal-length')
        self.laplace('petal-width', tuple=('<0.8','≥1.6','0.8-1.6'))
        return self.frequency


    def group(self, data):
        for column_name in data:
            self.frequency[column_name] = {}
            self.frequency[column_name]['Iris-setosa'] = {}
            self.frequency[column_name]['Iris-virginica'] = {}
            self.frequency[column_name]['Iris-versicolor'] = {}
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
            self.frequency['iris']['Iris-setosa'][0] = 5
            self.frequency['iris']['Iris-virginica'][0] = 5 # aun no se como resolver
            self.frequency['iris']['Iris-versicolor'][0] = 5
        

    def laplace(self,column_name,tuple):
    # ejeplo tuple = ('≥3.2', '<2.8', '2.8-3.2')
        for key in self.frequency[column_name]:
            for i in tuple:
                if i not in self.frequency[column_name][key]:
                    self.frequency[column_name][key][i] = 1
                else: 
                    self.frequency[column_name][key][i] += 1
    
    def mean_std(self, colum_name):
        
        # for values in self.frequency['sepal-length']['Iris-setosa'].values():
        for key in self.frequency[colum_name]:
            my_list = []
            for value in self.frequency[colum_name][key].values():
                my_list.append(value)
            
            my_array = np.array(my_list)
            self.frequency[colum_name][key]['m'] = my_array.mean()
            self.frequency[colum_name][key]['d'] = my_array.std()
    
    def compute_verisimilitude(self):
        columns = ('sepal-width','petal-width')
        for colum_name in columns:
            self.verisim = self.frequency
            for key1 in self.verisim[colum_name]:
                count = 0
                for value in self.verisim[colum_name][key1].values():
                    count += value

                for key2 in self.verisim[colum_name][key1]:
                    self.verisim[colum_name][key1][key2] = self.frequency[colum_name][key1][key2] / count
        
        return self.verisim
            