
import logging
from pathlib import Path

import pandas as pd

from src.data_loader import REQUIRED_COLUMNS, DataValidationError

logger = logging.getLogger(__name__)


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Validate and clean sales data without modifying the input."""
    if df.empty:
        raise DataValidationError("Cannot clean an empty DataFrame.")

    missing = REQUIRED_COLUMNS - set(df.columns)

    if missing:
        raise DataValidationError(
            f"Required columns are missing: {sorted(missing)}"
        )

    clean_df = df.copy()
    initial_rows = len(clean_df)

    # Convert dates and numeric columns.
    clean_df["order_date"] = pd.to_datetime(
        clean_df["order_date"], errors="coerce"
    )
    clean_df["sales"] = pd.to_numeric(
        clean_df["sales"], errors="coerce"
    )
    clean_df["quantity"] = pd.to_numeric(
        clean_df["quantity"], errors="coerce"
    )

    # Remove rows with missing essential values.
    clean_df["product_name"] = clean_df["product_name"].astype("string").str.strip()

    clean_df = clean_df.dropna(
        subset=["order_date", "product_name", "sales", "quantity"]
    )

    clean_df = clean_df[
        clean_df["product_name"].ne("")
        & clean_df["quantity"].gt(0)
    ]

    # Remove exact duplicate records.
    clean_df = clean_df.drop_duplicates().reset_index(drop=True)

    # Store numeric values consistently.
    clean_df["sales"] = clean_df["sales"].astype(float)
    clean_df["quantity"] = clean_df["quantity"].astype(int)

    removed_rows = initial_rows - len(clean_df)

    logger.info(
        "Cleaning completed: %s rows before, %s after, %s removed",
        initial_rows,
        len(clean_df),
        removed_rows,
    )

    if clean_df.empty:
        raise DataValidationError(
            "No valid rows remain after cleaning."
        )

    return clean_df


def save_clean_data(
    df: pd.DataFrame,
    output_path: str | Path = "data/clean/sales_clean.csv",
) -> Path:
    """Save cleaned data as CSV."""
    if df.empty:
        raise DataValidationError("Cannot save an empty DataFrame.")

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    try:
        df.to_csv(path, index=False)
    except OSError:
        logger.exception("Could not save cleaned data to %s", path)
        raise

    logger.info("Clean data saved to %s", path)
    return path
