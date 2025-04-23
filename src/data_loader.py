
import pandas as pd

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.filepath, parse_dates=["date"])
        return self.df

    def validate_data(self):
        required_columns = {"date", "category", "amount", "customer_id"}
        if not required_columns.issubset(set(self.df.columns)):
            raise ValueError("Missing required columns.")
        self.df.dropna(inplace=True)

    def filter_by_date_range(self, start_date, end_date):
        return self.df[(self.df['date'] >= start_date) & (self.df['date'] <= end_date)]

    def filter_by_category(self, categories):
        return self.df[self.df['category'].isin(categories)]
