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
    new_set = set(n)
    return list(new_set)


returned_list = list_to_set(item_list)
print(returned_list)
