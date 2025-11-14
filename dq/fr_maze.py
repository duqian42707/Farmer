from __builtins__ import *
import common


def step3():
	directions = [North, East, South, West]
	index = 0
	while True:
		if get_entity_type()!=Entities.Hedge:
			harvest()
			break
		front = directions[index]
		right = directions[(index+1)%4]
		if can_move(right):
			move(right)
			index=(index+1)%4
		elif can_move(front):
			move(front)
		else:
			index=(index+3)%4


def step3_2():
	directions = [North, East, South, West]
	index = 0
	while True:
		if get_entity_type()!=Entities.Hedge:
			harvest()
			break
		front = directions[index]
		left = directions[(index+3)%4]
		if can_move(left):
			move(left)
			index=(index+3)%4
		elif can_move(front):
			move(front)
		else:
			index=(index+1)%4

def to_obtain_gold(num):
	while num_items(Items.Gold) < num:
		size = get_world_size()
		substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
		if num_items(Items.Weird_Substance) < substance:
			return False
		clear()
		if get_ground_type()!=Grounds.Soil:
			till()
		plant(Entities.Bush)
		use_item(Items.Weird_Substance,substance)
		spawn_drone(step3)
		step3_2()



