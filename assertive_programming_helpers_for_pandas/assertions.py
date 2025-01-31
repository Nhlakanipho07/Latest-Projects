def assert_df_not_empty(df):
    assert not df.empty, "The DataFrame should not be empty."


def assert_df_dimensions_equal(df, height, width):
    assert_df_not_empty(df)
    assert df.shape == (
        height,
        width,
    ), "DataFrame dimensions do not match expected dimensions."


def assert_df_columns_equal(df, column_names):
    assert_df_not_empty(df)
    assert sorted(df.columns) == sorted(
        column_names
    ), "DataFrame column names do not match expected column names."


def assert_no_duplicate_rows(df):
    assert_df_not_empty(df)
    assert (
        not df.duplicated().any()
    ), "The DataFrame should not have any duplicate rows."


def assert_no_null_values(df):
    assert_df_not_empty(df)
    assert (
        not df.isnull().values.any()
    ), "The DataFrame should not have any null values."


def assert_all_values_positive(df):
    assert_df_not_empty(df)
    assert (df >= 0).all().all(), "The DataFrame should not have any negative values."
