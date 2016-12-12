from pandas_datareader import data as web
import talib
import numpy
import pandas
import matplotlib.pyplot as plt
from datetime import datetime

end = datetime.now()
start = datetime(end.year, end.month-4, end.day)
f = web.DataReader("A2A.MI", 'yahoo', start, end)

f = pandas.DataFrame(f, columns=["Open","High","Low","Close"])

open = numpy.array(f['Open'], dtype=float)
high = numpy.array(f['High'], dtype=float)
low = numpy.array(f['Low'], dtype=float)
close = numpy.array(f['Close'], dtype=float)


f['SMA_20'] = talib.SMA(close, 20)
f['SMA_50'] = talib.SMA(close, 50) 
f['macd'], f['macdsignal'], f['macdhist'] = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)

f.plot(y= ['Close','SMA_20','SMA_50'], title='AAPL Close & Moving Averages')
f.plot(y= ['macdsignal','macd','macdhist'], title='MACD')
plt.show()

integer1 = talib.CDLTRISTAR(open, high, low, close)
integer2 = talib.CDL2CROWS(open, high, low, close)
integer3 = talib.CDL3BLACKCROWS(open, high, low, close)
integer4 = talib.CDL3INSIDE(open, high, low, close)
integer5 = talib.CDL3LINESTRIKE(open, high, low, close)
integer6 = talib.CDL3OUTSIDE(open, high, low, close)
integer7 = talib.CDL3STARSINSOUTH(open, high, low, close)
integer8 = talib.CDL3WHITESOLDIERS(open, high, low, close)
integer9 = talib.CDLABANDONEDBABY(open, high, low, close, penetration=0)
integer10 = talib.CDLADVANCEBLOCK(open, high, low, close)
print(integer1)
print(integer2)
print(integer3)
print(integer4)
print(integer5)
print(integer6)
print(integer7)
print(integer8)
print(integer9)
print(integer10)