
import datetime
import pandas_ta as ta
import pandas as pd

from backtesting import Backtest
from backtesting import Strategy
from backtesting.lib import crossover
from backtesting.test import GOOG

#create class for testing strategy
class Rsi0scillator(Strategy):
    
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    
    def init(self):
        self.rsi = self.I(ta.rsi, pd.Series(self.data.Close), self.rsi_window)
        
    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
            
        elif crossover(self.lower_bound, self.rsi):
            self.buy()
 
#start backtesting
    bt = Backtest(GOOG, Rsi0scillator, cash = 10_000)
    stats = bt.run()
    print(stats)
    
#optimize backtesting

stats = bt.optimize(
            upper_bound = range(55, 85, 5),
            lower_bound = range(10, 45, 5),
            rsi_window = range(10,30,2),
            maximize = 'Sharpe Ratio', #optimize Sharpe Ratio
            constraint = lambda param: param.upper_bound > param.lower_bound)

print(stats)
