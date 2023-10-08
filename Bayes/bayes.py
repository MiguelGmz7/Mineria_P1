import pandas
class Bayes:
    def __init__(self):
        self.frequency = {}
    
    def compute_frequency(self, data):
        self.group(data)
        self.laplace('sepal-width', tuple=('≥3.2', '<2.8', '2.8-3.2'))
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
            
        
        if column_name == 'sepal-width':
            self.laplace(column_name, tuple=('≥3.2', '<2.8', '2.8-3.2'))
        
        if column_name == 'petal-width':
            self.laplace(column_name, tuple=('<0.8','≥1.6','0.8-1.6'))
        
        if column_name == 'iris':
            self.frequency['iris']['Iris-setosa'][0] = 5
            self.frequency['iris']['Iris-virginica'][0] = 5 # aun no se como resolver
            self.frequency['iris']['Iris-versicolor'][0] = 5
        
        #return self.frequency
    
    def laplace(self,column_name,tuple):
    # ejeplo tuple = ('≥3.2', '<2.8', '2.8-3.2')
        for key in self.frequency[column_name]:
            for i in tuple:
                if i not in self.frequency[column_name][key]:
                    self.frequency[column_name][key][i] = 1
                else: 
                    self.frequency[column_name][key][i] += 1