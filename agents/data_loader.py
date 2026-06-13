"""Load synthetic Syntrix demo data."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "synthetic_data"


def load_interactions(path: Path | None = None) -> pd.DataFrame:
    """Load synthetic Copilot-style interaction logs."""

    data_path = path or DATA_DIR / "copilot_interactions.csv"
    df = pd.read_csv(data_path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def load_profiles(path: Path | None = None) -> pd.DataFrame:
    """Load synthetic role profiles used by the sidebar selector."""

    data_path = path or DATA_DIR / "profiles.csv"
    return pd.read_csv(data_path)
