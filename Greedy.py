def greedy(capacity: int, weights: list, values: list):
    # stosunek wartości do wagi dla każdego elementu
    v_w_ratios = [values[i] / weights[i] for i in range(len(weights))]
    # obiekty 4-elementowe. stosunek, waga, wartość, numer
    items = [(v_w_ratios[i], weights[i], values[i], i) for i in range(len(weights))]
    # Sortowanie: najważniejszy stosunek, później waga, by elementy lżejsze o takim samym stosunku były
    # wpierw wybierane
    items.sort(key=lambda x: x[1], reverse=True) # po wadze
    items.sort(key=lambda x: x[0], reverse=True) # po stosuku, malejąco
    added_items = []
    weight_left = capacity

    for item in items:
        if item[1] <= weight_left:
            added_items.append(item)
            weight_left -= item[1]

    value = sum([item[2] for item in added_items])
    indices = sorted([item[-1] for item in added_items])
    return value, indices


if __name__ == "__main__":
    capacity = 9
    weights = [4, 5, 4, 2]
    values = [5, 3, 6, 1]
    print(greedy(capacity, weights, values))
