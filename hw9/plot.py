import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    concordia = pd.read_csv("final_labeled_dataset_concordia.tsv", sep='\t')
    mcgill = pd.read_csv("final_labeled_dataset_mcgill.tsv", sep='\t')

    concordia = concordia.groupby(["coding"]).size().reset_index()
    concordia = concordia.rename(columns={0: 'count'}).compute()

    mcgill = mcgill.groupby(["coding"]).size().reset_index()
    mcgill = mcgill.rename(columns={0: 'count'}).compute()

    ax = concordia.plot()
    plot = mcgill.plot(ax=ax)

    plot.get_figure().savefig('plot.png')
