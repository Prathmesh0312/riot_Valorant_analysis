import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# display settings
pd.set_option("display.max_columns", None)
sns.set(style="whitegrid")

# load data
df = pd.read_csv("valorant_games_project.csv")

#df.head()

#basic understanding
df.info()
df.describe()
df.isnull().sum()

df.shape

df["date"] = pd.to_datetime(df["date"])
