import common
grass_lines = 4

def do_single():
	x = get_pos_x()
	y = get_pos_y()
	if can_harvest():
		harvest()

	if x >= grass_lines:
		if get_ground_type()!=Grounds.Soil:
			till()
		if (x+y) % 2==0:
			plant(Entities.Tree)
		elif num_items(Items.Hay)>2 and num_items(Items.Wood)>2 :
			plant(Entities.Carrot)
	
clear()
common.loop_forever(do_single)