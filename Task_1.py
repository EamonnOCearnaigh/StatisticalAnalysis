# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:47:37 2021

@author: Éamonn Ó Cearnaigh

Programming & Mathematics for AI
Coursework Task 1
"""
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Selecting between game mode A and game mode B

def game_mode_selection():
    
    print("=-=-= GAME MODE SELECTION =-=-=\n")
    print("A - The time spent on a cell is the number on this cell.\n")
    print("B - The time spent on a cell is the absolute of the difference between the previous cell the agent was on and the current cell it is on.")
    
    selected = False
    while selected == False:
        
        game_mode = input("Select game mode (A/B): ").upper()
        
        if game_mode != "A" and game_mode != "B":
            print("\nInvalid option.  Game mode can be 'A' or 'B'.\n")
            
        else:
            print("Game mode selected.\n")
            selected = True
    
    return game_mode
    
# Selecting parameters for grid height, width, and n - the maximum integer for a cell    
    
def parameter_selection():
    
    print("=-=-= PARAMETER SELECTION =-=-=\n")
    
    #height = int(input("Grid height: "))
    #width = int(input("Grid width: "))
    #n = int(input("Max cell integer: "))
    
    height = 5
    width = 5
    n = 9
    
    game_parameters = height, width, n
    
    return game_parameters
    
def build_grid(game_parameters):
    
    print("=-=-= BUILDING GRID =-=-=\n")
    
    height = game_parameters[0]
    width = game_parameters[1]
    n = game_parameters[2]
    
    # Creating matrix
    matrix = np.random.randint(0, n, size=(width, height))
    print(matrix, "\n")
    
    # Agent spawns in upper-left corner cell
    agent_position = [0,0]
    agent_position_value = matrix[0][0]
    
    print("Agent position: {}\n".format(agent_position))
    print("Agent position value: {}\n".format(agent_position_value))
    
    # Destination is the bottom-right corner cell
    destination_position = [width-1, height-1]
    destination_position_value = matrix[width-1][height-1]
    
    print("Destination position: {}\n".format(destination_position))
    print("Destination position value: {}\n".format(destination_position_value))
    
    # Visualising matrix
    fig, ax = plt.subplots()
    ax.matshow(matrix, cmap=plt.cm.Blues)

    # Cell values
    for i in range(width):
        for j in range(height):
            c = matrix[j,i]
            ax.text(i, j, str(c), va='center', ha='center')
    
    return matrix, agent_position, destination_position
    
def baseline_path(game_mode, matrix, agent_position, destination_position):
    
    print("=-=-= BASELINE PATH =-=-=\n")
    
    destination_reached = False
    total_cost = 0
    
    while destination_reached == False:
        
        # If agent position matches destination position, end loop
        if agent_position == destination_position:
            print("Agent has reached destination\n")
            print("=-=-=-=-=-=-=-=-=-=\n")
            destination_reached = True
            continue
        
        # Moving diagonally towards destination
        # Comparing adjacent cells to choose whether to move right or down
        
        # Checking agent is not on right or bottom edge to avoid index error
        if agent_position[0] != destination_position[0] and agent_position[1] != destination_position[1]:
            
            # Checking cell to the right of agent against the cell below agent
            cell_right_position = [agent_position[0]+1, agent_position[1]]
            cell_right_position_value = matrix[agent_position[1]][agent_position[0]+1]
            print("Right position: {}\n".format(cell_right_position))
            print("Right position value: {}\n".format(cell_right_position_value))
            
            cell_down_position = [agent_position[0], agent_position[1]+1]
            cell_down_position_value = matrix[agent_position[1]+1][agent_position[0]]
            print("Down position: {}\n".format(cell_down_position))
            print("Down position value: {}\n".format(cell_down_position_value))
            
        else:
            # Agent is on edge
            
            # If agent at right edge, move down
            if agent_position[0] == destination_position[0]:
                print("Agent has hit right edge, moving down\n")
                print("=-=-=-=-=-=-=-=-=-=\n")
                
                cell_down_position = [agent_position[0], agent_position[1]+1]
                cell_down_position_value = matrix[agent_position[1]+1][agent_position[0]]
                print("Down position: {}\n".format(cell_down_position))
                print("Down position value: {}\n".format(cell_down_position_value))
                
                agent_position = cell_down_position
                agent_position_value = cell_down_position_value
                
                print("Agent position: {}\n".format(agent_position))
                print("Agent position value: {}\n".format(agent_position_value))
                continue
            
            # If agent at bottom edge, move right
            elif agent_position[1] == destination_position[1]:
                print("Agent has hit bottom edge, moving right\n")
                print("=-=-=-=-=-=-=-=-=-=\n")
                
                cell_right_position = [agent_position[0]+1, agent_position[1]]
                cell_right_position_value = matrix[agent_position[1]][agent_position[0]+1]
                print("Right position: {}\n".format(cell_right_position))
                print("Right position value: {}\n".format(cell_right_position_value))
                
                agent_position = cell_right_position
                agent_position_value = cell_right_position_value
                
                print("Agent position: {}\n".format(agent_position))
                print("Agent position value: {}\n".format(agent_position_value))
                continue
            
        # If right cell value < below cell value, move right
        if cell_right_position_value < cell_down_position_value:
            print("Agent moving right\n")
            print("=-=-=-=-=-=-=-=-=-=\n")
            
            agent_position = cell_right_position
            agent_position_value = cell_right_position_value
            
            print("Agent position: {}\n".format(agent_position))
            print("Agent position value: {}\n".format(agent_position_value))
        
        # If right cell value >= below cell value, move down
        elif cell_right_position_value >= cell_down_position_value:
            print("Agent moving down\n")
            print("=-=-=-=-=-=-=-=-=-=\n")
            
            agent_position = cell_down_position
            agent_position_value = cell_down_position_value
            
            print("Agent position: {}\n".format(agent_position))
            print("Agent position value: {}\n".format(agent_position_value))
        
        
        # Determine game mode
        if game_mode == "A":
            ...
            # Add cell value to cost accumulator
            #total_cost =+ agent_position_value
        
        elif game_mode == "B":
            
            ...
    
    
    
    
        


def dijkstra_path(game_mode):
    
    print("=-=-= DIJKSTRA PATH =-=-=\n")
    
    if game_mode == "A":
        ...
    
    elif game_mode == "B":
        ...
        
    else:
        print("dijkstra_path error\n")
        

def analysis():
    ...
    

def main():
    
    print("=-=-= BEGIN =-=-=\n")
    
    game_mode = game_mode_selection()
    game_parameters = parameter_selection()
    matrix, agent_position, destination_position = build_grid(game_parameters)
    baseline_path(game_mode, matrix, agent_position, destination_position)
    dijkstra_path(game_mode)

if __name__ == "__main__":
    main()
    
    