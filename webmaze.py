import random


startNumber = 1
endNumber = 10000

roomNumberList = []

i = startNumber

while i <= endNumber:
    roomNumberList.append(i)
    i = i + 1

random.shuffle(roomNumberList)

enterRoom = roomNumberList[0]
print "enterRoom" + str(enterRoom)
exitRoom = roomNumberList[-1]
print "exitRoom" + str(exitRoom)

roomNumberPath = roomNumberList[:]

for each in roomNumberList:
    
    doorList = []

    try:
        pathDoor = roomNumberPath.pop(1)
        doorList.append(pathDoor)
    except IndexError:
        pass
    randomDoor1 = random.randrange(startNumber,endNumber)
    doorList.append(randomDoor1)
    randomDoor2 = random.randrange(startNumber,endNumber)
    doorList.append(randomDoor2)

    
    room = "rooms/room" + str(each) + ".html"
    file = open(room,"w+")
    if each == enterRoom:
        file.write("WELCOME TO THE MAZE<br />")
        print "Enter " + str(each) + "."
    if each == exitRoom:
        file.write("YOU WIN!<br />")
        print "Exit " + str(each) + "."
        randomDoor3 = random.randrange(startNumber,endNumber)
        doorList.append(randomDoor3)
        
    a = 1
    while a < endNumber:
        b = random.randrange(0,1)
        if b == 1:
            random.shuffle(doorList)
        a = a + 1
        
    for door in doorList:
        aHrefElement = '<a href="room' + str(door) + '.html">A door leads out of this room.</a>'
        file.write(aHrefElement)
        file.write("</br>")
    file.close()
