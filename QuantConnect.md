# Quantconnect tutorial walkthrough

1. Set Up Cash

```
class BootCampTask(QCAlgorithm):

    def Initialize(self):
        
        self.AddEquity("SPY", Resolution.Daily)
        
        self.SetCash(1000000)
        
    def OnData(self, data):
        pass
```

Where put the amount into the `self.SetCash()` function. The above code sets up 1,000,000 cash amount initially.

2. Set up date range

```
class BootCampTask(QCAlgorithm):

    def Initialize(self):
        
        self.SetStartDate(2017, 1, 1)
        self.SetEndDate(2017, 10, 31)
        self.AddEquity("SPY", Resolution.Daily)
        
    def OnData(self, data):
        pass

```
The `self.SetStartDate()` and `self.SetEndDate()` are used to set date range. It follows the format of (yyyy, mm, dd), where mm and dd can either be 1 or 2 digits.
