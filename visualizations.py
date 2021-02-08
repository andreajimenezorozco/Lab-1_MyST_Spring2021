
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A SHORT DESCRIPTION OF THE PROJECT                                                         -- #
# -- script: visualizations.py : python script with data visualization functions                         -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: YOUR REPOSITORY URL                                                                     -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import matplotlib.pyplot as plt


def basic_plot(df, title, column, title_x, title_y):
    plt.figure(figsize=(15,4))
    ax = plt.axes()
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["top"].set_visible(False)
    plt.plot(df[column], lw=3,color="green", label=column)
    plt.legend(loc='best', fontsize=8)
    plt.title(title, fontsize=15)
    plt.xlabel(title_x, fontsize=8)
    plt.ylabel(title_y, fontsize=8)
    plt.show()
    return plt.show()
