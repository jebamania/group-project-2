"""Helper module to build encoders for the formatted dataset.

Due to encoders working across rows, They should be built on training data
first to not leak testing data.
"""

from pandas import concat, DataFrame
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder


class MultiColumnEncoder:
    """A class to configure a multi-column encoder."""

    def __init__(self, column: str, encoder: OneHotEncoder):
        self._column = column
        """The column the encoder targets."""
        self._encoder = encoder
        """A OneHotEncoder to use for fit & transform."""

    def fit(self, X: DataFrame):
        """Fit the encoder to a data frame containing the target column."""
        self._encoder.fit(X[self._column])
        return self

    def transform(self, X: DataFrame):
        """Transform a data frame's column and return its multi-column encoding."""
        return DataFrame(
            self._encoder.transform(X[self._column]),
            columns=self._encoder.get_feature_names_out(),
        )


class SingleColumnEncoder:
    """A class to configure a single column encoder."""

    def __init__(self, column: str, encoder: OrdinalEncoder):
        self.column = column
        """The column the encoder targets."""
        self._encoder = encoder
        """An OrdinalEncoder to use for fit & transform."""

    def fit(self, X: DataFrame):
        """Fit the encoder to a data frame containing the target column."""
        self._encoder.fit(X[self.column])
        return self

    def transform(self, X: DataFrame):
        """Transform a data frame's column and return an encoded column."""
        return self._encoder.transform(X[self.column])


def build_country_encoder(X: DataFrame):
    """Build and fit an encoder for the "country" column."""
    return MultiColumnEncoder(
        "country",
        OneHotEncoder(
            max_categories=4, handle_unknown="infrequent_if_exist", sparse_output=False
        ),
    ).fit(X)


def build_state_encoder(X: DataFrame):
    """Build and fit an encoder for the "state" column."""
    return MultiColumnEncoder(
        "state",
        OneHotEncoder(
            max_categories=6, handle_unknown="infrequent_if_exist", sparse_output=False
        ),
    ).fit(X)


def build_city_encoder(X: DataFrame):
    """Build and fit an encoder for the "city" column."""
    return MultiColumnEncoder(
        "city",
        OneHotEncoder(
            max_categories=10, handle_unknown="infrequent_if_exist", sparse_output=False
        ),
    ).fit(X)


def build_department_encoder(X: DataFrame):
    """Build and fit an encoder for the "department" column."""
    return MultiColumnEncoder(
        "department",
        OneHotEncoder(
            max_categories=10, handle_unknown="infrequent_if_exist", sparse_output=False
        ),
    ).fit(X)


def build_employment_type_encoder(X: DataFrame):
    """Build and fit an encoder for the "employment_type" column."""
    return MultiColumnEncoder(
        "employment_type",
        OneHotEncoder(
            categories=[["Full-time", "Part-time", "Contract", "Temporary", "Other"]],
            handle_unknown="infrequent_if_exist",
            sparse_output=False,
        ),
    ).fit(X)


def build_required_experience_encoder(X: DataFrame):
    """Build and fit an encoder for the "required_experience" column."""
    return MultiColumnEncoder(
        "required_experience",
        OneHotEncoder(
            categories=[
                [
                    "Internship",
                    "Entry level",
                    "Mid-Senior level",
                    "Associate",
                    "Director",
                    "Executive",
                    "Not Applicable",
                ]
            ],
            handle_unknown="infrequent_if_exist",
            sparse_output=False,
        ),
    ).fit(X)


def build_required_education_encoder(X: DataFrame):
    """Build and fit an encoder for the "required_education" column."""
    return MultiColumnEncoder(
        "required_education",
        OneHotEncoder(
            categories=[
                [
                    "Some High School Coursework",
                    "High School or equivalent",
                    "Some College Coursework Completed",
                    "Associate Degree",
                    "Bachelor's Degree",
                    "Master's Degree",
                    "Doctorate",
                    "Professional",
                    "Certification",
                    "Vocational",
                    "Vocational - HS Diploma",
                    "Vocational - Degree",
                    "Unspecified",
                ]
            ],
            handle_unknown="infrequent_if_exist",
            sparse_output=False,
        ),
    ).fit(X)


def build_industry_encoder(X: DataFrame):
    """Build and fit an encoder for the "industry" column."""
    return MultiColumnEncoder(
        "industry",
        OneHotEncoder(
            max_categories=10, handle_unknown="infrequent_if_exist", sparse_output=False
        ),
    ).fit(X)


def build_function_encoder(X: DataFrame):
    """Build and fit an encoder for the "function" column."""
    return MultiColumnEncoder(
        "function",
        OneHotEncoder(
            max_categories=10, handle_unknown="infrequent_if_exist", sparse_output=False
        ),
    ).fit(X)


def build_encoders(X: DataFrame):
    """Build and fit all supported encoders."""
    return [
        enc_func(X)
        for enc_func in [
            build_country_encoder,
            build_state_encoder,
            build_city_encoder,
            build_department_encoder,
            build_employment_type_encoder,
            build_required_experience_encoder,
            build_required_education_encoder,
            build_industry_encoder,
            build_function_encoder,
        ]
    ]


def encode(X: DataFrame, encoders: list[MultiColumnEncoder | SingleColumnEncoder]):
    """Apply column encoders, returning a modified data frame.

    The resulting data frame should only contain numeric data. Any text
    data not configured to encode will effectively be dropped.
    """
    single_col_encoders: list[SingleColumnEncoder] = []
    dfs = [X.select_dtypes(include="number").reset_index(drop=True)]

    for enc in encoders:
        if isinstance(enc, SingleColumnEncoder):
            single_col_encoders.append(enc)
        else:
            dfs.append(enc.transform(X))

    X_enc = concat(dfs, axis=1)

    for enc in single_col_encoders:
        X_enc[enc.column] = enc.transform(X)

    return X_enc
