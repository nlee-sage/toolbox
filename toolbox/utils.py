"""
Name: utils.py
definition: Useful functions
Contributors: Nicholas Lee

Notes:
- Using for general work
"""

import datetime
import os
import pathlib

import pandas as pd
import numpy as np


def display_full_table(df: object):
    """Show data table without width restrictions

    Args:
        df (dataFrame): _description_
    """
    with pd.option_context("display.max_colwidth", None):
        print(df)


def get_time():
    """Create time stamp with format YYYY-MM-DD.Hr-Min

    Returns:
        string: current date and time
    """
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d.%H-%M")
    return time_stamp


def load_and_backup_dm(file_path: str, output_dir: str):
    """Create backup of data model with time stamp.

    Args:
        file_path (string):  path to CSV
    Returns:
        object: Data frame object
    """

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    dm = pd.read_csv(file_path, index_col=False)

    # write out old data model before changes
    file_path = pathlib.Path(file_path).stem + "-" + get_time() + ".csv"

    output_path = pathlib.Path(output_dir, file_path)

    dm.to_csv(output_path, index=False)

    return dm


def clean_list(string):
    """Takes a list represented as a string and returns only unique values found

    Args:
        string (str): list represented as string

    Returns:
        string: list as string of unique values
    """

    new_list = string.split(",")
    new_list = [n.strip() for n in new_list if n != "nan"]
    new_list = ",".join(sorted(list(np.unique(new_list)))).strip(",")
    return new_list
