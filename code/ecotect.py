import re

#type in the absolute path of two Ecotect result txt file.
PATH_1 = r'C:\Users\tj371_000\Documents\ecotect_result_comparison\900.txt'
PATH_2 = r'C:\Users\tj371_000\Documents\ecotect_result_comparison\1500.txt'
ROW = 0 #The ROW and COLUMN has not been set yet. It will be parsed from user input file
COLUMN = 0

#read two file and store the data into two lists
heading_1=[]
heading_2=[]
result_table_1 = []
result_table_2 = []
output = []

#compare the heading information of the two file
with open(PATH_1) as f:
    for i, line in enumerate(f):
        if i < 5:
            heading_1.append(line)
#heading_1 = ['//ECOTECT ANALYSIS GRID DATA','// DATA, RAD Illuminance',....]
with open(PATH_2) as f:
    for i, line in enumerate(f):
        if i < 5:
            heading_2.append(line)
# check the heading information, if there's a difference, jump out the program with an error
for i in range(5):
    if heading_1[i] != heading_2[i]:
        print('The heading information of two files are different, make sure you choose the write file')
        break
    print('Checking heading information of two txt file')
    print('Heading information passed')
'''
To do: Heading information checking should able jump a error message out and interrupt halfway
'''

#read row and column length from txt heading information(in line 4 and line 5,respectively)
ROW = int(re.findall(r'\d+', heading_1[4])[0])
COLUMN = int(re.findall(r'\d+', heading_1[3])[0])

# Set the output to 54 row and 45column of '0'
for y in range(ROW):
    line = []
    for x in range(COLUMN):
        line.append(0)
    output.append(line)

#Read data in the user input file, and store data into a variable
with open(PATH_1,'r') as f:
    for i, line in enumerate(f):
        if i >= 5:
            result_table_1.append(line.split(', '))

with open(PATH_2,'r') as f:
    for i, line in enumerate(f):
        if i >= 5:
            result_table_2.append(line.split(', '))

#compare the result
for row in range(ROW):
    for column in range(COLUMN):
        if float(result_table_1[row][column])>107 and float(result_table_1[row][column])<5000 and float(result_table_2[row][column])>107 and float(result_table_2[row][column])<5000:
            output[row][column] = 1
        elif (float(result_table_1[row][column])>107 and float(result_table_1[row][column])<5000) or (float(result_table_2[row][column])>107 and float(result_table_2[row][column])<5000):
            output[row][column] = 0.5

#Write the output list into a new file result.txt
with open('result.txt', 'w+', encoding='utf-8') as file:
    for i in range(5): #Write the heading information into the file
        file.write(str(heading_1[i]))
    for row in range(ROW):#Write data information into the file
        for column in range(COLUMN):
            file.write(str(output[row][column])+ ', ')
        file.write('\n')



