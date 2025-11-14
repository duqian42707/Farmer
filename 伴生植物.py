import common
plants = [
	Entities.Grass,
	Entities.Bush,
	Entities.Tree,
	Entities.Carrot
]

map={}

def first_plant():
	if can_harvest():
		harvest()
	(x,y) = (get_pos_x(),get_pos_y())
	plant_type=plants[get_pos_y()%4]
	if (x,y) in map:
		plant_type = map[(x,y)]
	if plant_type == Entities.Carrot:
		if get_ground_type()!=Grounds.Soil:
			till()
	plant(plant_type)
	if get_water()<0.75:
		use_item(Items.Water)
	new_plant_type, (nx, ny) = get_companion()
	map[(nx,ny)]=new_plant_type

#set_world_size(8)

common.loop_forever(first_plant)
	


