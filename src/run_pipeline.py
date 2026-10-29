
import logging

from src.data_loader import load_raw_data
from src.cleaning import clean_sales_data, save_clean_data


def main():
    logging.basicConfig(level=logging.INFO)

    raw_data = load_raw_data("data/sales.csv")
    clean_data = clean_sales_data(raw_data)
    output_path = save_clean_data(clean_data)

    print(f"Cleaning completed. Output saved to: {output_path}")


if __name__ == "__main__":
    main()
