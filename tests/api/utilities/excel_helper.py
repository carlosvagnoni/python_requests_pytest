import os
import openpyxl


def get_excel_data(file_name, sheet_name):
    """
    Retrieves data from a specified Excel file and sheet.

    :param file_name: Name of the Excel file.
    :param sheet_name: Name of the sheet within the Excel file.
    :return: List containing data starting from the second row.
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = current_dir.rsplit("\\", 3)[0]
    file_path = os.path.join(base_dir, 'test_data', file_name)

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(row)

    workbook.close()
    return data
