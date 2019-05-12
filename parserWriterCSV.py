import csv
import datetime
import os
import time

startTime = time.time()

def first_last_line_display(csv_file_name, path):

    with open(os.path.join(path, csv_file_name), 'r') as csv_file:
        print('##### Analizing file: ',os.path.join(path, csv_file_name),'    ', sum(1 for row in csv_file),' lines long #####')

    fmt = "%Y-%m-%d %H:%M:%S"

    with open(os.path.join(path, csv_file_name), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # row_count = sum(1 for row in csv_file)
        
        lineCount = 1
        stepCount = 1
        tempEpoch = ""
        whichEnterCount = 1
        valuesList = []
        print("{: <15} {: <7} {: <10} {: <15} {: <21} {: >10} {: >20}".format('Step no:', 'LEN', 'Line no:', 'Epoch Time', 'Human Time','Value', 'Sec between vals'))

        for row in csv_reader:
            
            if lineCount == 1 and row[1] == 'TIME':
                pass

            # FIRST STEP
            elif tempEpoch == "":
                startRow = lineCount
                tempEpoch = row[1]
                tempEpochToHuman = datetime.datetime.fromtimestamp(float(tempEpoch)).strftime(fmt)
                tempValue = row[2]
                print("{: <15} {: ^7} {: <10} {: ^15} {: <21} {: >10}".format(0, lineCount-startRow, lineCount, tempEpoch, tempEpochToHuman, tempValue))

            # EACH OTHER STEP
            elif tempEpoch != row[1]:
                lastEpoch = tempEpoch
                tempEpoch = row[1]
                tempEpochToHuman = datetime.datetime.fromtimestamp(float(tempEpoch)).strftime(fmt)
                epochDifference = int(tempEpoch) - int(lastEpoch)
                tempValue = row[2]
                linesDifference = lineCount-startRow
                period_between_measurements = epochDifference/linesDifference

                # PRINT ONLY n FIRST LINES
                if whichEnterCount < 4:
                    whichEnterCount +=1
                    print("{: <15} {: ^7} {: <10} {: ^15} {: <21} {: >10} {: >20}".format(stepCount, linesDifference, lineCount, tempEpoch, tempEpochToHuman, tempValue, period_between_measurements))
                if whichEnterCount == 4:
                    whichEnterCount +=1
                    print(". . . . . ." )
                if len(valuesList) != 450:
                    print("For identical Epoch Time(", tempEpoch,") found len(valuesList) != 450 finishing about line ", lineCount, " | Actual length is:", len(valuesList))
                    print(". . . . . ." )

                # RECALCULATION OF EPOCH
                # for a in range(linesDifference):
                #     print    
                valuesList = []          

                startRow = lineCount
                stepCount += 1
            
            tempValue = row[2]
            # GRAB VALUE AND PUT IN LIST
            if tempEpoch[0:3] == '155':
                valuesList.append(tempValue)
            lineCount += 1 
            
        # FINISHING PRINT LINE
        tempEpochToHuman = datetime.datetime.fromtimestamp(float(tempEpoch)).strftime(fmt)
        print("{: <15} {: ^7} {: <10} {: ^15} {: <21} {: >10} {: >20}".format(stepCount, lineCount-startRow, lineCount, tempEpoch, tempEpochToHuman, tempValue, period_between_measurements))
        print(100*'-')

# path = 'ignoreFolder/dilightstudios'
path = 'ignoreFolder/Clonakilty'

print('>>> STARTED >>>')
for filename in os.listdir(path):
    first_last_line_display(filename, path)
print("--- %s seconds ---" % (time.time() - startTime))
    