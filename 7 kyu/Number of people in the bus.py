def number(bus_stops):
    pass_rem = 0
    for i in bus_stops:
        pass_rem += i[0] - i[1]
    return pass_rem