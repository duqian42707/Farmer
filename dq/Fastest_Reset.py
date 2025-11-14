from __builtins__ import *
import common
import fr_maze
import fr_snake


def to_obtain_hay(num):
	def func():
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Grassland:
			till()

	while num_items(Items.Hay) < num:
		common.loop_once(func)


def to_obtain_wood(num):
	to_unlock(Unlocks.Plant)

	def func1():
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Bush)

	while num_items(Items.Wood) < num:
		common.loop_once(func1)


def to_obtain_carrot(num):
	to_unlock(Unlocks.Carrots)

	def func():
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		if num_items(Items.Hay) < 512:
			to_obtain_hay(512)
		if num_items(Items.Wood) < 512:
			to_obtain_wood(512)
		plant(Entities.Carrot)

	while num_items(Items.Carrot) < num:
		common.loop_once(func)


def to_obtain_pumpkin(num):
	to_unlock(Unlocks.Pumpkins)

	def func():
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		if num_items(Items.Carrot) < 512:
			to_obtain_carrot(512)
		plant(Entities.Pumpkin)

	while num_items(Items.Pumpkin) < num:
		common.loop_once(func)


def to_obtain_cactus(num):
	to_unlock(Unlocks.Cactus)

	def func():
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		if num_items(Items.Pumpkin) < 64:
			to_obtain_pumpkin(64)
		plant(Entities.Cactus)

	while num_items(Items.Cactus) < num:
		common.loop_once(func)


def to_obtain_gold(num):
	to_unlock(Unlocks.Fertilizer)
	to_unlock(Unlocks.Mazes)

	def func():
		size = get_world_size()
		substance = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)
		if num_items(Items.Weird_Substance) < substance:
			to_obtain_weird(substance)

	while num_items(Items.Gold) < num:
		func()
		fr_maze.to_obtain_gold(num)


def to_obtain_bone(num):
	to_unlock(Unlocks.Hats)
	to_unlock(Unlocks.Speed, 2)
	to_unlock(Unlocks.Expand, 4)
	to_unlock(Unlocks.Dinosaurs)

	def func():
		size = get_world_size()
		if num_items(Items.Cactus) < 64 * size * size:
			to_obtain_cactus(64 * size * size)

	while num_items(Items.Bone) < num:
		func()
		fr_snake.to_obtain_bone(num)


def to_obtain_weird(num):
	to_unlock(Unlocks.Expand, 2)
	to_unlock(Unlocks.Carrots)
	to_unlock(Unlocks.Fertilizer)

	def func():
		if can_harvest():
			harvest()
		if get_ground_type() == Grounds.Grassland:
			till()
		if num_items(Items.Hay) < 512:
			to_obtain_hay(512)
		if num_items(Items.Wood) < 512:
			to_obtain_wood(512)
		plant(Entities.Carrot)
		while num_items(Items.Fertilizer) == 0:
			pass
		use_item(Items.Fertilizer)

	while num_items(Items.Weird_Substance) < num:
		common.loop_once(func)


def to_obtain_item(item, num):
	if item == Items.Hay:
		to_obtain_hay(num)
	if item == Items.Wood:
		to_obtain_wood(num)
	if item == Items.Carrot:
		to_obtain_carrot(num)
	if item == Items.Pumpkin:
		to_obtain_pumpkin(num)
	if item == Items.Cactus:
		to_obtain_cactus(num)
	if item == Items.Gold:
		to_obtain_gold(num)
	if item == Items.Bone:
		to_obtain_bone(num)
	if item == Items.Weird_Substance:
		to_obtain_weird(num)


def to_unlock(thing, level=1):
	while num_unlocked(thing) < level:
		cost_map = get_cost(thing)
		for item in cost_map:
			req_num = cost_map[item]
			while num_items(item) < req_num:
				to_obtain_item(item, req_num)
		unlock(thing)


if __name__ == '__main__':
	to_unlock(Unlocks.Hats)
	to_unlock(Unlocks.Speed, 3)
	to_unlock(Unlocks.Expand, 5)
	to_unlock(Unlocks.Grass, 3)
	to_unlock(Unlocks.Carrots, 2)
	to_unlock(Unlocks.Watering, 2)
	to_unlock(Unlocks.Fertilizer, 2)
	to_unlock(Unlocks.Trees, 2)
	to_unlock(Unlocks.Pumpkins, 2)
	to_unlock(Unlocks.Speed, 4)
	to_unlock(Unlocks.Expand, 6)
	to_unlock(Unlocks.Mazes, 2)
	to_unlock(Unlocks.Cactus, 2)
	to_unlock(Unlocks.Dinosaurs)
	to_unlock(Unlocks.Fertilizer, 4)
	to_unlock(Unlocks.Pumpkins, 6)
	to_unlock(Unlocks.Mazes, 3)
	to_unlock(Unlocks.Leaderboard)

	print('end')
