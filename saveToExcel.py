#this code helps in saving dataframe to excel
import pandas as pd

#libraries



def saveToExcel(self):
    column = ('Name','Drawing no.','Number Per Coach', 'Quantity Available', 'Quantity Purchased')
    df = pd.DataFrame(<list_name_with_data>)
    df.to_excel('excel file directory',sheet_name="Inventory",header=column,index=None)
