# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:16:06 2022

@author: DELL
"""

env = [["Start", "", "Blocked"], ["", "", ""],["Fire", "", "Diamond"]]
line = 1
col = 1
def action(env, i, j):
    if canGo(env, i+1, j):
        moveTo(env, i+1, j)
    else:
        if canGo(env, i, j+1):
            moveTo(env, i, j+1)
        else:
            print("Stuck")
            exit()    
def canGo(env, i, j):
    #check if cell exists
    if i>len(env):
        return False
    if j>len(env[i-1]):
        return False
        
    #check if cell does not contain fire
    if env[i-1][j-1] == "Fire":
        return False
    
    #check if cell is not blocked
    if env[i-1][j-1] == "Blocked":
        return False
    
    #cell is clear
    return True
    
def moveTo(env, i, j):
    global line
    global col
    line = i
    col = j
       
#test if goal is reached
def goal(env, i, j):
    if env[i-1][j-1] == "Diamond":
        return True
    return False
    
while (not goal(env, line, col)):
    print("On cell(" + str(line) + ", " + str(col) + ")")
    action(env, line, col)
print("Finished on cell(" + str(line) + ", " + str(col) + ")")