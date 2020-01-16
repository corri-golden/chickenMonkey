# Function and variable names are snake case instead of camel case
# def create_person(first_name, last_name, age, occupation):
#     return {
#         "first_name": first_name,
#         "last_name": last_name,
#         "age": age,
#         "occupation": occupation,
#     }

# melissa = create_person("Melissa", "Bell", 25, "Software Developer")
# # print(melissa)


# Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.
# def run(name):
#     run()
#     print(f'{name} ran')


# def run(name):
#     return print(f'{name} ran around the yard')
# run("Chase")

# def swing(name):
#     return print(f'{name} swim really fast')
# swing("Erin")

# def slide(name):
#     return print(f'{name} down the long slide')
# slide("Josh")

def hide_and_seek(name):
    return print(f'{name} plays hide and seek')
hide_and_seek("Chuck")


# The following lists of children should be iterated, and the names sent to the appropriate functions.  // iterate through list and call run function on each kid.  when I'm iterating, I called the run function and used the kid as an argument which is each kid in the list and sends it to the function.
running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

# for kid in running_kids:
#     run(kid)

# for kid in swinging_kids:
#     swing(kid)

# for kid in sliding_kids:
#     slide(kid)

for kid in hiding_kids:
    hide_and_seek(kid)
    


    



    




