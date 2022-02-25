from metadata.meta import WsolManage
from system.DBmssql import MSSQL
from datetime import datetime
from typing import Dict, List


def __column_check(keys:list, columns:dict):
    for k in keys:
        if "NOT NULL" not in columns[k]:
            raise TypeError("PRIMARY KEY CANDIDATE MUST BE NOT NULL")
    print("[EXPRESS TABLE MAKER] >>> Good to go")


def xprs_table(name:str, meta_data:dict):
    # FORMAT, TYPE CHECK
    assert isinstance(meta_data, Dict), "Check the type of your meta data. Not Dict"
    assert "meta" in meta_data.keys(), "Check your meta data, missing 'meta'"
    assert "columns" in meta_data.keys(), "Check your meta data, missing 'columns'"
    assert "keys" in meta_data.keys(), "Check your meta data, missing 'keys'. If no PK, enter []"

    # NULL CHECK
    __column_check(meta_data['keys'], meta_data['columns'])

    # CREATION
    db = MSSQL.instance()
    db.login(id='wsol1', pw='wsol1')

    db.create_table(
        table_name=name,
        variables=meta_data['columns'],
        database="WSOL"
    )
    db.create_pkey(
        table_name=name,
        database="WSOL",
        primary_key=meta_data['keys'],
        schema='dbo'
    )


def xprs_rows():

    ...