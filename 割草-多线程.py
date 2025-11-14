import common

def do_single():
	if can_harvest():
		harvest()

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
		common.goto(2*n,0)
		spawn_drone(func)
	# 自己也去
	common.goto(2*(num-1),0)
	thread(num-1)
	
clear()
harvest_hay(32)