
class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    def summary_statistics(self):
        return self.df.groupby("category")["amount"].agg(["mean", "median", "std"])

    def spending_over_time(self):
        return self.df.groupby("date")["amount"].sum()

    def top_categories(self, n=5):
        return self.df.groupby("category")["amount"].sum().sort_values(ascending=False).head(n)

    def customer_segmentation(self):
        return self.df.groupby("customer_id")["amount"].sum().sort_values(ascending=False)
