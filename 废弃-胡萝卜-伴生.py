import common

poss=[]
map={}

def first_plant(index):
	global poss
	global map
	pos = poss[index]
	common.goto(pos[0],pos[1])
	if get_ground_type()!=Grounds.Soil:			
		till()
	if get_entity_type() == Entities.Carrot and can_harvest():
		harvest()
	(x,y) = (get_pos_x(),get_pos_y())
	plant_type=Entities.Carrot
	if (x,y) in map:
		(ox,oy) = map[(x,y)]
		map.pop((x,y))
		index = common.index_of_list(poss,(ox,oy))
	else:
		plant(plant_type)
		if get_water()<0.75:
			use_item(Items.Water)
		new_plant_type, (nx, ny) = get_companion()
		map[(nx,ny)]=(x,y)
		common.goto(nx,ny)
		if get_ground_type()!=Grounds.Soil:			
			till()
		plant(new_plant_type)
		index = (index+1) % len(poss)
	return index
def start():
	global poss
	poss = common.get_com_poss(3,3)
	index=0
	while True:
		index = first_plant(index)
		
	
if __name__ == '__main__':
	set_world_size(8)
	#set_execution_speed(3)
	start()
	
	print('end')
	


