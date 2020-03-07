weight = input("Enter total weight: ")
barWeight = input("Enter bar weight (45): ")

if (barWeight == ""):
	barWeight = 45

barWeight = int(barWeight)
weight = int(weight)

avail = [45, 35, 25, 10, 5, 2.5]


weight = (weight-barWeight)/2
plates = []

for i in avail:
	while (1):
		if (weight >= i):
			weight = weight - i
			plates.append(i)

		else:
			break

print(plates)

				
