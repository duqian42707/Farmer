import common

def step1():
	if get_ground_type()!=Grounds.Soil:
		till()
	plant(Entities.Cactus)


def step2_inner():
	print(1)

def step2():
	size=get_world_size()
	swapped = True
	while swapped:
		swapped = False
		for i in range(size):
			for j in range(size):
				# 检查右侧元素（不越界且左>右时交换，保证左小右大）
				if j < size - 1 and measure() > measure(East):
					swap(East)
					swapped = True
				
				# 检查下方元素（不越界且上<下时交换，保证上大下小）
				if i < size - 1 and measure() > measure(North):
					swap(North)
					swapped = True
				move(East)
			move(North)


def plant_cactus():
	common.loop_once(step1)
	while True:
		if can_harvest():
			harvest()
			break

if __name__ == "__main__":
	set_world_size(8)
	common.loop_once(step1)
	step2()
	harvest()
	