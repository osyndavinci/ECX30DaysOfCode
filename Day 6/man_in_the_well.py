# Day 6: Man in the well.
# A man is stuck at the bottom of a well. Each day, he climbs up 8 metres, and then at night,
# he slips downwards by 3 metres. Using loops(any loop of your choice),
# write a function to determine(and print!) how many days it takes for him to climb out of a well of any given depth,
# where the depth of the well is taken as input.
# E.G: f(17)=> the well is 17 metres deep.
# Day 1: climbs 8m, height=8m; slips 3m, height=8-3=5m;
# Day 2: climbs 8m, height=5+8=13m; slips 3m, height= 13-3=10m
# Day 3: climbs 8m, height=10+8=18m.  But 18>17. STOP.(height climbed has exceeded well depth)
# Therefore, f(17)=3 days.


get_depth = int(input("Please enter the dept of the well: "))
# gets the depth of the well from the user.

print("The depth of the well is {} metres".format(get_depth))  # prints out the user's depth.


def climb_out(n_depth):
    """ A function to determine how many days it takes to get out of the well.

    n_depth(int): This is the depth entered by the user.
    x_days(int): measures the days it takes the man to climb out.
    y_climbed(int): this is the height the man climbs each day,
    it also drops each night if the man does not make it to the top of the well.

    The function returns x_days when the man finally makes it to the top of the well,
    or else, it will continue looping.

    """
    x_days = 0
    y_climbed = 0
    while y_climbed < n_depth:
        x_days += 1
        y_climbed += 8
        if y_climbed >= n_depth:
            return "It will take the man {} day(s) to climb out of the well.".format(x_days)
        else:
            y_climbed -= 3


free_man = climb_out(get_depth)
print(free_man)
