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
