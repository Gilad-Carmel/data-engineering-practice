import requests
import os
from zipfile import ZipFile
from pathlib import Path

download_path = Path("./downloads")
download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]


def create_folder_if_not_exists(folder_path: Path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
def main():
    create_folder_if_not_exists(download_path)

    for uri in download_uris:
        f_name = uri.split("/")[-1]
        f_path = download_path.joinpath(f_name)
        r = requests.get(uri)
        
        if r.status_code != 200:
            continue
        
        data = r.content
        with open(f_path, 'wb') as output_zip:
            output_zip.write(data)
            
        with ZipFile(f_path, 'r') as archive:
            file_names = archive.namelist()
            for file_name in file_names:
                if file_name.endswith('.csv') and not file_name.startswith("__"):
                    archive.extract(file_name, download_path)

        os.remove(f_path)

if __name__ == '__main__':
    main()
