import stddraw
import random
import pygame
from picture import Picture

def clicklocation(x, y,lent):
    grid = []
    length = lent
    reps = -1
    count = 0
    while reps < (y - 1):
        reps += 1
        for i in range(x):
            count += 1
            grid.append([-length + 1 * i, length + 1 * i, -length - 1 * reps, length - 1 * reps, count])
    return grid  

def gridmaker(x,y):
    grid = []
    reps = -1
    while reps < y:
        reps += 1
        if reps < y:
            for i in range(0,x):
                temp = random.randrange(1,3)
                grid.append([i , -reps , temp, ((reps *x) + (i+1))])
    return grid           

def checker(playing_field,x,y,clickcoords, clicklocal):
    checkmath = [1, -1, x, -x]
    complist = []
    oglist = []
    found = False
    valid = False
    
    for i in range(0,4,2):
        found = False
        reps = -1
        while found == False and not reps >= (x*y - 1):
            reps += 1
            if clicklocal[reps][0] < clickcoords[i] < clicklocal[reps][1] and clicklocal[reps][2] < clickcoords[i + 1] < clicklocal[reps][3]:
                complist.append(playing_field[reps])
                oglist.append(reps)
                found = True

    if found == True and len(complist) == 2:
        for i in range(4):
            if i < 2:
                if complist[0][3] + checkmath[i] == complist[1][3] and complist[1][1] == complist[0][1]:
                    valid = True   
            if i >= 2:
                if complist[0][3] + checkmath[i] == complist[1][3]:
                    valid = True
      
        if valid == True:
        
            switch1 = complist[0][2]
            switch2 = complist[1][2]
            complist[0][2] = switch2
            complist[1][2] = switch1
            

            for i in range(2):
               playing_field[oglist[i]] = complist[i]


    return playing_field

def mathmaster(math,x,y):
    temp = []
    if math == 1:
        temp = [y , x - 1, x, 0, 0]
        return temp

    if math == 2:
        temp = [x , y - 1, 1, x-1]
        return temp

def connectcheck(playing_field, x , y):
    math = 0
    totalconnectionlist = []
    for i in range(2):
        math += 1
        temp = mathmaster(math,x,y)
        mathreps = temp[0]
        mathsets = temp[1]
        repmove = temp[2]
        start = temp[3]
        reps = -1
        
        while reps < mathsets:
            reps += 1
            if reps <= mathsets:
                connectionlist = []
                for i in range(mathreps):
                    xy = playing_field[reps + (start * reps) + (i * repmove)]
                    connectionlist.append(xy)
                totalconnectionlist = leapfrog(connectionlist,totalconnectionlist,math)

    if len(totalconnectionlist) > 0:
        return True
    
    return False
    
           
def connectsearch(playing_field, x , y,totalscore):
    math = 0
    totalconnectionlist = []
    for i in range(2):
        math += 1
        temp = mathmaster(math,x,y)
        mathreps = temp[0]
        mathsets = temp[1]
        repmove = temp[2]
        start = temp[3]
        reps = -1
        
        while reps < mathsets:
            reps += 1
            if reps <= mathsets:
                connectionlist = []
                for i in range(mathreps):
                    xy = playing_field[reps + (start * reps) + (i * repmove)]
                    connectionlist.append(xy)
                totalconnectionlist = leapfrog(connectionlist,totalconnectionlist,math)

    temp = eliminator(playing_field, totalconnectionlist)
    playing_field = temp[0]
    totalscore += temp[1]
    return [playing_field,totalscore]

def leapfrog(connectionlist,totalconnectionlist,math):
    templist = []

    for i in range(len(connectionlist)):
        templist.append(connectionlist[i])
        if i < len(connectionlist) - 1:
            if not connectionlist[i][2] == connectionlist[i + 1][2]:
                if len(templist) >= 3:
                    totalconnectionlist.append(templist)
                    templist = []

                elif len(templist) < 3:
                    templist = []
    if len(templist) >= 3:
        totalconnectionlist.append(templist)
        templist = []

    return totalconnectionlist

def eliminator(playing_field, totalconnectionlist):
    score = 0
    for i in range(len(totalconnectionlist)):
        temp = totalconnectionlist[i]
        score += 10*len(temp)
        for i in range(len(temp)):
            bigh = -1
            temp1 = temp[i]
            found = False
            while not found == True:
                bigh += 1
                if temp1[3] == playing_field[bigh][3]:
                    playing_field[bigh][2] = 0
                    found = True
    
    return [playing_field, score]
                
def gravity(playing_field,x,y,lent,totalscore,finalscore,clickcoords,clicklocal,attempts,level,background,win):
    zcount = 0
    done = False
    for i in range(x * y - 1, x * y - x, -1):
        reps1 = -1
        zcount = 0
        while done == False:
            reps1 += 1
            if playing_field[i - reps1 *x][2] == 0 and reps1 < y - 1:
                playing_field[i + reps1 *x][2] = playing_field[i - reps1 *x][2]
                playing_field[i - reps1 *x][2] = 0
                display(playing_field,x,y,lent,totalscore,finalscore,clickcoords,clicklocal,attempts,level,background,win)
            if not reps1 < y - 1:
                done = True
            

                    
    
    return playing_field

def reset(playing_field,x,y):
    done = False
    while done == False:
        count = 0
        for i in range(x):
            if playing_field[i][2] == 0:
                count = 1
                playing_field[i][2] = random.randrange(1,7)
        if count == 0:
            done = True
    return playing_field

def image(background):
    if background == 1:
        jim = Picture('jimmy.jpg')
        stddraw.picture(jim)
    if background == 2:
        jim = Picture('a.png')
        stddraw.picture(jim)
    if background == 3:
        jim = Picture('b.png')
        stddraw.picture(jim)
    if background == 4:
        jim = Picture('c.png')
        stddraw.picture(jim)
    if background == 5:
        jim = Picture('d.png')
        stddraw.picture(jim)
    if background == 6:
        jim = Picture('e.png')
        stddraw.picture(jim)
    if background == 7:
        jim = Picture('f.png')
        stddraw.picture(jim)
    if background == 8:
        jim = Picture('g.png')
        stddraw.picture(jim)
    if background == 9:
        jim = Picture('h.png')
        stddraw.picture(jim)
    if background == 10:
        jim = Picture('i.png')
        stddraw.picture(jim)
    if background == 11:
        jim = Picture('j.png')
        stddraw.picture(jim)
    if background >= 12:
        jim = Picture('k.png')
        stddraw.picture(jim)

def display(playing_field,x,y,lent,totalscore,finalscore,clickcoords,clicklocal,attempts,level,background,win):
    stddraw.clear()
    image(background)
    stddraw.setXscale(-lent, (2* lent * x) - lent)
    stddraw.setYscale(-(2* lent * y) - 4* lent, lent)
    stddraw.setPenColor(stddraw.PINK)
    stddraw.filledRectangle(-lent,-(2* lent * y) - 4* lent,(2* lent * x),5* lent)
    stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
    stddraw.filledRectangle(-lent ,-(2* lent * y) - 3* lent,(2* lent * x),lent)
    stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
    stddraw.filledRectangle(-lent ,-(2* lent * y) - 1.5 * lent,(2* lent * x),lent)
    stddraw.setPenColor(stddraw.GRAY)
    stddraw.filledRectangle(-lent ,-(2* lent * y) - 2.2 * lent,(2* lent * x),lent)
    if totalscore < finalscore:
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.filledRectangle(-lent ,-(2* lent * y) - 2.2 * lent,((2* lent * x) - lent)/1.7 * (totalscore/finalscore),lent)
    if totalscore >= finalscore:
        stddraw.setPenColor(stddraw.GREEN)
        stddraw.filledRectangle(-lent ,-(2* lent * y) - 2.2 * lent,((2* lent * x) - lent),lent)
    stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
    stddraw.filledRectangle(x * lent + lent ,-(2* lent * y) - 3.5* lent,(lent * x),3.5* lent)
    stddraw.setPenRadius(0.010)
    stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
    stddraw.rectangle(-lent,-(2* lent * y) - 4* lent,(2* lent * x),5* lent)
    stddraw.setFontSize(25)
    stddraw.setPenColor(stddraw.DARK_GREEN)
    stddraw.text((((2* lent * x) - lent)/1.3 ),-((2* lent * y) + lent),'Points: ' + str(totalscore) + ' / ' + str(finalscore))
    stddraw.setPenColor(stddraw.RED)
    stddraw.setFontSize(20)
    stddraw.text((((2* lent * x) - lent) /1.3),-((2* lent * y) + 2.7* lent),'Attempts Left: ' + str(attempts))
    stddraw.setPenColor(stddraw.BLUE)
    stddraw.setFontSize(25)
    stddraw.text((((2* lent * x) - lent) / 20),-((2* lent * y) - 0.08* lent),'Level: ' + str(level))
    for i in range(len(clickcoords) - 1):
        found = False
        reps = -1
        while found == False and not reps >= (x*y - 1) :
            reps += 1
            if clicklocal[reps][0] < clickcoords[i] < clicklocal[reps][1] and clicklocal[reps][2] < clickcoords[i + 1] < clicklocal[reps][3]:
                spotx = playing_field[reps][0]
                spoty = playing_field[reps][1]
                stddraw.setPenColor(stddraw.DARK_RED)
                stddraw.setPenRadius(0.05)
                stddraw.filledSquare(spotx,spoty,lent)
                found = True
   
    for i in range(x * y):
        spotx = playing_field[i][0]
        spoty = playing_field[i][1]
        
        if playing_field[i][2] == 1:

            stddraw.setPenColor(stddraw.MAGENTA)
            stddraw.setPenRadius(0.05)
            stddraw.filledCircle(spotx,spoty,lent / 1.2)

        if playing_field[i][2] == 2:
            stddraw.setPenColor(stddraw.YELLOW)
            stddraw.setPenRadius(0.05)
            stddraw.filledSquare(spotx,spoty,lent / 1.2)
        
        if playing_field[i][2] == 3:
            stddraw.setPenColor(stddraw.BLUE)
            stddraw.setPenRadius(0.05)
            stddraw.filledPolygon([(spotx-lent) + 0.2, (spotx-lent) + 0.3, (spotx-lent) + 0.7, (spotx-lent) + 0.9, 
                (spotx-lent) + 0.6], [ (spoty-lent) + 0.6, (spoty-lent) + 0.9, (spoty-lent) + 0.9, (spoty-lent) + 0.6, (spoty-lent) + 0.1])
        
        if playing_field[i][2] == 4:
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.setPenRadius(0.05)
            stddraw.filledPolygon([(spotx-lent) + 0.1, (spotx-lent) + 0.4, (spotx-lent) + 0.9, (spotx-lent) + 0.4,], 
                [ (spoty-lent) + 0.4, (spoty-lent) + 0.1, (spoty-lent) + 0.4, (spoty-lent) + 0.9])

        if playing_field[i][2] == 5:
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.setPenRadius(0.05)
            stddraw.filledPolygon([(spotx-lent) + 0.5, (spotx-lent) + 0.1,(spotx-lent) + 0.9], [ (spoty-lent) + 0.8,(spoty-lent) + 0.1, (spoty-lent) + 0.1])
           
        if playing_field[i][2] == 6:
            stddraw.setPenColor(stddraw.CYAN)
            stddraw.setPenRadius(0.05)
            stddraw.filledPolygon([(spotx-lent) + 0.5, (spotx-lent) + 0.1,(spotx-lent) + 0.9,(spotx-lent) + 0.3,(spotx-lent) + 0.6 ], [ (spoty-lent) + 0.9,(spoty-lent) + 0.7, (spoty-lent) + 0.7,(spoty-lent) + 0.1, (spoty-lent) + 0.1])
    
    if attempts == 0 and totalscore < finalscore:
        while stddraw.mousePressed() == False:
            stddraw.setPenColor(stddraw.BLACK)
            stddraw.filledRectangle(-lent,-( lent * y) - 2* lent,(2* lent * x),3.5* lent)
            stddraw.setFontSize(40)
            stddraw.setPenColor(stddraw.RED)
            stddraw.text(lent * x - lent,-( lent * y),'YOU LOSE, CLICK TO EXIT')
            stddraw.show(0)
            if stddraw.mousePressed() == True:
                win = True
                return win

    if totalscore >= finalscore:
        while stddraw.mousePressed() == False:
            stddraw.setPenColor(stddraw.BOOK_BLUE)
            stddraw.filledRectangle(-lent,-( lent * y) - 2* lent,(2* lent * x),3.5* lent)
            stddraw.setFontSize(40)
            stddraw.setPenColor(stddraw.GREEN)
            stddraw.text(lent * x - lent,-( lent * y),'YOU WIN, CLICK TO PROCEED')
            stddraw.show(0)
            if stddraw.mousePressed() == True:
                win = False
                return win
    stddraw.show(250)
    return win



def master_function():
    win = False
    level = 0
    background = 0
    #while win == False:
    background += 1
    level += 1
    x = random.randrange(7,15)
    y = random.randrange(9,17)
    lent = 0.5
    clicklocal = clicklocation(x, y,lent)
    playing_field = gridmaker(x,y)
    count = 0
    finalscore = (x*y*10)
    totalscore = 0
    clickcoords = []
    attempts = random.randrange(12,16)
    temp = connectsearch(playing_field, x , y,totalscore)
    playing_field = temp[0]
    display(playing_field,x,y,lent,totalscore,finalscore,clickcoords,clicklocal,attempts,level,background,win)

    playing_field = gravity(playing_field,x,y,lent,totalscore,finalscore,clickcoords,clicklocal,attempts,level,background,win)
    
    
        #playing_field = reset(playing_field,x,y)
        #isplay(playing_field,x,y,lent,totalscore,finalscore,clickcoords,clicklocal,attempts,level,background,win)
        
    '''
    while stddraw.mousePressed() == False:
        display(playing_field,x,y,lent,totalscore,finalscore,clickcoords,clicklocal,attempts,level,background,win)
        temp = connectsearch(playing_field, x , y,totalscore)
        playing_field = temp[0]
        totalscore = temp[1]
        playing_field = gravity(playing_field,x,y)
        playing_field = reset(playing_field,x,y)
        if attempts == 0 or totalscore >= finalscore:
            win = display(playing_field,x,y,lent,totalscore,finalscore,clickcoords,clicklocal,attempts,level,background,win)
            print('AA')
                break
            elif stddraw.mousePressed() == True:
                count += 1
                clickcoords.append(stddraw.mouseX())
                clickcoords.append(stddraw.mouseY())
                if count == 2:
                    playing_field = checker(playing_field,x,y,clickcoords, clicklocal)
                    test = connectcheck(playing_field, x , y)
                    if test == True:
                        attempts = attempts - 1
                        temp = connectsearch(playing_field, x , y,totalscore)
                        playing_field = temp[0]
                        totalscore = temp[1]
                    if test == False:
                        playing_field = checker(playing_field,x,y,clickcoords, clicklocal)
                    count = 0
                    clickcoords = []
    '''


master_function()