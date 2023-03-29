import requests
import pandas as pd

URL = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"


def main():
    df = pd.read_html(URL)[0]

    filename = df[df["Last modified"] == "2022-02-07 14:03"]["Name"].min()

    file_path = URL+filename

    data = pd.read_csv(file_path)

    max_hourly_temp = data[data["HourlyDryBulbTemperature"]
                           == data["HourlyDryBulbTemperature"].max()]
    print(max_hourly_temp)


if __name__ == '__main__':
    main()
