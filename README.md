# Bitcoin EMA Crossover Trading Strategy
Bitcoin is perhaps the world’s most volatile asset class traded in large scale.  In addition, the inherent risks associated with Bitcoin because of cyberthreats and fraud can be enough to discourage most from trading it.  Despite these disadvantages, a simple yet effective speculative strategy that can be implemented to profit from Bitcoin is an exponential moving average (EMA) crossover.

An EMA crossover occurs when the “younger” exponential moving average crosses the “older” exponential moving average.  When this occurs, the investor should initiate a position (buying in an uptrend and selling in a downtrend).  This position should be closed when the crossover occurs again.  Since moving averages by nature are lagging indicators, getting the readings up to speed is important.  The EMA gives more weight to the most recent prices, thereby aligning the average closer to current prices.

## Using the Bitcoin EMA Crossover Trading Strategy
The first EMA crossover in this project is a 50-day and 200-day which is known as the golden cross and more commonly utilized in longer term trading.  The second EMA crossover is a 12-day and 26-day which is usually applied in medium term trading.  Both of these strategies will be visually represented with interactive charts that feature both zooming and panning capabilities for more precise analysis.

<p align="center">
<img src="images/Screen Shot 2019-11-09 at 5.45.15 PM.png" width="650" height="550">
<img src="images/Screen Shot 2019-11-09 at 5.47.25 PM.png" width="650" height="550">
</p>

First, download the data set bitstampUSD_1-min_data_2012-01-01_to_2019-08-12.csv from the Kaggle link provided below as well as the .ipynb and .py files from this repository.  If another data set is incorporated instead of the above, ensure minute to minute prices of OHLC (Open, High, Low, Close) are being used and timestamps are in Unix time to begin.

Once the necessary libraries are imported and the csv file is loaded as a pandas DataFrame, the main priority is completing the entire “Scrub” section which includes Drop Misprint, Date Format, and Data Preprocess.  After this has been entirely completed, feel free to advance to the section entitled “Model” if you would like to skip the visualization portion for the actual trading strategy component.

## Risk Disclosure
Gregory DeSantis is not a registered broker, analyst, investment advisor or anything of that sort.  This project is purely for guidance, informational and educational purposes.  All information contained herein should be independently verified and confirmed.  I do not accept any liability for any loss or damage whatsoever caused in reliance upon such information or services.  Please be aware of the risks involved with any trading done in any financial market.  Do not trade with money that you cannot afford to lose.  When in doubt, you should consult a qualified financial advisor before making any investment decisions.

## Disclaimer
Trading and investing in cryptocurrencies (also called digital or virtual currencies, crypto assets, altcoins and so on) involves substantial risk of loss and is not suitable for every investor.  The valuation of cryptocurrencies and futures may fluctuate, and, as a result, you may lose more than your original investment.  The highly leveraged nature of futures trading means that small market movements will have a great impact on your trading account and this can work against you, leading to large losses or can work for you, leading to large gains.

If the market moves against you, you may sustain a total loss greater than the amount you deposited into your account.  You are responsible for all the risks and financial resources you use and for the chosen trading system.  You should not engage in trading unless you fully understand the nature of the transactions you are entering into and the extent of your exposure to loss.  If you do not fully understand these risks you must seek independent advice from your financial advisor.

All trading strategies are used at your own risk.

Any content in this project should not be relied upon as advice or construed as providing recommendations of any kind.  It is your responsibility to confirm and decide which trades to make.  Trade only with risk capital; that is, trade with money that, if lost, will not adversely impact your lifestyle and your ability to meet your financial obligations.  Past results are no indication of future performance.  In no event should the content of this correspondence be construed as an express or implied promise or guarantee.

Gregory DeSantis is not responsible for any losses incurred as a result of using any of our trading strategies.  Loss-limiting strategies such as stop loss orders may not be effective because market conditions or technological issues may make it impossible to execute such orders.  Information provided in this correspondence is intended solely for informational purposes and is obtained from sources believed to be reliable. Information is in no way guaranteed.  No guarantee of any kind is implied or possible where projections of future conditions are attempted.

None of the content published in this project constitutes a recommendation that any particular cryptocurrency, portfolio of cryptocurrencies, transaction or investment strategy is suitable for any specific person.  None of the information providers or their affiliates will advise you personally concerning the nature, potential, value or suitability of any particular cryptocurrency, portfolio of cryptocurrencies, transaction, investment strategy or other matter.

The content provided in this project is solely for educational purposes.  The generic market recommendations provided are based solely on my personal judgment and should be considered as such.  You acknowledge that you enter into any transactions relying on your own judgment.  Any market recommendations provided are generic only and may or may not be consistent with the market positions or intentions of myself.  Any opinions, news, research, analyses, prices, or other information contained in this project are provided as general market commentary, and do not constitute an investment advice.

CFTC RULE 4.41 – HYPOTHETICAL OR SIMULATED PERFORMANCE RESULTS HAVE CERTAIN LIMITATIONS. UNLIKE AN ACTUAL PERFORMANCE RECORD, SIMULATED RESULTS DO NOT REPRESENT ACTUAL TRADING. ALSO, SINCE THE TRADES HAVE NOT BEEN EXECUTED, THE RESULTS MAY HAVE UNDER-OR-OVER COMPENSATED FOR THE IMPACT, IF ANY, OF CERTAIN MARKET FACTORS, SUCH AS LACK OF LIQUIDITY. SIMULATED TRADING PROGRAMS IN GENERAL ARE ALSO SUBJECT TO THE FACT THAT THEY ARE DESIGNED WITH THE BENEFIT OF HINDSIGHT. NO REPRESENTATION IS BEING MADE THAT ANY ACCOUNT WILL OR IS LIKELY TO ACHIEVE PROFIT OR LOSSES SIMILAR TO THOSE SHOWN.


## Links
* Bitcoin Historical Data: [Kaggle](https://www.kaggle.com/mczielinski/bitcoin-historical-data/data)
* Cryptocurrency Exchange: [Bitstamp](https://www.bitstamp.net/)
