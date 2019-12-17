
from matplotlib import pyplot as plt
import datetime


def main():
	reward = []
	policy_average = []
	reward2 = []
	policy_average2 = []
	reward3 = []
	policy_average3 = []
	# reward4 = []
	# policy_average4 = []
	oldDate = datetime.datetime(2019, 12, 11, 13, 17, 18)
	oldDate2 = datetime.datetime(2019, 12, 11, 13, 29, 27)
	oldDate3 = datetime.datetime(2019, 12, 11, 13, 32, 11)
	# oldDate4 = datetime.datetime(2019, 12, 7, 21, 57, 53)
	timediff = []
	timediff2 = []
	timediff3 = []
	# timediff4 = []

	with open('log_orw-6.txt') as openfile:
		for line in openfile:
			read = line.split()
			for part in range(len(read)):
				if "length" in read[part - 1]:
					continue
				elif "R:" in read[part]:
					reward.append(float(read[part][2:5]))
				elif "\'policy_average_value\'" in read[part]:
					policy_average.append(float(read[part + 1][:5]))

		
	with open('log_orw-6.txt') as openfile2:
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

	with open('log_orw-8.txt') as openfile:
		for line in openfile:
			read = line.split()
			for part in range(len(read)):
				if "length" in read[part - 1]:
					continue
				elif "R:" in read[part]:
					reward2.append(float(read[part][2:5]))
				elif "\'policy_average_value\'" in read[part]:
					policy_average2.append(float(read[part + 1][:5]))

		
	with open('log_orw-8.txt') as openfile2:
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

	with open('log_orw-10a.txt') as openfile:
		for line in openfile:
			read = line.split()
			for part in range(len(read)):
				if "length" in read[part - 1]:
					continue
				elif "R:" in read[part]:
					reward3.append(float(read[part][2:5]))
				elif "\'policy_average_value\'" in read[part]:
					policy_average3.append(float(read[part + 1][:5]))

		
	with open('log_orw-10a.txt') as openfile2:
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

	# with open('log_pui-1000.txt') as openfile:
	# 	for line in openfile:
	# 		read = line.split()
	# 		for part in range(len(read)):
	# 			if "length" in read[part - 1]:
	# 				continue
	# 			elif "R:" in read[part]:
	# 				reward4.append(float(read[part][2:5]))
	# 			elif "\'policy_average_value\'" in read[part]:
	# 				policy_average4.append(float(read[part + 1][:5]))

		
	# with open('log_pui-1000.txt') as openfile2:
	# 	for line in openfile2:
	# 		read = line.split()
	# 		for part in range(len(read) - 3):
	# 			if "2019" in read[part - 1] and "chainerrl" in read[part + 2] and "evaluat" not in read[part + 3] and "save" not in read[part + 3]:
	# 				temp = read[part].split(":")
	# 				temp2 = read[part - 1].split("-")
	# 				newDate = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))
	# 				if newDate - oldDate4 == datetime.timedelta(0):
	# 					pass
	# 				else:
	# 					delta = newDate - oldDate4
	# 					diff = divmod(delta.total_seconds(), 60)
	# 					timediff4.append(diff)
	# 					oldDate4 = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))


	f1 = plt.figure('Reward')
	plt.plot(range(0, 908), reward, color = 'r', label = 'ORW-6')
	plt.plot(range(0, 898), reward2, color = 'b', label = 'ORW-8')
	plt.plot(range(0, 945), reward3, color = 'g', label = 'ORW-10')
	# plt.plot(range(0, 541), reward4, color = 'purple', label = 'PUI-1000')
	plt.title("Episodic Rewards (Original Reward Weight)")
	plt.xlabel("Episode")
	plt.ylabel("Reward")
	plt.legend()

	f2 = plt.figure('Policy Average')
	plt.plot(range(0, 908), policy_average, color = 'r', label = 'ORW-6')
	plt.plot(range(0, 898), policy_average2, color = 'b', label = 'ORW-8')
	plt.plot(range(0, 945), policy_average3, color = 'g', label = 'ORW-10')
	# plt.plot(range(0, 541), policy_average4, color = 'purple', label = 'PUI-1000')
	plt.title("Episodic Reward Average (Original Reward Weight)")
	plt.xlabel("Episode")
	plt.ylabel("Average Reward")
	plt.legend()

	for num in range(len(timediff)):
		temp_min = timediff[num][0]
		temp_sec = timediff[num][1]
		timediff[num] = temp_min + (temp_sec / 100)

	timediff.append(0.5)

	for num in range(len(timediff2)):
		temp_min = timediff2[num][0]
		temp_sec = timediff2[num][1]
		timediff2[num] = temp_min + (temp_sec / 100)

	timediff2.append(0.5)

	for num in range(len(timediff3)):
		temp_min = timediff3[num][0]
		temp_sec = timediff3[num][1]
		timediff3[num] = temp_min + (temp_sec / 100)

	# timediff3.append(0.5)

	# for num in range(len(timediff4)):
	# 	temp_min = timediff4[num][0]
	# 	temp_sec = timediff4[num][1]
	# 	timediff4[num] = temp_min + (temp_sec / 100)

	# print(len(timediff), len(timediff2), len(timediff3))

	f3 = plt.figure('Runtime Difference')
	plt.scatter(range(0, 908), timediff, color = 'r', label = 'ORW-6')
	plt.scatter(range(0, 898), timediff2, color = 'b', label = 'ORW-8')
	plt.scatter(range(0, 945), timediff3, color = 'g', label = 'ORW-10')
	# plt.scatter(range(0, 541), timediff4, color = 'purple', label = 'PUI-1000')
	plt.title("Episodic Runtimes (Original Reward Weight)")
	plt.xlabel("Episode")
	plt.ylabel("Runtime (Minutes)")
	plt.legend()
	plt.show()

if __name__ == "__main__": 
    main()
