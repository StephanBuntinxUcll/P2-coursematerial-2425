

# class Person:
#     def __init__(self, *, name ,age):
#         self.name = name
#         self.age = age

# class Card:
#     def __init__(self,*,value,suit):
#         self.value = value
#         self.suit = suit


# def age(person):
#     return person.age

# print(age(Person(name='John', age = 14)))

def group_by(xs, key_function):
    a = {}
    for i in xs:
        z = []
        for n in xs:
            if key_function(i) == key_function(n):
                z.append(n)
            a[key_function(i)] = z

    return a




# print(group_by([
#     Person(name='John', age=14),
#     Person(name='Marc', age=17),
#     Person(name='Sophie', age=15),
#     Person(name='Chris', age=17),
#     Person(name='Morgan', age=15),
# ], age))


# def card_suit(card):
#     return card.suit


# print(group_by([
#     Card(value=2, suit='hearts'),
#     Card(value=5, suit='clubs'),
#     Card(value=4, suit='hearts'),
#     Card(value=10, suit='hearts'),
# ], card_suit))

# {
#     'hearts': [Card(value=2, suit='hearts'), Card(value=4, suit='hearts'), Card(value=10, suit='hearts')],
#     'clubs': [Card(value=5, suit='clubs')]
# }