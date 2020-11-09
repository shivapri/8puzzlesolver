import numpy as np
from numpy import *

initial_state=[]
print("Enter the input matrix")
for i in range(0, 3, 1):
    c = []
    for j in range(0, 3, 1):
         axisval = 0
         pr = input("Enter the value at row " + str(i)+" column "+str(j)+" of 8 puzzle")
         c.append(pr)
    initial_state.append(c)
print("Enter the solution matrix")
goal_state = []
for i in range(0, 3, 1):
    c = []
    for j in range(0, 3, 1):
         axisval = 0
         pr = input("Enter the value at row " + str(i)+" column "+str(j)+" of 8 puzzle")
         c.append(pr)
    goal_state.append(c)
print("The initial state is ")
for i in range(0,3,1):
    for j in range(0,3,1):
        print(initial_state[i][j],end=" ")
    print()
print("The goal state is ")
for i in range(0,3,1):
    for j in range(0,3,1):
        print(goal_state[i][j],end=" ")
    print()


def func(a,b):
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if(a[i][j]!=b[i][j]):
                return "Not same"
                break
    return "same"
def checkCost(a,b):
    cost = 0
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            if (a[i][j] != b[i][j]):
                cost =cost + 1
    return cost
def checkPosition(goal):
    new_goal_state = np.array(goal)
# new_goal_state = new_goal_state.reshape(-1,1)
    a,b = np.where(new_goal_state=='_')
    str = ''
    if(a[0]==1 and b[0]==1):
        str = "centre"
    elif(a[0]==0 and b[0]==0):
        str = "extreme up left"
    elif(a[0]==0 and b[0]==2):
        str = "extreme up right"
    elif(a[0]==2 and b[0]==0):
        str = "extreme down left"
    elif(a[0]==2 and b[0]==2):
        str = "extreme down right"
    elif(b[0]==0):
        str = "extreme left"
    elif(b[0]==2):
        str =  "extreme right"

    elif(a[0]==0):
        str = "up"
    elif(a[0]==2):
        str = "down"
    return str
# print(checkPosition(initial_state))
if(initial_state == goal_state):
    print("puzzle found")
    for i in range(0, 3, 1):
        for j in range(0, 3, 1):
            print(initial_state[i][j], end=" ")
        print()

else:
    current_state = initial_state
    new_current_state = current_state
    iter = 0
    while(new_current_state!=current_state or new_current_state!=goal_state):
        # print("Hi entered")
        cost_left=10
        cost_right = 10
        cost_up =10
        cost_down=10
        if(checkPosition(new_current_state)=="centre"):
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] + 1]
                work_current_state[a[0]][b[0] + 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_right = checkCost(work_current_state,goal_state)
               
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] - 1]
                work_current_state[a[0]][b[0] - 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_left = checkCost(work_current_state,goal_state)
                
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]-1][b[0]]
                work_current_state[a[0]-1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_up = checkCost(work_current_state,goal_state)
                # print("turn up")
                # new_goal_state = np.array(goal_state)
                # #down
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]+1][b[0]]
                work_current_state[a[0]+1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_down = checkCost(work_current_state, goal_state)
                
        elif(checkPosition(new_current_state)=="extreme up left"):
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] + 1]
                work_current_state[a[0]][b[0] + 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_right = checkCost(work_current_state, goal_state)
               
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] + 1][b[0]]
                work_current_state[a[0] + 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_down = checkCost(work_current_state, goal_state)
        elif(checkPosition(new_current_state)=="extreme up right"):
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] - 1]
                work_current_state[a[0]][b[0] - 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_left = checkCost(work_current_state, goal_state)
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] + 1][b[0]]
                work_current_state[a[0] + 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_down = checkCost(work_current_state, goal_state)
        elif(checkPosition(new_current_state)=="extreme down left"):
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] - 1][b[0]]
                work_current_state[a[0] - 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_up = checkCost(work_current_state, goal_state)
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] + 1]
                work_current_state[a[0]][b[0] + 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_right = checkCost(work_current_state, goal_state)
        elif(checkPosition(new_current_state)=="extreme down right"):
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] - 1]
                work_current_state[a[0]][b[0] - 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_left = checkCost(work_current_state, goal_state)
                
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] - 1][b[0]]
                work_current_state[a[0] - 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_up = checkCost(work_current_state, goal_state)
                
        elif(checkPosition(new_current_state)=="extreme left"):
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] - 1][b[0]]
                work_current_state[a[0] - 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_up = checkCost(work_current_state, goal_state)
                
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] + 1][b[0]]
                work_current_state[a[0] + 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_down = checkCost(work_current_state, goal_state)
                
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] + 1]
                work_current_state[a[0]][b[0] + 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_right = checkCost(work_current_state, goal_state)
                
        elif(checkPosition(new_current_state)=="extreme right"):
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] - 1][b[0]]
                work_current_state[a[0] - 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_up = checkCost(work_current_state, goal_state)
               
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] + 1][b[0]]
                work_current_state[a[0] + 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_down = checkCost(work_current_state, goal_state)
               
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] - 1]
                work_current_state[a[0]][b[0] - 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_left = checkCost(work_current_state, goal_state)
               
        elif(checkPosition(new_current_state)=="up"):
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] + 1]
                work_current_state[a[0]][b[0] + 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_right = checkCost(work_current_state, goal_state)
          
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] - 1]
                work_current_state[a[0]][b[0] - 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_left = checkCost(work_current_state, goal_state)
                
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] + 1][b[0]]
                work_current_state[a[0] + 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_down = checkCost(work_current_state, goal_state)
                
        elif(checkPosition(new_current_state)=="down"):
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] + 1]
                work_current_state[a[0]][b[0] + 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_right = checkCost(work_current_state, goal_state)
                
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0]][b[0] - 1]
                work_current_state[a[0]][b[0] - 1] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_left = checkCost(work_current_state, goal_state)
                
                work_current_state = np.array(new_current_state)
                a, b = np.where(work_current_state == '_')
                temp = work_current_state[a[0] - 1][b[0]]
                work_current_state[a[0] - 1][b[0]] = '_'
                work_current_state[a[0]][b[0]] = temp
                cost_up = checkCost(work_current_state, goal_state)
                




        iter = iter+1
        l = (cost_left,cost_right,cost_up,cost_down)
        X = l.index(min(l))
        p= [x for x in l if x==l[X]]
        if(iter>50 and len(p)>1):
            break
        work_current = []
        print(l)
        for i in range(0, 3, 1):
            c = []
            for j in range(0, 3, 1):
                c.append(work_current_state[i][j])
            work_current.append(c)
        print(work_current)
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                print(work_current[i][j], end=" ")
            print()
        l = (cost_left, cost_right, cost_up, cost_down)
        X = l.index(min(l))
        if(X==0):
            print("chosen left")
            work_current_state = np.array(new_current_state)
            a, b = np.where(work_current_state == '_')
            temp = work_current_state[a[0]][b[0] - 1]
            work_current_state[a[0]][b[0] - 1] = '_'
            work_current_state[a[0]][b[0]] = temp
            work_current = []
            for i in range(0, 3, 1):
                c = []
                for j in range(0, 3, 1):
                    c.append(work_current_state[i][j])
                work_current.append(c)
            current_state = new_current_state
            new_current_state = work_current
        elif(X==1):
            print("chosen right")
            work_current_state = np.array(new_current_state)
            a, b = np.where(work_current_state == '_')
            temp = work_current_state[a[0]][b[0] + 1]
            work_current_state[a[0]][b[0] + 1] = '_'
            work_current_state[a[0]][b[0]] = temp
            work_current = []
            for i in range(0, 3, 1):
                c = []
                for j in range(0, 3, 1):
                    c.append(work_current_state[i][j])
                work_current.append(c)
            current_state = new_current_state
            new_current_state = work_current
        elif(X==2):
            print("chosen up")
            work_current_state = np.array(new_current_state)
            a, b = np.where(work_current_state == '_')
            temp = work_current_state[a[0] - 1][b[0]]
            work_current_state[a[0] - 1][b[0]] = '_'
            work_current_state[a[0]][b[0]] = temp
            # cost_up = checkCost(work_current_state, goal_state)
            work_current = []
            for i in range(0, 3, 1):
                c = []
                for j in range(0, 3, 1):
                    c.append(work_current_state[i][j])
                work_current.append(c)
            current_state = new_current_state
            new_current_state = work_current

        if(X==3):
            print("chosen down")
            work_current_state = np.array(new_current_state)
            a, b = np.where(work_current_state == '_')
            temp = work_current_state[a[0] + 1][b[0]]
            work_current_state[a[0] + 1][b[0]] = '_'
            work_current_state[a[0]][b[0]] = temp
            # cost_down = checkCost(work_current_state, goal_state)
            work_current = []
            for i in range(0, 3, 1):
                c = []
                for j in range(0, 3, 1):
                    c.append(work_current_state[i][j])
                work_current.append(c)
            current_state = new_current_state
            new_current_state =work_current
print("The solution for the puzzle is ")
for i in range(0,3,1):
    for j in range(0,3,1):
        print(new_current_state[i][j],end=" ")
    print()
