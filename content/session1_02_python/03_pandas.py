#%%imports
from IPython.display import display
import logging
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

from cn5_pkg import cn5
hatches = cn5.cn5_style()


#%%definitions

#%%main
def main():

    #init
    nrows = 100
    df = pd.DataFrame(data=dict(
        col1=np.random.randint(0, nrows, size=nrows)/20,
        col2=np.linspace(0,1,nrows),
        col3=np.random.randn(nrows),
        label=np.random.choice(["a","b","c"], replace=True, size=nrows)
    ))
    display(df)

    #computation
    df["comp"] = df["col2"]**2 + df["col1"] + df["col3"]

    #exploration
    display(df.describe())

    #subsets
    display(df.query("(col1>3) & (label=='a')"))

    #plotting
    ##directly in pandas
    df.plot("col1", "comp", kind="scatter")
    ##seaborn corner plot
    g = sns.PairGrid(df, hue="label", diag_sharey=False, corner=True)
    g.map_lower(sns.kdeplot, levels=3, alpha=0.3)
    g.map_lower(sns.scatterplot, alpha=0.6, s=25)
    g.map_diag(sns.histplot, kde=True)
    g.add_legend()

    plt.show()  #avoid multiple `plt.show()`

if __name__ == "__main__":
    main()
