#Rohan Abraham
#Reads a file and calculates the average number of steps taken for each month
def main():
    line = ''
    number = 0.0
    count = 0.0
    

    infile = open('steps.txt', 'r')
    
    line = infile.readline()
    total = 0.0
    for count in range(0,31):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for January:  ',format(total/count,',.2f'))

    total = 0.0 
    for count in range(0,28):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for Febuary:  ', format(total/count,',.2f'))

    total = 0.0
    for count in range(0,31):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for March:    ', format(total/count,',.2f'))

    total = 0.0
    for count in range(0,30):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for April:    ', format(total/count,',.2f'))

    for count in range(0,31):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for May:      ', format(total/count,',.2f'))

    total = 0.0
    for count in range(0,30):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for June:     ', format(total/count,',.2f'))

    total = 0.0
    for count in range(0,31):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for July:     ', format(total/count,',.2f'))
    
    total = 0
    for count in range(0,31):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for August:   ', format(total/count,',.2f'))

    total = 0
    for count in range(0,30):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for September:', format(total/count,',.2f'))

    total = 0.0
    for count in range(0,31):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for October:  ', format(total/count,',.2f'))

    total = 0
    for count in range(0,30):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for November: ', format(total/count,',.2f'))

    total = 0.0
    for count in range(0,31):
        number = float(line)
        total+=number
        count+=1
        line = infile.readline()
    print('Average for December: ', format(total/count,',.2f'))
    
    infile.close()
main()
