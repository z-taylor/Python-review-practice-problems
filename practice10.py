import random
def cardList(titles, numbers):
    list = []
    for title in titles:
        for number in numbers:
            list.append(f"{number} of {title}")
    return list
def shuffleCards(cardList):
    for i in range(50):
        position1 = random.randint(0, 51)
        position2 = random.randint(0, 51)
        cardList[position1], cardList[position2] = cardList[position2], cardList[position1]
    return cardList
numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
titles = ["Hearts", "Clubs", "Diamonds", "Spades"]
cardDeckUnshuffled = cardList(titles, numbers)
print(shuffleCards(cardDeckUnshuffled))