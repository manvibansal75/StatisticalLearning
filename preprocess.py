#%% data import
import pandas as pd 
import numpy as np
import json
from glob import glob
from datetime import datetime

all_files = glob("data/*.csv")
dataset = []
for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    dataset.append(df)
df = pd.concat(dataset, axis=0, ignore_index=True)

#%% formatting
df['master_category'] = [json.loads(c)['slug'].split('/')[0] for c in df['category'].to_list()]
df['category'] = [json.loads(c)['slug'] for c in df['category'].to_list()]
df['created_at'] = [datetime.fromtimestamp(d) for d in df['created_at'].to_list()]
df['deadline'] = [datetime.fromtimestamp(d) for d in df['deadline'].to_list()]
df['launched_at'] = [datetime.fromtimestamp(d) for d in df['launched_at'].to_list()]
df['currency_trailing_code'][df['currency_trailing_code']] = 1
df['spotlight'][df['spotlight']] = 1
df['staff_pick'][df['staff_pick']] = 1
df['successful'] = 0
df['successful'][df['state']=='successful'] = 1

df.to_pickle('data.pkl')

# %%
