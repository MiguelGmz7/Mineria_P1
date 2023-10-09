import pandas as pd
import numpy as np
from bayes import Bayes


def main():
    file_path = "../datasets/iris.csv"
    df = pd.read_csv(file_path)
    #train_sample_size = .7
    bayes = Bayes()
    #frequency = bayes.compute_frequency(df)
    
   # print(frequency)

    
    # # Creating a Python list "my_list".
    # my_list = [2.1, 4.0, 3.2, 5.0, 3.5]
    # # Creating a NumPy array from my_list
    # my_array = np.array(my_list)
    # print( my_array.mean())
    
    # print("Tabla de frecuencia: ")
    # print(bayes.compute_frequency(df))
    # print("-------------------------------------------------")
    print("Tabla de frequencia: ") 
    print(bayes.compute_frequency(df)) 
    #bayes.compute_verisimilitude()
    # bayes.compute_verisimilitude()
    print("Tabla de Verosimilitud: ")
    print(bayes.compute_verisimilitude())
    bayes.dataframe(df)
if __name__ == '__main__':
    main()