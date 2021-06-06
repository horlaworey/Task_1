def dictComp(stop, step):

    # creates a list starting from 0
    generated_list = [*range(0, stop)]
    # creates another list split into groups using list comprehension
    print(step)
    new_list = [generated_list[x:x + step] for x in range(1, stop, step) if len(generated_list[x:x + step]) == step]
    # new_list.index(group_list))+1 finds the index of each loop on the group list
    # Then add 1 to make the index count start from 1, not 0.
    new_dict = {f"items-{(new_list.index(group_list))+1}": group_list for group_list in new_list}

    print(new_dict)


dictComp(29, 4)
