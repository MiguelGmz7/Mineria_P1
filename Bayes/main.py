import pandas as pd
from bayes import Bayes


def main():
    file_path = "../datasets/iris.csv"
    df = pd.read_csv(file_path)
    #train_sample_size = .7
    bayes = Bayes()
    frequency = bayes.compute_frequency(df)
    #tuple = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'iris']
    
    print("Tabla: ")
    print(frequency)

    # print("-------------------------------------------------------------------------------")

    # print("Tabla Normalizada")
    # print(bayes.laplace("sepal-width"))
if __name__ == '__main__':
    main()