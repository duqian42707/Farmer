import common

def do_single():
	if get_ground_type()!=Grounds.Soil:
		till()
	plant(Entities.Sunflower)    
	
def stats(num_points_map):
	if get_entity_type()==Entities.Sunflower:
		point = (get_pos_x(), get_pos_y())
		num_petals = measure()
		if not(num_petals in num_points_map):
			num_points_map[num_petals]=[]
		num_points_map[num_petals].append(point)
		
def harvest_points(points):
	for point in points:
		common.goto(point[0],point[1])
		if can_harvest():
			harvest()

				
def sort_harvest(num_points_map):
	keys=[]
	for key in num_points_map:
		keys.append(key)
	common.sort(keys, 'desc')

	for key in keys:
		harvest_points(num_points_map[key])
	

def plant_sunflower():
	common.loop_once(do_single)
	num_points_map = {}
	common.loop_once(stats,num_points_map)
	sort_harvest(num_points_map)
	
	
	
clear()
set_world_size(8)
while True:
	plant_sunflower()