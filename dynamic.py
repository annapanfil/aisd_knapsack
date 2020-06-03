import numpy as np

def createMatrix(capacity: int, weights: list, values: list):
    # Tworzy macierz. Kolumnami są kolejne pojemności plecaka, wierszami – kolejno dodawane przedmioty.
    # W komórkach macierzy są zapisane maksymalne wartości przedmiotów w plecaku.
    n = len(values)

    # indeksy w tej macierzy są przesunięte względem list weights i values –
    # – w 0. wierszu znajduje się zero przedmiotów,
    # w 1. wierszu jest jeden przedmiot,(zerowy) w 2. wierszu – 2 przedmioty (0. i 1.) itd.
    mtrx = np.zeros([n+1, capacity+1])

    for item in range(1, n+1):
        item_weight = weights[item-1]
        item_value = values[item-1]

        for cap in range(1, capacity+1): # zaczynamy od 1, bo do plecaka o pojemności 0 przedmiot się nie zmieści
            if(cap-item_weight>-1): # czy przedmiot się mieści
                mtrx[item][cap] = max(mtrx[item-1][cap], mtrx[item-1][cap-item_weight]+item_value) # czy zwiększa wartość plecaka
            else:
                # przepisujemy z poprzedniego wiersza
                mtrx[item][cap] = mtrx[item-1][cap]
    return mtrx


def readSolution(mtrx: list, values: list):
    # odczytuje rozwiązanie z uprzednio utworzonej tabeli
    knapsack_val = 0
    taken = []
    rows = len(mtrx)
    cols = len(mtrx[0])

    # mając wartość przedmiotów, które zabrał określa numery przedmiotów, które się na tę wartość składają
    to_uncover = max(mtrx[rows-1])

    item = rows-1   # numeracja od 1

    while to_uncover > 0:
        while to_uncover in mtrx[item-1]:
            item -=1

        # dodaj element do zabranych, usuń jego wartość z wartości do odkrycia
        taken.append(item)
        knapsack_val += values[item-1] # numeracja od 0
        to_uncover -= values[item-1]
        # print("Take", item, "\nCurrent knapsack value:", knapsack_val, ", left to uncover:", to_uncover)
        item -=1

    return (knapsack_val, taken)


def mainDynamic(capacity: int, weights: list, values: list):
    # capacity – pojemność plecaka, weights – wagi przedmiotów, values – wartości przedmiotów
    mtrx = createMatrix(capacity, weights, values)
    print(mtrx)
    # Tu można skończyć, jeżeli chcemy tylko wartość, a nie konkretne przedmioty. Wartość plecaka to max(mtrx[len(mtrx)-1])
    knapsack_val, taken = readSolution(mtrx, values)
    print("--------\nYou've taken items nr:", taken, ". Total value is:", knapsack_val)

    return (knapsack_val, taken)


if __name__ == '__main__':
    capacity = 9
    weights=[4,5,4,2]
    values=[5,3,6,1]
    mainDynamic(capacity, weights, values)
