import common

food=(0,0)
length=0

def move2(direction):
	global food
	global length
	result = move(direction)
	if get_entity_type()==Entities.Apple:
		food = measure()
		length +=1
	return result

# 纵向上去下来
def up_and_down():
	size = get_world_size()
	for i in range(size-2):
		move2(North)
	move2(East)
	
	for i in range(size-2):
		move2(South)

# 纵向上去下来后的回到原点
def back_to_zero():
	move2(South)
	x =	get_pos_x()
	for i in range(x):
		move2(West)
	move2(North)
		
# 纵向上去下来后的移动:
# 如果长度没超：
# 1. 往右移动n个单位
# 2. 回到原点
# 如果长度超了：
# 1. 往右移动1个单位
# 2. 回到原点
def move_next():
	global length
	global food
	size = get_world_size()
	x = get_pos_x()
	if length <= (x+1)*(size-1)+1 :
		# 长度没超
		targetX = food[0]
		if food[0]%2==1:
			targetX -=1
		if targetX > x:
			for i in range(targetX-x):
				move2(East)
		else:
			back_to_zero()
	else:
		# 长度超了
		if x < size-1:
			move2(East)
		else:
			back_to_zero()

def all_map_once(size):
	result = move2(North)
	if not result:
		return False
	for n in range(size/2):
		up_and_down()
		move_next()
	if not result:
		return False
	return True

def max_snake_once():
	global food
	global length 
	common.goto(0,0)
	change_hat(Hats.Dinosaur_Hat)
	food = measure()
	size = get_world_size()
	while True:
		result = all_map_once(size)
		if not result:
			break
	change_hat(Hats.Brown_Hat)
	length=0

def to_obtain_bone(num):
	clear()
	while num_items(Items.Bone)<num:
		max_snake_once()
	
		