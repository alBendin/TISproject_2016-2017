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
f1 = pandas.DataFrame(f, columns=["Open","High","Low","Close"])
f2 = pandas.DataFrame(f, columns=["Open","High","Low","Close"])

open = numpy.array(f['Open'], dtype=float)
high = numpy.array(f['High'], dtype=float)
low = numpy.array(f['Low'], dtype=float)
close = numpy.array(f['Close'], dtype=float)



#**********OSCILLATORI**********
#macd, macdsignal, macdhist = MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
# f['macd'], f['macdsignal'], f['macdhist'] = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
# f1['macd'], f1['macdsignal'], f1['macdhist'] = talib.MACD(close, fastperiod=5, slowperiod=35, signalperiod=5)
# f2['macd'], f2['macdsignal'], f2['macdhist'] = talib.MACD(close, fastperiod=6, slowperiod=13, signalperiod=5)

#real = CCI(high, low, close, timeperiod=14)
# f['cci'] = talib.CCI(high, low, close, timeperiod=14)
# f2['cci'] = talib.CCI(high, low, close, timeperiod=20)

#real = RSI(close, timeperiod=14)

f['rsi'] = talib.RSI(close, timeperiod=7)
f1['rsi'] = talib.RSI(close, timeperiod=14)
f2['rsi'] = talib.RSI(close, timeperiod=21)




#********PLOT*********
# f.plot(y= ['macdsignal','macd','macdhist'], title='MACD')
# f1.plot(y= ['macdsignal','macd','macdhist'], title='MACD1')
# f2.plot(y= ['macdsignal','macd','macdhist'], title='MACD2')
# f.plot(y= ['cci'], title='CCI')
# f2.plot(y= ['cci'], title='CCI20')
f.plot(y= ['rsi'], title='RSI')
f1.plot(y= ['rsi'], title='RSI_14')
f2.plot(y= ['rsi'], title='RSI_21')
plt.show()

	

#*********FIGURES**********	
# #"Upside/Downside Gap Three Method"
# # integer1 = talib.CDLXSIDEGAP3METHODS(open, high, low, close)

# #"Evening Star"
# integer2 = talib.CDLEVENINGSTAR(open, high, low, close, penetration=0)

# #"Morning Star"
# integer3 = talib.CDLMORNINGSTAR(open, high, low, close, penetration=0)

# #"Engulfing Pattern"
# integer4 = talib.CDLENGULFING(open, high, low, close)
# print()
# print("Upside/Downside Gap Three Method")
# print(integer1)
# f['CDLXSIDEGAP3METHODS'] = integer1

# print()
# print("Evening Star")
# print(integer2)
# f['CDLEVENINGSTAR'] = integer2

# print()
# print("Morning Star")
# print(integer3)
# f['CDLMORNINGSTAR'] = integer3

# print()
# print("Engulfing Pattern")
# print(integer4)
# f['CDLENGULFING'] = integer4


# #************OPTIONALS*************
# #"Dark Cloud Cover"
# integer5 = talib.CDLDARKCLOUDCOVER(open, high, low, close, penetration=0)
# print()
# print("Dark Cloud Cover")
# print(integer5)

# #"Doji"
# integer6 = talib.CDLDOJI(open, high, low, close)
# print()
# print("Doji")
# print(integer6)

# #"Hammer"
# integer7 = talib.CDLHAMMER(open, high, low, close)
# print()
# print("Hammer")
# print(integer7)

# #"Hanging Man"
# integer8 = talib.CDLHANGINGMAN(open, high, low, close)
# print()
# print("Hanging Man")
# print(integer8)

# #"Harami"
# integer9 = talib.CDLHARAMI(open, high, low, close)
# print()
# print("Harami")
# print(integer9)

# #"Piercing Line"
# integer10 = talib.CDLPIERCING(open, high, low, close)
# print()
# print("Piercing Line")
# print(integer10)

# #"Shooting Star"
# integer11 = talib.CDLSHOOTINGSTAR(open, high, low, close)
# print()
# print("Shooting Star")
# print(integer11)

# f.to_csv("foo.csv")

# #f1 = f.iloc[65:,:]