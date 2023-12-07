import json
import openpyxl


def get_json_data(filename):
    with open(filename) as file:
        file_data = json.load(file)
    return file_data


def get_excel_data(filename, row, col):
    wb_obj = openpyxl.load_workbook(filename)
    sheet_obj = wb_obj.active
    cell_obj = sheet_obj.cell(row, col)
    return cell_obj.value

#data = get_json_data("test_resource_data.json")
#print(data['url'])