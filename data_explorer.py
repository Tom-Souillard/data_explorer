import pandas as pd

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

if __name__ == "__main__":
    file_path = 'examples/example_data.csv'
    explorer = DataExplorer()

    data = explorer.load_data(file_path)
    clean_data = explorer.clean_data(data)
    description, correlation = explorer.analyze_data(clean_data)
    print("Descriptive Statistics:\n", description)
    print("Correlation Matrix:\n", correlation)
