import logging


# This is a comment line! It is started with a "#"!

# change the following line to open different file
file_1='log-a.strace'
file_2 = 'Log-B.strace'

print("First Log :  ")

# change the following line to search for another term
count = 0
term=' read('
term2 = 'tty'
term3 = 'pipe'

for line in lines:
    if term in line and term2 in line and term3 not in line:
        file_Name_Start = line.find('<')
        file_Name_End = line.find ('>')
        file_Name = lines[file_Name_Start + 1 : file_Name_End]
        if file_Name in fileDict.keys():
            fileDict[fileName] += 1
        else:
            fileDict[fileName] += 1
        print(line)
        count += 1

def extract_program_name(line, start_delimiter, end_delimiter):

    name_start = line.find(start_delimiter)
    name_end = line.find(end_delimiter, name_start + 1)
    name = line[name_start + 1 : name_end]
    return name

def get_program_stat(lines):

    program_names = [ ]
    timestamps = [ ]

for line in lines:
    if 'execve('in line:
        name = extract_program_name(line, ' " ', ' " ')
        if name not in program_names:
            program_names.append(name)
            timestamps.append([line_num])
        else:
            idx = program_names.index(name)
            timestamps[idx].append(line_num)
            
        line_num += 1
        
    #print(count)

print("OUTPUT 2: ")
count = 0
term1 = ' read('

term2 = 'tty'
term3 = 'pipe'

for line in lines2:
    if term1 in line and term2 not in line and term3 not in line:
        file_Name_Start = line.find('<')
        file_Name_End = line.find('>')
        file_Name_2 = line[file_Name_Start + 1: file_Name_End]
        
        if file_Name_2 in fileDict2.keys():
            fileDict2[fileName] += 1
            
        else:
            fileDict2[fileName] = 1
            
        print (line)
        count += 1

print ("OUTPUT 1 (Log a): ")
for key in fileDict.keys():
    print(key + ": " + str(fileDict.get(key)))


print("OUTPUT 2 (Log B): " )
for key in fileDict2.keys():
    print(key + ": " + str(fileDict2.get(key)))

#print(count)

    
    
