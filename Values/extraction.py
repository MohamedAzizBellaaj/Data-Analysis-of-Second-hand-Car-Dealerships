import json

import pandas as pd


def save_to_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


cars = pd.read_csv("../Cleaning/new_clean_data.csv", index_col=0)


models = list(cars["model"].dropna().unique())

save_to_json("models.json", models)

brand_models = cars.groupby("brand")["model"].unique()

brand_models.to_json("brand_models.json")

location = list(cars["location"].dropna().unique())

save_to_json("location.json", location)

body_type = list(cars["body_type"].dropna().unique())

save_to_json("body_type.json", body_type)

fuel = list(cars["fuel"].dropna().unique())

save_to_json("fuel.json", fuel)

transmission = list(cars["transmission"].dropna().unique())

save_to_json("transmission.json", transmission)

color = list(cars["color"].dropna().unique())

save_to_json("color.json", color)
