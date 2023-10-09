import pandas as pd
import numpy as np
from bayes import Bayes


def main():
    file_path = "../datasets/iris.csv"
    df = pd.read_csv(file_path)
    #train_sample_size = .7
    bayes = Bayes()
    
   
    bayes.compute_frequency(df)
    bayes.print_tables("Tabla de Frequencia")
    bayes.compute_verisimilitude()
    bayes.print_tables("Tabla de verisimilitud")
    bayes.dataframe(df)
if __name__ == '__main__':
    main()