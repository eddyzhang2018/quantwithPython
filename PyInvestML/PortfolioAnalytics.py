# To creat function allowing portfolio analytics

import pandas as pd

def drawdown(return_series: pd.Series):
    
    wealth_index = 10000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    
    return pd.DataFrame({"10K Growth": wealth_index,
                         "Previous Peak": previous_peaks,
                         "Drawdown": drawdowns})
