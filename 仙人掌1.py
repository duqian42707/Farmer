import common

def step1():
	if get_ground_type()!=Grounds.Soil:
		till()
	plant(Entities.Cactus)

def step2():
	size=get_world_size()
	for y in range(size):
		for i in range(size):
			for j in range(size-i-1):
				if measure()>measure(East):
					swap(East)
				move(East)
			common.goto(0,y)
		common.goto(0,y+1)
	
	for x in range(size):
		for i in range(size):
			for j in range(size-i-1):
				if measure()>measure(North):
					swap(North)
				move(North)
			common.goto(x,0)
		common.goto(x+1,0)
	
	


def plant_cactus():
	common.loop_once(step1)
	while True:
		if can_harvest():
			harvest()
			break

if __name__ == "__main__":
	clear()
	set_world_size(8)
	common.loop_once(step1)
	step2()
	print('end')
