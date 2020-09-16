from player import Player
from world import World
from queue import Queue
from stack import Stack
import random
from ast import literal_eval
from room import Room

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()  # UNCOMMENT THIS

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def traverse_graph(player):

    visited = set()  # Track vertex that have been visited

    go_back = []  # Save directions on how to back track

    while len(visited) < len(world.rooms):
        current_room = player.current_room  # Get the players current room

        exist = current_room.get_exits()  # Directions still unexplored
        unexplored = [direction for direction in exist if current_room.get_room_in_direction(
            direction) not in visited]

        visited.add(current_room)  # Mark current room as visited

        # If there are unxplored rooms, pick a random direction and explore
        if unexplored:
            direction = unexplored[random.randint(
                0, len(unexplored)-1)]
            player.travel(direction)
            go_back.append(direction)
            traversal_path.append(direction)

        else:  # else we are at the end, back track

            # get the last direction we went in
            last_direction = go_back.pop(-1)

            # reverse the last direction to go back
            reverse_direction = {'s': 'n', 'n': 's', 'w': 'e', 'e': 'w'}
            player.travel(reverse_direction[last_direction])
            traversal_path.append(reverse_direction[last_direction])


traverse_graph(player)


'''
Do not go below this section
|
|
|
|
|
'''


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# #######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
