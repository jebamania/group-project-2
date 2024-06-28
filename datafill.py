"""Helper module to fill missing data from the original dataset.

Use `fill_missing()` to apply to all supported columns, with functions
for each individual column for special use cases.

Note: functions will modify passed DataFrame objects. If you need to
keep unmodified data, make a copy that can be modified.
"""

from pandas import DataFrame


def fill_location(df: DataFrame):
    """Fill "location" column missing data."""
    # TODO determine what to fill with
    print("not implemented")


def fill_department(df: DataFrame):
    """Fill "department" column missing data."""
    # TODO determine what to fill with
    print("not implemented")


def fill_salary_range(df: DataFrame):
    """Fill "salary_range" column missing data."""
    # there are entries with "0-0", looks usable as a fill value
    df["salary_range"] = df["salary_range"].fillna("0-0")


def fill_company_profile(df: DataFrame):
    """Fill "company_profile" column missing data."""
    # TODO determine what to fill with
    print("not implemented")


def fill_description(df: DataFrame):
    """Fill "description" column missing data."""
    # TODO determine what to fill with
    print("not implemented")


def fill_requirements(df: DataFrame):
    """Fill "requirements" column missing data."""
    # TODO determine what to fill with
    print("not implemented")


def fill_benefits(df: DataFrame):
    """Fill "benefits" column missing data."""
    # TODO determine what to fill with
    print("not implemented")


def fill_employment_type(df: DataFrame):
    """Fill "employment_type" column missing data."""
    # TODO determine what to fill with
    # "Other" is an option
    print("not implemented")


def fill_required_experience(df: DataFrame):
    """Fill "required_experience" column missing data."""
    # TODO determine what to fill with
    # "Not Applicable" is an option
    print("not implemented")


def fill_required_education(df: DataFrame):
    """Fill "required_education" column missing data."""
    # TODO determine what to fill with
    # "Unspecified" is an option
    print("not implemented")


def fill_industry(df: DataFrame):
    """Fill "industry" column missing data."""
    # TODO determine what to fill with
    print("not implemented")


def fill_function(df: DataFrame):
    """Fill "function" column missing data."""
    # TODO determine what to fill with
    # "Other" is an option
    print("not implemented")


def fill_missing(df: DataFrame):
    """Fill all supported columns' missing data."""
    fill_location(df)
    fill_department(df)
    fill_salary_range(df)
    fill_company_profile(df)
    fill_description(df)
    fill_requirements(df)
    fill_benefits(df)
    fill_employment_type(df)
    fill_required_experience(df)
    fill_required_education(df)
    fill_industry(df)
    fill_function(df)
