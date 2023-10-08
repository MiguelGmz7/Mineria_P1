import pandas as pd
from bayes import Bayes


def main():
    file_path = "../datasets/iris.csv"
    df = pd.read_csv(file_path)
    #train_sample_size = .7
    bayes = Bayes()
    # frequency = bayes.group(df)
    #tuple = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'iris']
    
    # print(frequency)
    bayes.group(df)
if __name__ == '__main__':
    main()