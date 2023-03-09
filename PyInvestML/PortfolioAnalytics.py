# To creat function allowing portfolio analytics

import pandas as pd

# to calculate drawdown for one portfolio

def drawdown(return_series: pd.Series):
    
    wealth_index = 10000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    
    return pd.DataFrame({"10K Growth": wealth_index,
                         "Previous Peak": previous_peaks,
                         "Drawdown": drawdowns})




# allow check of return frequency in a return dataset

def check_date_frequency(data, datename):
        '''this function aims to check how frequent a return data is, eg yearly, quarterly, monthly, weekly or daily
           the function takes the last return values from a time series dataset, and run a check on the frequency
           the assumption is that  
    INPUTS:
        data: pandas df - must ensure there is a date column with datetime64[ns] type data
        datename: the name of the column of date data
'''
    secondLast = data[dateName].tail(2)[:-1]
    last = data[dateName].tail(1)
    diff_days = (last.values - secondLast.values)
    fqcy = diff_days / np.timedelta64(1, 'D')
    fqcy = fqcy[0]
    if (fqcy > 200):
        return 'yearly'
    elif (fqcy > 80):
        return 'quarterly'
    elif(fqcy > 20):
        return 'monthly'
    elif(fqcy > 5):
        return 'weekly'
    else:
        return 'daily'
