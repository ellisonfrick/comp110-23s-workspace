"""Ex08 - Data Wrangling!"""

__author__ = "730568890"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_vals(table: list[dict[str, str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    # Step through table
    for row in table:
        # Save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformats data so that it's dictionary with column headers as keys!"""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        # for each key, make a dictionary entry with all column values
        result[key] = column_vals(table, key)
    return result


def head(table: dict[str, list[str]], x: int) -> dict[str, list[str]]:
    """Produces a new column-based table with only the first N rows of data for each column!"""
    empty: dict = {}
    for column in table:
        empty_list: list = []
        variable: int = 0
        for item in table[column]:
            if x > variable:
                empty_list.append(item)
                variable += 1
        empty[column] = empty_list
    return empty


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce new column-based table with specific subset of original columns!"""
    empty_dict: dict[str, list[str]] = {}
    for column in names:
        empty_dict[column] = table[column]
    return empty_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce new column-based table with two column-based tabled combined."""
    empty_dict: dict[str, list[str]] ={}
    for column in table_1:
        empty_dict[column] = table_1[column]
    for column in table_2:
        if column in empty_dict:
            for key in table_2[column]:
                empty_dict[column].append(key)
        else:
            empty_dict[column] = table_2[column]
    return empty_dict


def count(list_1: list[str]) -> dict[str, int]:
    """Produce dict where each key is unique value associated with the count it appears in the input list."""
    empty_dict: dict[str, int] = {}
    for item in list_1:
        if item in empty_dict:
            empty_dict[item] += 1
        else:
            empty_dict[item] = 1
    return empty_dict

