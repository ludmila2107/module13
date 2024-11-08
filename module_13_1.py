import asyncio

async def start_strongman(name, power):
	print(f' Силач {name} начал соревнования.')
<<<<<<< HEAD
	for ball_number in range(1,6): #чем выше сила, тем mеньше задержка
=======
	for ball_number in range(1,6): #чем выше сила, тем еньше задержка
>>>>>>> 914b0f8fdd86d8a4a81ab318ce3d23c8544270eb
		delay = 1/power
		await asyncio.sleep(delay) #ждем время
		print(f'Силач {name} поднял {ball_number}')
	print(f'Силач {name} закончил соревнования.')


<<<<<<< HEAD
async def start_tournament():
=======
async  def start_tournament():
>>>>>>> 914b0f8fdd86d8a4a81ab318ce3d23c8544270eb
	tasks = [
		start_strongman("Misha", 3),
		start_strongman("Sacha", 4),
		start_strongman("Max", 5),
	]
	await asyncio.gather(*tasks)

if __name__ == "__main__":
	asyncio.run(start_tournament())
