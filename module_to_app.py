'''

席替えアプリ 2/2
３番めに作ったもの。シンプルにしている。

'''



import random


# 空のseat_noと、join_memberの配列をあらかじめ作る
def changing_seat(join_members):
    print('2019年 Python編\n\n')

    random.shuffle(join_members)

    print('---右側の席(1~4)---')
    for i in range(0, 4):
        print(f'{i + 1}. {join_members[i]}')
    print('')

    print('---左側の席(5~8)---')
    for i in range(4, 8):
        print(f'{i + 1}. {join_members[i]}')
    print('')

    print('---左側の席(9~14)---')
    for i in range(8, 14):
        print(f'{i + 1}. {join_members[i]}')
