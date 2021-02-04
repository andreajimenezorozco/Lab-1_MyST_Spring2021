
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab. 1                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: Andrea Jiménez IF706970 Github: andreajimenezorozco                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/andreajimenezorozco/Lab-1_MyST_Spring2021                                                                  -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import glob
import pandas as pd
import os


def multiple_csv(path):
    all_files = glob.glob(os.path.join(path, "*.csv"))
    file_list = []
    for file in all_files:
        df = pd.read_csv(file, usecols=[0, 3])
        df['Fecha'] = file
        df['Fecha'] = [i.replace('files\\NAFTRAC_','') for i in df['Fecha']]
        df['Fecha'] = [i.replace('.csv','') for i in df['Fecha']]
        file_list.append(df)
    all_df = pd.concat(file_list, ignore_index=True)
    return all_df
