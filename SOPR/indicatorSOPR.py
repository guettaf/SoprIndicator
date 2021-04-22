import numpy as np
import array
import matplotlib.pyplot as plt
from decimal import *


CVSfile = 'BTC.CSV'
utxoCVSfile = "utxo.csv"
my_BTCdata = np.genfromtxt(CVSfile,delimiter=',')
my_UTXOdata = np.genfromtxt(utxoCVSfile,delimiter=',')

##calculation MVRVZ score

btcempty=[]
l = 0
ar = 0
i = 0
while i < len(my_BTCdata):
	k = my_BTCdata[0:i]
	z = (my_BTCdata[i] - np.mean(k))/(np.std(k))
	btcempty.append(z)
	i=i+1
utxEmpty = []
l=0
while l < len(my_UTXOdata):
	k = my_UTXOdata[0:l]
	z = (my_UTXOdata[l] - np.mean(k))/(np.std(k))
	utxEmpty.append(z)
	l=l+1
empty = []
for i in range(0,len(btcempty)):
	m = btcempty[i]/utxEmpty[i]
	empty.append(m)
print ("utxO "+str(len(my_UTXOdata)))
#print ("\nutxO "+str(len(my_BTCdata)))
plt.plot(empty, 'r--')

plt.axhline(y=1)
plt.axhline(y=8)

#plt.show()