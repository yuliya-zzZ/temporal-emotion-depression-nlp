import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Load raw CSV data."""
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    df["text"] = df["text"].astype(str)
    return df


def basic_clean(text: str) -> str:
    """Basic lowercase and whitespace cleaning."""
    return text.lower().strip()


def preprocess_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Apply basic text preprocessing to the full dataframe."""
    df = df.copy()
    df["clean_text"] = df["text"].apply(basic_clean)
    return df
