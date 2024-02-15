def eat_apples(num_of_apples):
    remaining_apples = num_of_apples
    remaining_apples = num_of_apples-1
    print("Thank you")

    while remaining_apples > 0:
        remaining_apples -= 1
        print("Thank uhh")

    print("Done")
    return
# if apples are 0 then it will not work.
eat_apples(0)

#code 2(all test cases pass even if apples are 0)
def eat_apples(num_of_apples):
    remaining_apples = num_of_apples
    while remaining_apples > 0:
        remaining_apples -= 1
        print("Thank you")
    print("Done")
    return

eat_apples(0)

# code 3
def eat_apples(num_of_apples , on_diet):
    remaining_apples = num_of_apples
    while remaining_apples > 0 and not on_diet:
        remaining_apples -= 1
        print("Thank you")
    print("Done")
    return

eat_apples(5 , False)



