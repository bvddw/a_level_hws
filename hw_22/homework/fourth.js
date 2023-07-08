function infoAboutRoom(roomsOnFloor, floors, roomNumber) {
    // consider the common floor, if all the entrances were on top of each other
    let globalFloorNumber = (roomNumber % roomsOnFloor) ? (roomNumber - roomNumber % roomsOnFloor) / roomsOnFloor + 1 : roomNumber / roomsOnFloor
    // find the entrance number, dividing by the number of floors
    const porch = (globalFloorNumber % floors) ? (globalFloorNumber - globalFloorNumber % floors) / floors + 1 : globalFloorNumber / floors
    console.log('porch: ' + porch)
    // we find the floor number, looking at the remainder when dividing by the number of floors in the entrance
    const floor = (globalFloorNumber % floors) ? (globalFloorNumber % floors) : floors
    console.log('floor: ' + floor)
}

/*
infoAboutRoom(3, 9, 456)
porch: 17
floor: 8
 */