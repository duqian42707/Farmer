import common

def do_single():
	if can_harvest():
		harvest()

def thread(n):
	while True:
		common.goto(n,0)
		for i in range(2):
			for i in range(get_world_size()):
				do_single()
				move(North)
			move(East)
	
def harvest_all(num):
	# 启动n架无人机,分别执行工作
	for n in range(num-1):
		def func():
			return thread(n)
		common.goto((num-1),0)
		spawn_drone(func)
	# 自己也去
	common.goto((num-1),0)
	thread(num-1)
common.goto(0,0)
harvest_all(32)