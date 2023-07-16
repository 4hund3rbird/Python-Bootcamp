import pandas
squirrel_data=pandas.read_csv("squirrel_data.csv")
cinnamon_color=squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
grey_color=squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
black_color=squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

cinnamon_sqr=len(cinnamon_color)
black_sqr=len(black_color)
gray_sqr=len(grey_color)

dict_sqr={
            "Fur Color":["gray","cinnamon","black"] ,
            "count":[gray_sqr,cinnamon_sqr,black_sqr]

            }

sqr_count=pandas.DataFrame(data=dict_sqr)
sqr_count.to_csv("squirrel count.csv")