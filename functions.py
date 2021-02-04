
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab. 1                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: Andrea Jiménez IF706970 Github: andreajimenezorozco                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/andreajimenezorozco/Lab-1_MyST_Spring2021                                                                      -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""
import os
import pandas as pd


def dates_for_files(path):
    abspath = os.path.abspath(path)
    file_names = [f[:-4] for f in os.listdir(abspath) if os.path.isfile(os.path.join(abspath, f))]
    dates = [i.strftime('%Y-%m-%d') for i in sorted([pd.to_datetime(i[8:]).date() for i in file_names])]
    return dates

