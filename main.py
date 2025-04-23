
import argparse
from src.data_loader import DataLoader
from src.analyzer import DataAnalyzer
from src.visualizer import DataVisualizer

def main():
    parser = argparse.ArgumentParser(description="Data Analyzer Tool")
    parser.add_argument("filepath", help="Path to CSV file")
    parser.add_argument("--analysis", choices=["summary", "time", "top"], default="summary")
    parser.add_argument("--plot", choices=["bar", "line", "pie", "heatmap"], default=None)
    parser.add_argument("--output", help="Output image filename", default=None)
    args = parser.parse_args()

    loader = DataLoader(args.filepath)
    df = loader.load_data()
    loader.validate_data()

    analyzer = DataAnalyzer(df)
    visualizer = DataVisualizer(df)

    if args.analysis == "summary":
        print(analyzer.summary_statistics())
    elif args.analysis == "time":
        print(analyzer.spending_over_time())
    elif args.analysis == "top":
        print(analyzer.top_categories())

    if args.plot:
        fig = None
        if args.plot == "bar":
            fig = visualizer.bar_chart_by_category()
        elif args.plot == "line":
            fig = visualizer.line_chart_over_time()
        elif args.plot == "pie":
            fig = visualizer.pie_chart_by_category()
        elif args.plot == "heatmap":
            fig = visualizer.correlation_heatmap()

        if fig and args.output:
            fig.savefig(args.output)

if __name__ == "__main__":
    main()
