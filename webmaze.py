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
endNumber = 10000

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
print "enterRoom" + str(enterRoom)
exitRoom = roomNumberList[-1]
print "exitRoom" + str(exitRoom)

roomNumberPath = roomNumberList[:]

watchNumber = 1 #debugging

for each in roomNumberList:
    
	doorList = []
	doorList = generateDoors(doorList,startNumber,endNumber,minNumberofDoors,maxNumberofDoors)

	try:
		pathDoor = roomNumberPath.pop(1)
		doorList.append(pathDoor)
	except IndexError:
		pass
    
	room = "rooms/room" + str(each) + ".html"
	file = open(room,"w+")
	if each == enterRoom:
		file.write("WELCOME TO THE MAZE<br />")
		print "Enter " + str(each) + "."
	if each == exitRoom:
		file.write("YOU WIN!<br />")
		print "Exit " + str(each) + "."
        
	random.shuffle(doorList)
        
	for door in doorList:
		aHrefElement = '<a href="room' + str(door) + '.html">A door leads out of this room.</a>'
		file.write(aHrefElement)
		file.write("</br>")
	file.close()

	watchTest = watchNumber/1000.0 #debugging
	if watchTest%1 == 0: #debugging
		print watchNumber #debugging
	watchNumber = watchNumber + 1 #debugging
