import requests
import logging
import json
from requests import HTTPError
from pandas import DataFrame, read_csv

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Extract:

    def __init__(self, file_path, chunks, chunk_size=1000) -> None:
        self._file_path = file_path
        self._chunks = chunks
        self._chunk_size = chunk_size
        self._offset = 0
        self._data_types = {'DR_NO': int, 'TIME OCC': int, 'AREA': int, 'AREA NAME': str,
            'Rpt Dist No': int, 'Part 1-2': 'category', 'Crm Cd': int, 'Crm Cd Desc': str, 'Mocodes': str,
            'Vict Age': int, 'Vict Sex': 'category', 'Vict Descent': str, 'Premis Cd': float, 'Premis Desc': str,
            'Weapon Used Cd': float, 'Weapon Desc': str, 'Status': 'category', 'Status Desc': 'category', 'Crm Cd 1': float,
            'Crm Cd 2': float, 'Crm Cd 3': float, 'Crm Cd 4': float, 'LOCATION': str, 'Cross Street': str, 'LAT': float,
            'LON': float}

    def extract(self):
        if self._chunks:
            return self.read_as_chunks()
        else:
            return self.read_whole()

    def read_as_chunks(self):
        first_df = read_csv(self._file_path, dtype=self._data_types, skiprows=0, nrows=self._chunk_size, parse_dates=['Date Rptd', 'DATE OCC'])
        yield first_df
        move_on = True
        while move_on:
            df = read_csv(self._file_path, dtype=self._data_types, skiprows=self._offset, nrows=self._chunk_size, header=None, names=first_df.columns, parse_dates=['Date Rptd', 'DATE OCC'])
            self._offset += self._chunk_size
            yield df
            if len(df) < self._chunk_size:
                move_on = False

    def read_whole(self):
        df = read_csv(self._file_path, dtype=self._data_types, parse_dates=['Date Rptd', 'DATE OCC'])
        return df
        

class Transform:

    def __init__(self, df: DataFrame) -> None:
        self._dataframe = df

    def change_column_names(self):
        cols = self._dataframe.columns
        col_names_to_update = {}
        for col in cols:
            new_col = str(col).lower().replace(' ', '_')
            col_names_to_update[col] = new_col
        col_names_to_update['Part 1-2'] = 'part_1_2'
        self._dataframe.rename(columns= col_names_to_update, inplace=True)
        return self

    def set_dtypes(self):

        return self

    def execute_all(self):
        return self.change_column_names(self).set_dtypes(self)
    
    @property
    def dataframe(self) -> DataFrame:
        return self._dataframe

class Load:

    def __init__(self, url: str) -> None:
        self._api_url = url
        self._counter = 0

    def to_sqlite(self, df: DataFrame):
        json_dict = json.loads(df.to_json(orient='records'))
        for data in json_dict:
            if self._counter%10 == 0:
                logging.info(f'Posting: {self._counter}. column')
            try:
                response = requests.post(self._api_url, json=data)
                if response.status_code != 201:
                    print(response.status_code)
                    raise HTTPError
            except HTTPError:
                logging.exception(f'Failed to post due to an HTTP Error: {self._counter}. column')
            except Exception:
                logging.exception(f'Failed to post due to an unknown Error: {self._counter}. column')
            finally:
                self._counter += 1

def etl():
    file_path = './data/crime_data.csv'
    url = 'http://127.0.0.1:8000/crimes'
    load = Load(url)
    
    def tl(df):
        df = Transform(df).change_column_names().set_dtypes().dataframe
        load.to_sqlite(df)

    def chunking():
        ext = Extract(file_path, chunks=True, chunk_size=100)
        for df in ext.extract():
            tl(df)

    def without_chunking():
        df = Extract(file_path, chunks=False).extract()
        tl(df)

    without_chunking()


if __name__ == '__main__':
    etl()
    