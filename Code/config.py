import os
from pathlib import Path

#Set path
schema_path = Path(
        #os.environ['HOME'],
        "C:/Users/tolom/OneDrive/Desktop/"
        'Sysdata',
        'misc',
        'schemas.yaml'
    )
data_path = Path(
        "C:/Users/tolom/OneDrive/Desktop/",
        'Sysdata',
        'data'
    )

#Set db variables
host = 'localhost'
port = 5432
dbname = 'sysdata'
user = 'postgres'
password = 'mario'


