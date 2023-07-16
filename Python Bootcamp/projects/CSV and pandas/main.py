# with open("weather_data.csv") as file:
#     list1=file.readlines()
    
# print(list1)

# import csv

# temperatures=[]
# with open("weather_data.csv") as data:
#     table=csv.reader(data)
#     for i in table:
#         temperatures.append(i[1])
# temperatures.remove(temperatures[0])   
# temperature=[int(i) for i in temperatures]
# print(temperature)

import pandas
data=pandas.read_csv("weather_data.csv")
temp=data["temp"].tolist()
total=0
avg=sum(temp)/len(temp)
# print(avg)
maxvalue=data["temp"].max()
# print(maxvalue)

# #to print data in columns
# print(data["temp"],data.temp)
# print(data["condition"],data.condition)

# row=data[data.temp == maxvalue]
# maxtemp=row.day.tolist()
# print(maxtemp[0])

# print((data[data.day=="Monday"].temp*9/5)+32)

# to create a new dataframe from scratch

dict_table={
            "students" : ["Aniket","Rahul","Sumit"],
            "scores" : [20,40,23]
            }

new_dataframe=pandas.DataFrame(data=dict_table)
print(new_dataframe)
new_dataframe.to_csv("new_dataframe.csv")