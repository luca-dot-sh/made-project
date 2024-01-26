from urllib.request import urlretrieve
import pandas as pd
import zipfile
import sqlalchemy as sqla

path, http_msg = urlretrieve("https://gtfs.rhoenenergie-bus.de/GTFS.zip")

with open(path, mode="r") as file:
    zip_file = zipfile.ZipFile(path)
    with zip_file.open("stops.txt", mode="r") as stopsfile:
        columns = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]
        df = pd.read_csv(stopsfile)
        df = pd.DataFrame(df, columns=columns)
        df = df.set_index("stop_id")
        df = df.loc[df["zone_id"]==2001]
        df = df.loc[(df["stop_lat"]>=-90)&(df["stop_lon"]<=90)]
        
        engine = sqla.create_engine("sqlite:///gtfs.sqlite")    
        df.to_sql("stops", engine, if_exists="replace", index=True)