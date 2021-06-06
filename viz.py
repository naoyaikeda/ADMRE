# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
output_fit_0 = pd.read_table('output_fit_0', sep = ' ', header=None)
output_fit_1 = pd.read_table('output_fit_1', sep = ' ', header=None)
output_mut_0 = pd.read_table('output_mut_0', sep = ' ', header=None)
output_mut_1 = pd.read_table('output_mut_1', sep = ' ', header=None)

# %%
output_mut_0.describe()

# %%
output_mut_1.describe()

# %%
sns.heatmap(output_mut_0)

# %%
sns.heatmap(output_mut_1)


# %%
output_fit_0.shape

# %%
output_fit_1.shape

# %%
output_mut_0.shape

# %%
output_mut_1.shape

# %%
