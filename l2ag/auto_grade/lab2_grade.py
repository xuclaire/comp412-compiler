#!/usr/bin/python

import os

def check_output(alloc_output, correct_output):
    fa = open(alloc_output, 'r')
    fc = open(correct_output, 'r')
    line_a = ""
    line_c = ""
    is_bad = False
    while True:
        line_c = fc.readline()
        line_a = fa.readline()
        if 'cycle' in line_c:
            break
        if line_a == "":
            is_bad = True
            break
        if not line_a == line_c:
            is_bad = True
            break

    fa.close()
    fc.close()
    big_number = '100000'
    if is_bad == True:
        return big_number

    if not 'cycle' in line_a:
        return big_number

    return int(line_a.rsplit(' ', 1)[0].rsplit(' ', 1)[1])

#return number of cycles after allocation and checking the outputs
def lab2_grade(file, short_name, sim, num_regs, submission):
    #get input for simulator
    f = open(file, 'r')
    input = ""
    output = []

    while True:
        line = f.readline().strip()
        if line == "":
            break
        if '//SIM INPUT:' in line:
            input = line.split(':')[1]
            break

    f.close()

    result_file = ""
    if '/' in file:
        result_file = 'alloc_' +file.rsplit('/', 1)[1]
    else:
        result_file = 'alloc_' + file

    # get result without allocation
    correct_output = 'correct_output'
    os.system(sim + input + ' < ' + file + ' > ' + correct_output)

    # compare output with allocation to result without allocation
    # if same outputs, return number of cycles
    # if not same, return -1
    alloc_output = 'output'
    cycles = {} # dictionary to record num_reg to cycle mapping
    if len(short_name) > 6:
        print(short_name+":\t",end="")
    else:
        print(short_name+":\t\t",end="")
    for r in num_regs:
        #print 'checking ' + file + ' with ' + str(r) + ' registers, ',
        #
        # Run 412alloc
        os.system('timeout 300s ./412alloc ' + str(r) + ' ' + file + ' > ' + result_file)
        # Run the simulator on the allocated code
        os.system(sim + ' -r ' + str(r) + ' ' + input + ' < ' + result_file + ' > ' + alloc_output)
        # Check answers and cycles
        cycles[r] = check_output(alloc_output, correct_output)#outup comparison
        #print("k = ",r," took ",cycles[r],"cycles.")

    os.system('rm -rf ' + correct_output)
    print(cycles)
    return cycles
