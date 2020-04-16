import pandas as pd
from utils import *
import numpy as np

#df = pd.dataFrame
def loadAndCleanData(filename):
	df = pd.read_csv(filename) 
	
	return df

df = loadAndCleanData("time_series_covid19_confirmed_global.csv")

class covid:
	def __init__(self,name,df):
		self.outlet = name
		self.data = df.loc[df['Covid']==name]

	def correctDateFormat(dataframe, colName):
		pd.melt(dataframe, id_vars = ['Province/State', 'Country/Region'], var_name= 'colName' )
		pd.set_option('max_rows', 7)
		return pd

	df = correctDateFormat(df, 'Date')
	print df