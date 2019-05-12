import csv

def get_length():
    with open("id4106ip66.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)


print(get_length())


MONTH-2	TIME	DATA-PROBE=200	CALIBRATION=2.1230
