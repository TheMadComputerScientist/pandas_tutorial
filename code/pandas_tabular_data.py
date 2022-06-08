# -------------------- 12345678901234567890 --------------------
# Author: Raikesson W. Charles
# Date: 06/2022
# Description: Application used to read PDF file, convert tabular
#	       	   data to DataFrame for analytics and data 
#	           manipulation

#OCR library, based in java, used to convert pdf to dataframe
import tabula as tb

#Pandas, Data analysis library
import pandas as pd

#PDF file path
input_file_path = "<your_location>/resources/Pandas_Sample_Data.pdf"

#Location to store our PDF that will be converted to csv
output_file_path = "<your_location>/resources/Pandas_Sample_Data.csv"

#Convert our PDF file into a CSV file
tb.convert_into(input_file_path, output_file_path, "csv", pages="all") 

#Create the DataFrame from the new CSV file
initial_data = pd.read_csv(output_file_path, delimiter=",")

#Print the DataFrame
print(initial_data)

#Selecting the first two rows
rows = pd.DataFrame(initial_data.loc[[0, 1]])

print(rows)

#Select the qty column
cols = pd.DataFrame(initial_data, columns = ['qty'])

print(cols)

#Display true when "Not a Number" (NaN) values are detected
print(cols.isna())

