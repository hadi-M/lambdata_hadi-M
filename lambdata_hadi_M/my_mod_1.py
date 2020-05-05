import pandas as pd
from tabulate import tabulate


def beautiful_nan_table(dataframe):
    nans = dataframe.isna().sum().to_frame().rename(columns={0:"Number of Null Values"}).T
    print(tabulate(nans, nans.columns, tablefmt="fancy_grid"))


if __name__ == "__main__":
    from pdb import set_trace as st
    from sklearn.datasets import load_boston
    
    dataset = load_boston()
    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    df['target'] = dataset.target

    beautiful_nan_table(df)