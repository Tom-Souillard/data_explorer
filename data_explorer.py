import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataExplorer:

    @staticmethod
    def load_data(filepath):
        data = pd.read_csv(filepath)
        return data

    @staticmethod
    def clean_data(data):
        data = data.drop_duplicates()
        data = data.fillna(data.mean())
        return data

    @staticmethod
    def analyze_data(data):
        description = data.describe()
        correlation = data.corr()
        return description, correlation

    @staticmethod
    def visualize_data(data):
        data.hist(bins=50, figsize=(20, 15))
        plt.show()

        correlation = data.corr()
        mask = np.triu(np.ones_like(correlation, dtype=bool))
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap='coolwarm', mask=mask, cbar_kws={"shrink": .8})
        plt.show()

if __name__ == "__main__":
    file_path = 'examples/example_data.csv'
    explorer = DataExplorer()

    data = explorer.load_data(file_path)
    clean_data = explorer.clean_data(data)
    description, correlation = explorer.analyze_data(clean_data)
    print("Descriptive Statistics:\n", description)
    print("Correlation Matrix:\n", correlation)
    explorer.visualize_data(clean_data)
