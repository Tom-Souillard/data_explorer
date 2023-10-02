import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class DataExplorer:
    """A class for performing exploratory data analysis (EDA).

    This class provides methods for loading data, cleaning data,
    performing descriptive analysis, and visualizing data.
    """

    @staticmethod
    def load_data(filepath):
        """Load data from a CSV file.

        Args:
            filepath (str): The path to the CSV file.

        Returns:
            pd.DataFrame: The loaded data as a pandas DataFrame.
        """
        try:
            data = pd.read_csv(filepath)
            return data
        except Exception as e:
            raise ValueError(f"Failed to load data from {filepath}: {e}")

    @staticmethod
    def clean_data(data):
        """Clean the data by removing duplicates and handling missing values.

        Args:
            data (pd.DataFrame): The data to be cleaned.

        Returns:
            pd.DataFrame: The cleaned data.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame")

        # Drop duplicate rows
        data = data.drop_duplicates()

        # Impute missing values with the mean of each column
        data = data.fillna(data.mean())

        return data

    @staticmethod
    def analyze_data(data):
        """Perform descriptive analysis on the data.

        Args:
            data (pd.DataFrame): The data to be analyzed.

        Returns:
            tuple: A tuple containing:
                - pd.DataFrame: Descriptive statistics of the data.
                - pd.DataFrame: Correlation matrix of the data.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame")

        # Generate descriptive statistics
        description = data.describe()

        # Generate correlation matrix, leaving NaN values
        correlation = data.corr()

        return description, correlation

    @staticmethod
    def visualize_data(data):
        """Visualize the data using histograms and a heatmap.

        Args:
            data (pd.DataFrame): The data to be visualized.

        Raises:
            ValueError: If the input data is not a pandas DataFrame.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame")

        # Plot histograms for each feature
        data.hist(bins=50, figsize=(20, 15))
        plt.suptitle('Histograms of Data Features')
        plt.show()

        # Plot a heatmap of the correlation matrix
        correlation = data.corr()
        mask = np.triu(np.ones_like(correlation, dtype=bool))
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation, annot=True, cmap='coolwarm', mask=mask, cbar_kws={"shrink": .8})
        plt.title('Heatmap of Feature Correlations')
        plt.show()


if __name__ == "__main__":
    # Example usage
    file_path = 'examples/example_data.csv'
    explorer = DataExplorer()

    # Load data
    data = explorer.load_data(file_path)
    print("Data loaded successfully.")

    # Clean data
    clean_data = explorer.clean_data(data)
    print("Data cleaned successfully.")

    # Analyze data
    description, correlation = explorer.analyze_data(clean_data)
    print("Data analysis completed successfully.")
    print("Descriptive Statistics:\n", description)
    print("Correlation Matrix:\n", correlation)

    # Visualize data
    explorer.visualize_data(clean_data)
    print("Data visualization completed successfully.")
