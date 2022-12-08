#!/usr/bin/python

import os

#submission is the name of a given tar ball
def change_to_test_location(submission):
    #in case of "frag1 frag2 (frag3) frag4's"
    fixed_submission = submission.replace(" ", "\ ").replace("(", "\(").replace(")", "\)").replace("'", "\\'")
    folder = submission.split('.', 1)[0]
    fixed_folder = fixed_submission.split('.', 1)[0]

    # if folder exists, remove it to restart what we are doing
    if os.path.exists(folder):
        cmd = 'rm ' + fixed_folder + ' -rf'
        os.system(cmd)

    # make dir and cp
    #print '========' + submission
    #print '========' + folder
    os.makedirs(folder)
    cmd = 'cp ' + fixed_submission + ' ' + fixed_folder
    os.system(cmd)
    #print fixed_submission + ' '+ submission + ' ' + fixed_folder +' ' + folder

    # change dir
    os.chdir(folder)
    # unzip or untar
    if '.zip' in fixed_submission:
        cmd = 'unzip ./' + fixed_submission + ' > /dev/null'
    if '.tar' in fixed_submission:
        if 'tar.gz' in fixed_submission:
            cmd = 'tar xfvz ./' + fixed_submission + ' > /dev/null'
        elif 'tar.bz' in fixed_submission:
            cmd = 'tar xfv ./' + fixed_submission + ' > /dev/null'
        else:
            cmd = 'tar xfv ./' + fixed_submission + ' > /dev/null'
    elif '.tgz' in fixed_submission:
        cmd = 'tar xfv ./' + fixed_submission + ' > /dev/null'
    os.system(cmd)

    # rm the copied tar ball
    cmd = 'rm -rf ' + fixed_submission
    os.system(cmd)

def locate_exe(submission):
    #must have either makefile or 412alloc script
    subDir = os.getcwd()
    os.system('find -iname "makefile" > tmp')
    f = open('tmp', 'r')
    line = f.readline()
    f.close()
    os.system('rm -rf tmp')
    if line != "":
        os.chdir(line.strip().rsplit('/', 1)[0])
        os.system('make clean')
        os.system('make build')
        #os.system('make')
        os.chdir(subDir)
    #os.system('ls')
    os.system('find -name "412alloc" -type f > tmp')
    f = open('tmp', 'r')
    line = f.readline()
    f.close()
    os.system('rm -rf tmp')
    if line == "":
        print(submission ,' didn\'t folllow the instructions: no makefile and no allocator')
        return -1

    #change to dir that contains 412alloc
    os.chdir(line.strip().rsplit('/', 1)[0])
    os.system("chmod a+x 412alloc")        # moved here from lab2_grade
    return 0
