list_pt = ["Sim", "N~ao", "", "", "", "", "", ""]
list_en = ["Yes", "No", "", "", "", "", "", "", ""]

file_pt = ""
file_en = "output_en.csv"

columns = [0, 2, 5, ...]

with open(file_pt, "r") as f:
    for raw_line in f:
        split_line = raw_line.split(",")
        line_en = split_line
        for col in columns:
            line_en[col] = split_line[col]

