
"""
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Lab. 1                                                         -- #
# -- script: main.py : python script with the main functionality                                         -- #
# -- author: Andrea Jiménez IF706970 Github: andreajimenezorozco                                                                       -- #
# -- license: GPL-3.0 License                                                                            -- #
# -- repository: https://github.com/andreajimenezorozco/Lab-1_MyST_Spring2021                                                                  -- #
# -- --------------------------------------------------------------------------------------------------- -- #
"""

import pandas_datareader.data as web
import glob
from functions import *


def get_closes(tickers, start_date=None, end_date=None, freq=None):
    closes = pd.DataFrame(columns=tickers, index=web.YahooDailyReader(tickers[0], start=start_date, end=end_date
                                                                      , interval=freq).read().index)
    for ticker in tickers:
        df = web.YahooDailyReader(symbols=ticker, start=start_date, end=end_date, interval=freq).read()
        closes[ticker] = df['Adj Close']
    closes.index_name = 'Date'
    closes = closes.sort_index()
    return closes


# Read multiple CSV files and creat one single DataFrame
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


# Global DataFrame with dates, prices, weights (fix and float) and tickers
def global_df(prices, dates, historical, fix):
    # Fix dates from historical
    fix_dates = sorted(list(set(prices.index.astype(str).tolist()) & set(dates)))

    # Corresponding price to fix dates
    fix_prices = prices.iloc[[int(np.where(prices.index.astype(str) == i)[0]) for i in fix_dates]]
    fix_prices = fix_prices.reindex(sorted(fix_prices.columns), axis=1)

    # Match fix dates to prices
    match = 0
    historical['Precio'] = [fix_prices.iloc[match, fix_prices.columns.to_list().index(i)] for i in historical['Ticker']]

    # Merge fix weights column
    fix = fix_weight(historical)
    join = pd.merge(historical, fix, on='Ticker', how='outer')
    join['Peso (%) Fijo'] = join['Peso (%) Fijo'].fillna(0)
    df = join.set_index('Fecha')
    df_final = df.sort_index(ascending=True)

    return df_final[['Ticker', 'Precio', 'Peso (%)', 'Peso (%) Fijo']]

