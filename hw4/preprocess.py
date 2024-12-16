# Pre-processing Script
import dask.dataframe as dd
import pandas as pd
import tarfile
from io import BytesIO

def preprocess_data(input_file):
    with tarfile.open(input_file, 'r:gz') as tar:
        csv_file = tar.extractfile(tar.getmembers()[0])
        csv_data = BytesIO(csv_file.read())  

    df = pd.read_csv(csv_data, header=None, usecols=[1, 2, 5, 8], 
                     names=['created_date', 'closed_date', 'complaint_type', 'incident_zip'],
                     dtype={'incident_zip': 'float64'})

    df['created_date'] = pd.to_datetime(df['created_date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')
    df['closed_date'] = pd.to_datetime(df['closed_date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

    df = df.dropna(subset=['created_date', 'closed_date', 'incident_zip'])

    df = df[(df['created_date'] >= '2020-01-01') & (df['created_date'] < '2021-01-01')]

    df['incident_zip'] = df['incident_zip'].astype('int64')
    df['response_time_hours'] = (df['closed_date'] - df['created_date']).dt.total_seconds() / 3600
    df = df[df['response_time_hours'] > 0]

    df['month'] = df['closed_date'].dt.to_period('M')

    ddf = dd.from_pandas(df, npartitions=4)
    result = ddf.groupby(['incident_zip', 'month'])['response_time_hours'].mean().reset_index()

    result.compute().to_csv('monthly_avg_response_times.csv', index=False)

preprocess_data('nyc_311_2020.tgz')