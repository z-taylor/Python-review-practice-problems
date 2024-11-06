def cardList(titles, numbers):
    list = []
    for title in titles:
        for number in numbers:
            list.append(f"{number} of {title}")
    return list
numbers = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
titles = ["Hearts", "Clubs", "Diamonds", "Spades"]
print(cardList(titles, numbers))
