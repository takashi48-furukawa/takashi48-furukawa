import random

class Player:
    def __init__(self, hands, name):
        self.hands = hands
        self.name = name
        self.hand = ''

    def random_select(self):
        self.hand = random.choice(list(self.hands.keys()))

    def select(self):
        while True:
            p_hand_input = input(f'{self.name}の手を入力してください (グー: 0, チョキ: 2, パー: 5, 終了: q): ')
            if p_hand_input.lower() == 'q':
                print('ゲームを終了します')
                exit()
            elif p_hand_input in self.hands.keys():
                self.hand = p_hand_input
                break
            else:
                print('想定外の手です。0, 2, 5, qのいずれかを入力してください。')

    def show(self):
        print(f'{self.name}の手: {self.hands[self.hand]}')

    def win_lose_check(self, enemy_hand):
        if (self.hand == '0' and enemy_hand == '2') or \
           (self.hand == '2' and enemy_hand == '5') or \
           (self.hand == '5' and enemy_hand == '0'):
            return True
        else:
            return False

# プレイヤーの手の辞書
hands = {'0': 'グー', '2': 'チョキ', '5': 'パー'}

# プレイヤーの作成
player = Player(hands, 'あなた')
enemy = Player(hands, '相手')

# ゲーム開始
print("Game Start")

while True:
    # プレイヤーの手を選択
    player.select()

    # 相手の手をランダムに選択
    enemy.random_select()

    # プレイヤーと相手の手を表示
    player.show()
    enemy.show()

    # 勝敗判定
    if player.hand == enemy.hand:
        print('Draw!!!')
    elif player.win_lose_check(enemy.hand):
        print('You Win!!!')
    else:
        print('You Lose!!!')