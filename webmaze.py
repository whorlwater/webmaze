import random

def generateDoors(doorList,startNumber,endNumber,minNumberofDoors,maxNumberofDoors):
	numberofDoors = random.randrange(minNumberofDoors,maxNumberofDoors)
	i = 1
	while i <= numberofDoors:
		roomNumber = random.randrange(startNumber,endNumber)
		doorList.append(roomNumber)
		i = i + 1
	return doorList

#maze overall
startNumber = 1
endNumber = 100

#per room
minNumberofDoors = 2
maxNumberofDoors = 13


roomNumberList = []

i = startNumber

while i <= endNumber:
    roomNumberList.append(i)
    i = i + 1

random.shuffle(roomNumberList)

enterRoom = roomNumberList[0]
print 'enterRoom{0}'.format(str(enterRoom))
exitRoom = roomNumberList[-1]
print 'exitRoom{0}'.format(str(exitRoom))

roomNumberPath = roomNumberList[:]

watchNumber = 1 #debugging

for roomInt in roomNumberList:
    	roomStr = str(roomInt)
	doorList = []
	doorList = generateDoors(doorList,startNumber,endNumber,minNumberofDoors,maxNumberofDoors)

	try:
		pathDoor = roomNumberPath.pop(1)
		doorList.append(pathDoor)
	except IndexError:
		pass
    
	room = 'rooms/room{0}.html'.format(roomStr)
	file = open(room,'w+')
	roomMessage = '<div id="roomNumber">Room {0}</div><br />'.format(roomStr)
	file.write(roomMessage)

	if roomInt == enterRoom:
		file.write('<div id="message">WELCOME TO THE MAZE</div><br />')
		print 'Enter {0}.'.format(roomStr)
	elif roomInt == exitRoom:
		file.write('<div id="message">YOU WIN!</div><br />')
		print 'Exit {0}.'.format(roomStr)

	random.shuffle(doorList)
        
	for door in doorList:
		aHrefElement = '<a href="room{0}.html">A door leads out of this room.</a>'.format(str(door))
		file.write(aHrefElement)
		file.write('</br>')
	file.close()

	watchTest = watchNumber/1000.0 #debugging
	if watchTest%1 == 0: #debugging
		print watchNumber #debugging
	watchNumber = watchNumber + 1 #debugging
