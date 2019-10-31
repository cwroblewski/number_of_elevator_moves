
def solution(A, B, X, Y):

    list_of_persons = []

    for x in range(0, len(A)):
        person = dict(num=x, weight=A[x], floor=B[x])
        list_of_persons.append(person)

    first_person_in_row = 0

    courses = []

    movement_count = 0

    check = False

    while not check:

        if first_person_in_row < list_of_persons[-1]['num']:


            weight = 0
            x = first_person_in_row

            check_2 = False
            course = []
            while not check_2:


                if first_person_in_row <= list_of_persons[-1]['num']:

                    if weight < Y or x < X:
                        if weight + list_of_persons[first_person_in_row]['weight'] < Y:

                            course.append(B[x])

                            weight += list_of_persons[first_person_in_row]['weight']
                            x += 1
                            first_person_in_row += 1

                        else:
                            check_2 = True

                else:
                    check_2 = True

            courses.append(course)

        else:
            check = True
    floor = 0

    for move in courses:
        for x in move:
            if x != floor:
                movement_count += 1
                floor = x
        movement_count += 1
        floor = 0

    return movement_count, courses


A = [69, 56, 97, 100, 56, 75, 45, 87, 12]
B = [1, 1, 1, 1, 1, 1, 1, 1, 1]
X = 3
Y = 200

print(solution(A, B, X, Y))