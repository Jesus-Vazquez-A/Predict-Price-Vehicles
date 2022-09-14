# -*- coding: utf-8 -*-
def histogram(feature,title):
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    

    sns.set_style("whitegrid")

    fig,ax=plt.subplots(1,1,figsize=(20,8))

    ax.set_title(title)
    ax.hist(feature,ec="k",color="#FADA5E",lw=3)


    ax.axvline(feature.mean(),
           color="red",
           linestyle="--",
           lw=3,label="Mean")


    ax.axvline(feature.median(),
           color="blue",
           linestyle="--",
           lw=3,label="Median")

    ax.legend()

    plt.show()