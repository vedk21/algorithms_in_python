'''
    Solution to Tower of Hanoi problem using recursion
'''

def tower_of_hanoi(number_of_disks, source_tower, dest_tower, aux_tower):
    # if there are only one disk left in tower, add it to dest_tower
    if (number_of_disks == 1):
        dest_tower.append(source_tower.pop())
        return

    # solve problem for n-1 disks, moving disk from source to aux tower
    tower_of_hanoi(number_of_disks - 1, source_tower, aux_tower, dest_tower)

    # add disk to dest_tower
    dest_tower.append(source_tower.pop())

    # move remaining n-1 disk in aux_tower to dest_tower
    tower_of_hanoi(number_of_disks - 1, aux_tower, dest_tower, source_tower)

    return dest_tower

if __name__ == '__main__':
    print('Tower of hanoi problem')
    source_tower = [i for i in range(20, 0, -1)]
    print(f'Source Tower: {source_tower}')
    dest_tower = []
    aux_tower = []
    print(f'Destination Tower: {tower_of_hanoi(len(source_tower), source_tower, dest_tower, aux_tower)}')
