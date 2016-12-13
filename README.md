#Technologies for Information Systems

Course project, year 2016/2017  
Politecnico di Milano

Students: Francesco Giarola, Alberto Bendin

The goal of the project is to perform a technical analysis on financial market data and highlight some patterns in the behavior of some stocks.

The analysis was carried out considering the following:

###Indicators
* MACD
* CCI
* RSI

###Patterns
* Upside/Downside Gap Three Method
* Evening/Morning Star
* Engulfing Pattern
* Dark Cloud Cover
* Doji
* Hammer
* Hanging Man
* Harami
* Piercing Line
* Shooting Star

###Stocks
* PIA.MI
* GEO.MI
* SO.MI
* ERG.MI
* SPM.MI
* FCT.MI
* AST.MI
* CAI.MI
* CPR.MI

###Time window
From 1.11.2015 to 31.10.2016


##How to interpret the results
In the "results" folder there is a .xlxs file for every company.  
The granularity of the analysis is daily; thus every row in the resulting files represents a day.  
Each file contains five sheets. The first five columns are repeated in all the sheets (Date, OHLC).

**Sheets content**  

1. RAW data.  
2. **Pattern matching:** every column represents a pattern; if a match has been found we highlighted whether the prices of the shares were in a bullish (rising) or bearish (falling) trend respectively using the _"UP"_ and _"DOWN"_ keywords. If the cell is empty there is no match with the pattern for the corresponding day.  
3. **MACD:** we tried two different setups for this indicator. 
  * **Classical:** the most commonly used values are 12, 26, and 9 days, that is, MACD(12,26,9), where the period settings of (12, 26, 9) represent 2 weeks, 1 month and one and a half week.
  * **Short term:** one of the popular short-term set-ups that is the (5,35,5).  
  
 Here we highlighted in YELLOW the days in which there is a change of sign (with respect to the previous day) for the MACD histogram value (difference between the slow and fast values), that is when the line crosses the zero line. These situations coincide with actual MACD crossover buy and sell signals.  
4. **CCI:** even for this oscillator we considered two different parameters corresponding respectively to time periods of 14 and 20 days.  
 Here we highlighted in GREEN the readings above 100 (overbought) and in RED the ones below -100 (oversold).  
5. **RSI:** three configurations were tested; the usual 14 days time period and two other settings for 7 and 21 days.  
 Movements above 70 are considered overbought and again highlighted in GREEN, while an oversold condition would be a move under 30, highlighted in RED. We also marked in YELLOW the days whose RSI crossed the 50 line which is the RSI midpoint value. This because often traders treat RSI crossings above and below the 50 level as buying and selling signals respectively.
