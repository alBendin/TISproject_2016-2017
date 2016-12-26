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

###Data retrieval and processing
We wrote a python script which uses the _TA-lib_ implementation for python to gather all the raw data about the above-mentioned list of patterns and oscillators.  
Then we exported the resulting output to CSV files (in _results/RAW/_) where every figure and indicator is assigned to an attribute.  
The rest of the elaboration has been carried out inside Microsoft Excel where we used some filters and formulas to achieve the expected results (the .xlxs files in _results/_ named "\*\*(\*).MI" (name of the stock)).  
Finally we created a Visual Basic macro to export the data to two summary files, one related to the patterns and the other about the indicators ("Stats Indicators.xlxs" and "Stats Patterns.xlxs" in _results/_).


##How to interpret the results
We considered that for analyses in this field it could be important to give the user the ability to dynamically choose the time scope of the analysis for instance to better highlight behavioral patterns over typical time periods like quarter of the year, semester, etc.  
For this reason we setup a way to browse these files consisting of two steps: the user first selects the sheet for the analysis he/she is interested in (PATTERN|MACD|CCI|RSI), here he/she chooses the time period which is the scope for the analysis, then the user switches to the result sheet for that specific analysis ("STATISTICS (PATTERN|MACD|CCI|RSI)").  
Of course if the user does not select any filter for the date the default analysis is done over the whole year.

In the "results" folder there is a .xlxs file for every company named "\*\*(\*).MI" (name of the stock).  

The granularity of the analysis is daily; thus every row in the resulting files represents a day.

Each file contains a total of nine sheets. Eight of these are because of the dual structure described above (4 couples of (setup-result) sheets for the 1(patterns) + 3(oscillators) analyses).  
The first five columns are the raw data (Date, OHLC) used to compute the different statistics and are repeated in the sheets number 1, 2, 4, 6, 8.

**Sheets content**  

1. **RAW:** data used as source for the analyses in the other sheets.
2. **PATTERNS:** every column represents a pattern; if a match has been found we highlighted whether the prices of the shares were in a bullish (rising) or bearish (falling) trend respectively using the _"UP"_ and _"DOWN"_ keywords. If the cell is empty there is no match with the pattern for the corresponding day. The user selects the date range in cell A1.
3. **STATISTICS PATTERNS:** results of the pattern analysis.
4. **MACD:** we tried two different setups for this indicator. 
  * **Classical:** the most commonly used values are 12, 26, and 9 days, that is, MACD(12,26,9), where the period settings of (12, 26, 9) represent 2 weeks, 1 month and one and a half week.
  * **Short term:** one of the popular short-term set-ups that is the (5,35,5).  
  
 Here we highlighted in YELLOW the days in which there is a change of sign (with respect to the previous day) for the MACD histogram value (difference between the slow and fast values), that is when the line crosses the zero line. These situations coincide with actual MACD crossover buy and sell signals. The user selects the date range in cell A2.  
5. **STATISTICS MACD:** results of the MACD analysis.
6. **CCI:** even for this oscillator we considered two different parameters corresponding respectively to time periods of 14 and 20 days.  
 Here we highlighted in GREEN the readings above 100 (overbought) and in RED the ones below -100 (oversold).  
7. **STATISTICS CCI:** results of the CCI analysis.
8. **RSI:** three configurations were tested; the usual 14 days time period and two other settings for 7 and 21 days.  
 Movements above 70 are considered overbought and again highlighted in GREEN, while an oversold condition would be a move under 30, highlighted in RED. We also marked in YELLOW the days whose RSI crossed the 50 line which is the RSI midpoint value. This because often traders treat RSI crossings above and below the 50 level as buying and selling signals respectively.
9. **STATISTICS RSI:** results of the RSI analysis.
