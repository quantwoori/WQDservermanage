from system.DBmssql import MSSQL
from util.cleankrx import KRXClean
from typing import Dict

from os.path import isfile, join
from os import listdir
import os


def xprs_index(index_name:str, data_path:str, work_dir:str) -> None:
    """
    :param data_path: 'C:/Users/Wooriam/PycharmProjects/krxCrawler/download/'
    :param work_dir: 'C:/Users/Wooriam/PycharmProjects/dbm/wd/'

    Clean KRX data
    Push it in WSOL.dbo.indcomp
    """
    # DATABASE
    db = MSSQL.instance()
    db.login(id='wsol1', pw='wsol1')

    # INSERTION
    f = [f for f in listdir(data_path)
         if isfile(join(data_path, f))]
    workfile = list()
    for file in f:
        os.rename(f"{data_path}{file}",
                  f"{work_dir}{file}")
        workfile.append(
            (f"{work_dir}{file}", file)
        )
        print(f"{file} moved from data_path to work_dir")

    for _, fn in workfile:
        print(work_dir, fn)
        kc = KRXClean(
            file_loc=work_dir,
            file_name=fn,
            index_name=index_name
        )
        dnp = kc.result.to_numpy()
        db.insert_row(
            table_name='indcomp',
            schema='dbo',
            database='WSOL',
            col_=['year', 'chg_no', 'code',' stk_no', 'ind_'],
            rows_=[tuple(r) for r in dnp]
        )
        print(f"{fn} inserted")


if __name__ == "__main__":
    p = 'C:/Users/Wooriam/PycharmProjects/krxCrawler/download/'
    wd = 'C:/Users/Wooriam/PycharmProjects/dbm/wd/'
    xprs_index("ksbig", data_path=p, work_dir=wd)