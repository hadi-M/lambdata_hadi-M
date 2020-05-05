

# from my_mod_1 import enlarge
from my_mod_1 import beautiful_nan_table
# from lambdata_hadi_M.my_mod_1 import enlarge

from pdb import set_trace as st
from sklearn.datasets import load_boston

dataset = load_boston()
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
df['target'] = dataset.target

beautiful_nan_table(df)