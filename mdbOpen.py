import pandas as pd
import subprocess

def show_tables(path='<file_name>.mdb'):
    tables = subprocess.check_output(["mdb-tables", path])
    return tables.decode().split()


def show_data(path='<file_name>.mdb', table='<table_name>'):
    tables = subprocess.check_output(["mdb-export", path, table])
    return tables.decode().split('\n')


mdb_file = '/Users/jamesbrown/Desktop/epiStuff/epiMetrics.mdb';
tables = show_tables(mdb_file)
data = show_data(path=mdb_file, table='metaFields')

columns = data[0].split(',')
columns.append('')
rows = [i.split(',') for i in data[1:]]

df = pd.DataFrame(columns=columns, data=rows)
# df = df.iloc[:, :-1]
