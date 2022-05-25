from util.xprsd import xprs_index
from metadata.workdir import WorkDirectory
import os


def main(index_name:str):
    # Insert data
    p = WorkDirectory().ORIGIN
    wd = WorkDirectory().CURR
    xprs_index(index_name, data_path=p, work_dir=wd)

    # Move used data into uwd
    os.rename(f"{data_path}{file}", f"{work_dir}{file}")