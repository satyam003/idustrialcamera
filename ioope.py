import csv

def conv():
    filename1: str = "C:\\Users\satyam\Desktop\\NOK\\"
    filename2: str = "Data.csv"
    filename = filename1+filename2
    with open('ReceiveFile.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split(",") for line in stripped if line)
        with open(filename, 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Result', 'Code','Quality'))
            writer.writerows(lines)
    out_file.close()
    in_file.close()
    return None