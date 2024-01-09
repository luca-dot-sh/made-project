import scipy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime

def find_peaks(timeseries, min_value_for_peak = None):
    if(min_value_for_peak is not None):
        peaks,_  = scipy.signal.find_peaks(timeseries, height=min_value_for_peak)
    else:
        peaks,_  = scipy.signal.find_peaks(timeseries)
    peak_dates = timeseries.iloc[peaks].index.values
    return peak_dates

def show_plot_with_peaks(peak_dates):
    for peak in peak_dates:
        plt.axvline(x=peak, color='r', linestyle='--', alpha=0.7)
    plt.show()

def plot_regression_line(input, degree=3):
    X = input.index.isocalendar().week.astype(float)
    Y= input.astype(float)
    polyfunc = np.polynomial.Polynomial.fit(X,Y.values,degree)
    values = [polyfunc(y) for y in range(0,input.size)]
    pd.Series(data=values,index=input.index).plot()

def filter_only_2022_data(input_df,timecolumn = None):
    if(timecolumn == None):
        return input_df[(input_df.index >= datetime(year=2022,month=1,day=1)) & (input_df.index <= datetime(year=2022,month=12,day=30))]
    else:
        return input_df[(input_df[timecolumn] >= datetime(year=2022,month=1,day=1)) & (input_df[timecolumn] <= datetime(year=2022,month=12,day=30))]

def convert_columns_to_datetime(input_df, columns):
    for column in columns:
        input_df[column] = pd.to_datetime(input_df[column])
    return input_df