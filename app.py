import pandas as pd 

table = pd.read_csv("Resources/clean_weather.csv")

table.to_html("data_output.html")

