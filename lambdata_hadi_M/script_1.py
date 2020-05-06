
import pandas as pd
# from my_mod_1 import enlarge
# from my_mod_1 import beautiful_nan_table, list_to_new_col
# from lambdata_hadi_M.my_mod_1 import enlarge

from pudb import set_trace as st
from sklearn.datasets import load_boston

dataset = load_boston()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target
st()
# beautiful_nan_table(df)

# df = list_to_new_col(df, len(df)*[0], "ZEROS")
print(df)