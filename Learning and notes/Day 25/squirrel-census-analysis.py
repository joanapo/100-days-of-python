import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = data["Primary Fur Color"]

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_color_dict = {
    "Fur color": ["Gray", "Red", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

squirrel_color_data = pandas.DataFrame(squirrel_color_dict)
squirrel_color_data.to_csv("squirrel_color_data.csv")