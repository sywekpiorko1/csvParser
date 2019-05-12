import csv
import datetime
import os

def first_last_line_display(csv_file_name, path):

    with open(os.path.join(path, csv_file_name), 'r') as csv_file:
        print('Analizing file: ',os.path.join(path, csv_file_name),'    ', sum(1 for row in csv_file),' lines long')

    fmt = "%Y-%m-%d %H:%M:%S"

    with open(os.path.join(path, csv_file_name), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # row_count = sum(1 for row in csv_file)
        
        line_count = 1
        step_count = 1
        tempEpoch = ""
        which_enter_count = 1
        print("{: <15} {: <7} {: <10} {: <15} {: <21} {: <10}".format('Step no:', 'LEN', 'Line no:', 'Epoch Date', 'Human Date','Value'))

        for row in csv_reader:
            
            if line_count == 1 and row[1] == 'TIME':
                pass
            
            # FIRST STEP
            elif tempEpoch == "":
                startRow = line_count
                tempEpoch = row[1]
                tempEpochToHuman = datetime.datetime.fromtimestamp(float(tempEpoch)).strftime(fmt)
                tempValue = row[2]
                print("{: <15} {: ^7} {: <10} {: ^15} {: <21} {: >10}".format(step_count, line_count-startRow, line_count, tempEpoch, tempEpochToHuman, tempValue))

            # EACH OTHER STEP
            elif tempEpoch != row[1]:
                lastEpoch = tempEpoch
                tempEpoch = row[1]
                tempEpochToHuman = datetime.datetime.fromtimestamp(float(tempEpoch)).strftime(fmt)
                epochDifference = int(tempEpoch) - int(lastEpoch)
                tempValue = row[2]
                period_between_measurements = epochDifference/(line_count-startRow)

                # PRINT ONLY n FIRST LINES
                if which_enter_count < 4:
                    which_enter_count +=1
                    print("{: <15} {: ^7} {: <10} {: ^15} {: <21} {: >10} {: >20}".format(step_count, line_count-startRow, line_count, tempEpoch, tempEpochToHuman, tempValue, period_between_measurements))
                if which_enter_count == 4:
                    which_enter_count +=1
                    print(". . . . . ." )   
                startRow = line_count
                step_count += 1

            tempValue = row[2]
            line_count += 1 
            
        # FINISHING PRINT LINE
        tempEpochToHuman = datetime.datetime.fromtimestamp(float(tempEpoch)).strftime(fmt)
        print("{: <15} {: ^7} {: <10} {: ^15} {: <21} {: >10}".format(step_count, line_count-startRow, line_count, tempEpoch, tempEpochToHuman, tempValue))
        print('Period between measurements:', epochDifference/(line_count-startRow))
        print('')


# path = 'ignoreFolder/dilightstudios'
path = 'ignoreFolder/Clonakilty'

for filename in os.listdir(path):
    first_last_line_display(filename, path)
    