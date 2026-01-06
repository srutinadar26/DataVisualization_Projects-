import pandas as pd
import matplotlib.pyplot as plt

# Load the Netflix dataset
df = pd.read_csv(r"C:\Users\sruti\OneDrive\Pictures\Desktop\Data Visualization mini projects\Diwali Sales\Diwali Sales Data.csv",
    encoding="unicode_escape")
df.info()
df.head()
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
pd.isnull(df).sum()
df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype('int')
df['Amount'].dtypes
print(df)