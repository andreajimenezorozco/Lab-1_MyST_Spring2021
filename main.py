
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

# CSV

# IPC TICKERS FROM YAHOO FINANCE

tickers = ["KIMBERA.MX", "BBAJIOO.MX", "BIMBOA.MX", "ALSEA.MX", "AMXL.MX", "AC.MX",
         "MEGACPO.MX", "GCARSOA1.MX", "FEMSAUBD.MX", "GAPB.MX", "GFNORTEO.MX",
         "GRUMAB.MX", "TLEVISACPO.MX", "CUERVO.MX", "GENTERA.MX", "ASURB.MX", "PINFRA.MX",
          "OMAB.MX", "IENOVA.MX", "LABB.MX", "GMEXICOB.MX", "BOLSAA.MX", "CEMEXCPO.MX", 'LIVEPOLC-1.MX',
         "KOFUBL.MX", "PE&OLES.MX", "SITESB-1.MX", "Q.MX", "ELEKTRA.MX",
         "ORBIA.MX", 'NEMAKA.MX', "ALFAA.MX", "WALMEX.MX", "VESTA.MX", "GFINBURO.MX"]

start, end = '2018-01-01', '2020-12-01'
daily_closes = get_closes(tickers, start, end)

# PASSIVE INVESTMENT

# ACTIVE INVESTMENT

# METRICS
