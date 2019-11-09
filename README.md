# Bitcoin EMA Crossover Trading Strategy
Bitcoin is perhaps the world’s most volatile asset class traded in large scale.  In addition, the inherent risks associated with Bitcoin because of cyberthreats and fraud can be enough to discourage most from trading it.  Despite these disadvantages, a simple yet effective speculative strategy that can be implemented to profit from Bitcoin is an exponential moving average crossover (EMA).

An EMA crossover occurs when the “younger” exponential moving average crosses the “older” exponential moving average.  When this occurs, the investor should initiate a position (buying in an uptrend and selling in a downtrend).  This position should be closed when the crossover occurs again.  Since moving averages by nature are lagging indicators, getting the readings up to speed is important.  The EMA gives more weight to the most recent prices, thereby aligning the average closer to current prices.

## Using the Bitcoin EMA Crossover Trading Strategy
The first EMA crossover in this project is a 50-day and 200-day which is known as the golden cross and more commonly utilized in longer term trading.  The second EMA crossover is a 12-day and 26-day which is usually applied in medium term trading.  Both of these strategies will be visually represented with interactive charts that feature both zooming and panning capabilities for more precise analysis.

<img src="images/Screen Shot 2019-11-09 at 5.45.15 PM.png" width="650" height="550" align="center">
<img src="images/Screen Shot 2019-11-09 at 5.47.25 PM.png" width="650" height="550" align="center">

First, download the bitstampUSD_1-min_data_2012-01-01_to_2019-08-12.csv from the Kaggle link provided below as well as the .ipynb and .py files from this repository.

Once the necessary libraries are imported and the csv file is loaded as a pandas DataFrame, the main priority is completing the entire “Scrub” section which includes Drop Misprint, Date Format, and Data Preprocess.  After this has been entirely completed, feel free to advance to the section entitled “Model” if you would like to skip the visualization portion for the actual trading strategy component.

## Links
* Bitcoin Historical Data: [Kaggle](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data)
* Cryptocurrency Exchange: [Bitstamp](https://www.bitstamp.net/)
