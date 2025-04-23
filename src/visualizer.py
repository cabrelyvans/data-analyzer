
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def bar_chart_by_category(self):
        data = self.df.groupby("category")["amount"].sum().sort_values()
        ax = data.plot(kind="bar", title="Spending by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Spending")
        plt.tight_layout()
        return ax.get_figure()

    def line_chart_over_time(self):
        data = self.df.groupby("date")["amount"].sum()
        ax = data.plot(title="Spending Over Time")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.tight_layout()
        return ax.get_figure()

    def pie_chart_by_category(self):
        data = self.df.groupby("category")["amount"].sum()
        fig, ax = plt.subplots()
        ax.pie(data, labels=data.index, autopct="%1.1f%%")
        ax.set_title("Spending Distribution")
        return fig

    def correlation_heatmap(self):
        corr = self.df.select_dtypes(include=["float", "int"]).corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, ax=ax)
        ax.set_title("Correlation Heatmap")
        return fig
