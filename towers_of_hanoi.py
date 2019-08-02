# def super_move_block(home, target, other):
#     move_block(home, other, target, 0)
#     move_block(home, target, other, 0)
#     move_block(other, target, home, 0)
#
#
# def super_super_move_block(home, target, other):
#     super_move_block(home, other, target, 1)
#     move_block(home, target, other, 0)
#     super_move_block(other, target, home, 1)
#
#
# def super_super_super_move_block(home, target, other, 3):
#     super_super_move_block(home, other, target, 2)
#     move_block(home, target, other, 0)
#     super_super_move_block(other, target, home, 2)
#
#
# def super_super_super_super_move_block(home, target, other, 4):
#     super_super_super_move_block(home, other, target, 3)
#     move_block(home, target, other, 0)
#     super_super_super_move_block(other, target, home, 3)


def blocks_print(l1, l2, l3):
    list1 = []
    list2 = []
    list3 = []
    for element in l1:
        list1.append(element)
    for element in l2:
        list2.append(element)
    for element in l3:
        list3.append(element)

    height = max(len(list1), len(list2), len(list3))
    for current_list in [list1, list2, list3]:
        while len(current_list) < height:
            current_list.append(0)
    width = max(max(list1), max(list2), max(list3))
    print_key = []
    for i in range(0, width + 1):
        print_key.append('# ' * i)
        print_key[i] = print_key[i].strip()
        print_key[i] = print_key[i].center(width*2 + 1, ' ')

    while len(list1) > 0:
        print(print_key[list1.pop()], print_key[list2.pop()], print_key[list3.pop()], sep=' ')
    print('\n')


def move_block(home, target):
    if [] != home:  # TODO: make prettier
        target.append(home.pop())
        blocks_print(L1, L2, L3)


def tower_of_hanoi(home, target, other, level):
    if level != 0:
        tower_of_hanoi(home, other, target, level - 1)
        tower_of_hanoi(home, target, other, 0)
        tower_of_hanoi(other, target, home, level - 1)
    else:
        move_block(home, target)


L1 = [3, 2, 1]
L2 = []
L3 = []

blocks_print(L1, L2, L3)

tower_of_hanoi(L1, L3, L2, len(L1))

