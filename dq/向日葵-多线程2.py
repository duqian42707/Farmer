import common

def do_single():
	x = get_pos_x()
	y = get_pos_y()
	if can_harvest():
		harvest()

	if get_ground_type()!=Grounds.Soil:
		till()
	plant(Entities.Sunflower)
	if get_water()<0.75:
		use_item(Items.Water)

def thread(n):
	while True:
		common.goto(n,0)
		for i in range(get_world_size()):
			do_single()
			move(North)
		move(East)
	
def harvest_hay(num):
	# 启动n架无人机,分别执行工作
	for n in range(num-1):
		def func():
			return thread(n)
		common.goto(n,0)
		spawn_drone(func)
	# 自己也去
	common.goto((num-1),0)
	thread(num-1)
	
clear()
harvest_hay(32)