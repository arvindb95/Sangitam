import csv
from glob import glob
import os.path


def csv_to_latex(csv_file, filename_root):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        row_id = 0
        all_rows = r""
        len_of_row = 0
        for row in reader:
            row_str = r""
            len_of_row = len(row)
            if row[0] != "#":
                if row_id > 0:
                    for element in row[:-1]:
                        row_str += r"{e}".format(e=element) + r"&"
                    all_rows += row_str + r"{e}".format(e=row[-1]) + r"""\\""" + "\n"
            elif row[0] == "#":
                if row[1] != "#":
                    print(row)
                    for element in row[1:]:
                        row_str += r"{e}".format(e=element)
                    if row[1] != r"""\sah""":
                        all_rows += row_str + r"""\\""" + "\n"
                    else:
                        all_rows += row_str + "\n"

            if row_id == 0 and row[0] != "#":
                table_start_line = (
                    r"""\begin{center}"""
                    + "\n"
                    + r"""\begin{longtable}{ @{\extracolsep{\fill}} """
                    + len_of_row * "c "
                    + """} """
                    + "\n"
                )
            else:
                table_start_line = (
                    r"""\begin{center}"""
                    + "\n"
                    + r"""\begin{longtable}{ """
                    + len_of_row * "c "
                    + """} """
                    + "\n"
                )
            row_id += 1

        table_end_line = r"""\end{longtable} """ + "\n" + r"""\end{center} """

        full_str = table_start_line + all_rows + table_end_line
        text_file = open(filename_root + ".tex", "w")
        text_file.write(full_str)
        text_file.close()
    return 0


all_csv = glob("*/*.csv")

print(all_csv)

for csv_file in all_csv:
    filename_root = csv_file.split(".")[0]
    # if not os.path.exists(filename_root + ".tex"):
    csv_to_latex(csv_file, filename_root)
