
from matplotlib import pyplot as plt
import datetime

# Note: Certain values here correspond to logged values within the texts containing our data. 
# In the case you wish to reproduce the same graphs made on our behalf, do update all the oldDate 
# values with the first corresponding episode of each text file, and subsequently change the text 
# files you are accessing within the open() functions, as well as any labels within the plots so
# that they match accordingly with the hyperparameter in question.


def main():
	reward = []
	policy_average = []
	reward2 = []
	policy_average2 = []
	reward3 = []
	policy_average3 = []
	reward4 = []
	policy_average4 = []
	oldDate = datetime.datetime(2019, 12, 9, 15, 42, 5)
	oldDate2 = datetime.datetime(2019, 12, 9, 15, 38, 50)
	oldDate3 = datetime.datetime(2019, 12, 9, 15, 34, 50)
	oldDate4 = datetime.datetime(2019, 12, 9, 15, 31, 45)
	timediff = []
	timediff2 = []
	timediff3 = []
	timediff4 = []

	with open('log_dui-2000.txt') as openfile:
		for line in openfile:
			read = line.split()
			for part in range(len(read)):
				if "length" in read[part - 1]:
					continue
				elif "R:" in read[part]:
					reward.append(float(read[part][2:5]))
				elif "\'policy_average_value\'" in read[part]:
					policy_average.append(float(read[part + 1][:5]))

		
	with open('log_dui-2000.txt') as openfile2:
		for line in openfile2:
			read = line.split()
			for part in range(len(read) - 3):
				if "2019" in read[part - 1] and "chainerrl" in read[part + 2] and "evaluat" not in read[part + 3] and "save" not in read[part + 3]:
					temp = read[part].split(":")
					temp2 = read[part - 1].split("-")
					newDate = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))
					if newDate - oldDate == datetime.timedelta(0):
						pass
					else:
						delta = newDate - oldDate
						diff = divmod(delta.total_seconds(), 60)
						timediff.append(diff)
						oldDate = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))

	with open('log_dui-3000.txt') as openfile:
		for line in openfile:
			read = line.split()
			for part in range(len(read)):
				if "length" in read[part - 1]:
					continue
				elif "R:" in read[part]:
					reward2.append(float(read[part][2:5]))
				elif "\'policy_average_value\'" in read[part]:
					policy_average2.append(float(read[part + 1][:5]))

		
	with open('log_dui-3000.txt') as openfile2:
		for line in openfile2:
			read = line.split()
			for part in range(len(read) - 3):
				if "2019" in read[part - 1] and "chainerrl" in read[part + 2] and "evaluat" not in read[part + 3] and "save" not in read[part + 3]:
					temp = read[part].split(":")
					temp2 = read[part - 1].split("-")
					newDate = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))
					if newDate - oldDate2 == datetime.timedelta(0):
						pass
					else:
						delta = newDate - oldDate2
						diff = divmod(delta.total_seconds(), 60)
						timediff2.append(diff)
						oldDate2 = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))

	with open('log_dui-4000.txt') as openfile:
		for line in openfile:
			read = line.split()
			for part in range(len(read)):
				if "length" in read[part - 1]:
					continue
				elif "R:" in read[part]:
					reward3.append(float(read[part][2:5]))
				elif "\'policy_average_value\'" in read[part]:
					policy_average3.append(float(read[part + 1][:5]))

		
	with open('log_dui-4000.txt') as openfile2:
		for line in openfile2:
			read = line.split()
			for part in range(len(read) - 3):
				if "2019" in read[part - 1] and "chainerrl" in read[part + 2] and "evaluat" not in read[part + 3] and "save" not in read[part + 3]:
					temp = read[part].split(":")
					temp2 = read[part - 1].split("-")
					newDate = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))
					if newDate - oldDate3 == datetime.timedelta(0):
						pass
					else:
						delta = newDate - oldDate3
						diff = divmod(delta.total_seconds(), 60)
						timediff3.append(diff)
						oldDate3 = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))

	with open('log_dui-5000.txt') as openfile:
		for line in openfile:
			read = line.split()
			for part in range(len(read)):
				if "length" in read[part - 1]:
					continue
				elif "R:" in read[part]:
					reward4.append(float(read[part][2:5]))
				elif "\'policy_average_value\'" in read[part]:
					policy_average4.append(float(read[part + 1][:5]))

		
	with open('log_dui-5000.txt') as openfile2:
		for line in openfile2:
			read = line.split()
			for part in range(len(read) - 3):
				if "2019" in read[part - 1] and "chainerrl" in read[part + 2] and "evaluat" not in read[part + 3] and "save" not in read[part + 3]:
					temp = read[part].split(":")
					temp2 = read[part - 1].split("-")
					newDate = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))
					if newDate - oldDate4 == datetime.timedelta(0):
						pass
					else:
						delta = newDate - oldDate4
						diff = divmod(delta.total_seconds(), 60)
						timediff4.append(diff)
						oldDate4 = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))

	print(sum(reward) / len(reward))
	print(sum(reward2) / len(reward2))
	print(sum(reward3) / len(reward3))
	print(sum(reward4) / len(reward4))

	print("BREAK")

	print(sum(policy_average) / len(policy_average))
	print(sum(policy_average2) / len(policy_average2))
	print(sum(policy_average3) / len(policy_average3))
	print(sum(policy_average4) / len(policy_average4))

	print("BREAK2")


	f1 = plt.figure('Reward')
	plt.plot(range(0, len(reward)), reward, color = 'r', label = 'DUI-2000')
	plt.plot(range(0, len(reward2)), reward2, color = 'b', label = 'DUI-3000')
	plt.plot(range(0, len(reward3)), reward3, color = 'g', label = 'DUI-4000')
	plt.plot(range(0, len(reward4)), reward4, color = 'purple', label = 'DUI-5000')
	plt.title("Episodic Rewards (Discriminator Update Interval)")
	plt.xlabel("Episode")
	plt.ylabel("Reward")
	plt.legend()

	f2 = plt.figure('Policy Average')
	plt.plot(range(0, len(policy_average)), policy_average, color = 'r', label = 'DUI-2000')
	plt.plot(range(0, len(policy_average2)), policy_average2, color = 'b', label = 'DUI-3000')
	plt.plot(range(0, len(policy_average3)), policy_average3, color = 'g', label = 'DUI-4000')
	plt.plot(range(0, len(policy_average4)), policy_average4, color = 'purple', label = 'DUI-5000')
	plt.title("Episodic Reward Average (Discriminator Update Interval)")
	plt.xlabel("Episode")
	plt.ylabel("Average Reward")
	plt.legend()

	print(len(timediff))
	print(len(timediff2))
	print(len(timediff3))
	print(len(timediff4))

	for num in range(len(timediff)):
		temp_min = timediff[num][0]
		temp_sec = timediff[num][1]
		timediff[num] = temp_min + (temp_sec / 100)

	# timediff.append(0.5)

	for num in range(len(timediff2)):
		temp_min = timediff2[num][0]
		temp_sec = timediff2[num][1]
		timediff2[num] = temp_min + (temp_sec / 100)

	# timediff2.append(0.5)

	for num in range(len(timediff3)):
		temp_min = timediff3[num][0]
		temp_sec = timediff3[num][1]
		timediff3[num] = temp_min + (temp_sec / 100)

	# timediff3.append(0.5)

	for num in range(len(timediff4)):
		temp_min = timediff4[num][0]
		temp_sec = timediff4[num][1]
		timediff4[num] = temp_min + (temp_sec / 100)

	# print(len(timediff), len(timediff2), len(timediff3))

	f3 = plt.figure('Runtime Difference')
	plt.scatter(range(0, len(timediff)), timediff, color = 'r', label = 'DUI-2000')
	plt.scatter(range(0, len(timediff2)), timediff2, color = 'b', label = 'DUI-3000')
	plt.scatter(range(0, len(timediff3)), timediff3, color = 'g', label = 'DUI-4000')
	plt.scatter(range(0, len(timediff4)), timediff4, color = 'purple', label = 'DUI-5000')
	plt.title("Episodic Runtimes (Discriminator Update Interval)")
	plt.xlabel("Episode")
	plt.ylabel("Runtime (Minutes)")
	plt.legend()
	plt.show()

if __name__ == "__main__": 
    main()
