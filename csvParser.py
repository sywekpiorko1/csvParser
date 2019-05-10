import csv
import datetime

fmt = "%Y-%m-%d %H:%M:%S"

with open('id4106ip54.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # row_count = sum(1 for row in csv_file)
    
    line_count = 1
    step_count = 1
    tempEpoch = ""

    for row in csv_reader:
        
        if line_count == 1 and row[1] == 'TIME':
            pass
        
        elif tempEpoch == "":
            startRow = line_count
            tempEpoch = row[1]
        elif tempEpoch != row[1]:
            tempEpoch = row[1]
            tempValue = row[2]         
            print(step_count, line_count-startRow, line_count, tempEpoch, datetime.datetime.fromtimestamp(float(tempEpoch)).strftime(fmt), tempValue)
            startRow = line_count
            step_count += 1

        tempValue = row[2]
        line_count += 1 
        
    print(step_count, line_count-startRow, line_count , tempEpoch, tempValue)

        


        # elif (line_count-2)%450 == 0:
        #     data = int(row[1])
        #     dataHuman = datetime.datetime.fromtimestamp(float(data))
        #     print("Linia", line_count, data, dataHuman.strftime(fmt), row[2])
        #     line_count +=1
        # else:
        #     line_count +=1


    