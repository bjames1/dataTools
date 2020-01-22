import pandas as pd
import subprocess

def show_tables(path='<file_name>.mdb'):
    tables = subprocess.check_output(["mdb-tables", path])
    return tables.decode().split()


def show_data(path='<file_name>.mdb', table='<table_name>'):
    tables = subprocess.check_output(["mdb-export", path, table])
    return tables.decode().split('\n')


mdb_file = '/Users/jamesbrown/Desktop/epiStuff/epiMetrics.mdb';

d = show_data(path=mdb_file, table='metaFields')

columns = d[0].split(',')
columns.append('')
data = [i.split(',') for i in d[1:]]

df = pd.DataFrame(columns=columns, data=data)
df = df.iloc[:, :-1]
