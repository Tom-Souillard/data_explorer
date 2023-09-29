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

if __name__ == "__main__":
    file_path = 'examples/example_data.csv'
    explorer = DataExplorer()

    data = explorer.load_data(file_path)
    clean_data = explorer.clean_data(data)
