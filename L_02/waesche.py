import array, json, sys

#-Clothes with dirty state True
clothes = {
    'jeans': True,
    'shirts': True,
    'socks': True
}

#-globals and helpers
washingRoomItems = {}
wardrobeItems = {}
washerState = False #True will exit the running programm - you can try!

def washingProcess(dictObj):
    for key, value in dictObj.items():
        dictObj[key] = False
    return dictObj

#-Collect clothes to washing room
washingRoomItems.update(clothes)
print(washingRoomItems) #self check

#-Check if the given machine is in use
if washerState is False:
    washingProcess(washingRoomItems)    #-every clothes item gets washed
else:
    sys.exit('Machine is in use!')

print(washingRoomItems) #self check

#-Clear out items for drying process 
clothes.update(washingRoomItems)
wardrobeItems.update(clothes)

print(clothes) #self check
print(wardrobeItems) #self check






















    







