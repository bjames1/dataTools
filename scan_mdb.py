import pandas as pd
import subprocess
from params import *
from value2key import *
#
def show_tables(path='<file_name>.mdb'):
    tables = subprocess.check_output(["mdb-tables", path])
    return tables.decode().split()

def show_data(path='<file_name>.mdb', table='<table_name>'):
    tables = subprocess.check_output(["mdb-export", path, table])
    return tables.decode().split('\n')
#
mdb_tables = show_tables(mdb_file)
metaFields = show_data(path=mdb_file, table='metaFields')

columns = metaFields[0].split(',')
for i in range(24):
    colName = 'col' + (str(47+i+1))
    columns.append(colName)
rows = [i.split(',') for i in metaFields[1:]]
# #
dfMetaFields = pd.DataFrame(columns=columns, data=rows)
mf_Name = dfMetaFields['Name'].tolist()
mf_PromptText = dfMetaFields['PromptText'].tolist()

subs = 'code';
code_names = [i for i in mdb_tables if subs in i];
code_index = [];
for code in code_names:
    code_index.append(code_names.index(code))


# dfMetaFields.columns
SourceTable_values = [];
SourceTable_index = [];
SourceTables = list(dfMetaFields['SourceTableName'])
for i in range(len(SourceTables)):
    SourceTable = SourceTables[i];
    if SourceTable == "" or type == None:
        SourceTable = 'None';

    SourceTable_values.append(SourceTable)
    SourceTable_index.append(i)

codeMaster_values = [];
codeMaster_index = [];
for i in range(len(SourceTable_values)):
    value = SourceTable_values[i];
    if value == None:
        value = 'None';
    else:

        if 'code' in value:
            codeMaster_values.append(value)
            codeMaster_index.append(i)

# codeMaster_values
# codeMaster_index


codeMaster_dict = dict(zip(codeMaster_values, codeMaster_index))







# participanteducation = show_data(path=mdb_file, table='codeparticipanteducation1')
# df_participanteducation = pd.DataFrame(participanteducation)
