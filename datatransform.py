"""Helper module to transform the original dataset.

Use `transform()` to apply to all supported columns, with functions
for each individual column for special use cases.
"""

import pandas as pd
from pandas import DataFrame, Series


def expand_location(df: DataFrame):
    """Expand the "location" column to country, state, city."""
    new_cols = df["location"].str.split(",", expand=True, n=2)
    new_cols.rename(columns={0: "country", 1: "state", 2: "city"}, inplace=True)
    for col in ["country", "state", "city"]:
        new_cols[col] = new_cols[col].str.strip().str.lower()
    return pd.concat([df.drop(columns="location"), new_cols], axis=1)


def transform(df: DataFrame):
    """Transform all supported columns for usable features."""
    print("not implemented")
