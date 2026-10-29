
import logging
import re
from pathlib import Path

import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

REQUIRED_COLUMNS = {
    "order_date",
    "product_name",
    "sales",
    "quantity",
}


class DataValidationError(ValueError):
    """Raised when the input data is invalid."""


def normalize_column_name(name: str) -> str:
    """Convert column names to lowercase snake_case."""
    name = name.strip().lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")


def load_raw_data(file_path: str | Path) -> pd.DataFrame:
    """Load a CSV file and validate its structure."""
    path = Path(file_path)

    if not path.exists():
        logger.error("Input file does not exist: %s", path)
        raise FileNotFoundError(f"Input file not found: {path}")

    try:
        df = pd.read_csv(path)
    except (OSError, UnicodeError, pd.errors.ParserError) as exc:
        logger.exception("Could not read input file")
        raise DataValidationError(
            f"Could not read CSV file: {exc}"
        ) from exc

    if df.empty:
        raise DataValidationError("The input file contains no data.")

    df.columns = [
        normalize_column_name(str(column))
        for column in df.columns
    ]

    if df.columns.duplicated().any():
        raise DataValidationError(
            "Duplicate column names found after normalization."
        )

    missing = REQUIRED_COLUMNS - set(df.columns)

    if missing:
        raise DataValidationError(
            f"Required columns are missing: {sorted(missing)}"
        )

    logger.info(
        "Loaded %s rows and %s columns from %s",
        len(df),
        len(df.columns),
        path,
    )

    return df
