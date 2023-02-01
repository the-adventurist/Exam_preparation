people = int(input())
lift = [int(x) for x in input().split()]
lift_new_state = []
lift_has_empty_spaces = False
for current_wagon in lift:
    free_space = 4 - current_wagon
    if people >= free_space:
        people -= free_space
        current_wagon = 4
        if not people:
            lift_new_state.append(current_wagon)
            break
    else:
        free_space = people
        people = 0
        current_wagon += free_space
    if current_wagon < 4:
        lift_has_empty_spaces = True
    lift_new_state.append(current_wagon)
if people and not lift_has_empty_spaces:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join([str(x) for x in lift_new_state]))
elif lift_has_empty_spaces and not people:
    print(f"The lift has empty spots!")
    print(" ".join([str(x) for x in lift_new_state]))
else:
    print(" ".join([str(x) for x in lift_new_state]))
