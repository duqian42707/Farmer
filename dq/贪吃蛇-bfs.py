
# 方向常量定义
NORTH = North
SOUTH = South
EAST = East
WEST = West

def is_valid_pos(pos,word_size):
	flag0 = (pos[0]>=0 and pos[0]<word_size)
	flag1 = (pos[1]>=0 and pos[1]<word_size)
	return flag0 and flag1


def get_neighbors(pos, word_size):
	#获取指定位置的四个相邻位置
	x, y = pos
	positions = [
		(x, y + 1),  # 北
		(x, y - 1),  # 南
		(x + 1, y),  # 东
		(x - 1, y)   # 西
	]
	result = []
	for p in positions:
		if is_valid_pos(p,word_size):
			result.append(p)
	return result

def get_direction(current_pos, next_pos):
	#根据当前位置和下一个位置确定移动方向"""
	current_x, current_y = current_pos
	next_x, next_y = next_pos
	
	if next_y > current_y:
		return NORTH
	elif next_y < current_y:
		return SOUTH
	elif next_x > current_x:
		return EAST
	else:
		return WEST

def bfs_path(start, target, obstacles):
	#"""使用BFS寻找从起点到目标的最短路径（不使用deque，用列表模拟队列）"""
	queue = [[start]]  # 用列表作为队列，左侧为队首
	visited = set([start])
	
	while queue:
		# 取队列第一个元素（模拟出队）
		path = queue.pop(0)
		current_pos = path[-1]
		
		if current_pos == target:
			return path
			
		# 探索四个方向
		for next_pos in get_neighbors(current_pos,get_world_size()):
			if next_pos not in visited and next_pos not in obstacles:
				visited.add(next_pos)
				new_path = list(path)
				new_path.append(next_pos)
				queue.append(new_path)  # 加入队尾
				
	return None  # 找不到路径

def get_safe_random_direction(head_pos, body_positions):
	#"""当找不到路径时，返回一个安全的随机方向"""
	x, y = head_pos
	possible_directions = []
	
	# 检查各个方向是否安全
	if (x, y + 1) not in body_positions:
		possible_directions.append(NORTH)
	if (x, y - 1) not in body_positions:
		possible_directions.append(SOUTH)
	if (x + 1, y) not in body_positions:
		possible_directions.append(EAST)
	if (x - 1, y) not in body_positions:
		possible_directions.append(WEST)
		
	# 如果有安全方向，随机返回一个；否则只能结束游戏了
	if len(possible_directions)>0:
		return possible_directions[0]
	change_hat(Hats.Brown_Hat)
	return None


def get_next_direction(snake_body, food_pos):
	#"""计算蛇头下一步应该移动的方向"""
	head_pos = snake_body[0]
	body_positions = set(snake_body)
	
	# 使用BFS寻找最短路径
	path = bfs_path(head_pos, food_pos, body_positions)
	
	if not path or len(path) < 2:
		# 如果找不到路径，尝试随机安全移动
		return get_safe_random_direction(head_pos, body_positions)
		
	# 返回下一步方向
	return get_direction(head_pos, path[1])

def move_snake(snake_body, direction, food_pos):
	move(direction)
	#"""移动蛇并返回新的身体状态"""
	x, y = snake_body[0]
	
	# 计算新头部位置
	if direction == NORTH:
		new_head = (x, y + 1)
	elif direction == SOUTH:
		new_head = (x, y - 1)
	elif direction == EAST:
		new_head = (x + 1, y)
	else:  # WEST
		new_head = (x - 1, y)
		
	# 创建新的身体列表（头部新增）
	new_body = [new_head] + snake_body
	
	# 检查是否吃到食物（吃到则保留尾部，否则移除尾部）
	if new_head == food_pos:
		return new_body  # 长度增加
	else:
		return new_body[:-1]  # 长度不变


# 使用示例
if __name__ == "__main__":
	set_world_size(12)
	change_hat(Hats.Dinosaur_Hat)
	# 初始化蛇身体（头部在第一个位置）
	snake_body = [(0,0)]
	# 初始化食物位置
	food_pos = measure()
	
	quick_print("初始蛇头位置:", snake_body[0])
	quick_print("食物位置:", food_pos)
	quick_print("-" , 50)
	
	# 模拟15步自动移动
	while True:
		# 获取下一步方向
		direction = get_next_direction(snake_body, food_pos)
		# 移动蛇
		snake_body = move_snake(snake_body, direction, food_pos)
		# 输出信息
		quick_print("第{i+1}步")
		quick_print("移动方向: {direction}")
		quick_print("当前蛇头位置: {snake_body[0]}")
		quick_print("蛇长度: {len(snake_body)}")
		quick_print("-" , 50)
		
		# 如果吃到食物，重新生成食物
		if snake_body[0] == food_pos:
			quick_print("吃到食物！生成新食物...")
			food_pos = measure()  # 新食物位置
			quick_print("新食物位置: {food_pos}")
			quick_print("-" , 50)