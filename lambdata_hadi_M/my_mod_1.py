import pandas as pd
from tabulate import tabulate
from sklearn.model_selection import train_test_split


def beautiful_nan_table(dataframe):
    nans = dataframe.isna().sum().to_frame().rename(columns={0:"Number of Null Values"}).T
    print(tabulate(nans, nans.columns, tablefmt="fancy_grid"))


def train_valiadate_test_split(df, train_size, validate_size, test_size):
    test_fraction = (test_size) / (train_size + validate_size + test_size)
    X_train_validate, X_test = train_test_split(df, test_size=test_fraction)

    validate_fraction = (validate_size) / (train_size + validate_size)
    X_train, X_validate = train_test_split(X_train_validate, test_size=validate_fraction)

    return X_train, X_validate, X_test


def list_to_new_col(df, input_list, col_name):
    df = df.copy()
    df[col_name] = pd.Series(input_list)
    return df


if __name__ == "__main__":
    from pdb import set_trace as st
    from sklearn.datasets import load_boston
    
    dataset = load_boston()
    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    df['target'] = dataset.target

    beautiful_nan_table(df)

    train, validate, test = train_valiadate_test_split(df, 0.5, 0.3, 0.2)
    assert len(train) + len(validate) + len(test) == len(df)

    df = list_to_new_col(df, len(df)*[0], "ZEROS")