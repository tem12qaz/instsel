import xlsxwriter

xlsx_table_name = 'new_parse'
xlsx_table_columns = ('url', 'count', 'email')


def make_xlsx():
    path = f'new_parse.xlsx'
    with xlsxwriter.Workbook(path) as workbook:
        worksheet = workbook.add_worksheet()
        length = len(xlsx_table_columns)

        cell_format = workbook.add_format()
        cell_format.set_bold()

        for i in range(length):
            worksheet.write(0, i, xlsx_table_columns[i], cell_format)

        return worksheet


def write_xlsx(j, data):
    path = f'new_parse.xlsx'
    with xlsxwriter.Workbook(path) as workbook:
        worksheet = workbook.add_worksheet()
        length = len(xlsx_table_columns)

        cell_format = workbook.add_format()
        cell_format.set_bold()

        for i in range(length):
            worksheet.write(0, i, xlsx_table_columns[i], cell_format)

        for i in range(len(data)):
            worksheet.write(j, i, data[i])
