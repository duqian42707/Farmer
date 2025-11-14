import common

def all_map_once(size):
	result = move(North)
	if not result:
		return False
	for n in range(size/2):
		for i in range(size-2):
			move(North)
		move(East)
		
		for i in range(size-2):
			move(South)
		if n < size/2-1:
			move(East)
	result = move(South)
	if not result:
		return False
	for _ in range(size-1):
		result = move(West)
		if not result:
			return False
	return True

def max_snake_once():
	common.goto(0,0)
	change_hat(Hats.Dinosaur_Hat)
	size = get_world_size()
	while True:
		result = all_map_once(size)
		if not result:
			break
	change_hat(Hats.Brown_Hat)
	
if __name__ == "__main__":
	clear()
	#set_world_size(20)
	while num_items(Items.Bone)<33488928:
		max_snake_once()
	
