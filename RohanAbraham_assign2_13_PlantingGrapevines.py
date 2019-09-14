print("Please enter all vlaues in feet")
length_of_row = int(input("What is the length of the row?"))
end_post_space = int(input("How much space is used up by the end-post assembly?"))
vine_space = int(input("How much space is there in between vines?"))

number_of_grapevines = (length_of_row - (2 * end_post_space)) / vine_space


print(format(number_of_grapevines, ',.1f') + " grapevines will fit in each row")
