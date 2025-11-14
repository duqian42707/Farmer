
def loop_forever(func, args=None):
	size=get_world_size()
	while True:
		for i in range(size):
			for j in range(size):
				if args!=None :                
					func(args)
				else:
					func()
				move(North)
			move(East)

def loop_once(func, args=None):
	size=get_world_size()
	for i in range(size):
		for j in range(size):
			if args!=None :                
				func(args)
			else:
				func()
			move(North)
		move(East)


def thread_loop(func,args=None):
	size=get_world_size()
	threads = max_drones()
	for i in range(size/threads):
		for j in range(size):
			if args!=None :                
				func(args)
			else:
				func()
			move(North)
		for k in range(threads):
			move(East)
	
	

def loop_points(points,func,args=None):
	for point in points:
		goto(point[0],point[1])
		func(args)

def sort(nums, order='asc'):
	for i in range(len(nums)):
		for j in range(0, len(nums) - i - 1):
			flag1 = order=='asc' and nums[j] > nums[j + 1]
			flag2 = order=='desc' and nums[j] < nums[j + 1]
			if (flag1 or flag2):
				nums[j], nums[j + 1] = nums[j + 1], nums[j]

def clone_set(origin):
	cloned=set()
	for item in origin:
		cloned.add(item)
	return cloned
	
	
def moveX(n):
	size = get_world_size()
	n = n % size
	if n <= size / 2:
		for i in range(n):
			move(East)
	else:
		for i in range(size-n):
			move(West)

def moveY(n):
	size = get_world_size()
	n = n % size
	if n <= size / 2:
		for i in range(n):
			move(North)
	else:
		for i in range(size-n):
			move(South)
	
def goto(target_x,target_y):
	x = get_pos_x()
	y = get_pos_y()
	right = target_x - x
	up = target_y - y
	moveX(right)
	moveY(up)

		
def addAll(list1,list2):
	for item in list2:
		list1.append(item)

def index_of_list(list,item):
	for i in range(len(list)):
		if list[i]==item :
			return i
	return -1

def get_com_poss(x,y):
	return [
		(x,y),(x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),
		(x-1,y+2),(x,y+2),(x+1,y+2),(x+2,y+2),(x+2,y+1),(x+2,y),(x+2,y-1),(x+2,y-2),
		(x+1,y-2),(x,y-2),(x-1,y-2),(x-2,y-2),(x-2,y-1),(x-2,y),(x-2,y+1),(x-2,y+2),
		(x-2,y+3),(x-1,y+3),(x,y+3),(x+1,y+3),(x+2,y+3),(x+3,y+3),(x+3,y+2),(x+3,y+1),
		(x+3,y),(x+3,y-1),(x+3,y-2),(x+3,y-3),(x+2,y-3),(x+1,y-3),(x,y-3),(x-1,y-3),
		(x-2,y-3),(x-3,y-3),(x-3,y-2),(x-3,y-1),(x-3,y),(x-3,y+1),(x-3,y+2),(x-3,y+3)
	]
	