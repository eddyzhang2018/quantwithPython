# Quantconnect tutorial walkthrough

**1. Set Up Cash**

```
class BootCampTask(QCAlgorithm):

    def Initialize(self):
        
        self.AddEquity("SPY", Resolution.Daily)
        
        self.SetCash(1000000)
        
    def OnData(self, data):
        pass
```

Where put the amount into the `self.SetCash()` function. The above code sets up 1,000,000 cash amount initially.

**2. Set up date range**

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

**3. Manually selecting data**

```
class BootCampTask(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2017, 6, 1)
        self.SetEndDate(2017, 6, 15)
        
        # Manually Select Data
        self.spy = self.AddEquity("SPY", Resolution.Minute)
        
        self.iwm = self.AddEquity("IWM", Resolution.Minute)
        
    def OnData(self, data):
        pass

```

`self.AddEquity()` is to select equity where one of the inputs "Resolution.xxx" control the resolution of the data. It can be Tick, Second, Minute, Hour and Daily.

**4. Set Data Normalization Mode**

Historical data are adjusted by default on QuantConnect. However, it can set it back to Raw using `Security.SetDataNormalizationMode()` with inputs are: DataNormalizationMode.Raw, DataNormalizationMode.Adjusted, DataNormalizationMode.SplitAdjusted or DataNormalizationMode.TotalReturn.

```
class BootCampTask(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2017, 6, 1)
        self.SetEndDate(2017, 6, 15)
        
        self.spy = self.AddEquity("SPY", Resolution.Daily)
        self.spy.SetDataNormalizationMode(DataNormalizationMode.Raw)
        
        self.iwm = self.AddEquity("IWM", Resolution.Daily)
        self.iwm.SetLeverage(1)
        
    def OnData(self, data):
        pass

```
