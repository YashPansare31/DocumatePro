from openpyxl import Workbook

def write_text_to_excel(text, output_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Extracted Text"

    lines = text.split("\n")

    for i, line in enumerate(lines, start=1):
        ws.cell(row=i, column=1).value = line

    wb.save(output_path)
    return output_path
