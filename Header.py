from pandas_datareader import data as web
import talib
import numpy
import pandas
import csv
import matplotlib.pyplot as plt
from datetime import datetime

#***********TIME RANGE***********
# end = datetime(2016, 10, 31)
# start = datetime(2015, 11, 1)
end = datetime(2016, 10, 31)
start = datetime(2015, 8, 1)


#***********DATA ACQUISITION*************
f = web.DataReader("PIA.MI", 'yahoo', start, end)
#f = web.DataReader("GEO.MI", 'yahoo', start, end)
#f = web.DataReader("SO.MI", 'yahoo', start, end)

#***********OPTIONAL***********
#f = web.DataReader("ERG.MI", 'yahoo', start, end)
#f = web.DataReader("SPM.MI", 'yahoo', start, end)
#f = web.DataReader("FCT.MI", 'yahoo', start, end)
#f = web.DataReader("AST.MI", 'yahoo', start, end)
#f = web.DataReader("CAI.MI", 'yahoo', start, end)
#f = web.DataReader("CPR.MI", 'yahoo', start, end)




#***********OHLC SETUP************
f = pandas.DataFrame(f, columns=["Open","High","Low","Close"])

open = numpy.array(f['Open'], dtype=float)
high = numpy.array(f['High'], dtype=float)
low = numpy.array(f['Low'], dtype=float)
close = numpy.array(f['Close'], dtype=float)




#**********OSCILLATORI**********
# real = SMA(close, timeperiod=30)
f['SMA_20'] = talib.SMA(close, 20)
f['SMA_50'] = talib.SMA(close, 50) 

#macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
f['macd'], f['macdsignal'], f['macdhist'] = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

#real = CCI(high, low, close, timeperiod=14)
f['cci'] = talib.CCI(high, low, close, timeperiod=14)

#real = RSI(close, timeperiod=14)
f['rsi'] = talib.RSI(close, timeperiod=14)




#********PLOT*********
f.plot(y= ['Close','SMA_20','SMA_50'], title='AAPL Close & Moving Averages')
f.plot(y= ['macdsignal','macd','macdhist'], title='MACD')
f.plot(y= ['cci'], title='CCI')
f.plot(y= ['rsi'], title='RSI')
plt.show()


for macd_item in f['macd']:
	print(macd_item)
	

#*********FIGURES**********	
#"Upside/Downside Gap Three Method"
integer1 = talib.CDLXSIDEGAP3METHODS(open, high, low, close)

#"Evening Star"
integer2 = talib.CDLEVENINGSTAR(open, high, low, close, penetration=0)

#"Morning Star"
integer3 = talib.CDLMORNINGSTAR(open, high, low, close, penetration=0)

#"Engulfing Pattern"
integer4 = talib.CDLENGULFING(open, high, low, close)
print()
print("Upside/Downside Gap Three Method")
print(integer1)
f['CDLXSIDEGAP3METHODS'] = integer1

print()
print("Evening Star")
print(integer2)
f['CDLEVENINGSTAR'] = integer2

print()
print("Morning Star")
print(integer3)
f['CDLMORNINGSTAR'] = integer3

print()
print("Engulfing Pattern")
print(integer4)
f['CDLENGULFING'] = integer4


#************OPTIONALS*************
#"Dark Cloud Cover"
integer5 = talib.CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
print()
print("Dark Cloud Cover")
print(integer5)

#"Doji"
integer6 = talib.CDLDOJI(open, high, low, close)
print()
print("Doji")
print(integer6)

#"Hammer"
integer7 = talib.CDLHAMMER(open, high, low, close)
print()
print("Hammer")
print(integer7)

#"Hanging Man"
integer8 = talib.CDLHANGINGMAN(open, high, low, close)
print()
print("Hanging Man")
print(integer8)

#"Harami"
integer9 = talib.CDLHARAMI(open, high, low, close)
print()
print("Harami")
print(integer9)

#"Piercing Line"
integer10 = talib.CDLPIERCING(open, high, low, close)
print()
print("Piercing Line")
print(integer10)

#"Shooting Star"
integer11 = talib.CDLSHOOTINGSTAR(open, high, low, close)
print()
print("Shooting Star")
print(integer11)

f.to_csv("foo.csv")