clear()
set_world_size(8)

hats = [
  Hats.Brown_Hat,
  Hats.Cactus_Hat,
  Hats.Carrot_Hat,
  Hats.Gold_Hat,
  Hats.Golden_Cactus_Hat,
  Hats.Golden_Gold_Hat,
  Hats.Golden_Tree_Hat,
  Hats.Golden_Pumpkin_Hat,
  Hats.Dinosaur_Hat,
  Hats.Purple_Hat
]


for i in range(10):
	change_hat(hats[i])
	do_a_flip()
	pet_the_piggy()
print('end')