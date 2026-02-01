import sys
from src.load_data import load_data

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_analysis.py <path_to_csv>")
        return

    csv_path = sys.argv[1]
    df = load_data(csv_path)

if __name__ == "__main__":
    main()
