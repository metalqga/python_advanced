def flights(*args):
    flights_dic = dict()

    for arg in args:
        if type(arg) == int:
            passengers = arg
            if destination in flights_dic:
                flights_dic[destination] += int(passengers)
            else:
                flights_dic[destination] = passengers
        else:
            destination = arg

        if destination == "Finish":
            break

    return flights_dic


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))