import numpy as np

def golden_cross_model(df):
    """Returns a tuple of date and price"""
    x = []
    for i in range(len(df)):
        if i == len(df) - 1:
            return x
        elif df.golden[i] == df.golden[i + 1]:
            continue
        else:
            x.append((df.date[i + 1], df.Close[i + 1]))
            
def PNL(crossover: float) -> str:
    """Returns Profit or Loss on crossover calculation"""
    if crossover > 0:
        return "Profit"
    else:
        return "Loss" 