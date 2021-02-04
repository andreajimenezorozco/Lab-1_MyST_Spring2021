
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


def cleaning_data(df):
    df['Ticker'] = [i.replace('*', '') for i in df['Ticker']]
    df['Ticker'] = df['Ticker'] + '.MX'
    df['Peso (%)'] = df['Peso (%)'] / 100

    # Tickers
    df['Ticker'] = df['Ticker'].replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX')
    df['Ticker'] = df['Ticker'].replace('MEXCHEM.MX', 'ORBIA.MX')
    df['Ticker'] = df['Ticker'].replace('SITESB.1.MX', 'SITESB-1.MX')
    df['Ticker'] = df['Ticker'].replace('GFREGIOO.MX', 'RA.MX')
    df['Ticker'] = df['Ticker'].replace('NMKA.MX', 'NEMAKA.MX')

    # Remover tickers para CASH
    tickers_drop = ['KOFL.MX', 'BSMXB.MX', 'MXN.MX', 'USD.MX', '\xa0.MX', 'KOFUBL.MX']
    rows = list(df[list(df['Ticker'].isin(tickers_drop))].index)
    df.drop(rows, inplace=True)
    return df.set_index('Fecha')

