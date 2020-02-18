def fit_people(attendees, index, comb=[]):
    if index == len(comb):
        print(', '.join(comb))
        return

    for i in range(len(attendees)):
        x = attendees[i]
        comb.append(x)
        fit_people(attendees[i + 1:], index, comb)
        comb.pop()


people_for_chairs = input().split(", ")
chairs = int(input())
fit_people(people_for_chairs, chairs)
