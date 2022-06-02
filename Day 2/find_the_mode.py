# Find the mode
# Extend the function from day 1, to also print out the modal element(s) of the input list.
# i.e, to determine which element occurs the most. If there are multiple such elements,
# then return a list containing them all.

from statistics import multimode
""" The multimode() function in the statistics module used in line 18 
    takes a data set as a parameter and returns a list of modes. 
    We can use this function when there is more than one possible 
    modal value in a given record.
"""


input_list = input("Please enter a list of items, separate them by a comma(,): ")
# the input takes a list of items separated by a comma(,).

item_list = input_list.split(",")  # splits the items into a list of strings using the comma as their separator.


def list_to_set(n):
    """A list to Set converter function.
    The function converts a list(input) to a set and returns a list.
    item_list(list): Input list, contains a list of items.
    new_set(Set): A set; sets the items in item_list to a set, removing the duplicates.
    return list(new_set): Returns a list of items in new_set.
    """
    mode_list = multimode(n)
    print("The modal value(s) of the list is/are %s" % mode_list)
    new_set = set(n)
    return list(new_set)


returned_list = list_to_set(item_list)
print("The new list without duplicate is {}".format(returned_list))
