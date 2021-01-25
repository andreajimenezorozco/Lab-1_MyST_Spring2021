
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
import numpy as np
import pandas as pd
import datetime


def dates_for_files(path):
    abspath = os.path.abspath(path)
    file_names = [f[:-4] for f in os.listdir(abspath) if os.path.isfile(os.path.join(abspath, f))]
    dates = [i.strftime('%Y-%m-%d') for i in sorted([pd.to_datetime(i[8:]).date() for i in file_names])]
    return dates


def cleaning_data(df):
    df['Ticker'] = [i.replace('*', '') for i in df['Ticker']]
    df['Ticker'] = df['Ticker'] + '.MX'
    df['Peso (%)'] = df['Peso (%)'] / 100

    # Tickers discrepancy
    df['Ticker'] = df['Ticker'].replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX')
    df['Ticker'] = df['Ticker'].replace('MEXCHEM.MX', 'ORBIA.MX')
    df['Ticker'] = df['Ticker'].replace('SITESB.1.MX', 'SITESB-1.MX')
    df['Ticker'] = df['Ticker'].replace('GFREGIOO.MX', 'RA.MX')
    df['Ticker'] = df['Ticker'].replace('NMKA.MX', 'NEMAKA.MX')

    # Remove tickers for CASH
    tickers_drop = ['KOFL.MX', 'BSMXB.MX', 'MXN.MX', 'USD.MX', '\xa0.MX', 'KOFUBL.MX']
    rows = list(df[list(df['Ticker'].isin(tickers_drop))].index)
    df.drop(rows, inplace=True)
    return df


# Tickers as index
def global_tickers(data):
    tickers_list = list(data['Ticker'])
    return np.unique(tickers_list).tolist()


def fix_weight(historical, dates):
    fix_weights = historical['Fecha'] == dates[0]
    fix_weights = historical[fix_weights]
    fix = fix_weights.drop(['Fecha', 'Precio'], axis=1)
    return  fix.rename(columns={'Peso (%)':'Peso (%) Fijo'})


def passive_investment(k, c, data):
    data['Capital'] = round(data['Peso (%) Fijo'] * k - data['Peso (%) Fijo'] * k * c,2)
    data['Titulos'] = round(data['Capital'] / data['Precio'],0)
    data['Postura'] = round(data['Titulos'] * data['Precio'],2)
    data['Comision'] = round(data['Postura'] * c,2)
    data['Rend.'] = data['Capital'].pct_change().fillna(0)
    data['Rend. Acum'] = np.cumsum(data['Rend.']).fillna(0)
    return data.drop(['Peso (%)'], axis=1)

