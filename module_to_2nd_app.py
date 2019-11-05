'''

2番めに作ったアプリ 1/2
1.席を 4, 4, 6 に分ける

'''

import random


class Members:
    def __init__(self):
        self.members = ['吉田力',
                        '田中潤',
                        '舞鶴翔',
                        '兼松智恵子',
                        '速水駿',
                        '徳田貴一',
                        '中野英磨',
                        '熊谷航',
                        '下川孝宣',
                        '柴田雅幸',
                        '山田いつき',
                        '塚田崇博',
                        '高橋通',
                        '望月ちかこ']

    def random(self):
        random.shuffle(self.members)

    def disply_members(self):

        print('---右側の席(1~4)---')

        for i in range(0, 4):
            print(f'{i + 1}. {self.members[i]}')

        print('---左側の席(5~8)---')

        for i in range(4, 8):
            print(f'{i + 1}. {self.members[i]}')

        print('---左側の席(9~14)---')

        for i in range(8, 14):
            print(f'{i + 1}. {self.members[i]}')
