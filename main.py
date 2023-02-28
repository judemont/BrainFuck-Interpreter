#!/usr/bin/env python

import sys

try:
    code = open(sys.argv[1], "r").read() 
except:
    print("Please specify the path of the BrainFuck file")
    exit()



code = code.replace(" ", "").replace("\n", "").replace("\r", "")

pointer_index = 0

i=0
vars = [0]
while i < len(code):
    
 
    if code[i] == "[":
        boucle_pointer_index = pointer_index
        boucle_i = i
        while vars[boucle_pointer_index] != 0:
            
            i+=1
            
            if code[i] == "]":
                i = boucle_i
            else:
      
                
                            
                if pointer_index >= len(vars):
                    vars.append(0)
                
                ins = code[i]
                
                if ins == "<":
                    pointer_index -= 1

                elif ins == ">":
                    pointer_index += 1

                    
                
                elif ins == "+":
                    vars[pointer_index] += 1

                elif ins == "-":
                    vars[pointer_index] -= 1

                elif ins == ".":
                    print(chr(vars[pointer_index]), end="")

                elif ins == ",":
                    vars[pointer_index] = int(input())


    else:
        
        if pointer_index >= len(vars):
            vars.append(0)
        
        ins = code[i]
        
        if ins == "<":
            pointer_index -= 1

        elif ins == ">":
            pointer_index += 1

            
        
        elif ins == "+":
            vars[pointer_index] += 1

        elif ins == "-":
            vars[pointer_index] -= 1

        elif ins == ".":
            print(chr(vars[pointer_index]), end="")

        elif ins == ",":
            vars[pointer_index] = int(input())



    i+=1

