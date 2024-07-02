"""Helper module to transform the original dataset.

Use `transform()` to apply to all supported columns, with functions
for each individual column for special use cases.
"""

from pandas import concat, to_numeric, DataFrame


def _insert_replace(df: DataFrame, new_data: DataFrame, column: str):
    """Insert columns of new data to replace an existing column in a data frame."""
    col_idx = df.columns.get_loc(column)
    return concat([df.iloc[:, :col_idx], new_data, df.iloc[:, col_idx + 1 :]], axis=1)


def expand_location(df: DataFrame):
    """Expand the "location" column to "country", "state", "city" columns."""
    new_cols = df["location"].str.split(",", expand=True, n=2)
    new_cols.rename(columns={0: "country", 1: "state", 2: "city"}, inplace=True)
    for col in new_cols.columns:
        new_cols[col] = new_cols[col].str.strip().str.lower()
    return _insert_replace(df, new_cols, "location")


def expand_salary_range(df: DataFrame):
    """Expand the "salary_range" column to "salary_min" & "salary_max" columns.

    Values that can't coerce to numbers will be substituted with `-1`.
    """
    new_cols = df["salary_range"].str.split("-", expand=True, n=1)
    new_cols.rename(columns={0: "salary_min", 1: "salary_max"}, inplace=True)
    for col in new_cols.columns:
        new_cols[col] = to_numeric(new_cols[col], errors="coerce").fillna(-1)
    return _insert_replace(df, new_cols, "salary_range")


def transform(df: DataFrame):
    """Transform all supported columns for usable features."""
    new_df = expand_location(df)
    new_df = expand_salary_range(new_df)
    return new_df
