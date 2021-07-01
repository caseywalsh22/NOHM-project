import pandas as pd#data analysis library
from openpyxl import load_workbook #actually need?
import matplotlib.pyplot as plt

#change out with apporpiate file path
#change out approproate excel sheet name as well
excel_sheet_nohms = r'C:\Users\Greenbaum\Downloads\Corrected NOHM LITFSI DATA.xlsx'

#create one dataframe

#change sheet name when approproate, starts count at zero
#could possibly make a for loop to automate
nohm_df = pd.read_excel(excel_sheet_nohms, sheet_name = 0)
nohm_df.columns = ['gzlvl_point1', 'i_point1', 'na', 'gzlvl_point25', 'i_point25', 'na', 'gzlvl_point5', 'i_point5', 'na', 'gzlvl_point75', 'i_point75', 'na', 'gzlvl_1', 'i_1', 'na', 'calc', 'other_calc']


#for .1% weight
#select dataframes for the norm and gz
int_point1_df = nohm_df.i_point1[6:22]
gz_point1_df = nohm_df.gzlvl_point1[6:22]
#join the two dataframes to create one
full_df = pd.concat([gz_point1_df, int_point1_df], axis=1, join='outer')
#give the columns names
full_df.columns = ['Gz', 'intensity']
print(full_df)
#change objects into numeric values
full_df = full_df.apply(pd.to_numeric)
#print graph
full_df.plot.line(x= 'Gz', y = 'intensity', title = '.1 weight %')
plt.show()

#for .25% weight
#select dataframes for the norm and gz
int_point25_df = nohm_df.i_point25[6:22]
gz_point25_df = nohm_df.gzlvl_point25[6:22]
#join the two dataframes to create one
full_df = pd.concat([gz_point25_df, int_point25_df], axis=1, join='outer')
#give the columns names
full_df.columns = ['Gz', 'intensity']
print(full_df)
#change objects into numeric values
full_df = full_df.apply(pd.to_numeric)
#print graph
full_df.plot.line(x= 'Gz', y = 'intensity', title = '.25 weight %')
plt.show()

#for .5% weight
#select dataframes for the norm and gz
int_point5_df = nohm_df.i_point5[6:22]
gz_point5_df = nohm_df.gzlvl_point5[6:22]
#join the two dataframes to create one
full_df = pd.concat([gz_point5_df, int_point5_df], axis=1, join='outer')
#give the columns names
full_df.columns = ['Gz', 'intensity']
print(full_df)
#change objects into numeric values
full_df = full_df.apply(pd.to_numeric)
#print graph
full_df.plot.line(x= 'Gz', y = 'intensity', title = '.5 weight %')
plt.show()

#for .75% weight
#select dataframes for the norm and gz
int_point75_df = nohm_df.i_point75[6:22]
gz_point75_df = nohm_df.gzlvl_point75[6:22]
#join the two dataframes to create one
full_df = pd.concat([gz_point75_df, int_point75_df], axis=1, join='outer')
#give the columns names
full_df.columns = ['Gz', 'intensity']
print(full_df)
#change objects into numeric values
full_df = full_df.apply(pd.to_numeric)
#print graph
full_df.plot.line(x= 'Gz', y = 'intensity', title = '.75 weight %')
plt.show()

#for 1% weight
#select dataframes for the norm and gz
int_1_df = nohm_df.i_1[6:22]
gz_1_df = nohm_df.gzlvl_1[6:22]
#join the two dataframes to create one
full_df = pd.concat([gz_1_df, int_1_df], axis=1, join='outer')
#give the columns names
full_df.columns = ['Gz', 'intensity']
print(full_df)
#change objects into numeric values
full_df = full_df.apply(pd.to_numeric)
#print graph
full_df.plot.line(x= 'Gz', y = 'intensity', title = '1 weight %')
plt.show()
