#Simulating an assembler for a simple CPU


#memory could be stored in a text file but should also reset every time you run code so storing it this way is limiting but effective
#memory = [0,0,0,0,0,0] #6 memory locations
memory = [0,1,2,3,4,5] #tester values
accumulator = 0
instructions = [ "MOVE", 'ADD', "SUB", "AND", "LOAD", "STORE", "ADDM", "SUBM", "JUMP", "JUMPZ", "JUMPNZ"]
code_file = open("/Users/amberfaruque/Documents/Personal projects/code.txt", 'r') 

lines = code_file.readlines()

#allows people to write comments in python hash format
def comment_checker(current_line):
    global code_line
    code_line = current_line
    char_index = 0
    for character in code_line:
        if character == "#":
            code_line =code_line[:char_index]
        char_index += 1
        
line_num = 0
for i in range(0, len(lines)):

    code_line= lines[line_num]
    comment_checker(code_line)
    
    tokens = code_line.split()
    
    try:
        tokens[1]= int(tokens[1])
    except: 
        "Error: Your operand should be a numerical value or memory location"
    
    if  (len(tokens) != 2):
        print("Unknown token: please ensure your assemly code is written in the format 'OPCODE OPERAND'")
    elif (tokens[0] not in instructions):
        print("Error: Your opcode is not a valid instruction- please keep it simple :()")
    elif ((tokens[0] in instructions[4:8]) and tokens[1] >(len(memory) -1)) :
        print("Error: Please forgive us, we only have 6 memory locations at the moment")
    
    else: 
        #these are immediate memory addressing modes
        if tokens[0] == "MOVE":
            accumulator = tokens[1]
        elif tokens[0] == "ADD":
            accumulator += tokens[1]
        elif tokens[0] == "SUB":
            accumulator -= tokens[1]
        elif tokens[0] == "AND":
            accumulator  &= tokens[1]
                
        
        #These are absolute addressing modes
        elif tokens[0] == "LOAD":
            accumulator = memory[tokens[1]]
        elif tokens[0] == "STORE": 
            memory[tokens[1]] = accumulator
        elif tokens[0] == "ADDM":
            accumulator += memory[tokens[1]]
        elif tokens[0] == "SUBM":     
            accumulator  &= tokens[1] 
        
        line_num += 1
            
        #These are direct addressing modes 
        #In this case, the line number being incremented will be overriden
        if tokens[0] == "JUMP":   
            line_num= tokens[1]-1
            
           
        elif tokens[0] == "JUMPZ":  
            if accumulator == 0:
                line_num= tokens[1]-1
                
        elif tokens[0] == "JUMPNZ":  
            if accumulator != 0:
                line_num= tokens[1]-1
            

print("Accumulator:" ,accumulator, ", Memory:" , memory)