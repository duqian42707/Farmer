import common




def do_single():
	if get_ground_type()!=Grounds.Soil:
		till()
	plant(Entities.Sunflower)
	if get_water()<0.75:
		use_item(Items.Water)
	

def stats():
	results = []
	if get_entity_type()==Entities.Sunflower:
		results.append((get_pos_x(), get_pos_y(),measure()))
	return results
		
def harvest_points(points):
	for point in points:
		common.goto(point[0],point[1])
		while True:
			if can_harvest():
				harvest()
				break
			else:
				use_item(Items.Fertilizer)
	
def sort_harvest(num_points_map):
	keys=[]
	for key in num_points_map:
		keys.append(key)
	common.sort(keys, 'desc')

	for key in keys:
		harvest_points(num_points_map[key])
	
def thread(n):
	results=[]
	common.goto(n,0)
	for i in range(get_world_size()):
		do_single()
		move(North)
	move(East)
	for i in range(get_world_size()):
		arrs = stats()
		common.addAll(results,arrs)
		move(North)
	move(East)
	return results
	
def list_to_map(list):
	num_points_map = {}
	for item in list:
		point = (item[0],item[1])
		num_petals = item[2]
		if not(num_petals in num_points_map):
			num_points_map[num_petals]=[]
		num_points_map[num_petals].append(point)
	return num_points_map

def plant_sunflower(num):
	drones=[]
	# 启动n架无人机,分别执行工作
	for n in range(num-1):
		def func():
			return thread(n)
		common.goto(2*n,0)
		drone = spawn_drone(func)
		drones.append(drone)
	# 自己也去
	common.goto(2*(num-1),0)
	result_last = thread(num-1)
	results = []
	for drone in drones:
		result = wait_for(drone)
		common.addAll(results,result)
		
	common.addAll(results,result_last)
	num_points_map = list_to_map(results)
	sort_harvest(num_points_map)
	
	
	
clear()
set_world_size(8)
while True:
	plant_sunflower(8)