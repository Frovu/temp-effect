import temperature
import logging
logging.disable(logging.DEBUG)
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, time
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['figure.facecolor'] = 'darkgrey'

dfrom = datetime.strptime('2020-01-01', '%Y-%m-%d')
dto = datetime.strptime('2020-01-11', '%Y-%m-%d')

logging.disable(logging.NOTSET)
data = temperature.get(55.47, 37.32, dfrom, dto)

if isinstance(data, list):
    logging.disable(logging.DEBUG)
    fig, ax = plt.subplots()
    level = [a[1] for a in data]
    drange = [a[0] for a in data]
    ax.plot(drange, level, 'c')
    legend = plt.legend(['temperature'])
    plt.setp(legend.get_texts(), color='grey')
    plt.show()
