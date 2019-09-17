# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 4000
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    refills = 0
    at_station = 0
    tank = m
    while True:
        # 1. find the farthest station car can reach
        # 2. if destination is less than farthest station: go to destination
        # 3. if not: go to farthest station
        # 4 repeat

        stations_in_reach = list(filter(lambda x: x <= tank, stops))
        if stations_in_reach == []:
            if d <= tank:       return refills
            else:               return -1
        elif d <= tank:         return refills
        else:
            at_station = stations_in_reach[-1]
            stops = stops[len(stations_in_reach):]
            tank = at_station + m
            refills += 1




if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
