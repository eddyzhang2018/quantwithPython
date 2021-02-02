# Save all codes relevant tot Quantconnect tutorial walkthrough

# 1. Set Up Cash

class BootCampTask(QCAlgorithm):

    def Initialize(self):
        
        self.AddEquity("SPY", Resolution.Daily)
        
        self.SetCash(x)
        
    def OnData(self, data):
        pass
