
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab. 1                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: Andrea Jiménez IF706970 Github: andreajimenezorozco                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/andreajimenezorozco/Lab-1_MyST_Spring2021                                                                    -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

from data import *
from functions import *

dates = dates_for_files(path=str)
data_from_files = multiple_csv(path=str)
historical = cleaning_data(data_from_files)
data = global_df(prices=float, dates=str, historical,fix)

passive_df = passive_investment(k=int, c=float, data)






