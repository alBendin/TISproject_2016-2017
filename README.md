#Technologies for Information Systems

Course project, year 2016/2017

Students: Francesco Giarola, Alberto Bendin

The goal of the project is to perform a technical analysis on financial market data and highlight some patterns in the behavior of some stocks.

The analysis was carried out considering the following:

##Indicators
* MACD
* CCI
* RSI

##Patterns
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

##Stocks
* PIA.MI
* GEO.MI
* SO.MI
* ERG.MI
* SPM.MI
* FCT.MI
* AST.MI
* CAI.MI
* CPR.MI

##Time window
From 1.11.2015 to 31.10.2016


##How to read the results
In the "results" folder there is a .xlxs file for every company.  
The granularity of the analysis is daily; thus every row in the resulting files represents a day.  
Each file contains five sheets. The first five columns are repeated in all the sheets (Date, OHLC).

**Sheets content**  
1. RAW data  
2. Pattern matching: every column represents a pattern; if a match is found we highlighted whether the prices of the shares were in a bullish (rising) or bearish (falling) trend respectively using the "UP" and "DOWN" keyword. If the cell is empty there is no match with the pattern for the corresponding day.  
