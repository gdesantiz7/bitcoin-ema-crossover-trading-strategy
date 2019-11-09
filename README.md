# Bitcoin EMA Crossover Trading Strategy
Bitcoin is perhaps the world’s most volatile asset class traded in large scale.  In addition, the inherent risks associated with Bitcoin because of cyberthreats and fraud can be enough to discourage most from trading it.  Despite these disadvantages, a simple yet effective speculative strategy that can be implemented to profit from Bitcoin is an exponential moving average crossover (EMA).

An EMA crossover occurs when the “younger” exponential moving average crosses the “older” exponential moving average.  When this occurs, the investor should initiate a position (buying in an uptrend and selling in a downtrend).  This position should be closed when the crossover occurs again.  Since moving averages by nature are lagging indicators, getting the readings up to speed is important.  The EMA gives more weight to the most recent prices, thereby aligning the average closer to current prices.

## Using the Bitcoin EMA Crossover Trading Strategy
First, download the bitstampUSD_1-min_data_2012-01-01_to_2019-08-12.csv from the Kaggle link provided below.

Once the csv file is loaded as a pandas DataFrame,


The first EMA crossover in this project is a 50-day and 200-day which is known as the golden cross and more commonly utilized in longer term trading.  The second EMA crossover is a 12-day and 26-day which is usually applied in medium term trading.

Both of these strategies will be visually represented with interactive charts that feature both zooming and panning capabilities for more precise analysis.

## Links
* Bitcoin Historical Data: [Kaggle](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data)
* Cryptocurrency Exchange: [Bitstamp](https://www.bitstamp.net/)
