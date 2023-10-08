import pandas
class Bayes:
    def __init__(self):
        self.frequency = {}

    def group(self, data):
        self.frequency = {}
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
            
        # if column_name == 'sepal-width':
        #     print("hola")
        #     tuple = ('≥3.2', '<2.8', '2.8-3.2')
        #     for key in self.frequency[column_name]:
        #         print("entrando en ciclo")
        #         print(key)
        #         #if self.frequency[column_name][key].keys() != tuple:
        #         for i in self.frequency[column_name][key]:
        #             for j in tuple:
        #                 print(i, " = ", j)
        #                 if i == j:
        #                     self.frequency[column_name][key][i] += 1
        #                 else:
        #                     self.frequency[column_name][key][j] = 0

 
            #   tuple = ('≥3.2', '<2.8', '2.8-3.2')
            #   for i in tuple:
            #       if i not in self.frequency[column_name]['Iris-setosa']:
            #           self.frequency[column_name]['Iris-setosa'][i] = 0
            #       if i not in self.frequency[column_name]['Iris-virginica']:
            #           self.frequency[column_name]['Iris-virginica'][i] = 0
            #       if i not in self.frequency[column_name]['Iris-versicolor']:
            #           self.frequency[column_name]['Iris-versicolor'][i] = 0
        # como iterar en un diccionario dentro de otro diccionario
        
        
        if column_name == 'iris':
            self.frequency['iris']['Iris-setosa'][0] = 5
            self.frequency['iris']['Iris-virginica'][0] = 5 # aun no se como resolver
            self.frequency['iris']['Iris-versicolor'][0] = 5
        
        #return self.frequency