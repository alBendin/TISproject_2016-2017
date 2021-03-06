from pandas_datareader import data as web
import talib
import numpy
import pandas
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def do_it(index):
	#***********TIME RANGE***********
	end = datetime(2016, 10, 31)
	start = datetime(2015, 8, 1)


	#***********DATA ACQUISITION*************
	f = web.DataReader(index, 'yahoo', start, end)


	#***********OHLC SETUP************
	f = pandas.DataFrame(f, columns=["Open","High","Low","Close"])
	f1 = pandas.DataFrame(f, columns=["Open","High","Low","Close"])
	f2 = pandas.DataFrame(f, columns=["Open","High","Low","Close"])

	open = numpy.array(f['Open'], dtype=float)
	high = numpy.array(f['High'], dtype=float)
	low = numpy.array(f['Low'], dtype=float)
	close = numpy.array(f['Close'], dtype=float)




	#**********OSCILLATORI**********
	#macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
	f['macd_cla'], f['macdsignal_cla'], f['macdhist_cla'] = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
	f['macd_sh'], f['macdsignal_sh'], f['macdhist_sh'] = talib.MACD(close, fastperiod=5, slowperiod=35, signalperiod=5)

	#real = CCI(high, low, close, timeperiod=14)
	f['cci_14'] = talib.CCI(high, low, close, timeperiod=14)
	f['cci_20'] = talib.CCI(high, low, close, timeperiod=20)

	#real = RSI(close, timeperiod=14)
	f['rsi_7'] = talib.RSI(close, timeperiod=7)
	f['rsi_14'] = talib.RSI(close, timeperiod=14)
	f['rsi_21'] = talib.RSI(close, timeperiod=21)





	#*********FIGURES**********	
	#"Upside/Downside Gap Three Method"
	integer1 = talib.CDLXSIDEGAP3METHODS(open, high, low, close)
	f['CDLXSIDEGAP3METHODS'] = integer1
	
	#"Evening Star"
	integer2 = talib.CDLEVENINGSTAR(open, high, low, close, penetration=0)
	f['CDLEVENINGSTAR'] = integer2

	#"Morning Star"
	integer3 = talib.CDLMORNINGSTAR(open, high, low, close, penetration=0)
	f['CDLMORNINGSTAR'] = integer3

	#"Engulfing Pattern"
	integer4 = talib.CDLENGULFING(open, high, low, close)
	f['CDLENGULFING'] = integer4
	
	#"Dark Cloud Cover"
	integer5 = talib.CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
	f['CDLDARKCLOUDCOVER'] = integer5

	#"Doji"
	integer6 = talib.CDLDOJI(open, high, low, close)
	f['CDLDOJI'] = integer6

	#"Hammer"
	integer7 = talib.CDLHAMMER(open, high, low, close)
	f['CDLHAMMER'] = integer7

	#"Hanging Man"
	integer8 = talib.CDLHANGINGMAN(open, high, low, close)
	f['CDLHANGINGMAN'] = integer8

	#"Harami"
	integer9 = talib.CDLHARAMI(open, high, low, close)
	f['CDLHARAMI'] = integer9

	#"Piercing Line"
	integer10 = talib.CDLPIERCING(open, high, low, close)
	f['CDLPIERCING'] = integer10

	#"Shooting Star"
	integer11 = talib.CDLSHOOTINGSTAR(open, high, low, close)
	f['CDLSHOOTINGSTAR'] = integer11

	f.to_csv("results/" + index + ".csv")
	

	
for i in ['PIA.MI','GEO.MI','SO.MI','ERG.MI','SPM.MI','FCT.MI','AST.MI','CAI.MI','CPR.MI']:
	do_it(i)
