import common

def step1():
	if get_ground_type()!=Grounds.Soil:
		till()
	if get_entity_type() != Entities.Pumpkin:
		plant(Entities.Pumpkin)

def step2(dead_points):
	point = (get_pos_x(),get_pos_y())
	if get_entity_type() == Entities.Dead_Pumpkin:
		dead_points.add(point)
		plant(Entities.Pumpkin)        
	elif can_harvest() and point in dead_points:
		dead_points.remove(point)
		
def plant_pumpkin():
	dead_points = set()
	common.loop_once(step1)
	common.loop_once(step2,dead_points)

	while len(dead_points)>0:
		cloned_points=common.clone_set(dead_points)
		common.loop_points(cloned_points,step2,dead_points)
	
	while True:
		if can_harvest():
			harvest()
			break

set_world_size(8)
if __name__ == "__main__":
	clear()
	while True:
		plant_pumpkin()



