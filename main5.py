from utils import *
from covid import covid
import numpy as np

df = loadAndCleanData("time_series_covid19_confirmed_global.csv")

def loadAndCleanData(filename):
	df = pd.read_csv(filename) 
	
	return df

