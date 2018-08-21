import pandas as pd

## dataFrame 에서 Filter 기능
def eq_mask(df, key, value):
    return df[df[key] == value]

def ge_mask(df, key, value):
    return df[df[key] >= value]

def gt_mask(df, key, value):
    return df[df[key] > value]

def le_mask(df, key, value):
    return df[df[key] <= value]

def lt_mask(df, key, value):
    return df[df[key] < value]

def ne_mask(df, key, value):
    return df[df[key] != value]

def gen_mask(df, f):
    return df[f(df)]

def apply_masks():

    pd.DataFrame.eq_mask = eq_mask
    pd.DataFrame.ge_mask = ge_mask
    pd.DataFrame.gt_mask = gt_mask
    pd.DataFrame.le_mask = le_mask
    pd.DataFrame.lt_mask = lt_mask
    pd.DataFrame.ne_mask = ne_mask
    pd.DataFrame.gen_mask = gen_mask

    return pd.DataFrame