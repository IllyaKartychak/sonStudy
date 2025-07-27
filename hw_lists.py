from multiprocessing.forkserver import set_forkserver_preload

my_things = ["backpack"]
friend_things = ["backpack"]

my_things.append("tent")
friend_things.extend(["napkins", "lightfire"])

all_things = my_things + friend_things
print(all_things)
all_things.sort()
all_things.reverse()
print(all_things)

last = all_things[2::3]
print(last)
the_most_last = all_things[::-2]
print(the_most_last)

all_things[1] = "powerbank"
all_things[2] = "powerbank"
all_things.pop()
del all_things[0]
print(all_things)
print(
    len(all_things),
    len(all_things[0]),
    all_things.index("powerbank"),
    "powerbank" in all_things,
    all_things.count("powerbank"),
)
