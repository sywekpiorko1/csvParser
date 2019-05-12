import csv
import datetime

def first_last_line_display(csv_file_name):

    out = csv.writer(open('output.csv', 'r'), delimiter=',')

    with open(csv_file_name, 'r') as csv_file:
        print('Analizing file: ',csv_file_name,'    ', sum(1 for row in csv_file),' lines long')

    fmt = "%Y-%m-%d %H:%M:%S"

    with open(csv_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # row_count = sum(1 for row in csv_file)
        
        line_count = 1
        step_count = 1
        tempEpoch = ""
        print("{: <15} {: <7} {: <10} {: <15} {: <21} {: <5}".format('Step no:', 'LEN', 'Line no:', 'Epoch Date', 'Human Date','Value'))

        for row in csv_reader:
            
            if line_count == 1 and row[1] == 'TIME':
                pass

            # elif line_count == 100000:
            #     break
            
            elif tempEpoch == "":
                startRow = line_count
                tempEpoch = row[1]
                tempEpochToHuman = datetime.datetime.fromtimestamp(float(tempEpoch)).strftime(fmt)
                tempValue = row[2]
                print("{: <15} {: ^7} {: <10} {: ^15} {: <21} {: >5}".format(step_count, line_count-startRow, line_count, tempEpoch, tempEpochToHuman, tempValue))
            elif tempEpoch != row[1]:
                lastEpoch = tempEpoch
                tempEpoch = row[1]
                epochDifference = int(tempEpoch) - int(lastEpoch)
                tempValue = row[2]
                startRow = line_count
                step_count += 1

            tempValue = row[2]
            line_count += 1 
            
        tempEpochToHuman = datetime.datetime.fromtimestamp(float(tempEpoch)).strftime(fmt)
        print("{: <15} {: ^7} {: <10} {: ^15} {: <21} {: >5}".format(step_count, line_count-startRow, line_count, tempEpoch, tempEpochToHuman, tempValue))
        print('Period between measurements:', epochDifference/(line_count-startRow))
        print('')

first_last_line_display('id4106ip54.csv')
    