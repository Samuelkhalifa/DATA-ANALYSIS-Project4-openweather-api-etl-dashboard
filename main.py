from etl_files.extract import extract
from etl_files.transform import transform
from etl_files.load import load
import csv
import pandas as pd


def main():

    # Get list of cities, isolated into an array list
    
    df = pd.read_csv("./csv_data/world_cities.csv")
    cities = df["name_en"].to_list()

    # Main intructions of the program

    raw_data = extract(cities)
    transformed_data = transform(raw_data)
    with open("./csv_data/weather_data.csv", "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=transformed_data[0].keys())
        writer.writeheader()
        writer.writerows(transformed_data)
    load(transformed_data)


main()