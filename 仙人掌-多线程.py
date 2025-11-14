import common

def step1():
	if get_ground_type()!=Grounds.Soil:
		till()
	plant(Entities.Cactus)


def thread(n):
	# 种植
	common.goto(n,0)
	for i in range(get_world_size()):
		step1()
		move(North)
	move(East)
		
	size=get_world_size()
	# 排序x轴
	common.goto(0,n)
	for i in range(size):
		for j in range(size-i-1):
			if measure()>measure(East):
				swap(East)
			move(East)
		common.goto(0,n)
	common.goto(0,n+1)
		
def thread2(n):
	size=get_world_size()
	# 排序y轴
	common.goto(n,0)
	for i in range(size):
		for j in range(size-i-1):
			if measure()>measure(North):
				swap(North)
			move(North)
		common.goto(n,0)
	common.goto(n+1,0)
	
def plant_cactus(num):
	# 启动n架无人机,分别执行工作
	for n in range(num-1):
		def func():
			return thread(n)
		common.goto(n,0)
		spawn_drone(func)
	# 自己也去
	common.goto((num-1),0)
	thread(num-1)
	while True:
		if num_drones()==1:	
			break
	# 启动n架无人机,分别执行工作
	for n in range(num-1):
		def func():
			return thread2(n)
		common.goto(n,0)
		spawn_drone(func)
	# 自己也去
	common.goto((num-1),0)
	thread2(num-1)

	while True:
		if num_drones()==1:	
			break
	harvest()
	
if __name__ == "__main__":
	clear()
#	set_world_size(8)
#	while num_items(Items.Cactus)<33554432:
	while True:
		plant_cactus(32)