# -*- coding: utf-8 -*-
"""
tile.py
__name__: wangchongbin
__pkuid__: 1800011716
__email__: 1800011716@pku.edu.cn
"""

import turtle
import copy



def input_inf():
    '''the founction is used for inputing the information
    wall: a list, a storage of the size of the wall(width and length)
    brick: a list, a storage of the size of the brick (width and length)
    '''
    
    global wall
    global brick
    
    wall0 = input('please input the size of wall(saperate by space) ').split()
    brick0 =input('please input the size of wall(saperate by space) ').split()
    wall = list(map(int, wall0))
    brick = list(map(int, brick0))
    print('wall = ', wall)
    print('brick = ', brick)


def conflict(index, case, state):
    '''the founction is used to check whether 'index' can be filled with tile 
    if there are some conflicts, it return True; if 'index' is empty, it return 
    False
    index: refer to current position, we will start from here
    case: state of the wall, if 'index' position is 1, there has been filled
    state: refer to the two different ways to use the brick
    '''
    
    if index % wall[0] + brick[state] > wall[0]:
        #at the 'index' position, if the brick over the x direction, it will conflict 
        return True
    elif index // wall[0] + brick[1 - state] > wall[1]:
        #if the brick over the y direction, it will conflict
        return True
    else:
        for y in range(brick[1 - state]):
            for x in range(brick[state]):
                index2 = index + y * wall[0] + x
                if case[index2] == 1:
                    #if the area you want to fill have '1', it will conflict
                    return True
        return False


def fill(case, ans, index, alls = []):
    '''this founction is used for fill the wall and collect all the solutions
    case: the state of the wall
    ans: refer to one kind of method to fill the wall, the index of the area 
          that you filled by a brick will save in a tuple, the lists is consisted 
          of the tuples
    index: the current position in the wall
    alls: all the solution in list alls
    '''
    global n

    for i in range(int(index / 1.01), len(case)):
    #to find a empty position;
        if case[i] == 0:
            break
    else:
        if ans not in alls:
        #to avoid possibily repeated answer
            ans_copy = copy.deepcopy(ans)
            #we must use 'deepcopy' or ans will be changed 
            #in following procedures
			#it seems that 'deepcopy' will take a lot of time
            alls.append(ans_copy)
            return
            
    for state in range(2):
        if not conflict(i, case, state):
            block = tuple()
            block1 = []
            for y in range(brick[1 - state]):
                for x in range(brick[state]):
                    #index2 is the position of the wall you will fill
                    index2 = i + y * wall[0] + x
                    case[index2] = 1
                    block1.append(index2)
            block = tuple(block1)
            #make a tuple to represent the brick
            ans.append(block)
            fill(case, ans, i + brick[state], alls)
            #fill the next position
            for index2 in block:
            #reset your wall's state and try another situation
                case[index2] = 0
            ans.remove(block)


def fillthewall(all = []):
    '''this founction is used to give all the solution to this problem
    '''
    input_inf()
    if wall[0] * wall[1] % (brick[0] * brick[1]) == 0:
        ans = []
        index = 0
        case = [0] * wall[0] * wall[1]
        fill(case, ans, index, all)
        if all == []:
            print('sorry, your brick could not cover the whole wall')
        else:
            cnt = 0
            for i in all:
                print(i)
                cnt += 1
            print('you have', cnt, 'methods')
            return True
    else:
        print('sorry, your brick could not cover the whole wall')
        return False

def draw_edge():
    '''this founction is used to draw the edge of the wall
    '''
    global s
    global times
    
    s = turtle.Screen()
    s.delay(0)
    t = turtle.Turtle()
    t.color('green')
    
    times = 400 / wall[0]
    t.penup()
    x, y = - wall[0] * times / 2, wall[1] * times / 2
    t.goto(x, y)
    t.pendown()
    for i in range(2):
        for length in wall:
            t.forward(length * times)
            t.right(90)
    t.hideturtle()


def draw_square():
    '''this founction is used to draw all the 'squares' on the screen
    and draw their number
    '''
    
    t = turtle.Turtle()
    t.color('grey')

    for i in range(1, wall[0]):
        t.penup()
        x1, y1 = - wall[0] * times / 2 + i * times, wall[1] * times / 2
        t.goto(x1, y1)
        t.pendown()
        x2, y2 = - wall[0] * times / 2 + i * times, - wall[1] * times / 2
        t.goto(x2, y2)
    
    for i in range(1, wall[1]):
        t.penup()
        x1, y1 = - wall[0] * times / 2, wall[1] * times / 2 - i * times
        t.goto(x1, y1)
        t.pendown()
        x2, y2 = wall[0] * times / 2, wall[1] * times / 2 - i * times
        t.goto(x2, y2)
     
    for j in range(wall[1]):
        for i in range(wall[0]):
            x = - wall[0] * times / 2 + (i + 0.5) * times
            y = (wall[1] / 2 - (j + 0.5)) * times
            t.penup()
            t.goto(x, y)
            position = j * wall[0] + i
            t.write(position)
    t.hideturtle()

    
def draw_brick(all):
    '''this founction is used to draw the method you select, it will draw 
    all the brick on the wall
    all: refer to the list which contain all the methods 
    '''
    
    t = turtle.Turtle()
    t.color('green')
    t.pensize(5)
    num = s.numinput('select', 
                 'please input a number to select which method to display')
    while True:
        try:
            num = s.numinput('select', 
                 'please input a number to select which method to display')
            method = all[int(num) - 1]
            break
        except IndexError:
            print('Sorry, you do not have this method, please try another one')

    for brick in method:
        l = min(brick)
        r = max(brick)
        width = (r - l + 1) % wall[0] * times
        hight = (r - l) // wall[0] * times + times
        i = l % wall[0]
        j = l // wall[0]
        x = - wall[0] * times / 2 + i * times
        y = wall[1] * times / 2 - j * times
        t.penup()
        t.goto(x, y)
        t.pendown()
        for i in range(2):
            t.forward(width)
            t.right(90)
            t.forward(hight)
            t.right(90)
    t.hideturtle()


def display(all):
    draw_edge()
    draw_square()
    draw_brick(all)
    s.exitonclick()

def main():
    all = []
    yes = fillthewall(all)
    if yes == True:
        display(all)
    else:
        print('I can not display it for you (:-')
        print('please try other sizes')


if __name__ == '__main__':
    main()
