
# 一张扑克牌 ♠♥♦♣
class Card:

    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank

    #♠♤♥♡♣♧♦♢
    SUITS = [ '♧','♦','♤','♥' ]
    RANKS = [None,'3','4','5','6','7','8','9','10','J','Q','K','A','2']

    def __str__(self):
        return '%2s%s' % (Card.RANKS[self.rank],Card.SUITS[self.suit])

    #比较大小
    def __lt__(self, other):
        t1 = self.suit,self.rank
        t2 = other.suit,other.rank
        return t1 < t2

    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


# 一副扑克
class Poker:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                # print(Card(suit,rank))
                cardtemp = Card(suit, rank)
                self.cards.append(cardtemp)

    def __str__(self):
        res = []
        for card in self.cards:
            # print(card)
            res.append(str(card))
        return ','.join(res)

    # 出牌
    def pop_card(self):
        return self.cards.pop()

    # 回牌
    def add_card(self,card):
        self.cards.append(card)

    # 洗牌
    def shuffle(self):
        import random
        random.shuffle(self.cards)

    # 排序
    def sort(self):
        self.cards.sort()

    # 牌组发牌到另一个牌组

    def move_card(self,poker,num=1):
        for i in range(num):
            poker.add_card(self.pop_card())




# 手牌
# 手牌属于一个牌组，Hand类 继承 Poker类
class Hand(Poker):



    # 重写覆盖父类的构造方法
    def __init__(self,lable=''):
        self.cards=[]
        self.lable = lable

    # 显示牌组
    def show(self):
        print(self.lable,self)


# test==========

poker = Poker()
hand1 = Hand("张三")
hand2 = Hand("李四")
hand3 = Hand("王五")
hand4 = Hand("赵六")

poker.shuffle()

while poker.cards.__len__()>0:
    poker.move_card(hand1)
    poker.move_card(hand2)
    poker.move_card(hand3)
    poker.move_card(hand4)

hand1.sort()
hand2.sort()
hand3.sort()
hand4.sort()

hand1.show()
hand2.show()
hand3.show()
hand4.show()




