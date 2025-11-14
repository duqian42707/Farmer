import common

def step1():
	if get_ground_type()!=Grounds.Soil:
		till()
	if get_entity_type() != Entities.Pumpkin:
		plant(Entities.Pumpkin)
	if get_water()<0.75:
		use_item(Items.Water)

def step2(dead_points):
	point = (get_pos_x(),get_pos_y())
	if get_entity_type() == Entities.Dead_Pumpkin:
		dead_points.add(point)
		plant(Entities.Pumpkin)
		if len(dead_points)<3:
			use_item(Items.Fertilizer)
	elif can_harvest() and point in dead_points:
		dead_points.remove(point)
		
def thread(n):
	common.goto(n,0)
	for i in range(get_world_size()):
		step1()
		move(North)
	move(East)
		
	dead_points = set()
	for i in range(get_world_size()):
		step2(dead_points)
		move(North)
	move(East)

	while len(dead_points)>0:
		cloned_points=common.clone_set(dead_points)
		common.loop_points(cloned_points,step2,dead_points)
	

def plant_pumpkin():
	# 启动n架无人机,分别执行工作
	for n in range(31):
		def func():
			return thread(n)
		common.goto(2*n,0)
		spawn_drone(func)
	# 自己也去
	common.goto(31,0)
	thread(31)
	
	while True:
		if num_drones()==1 and can_harvest():
			harvest()
			break

if __name__ == "__main__":
	clear()
	while num_items(Items.Pumpkin) < 200*1000*1000:
		plant_pumpkin()
		