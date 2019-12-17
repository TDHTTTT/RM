
from matplotlib import pyplot as plt
import datetime


def main():
	reward = []
	policy_average = []
	reward2 = []
	policy_average2 = []
	oldDate = datetime.datetime(2019, 12, 11, 13, 32, 11)
	timediff = []
	with open('log_orw-10a.txt') as openfile:
		for line in openfile:
			read = line.split()
			for part in range(len(read)):
				if "length" in read[part - 1]:
					continue
				elif "R:" in read[part]:
					print(read[part][2:9])
					reward.append(float(read[part][2:5]))
				elif "\'policy_average_value\'" in read[part]:
					print(read[part + 1][:5])
					policy_average.append(float(read[part + 1][:5]))

		
	with open('log_orw-10a.txt') as openfile2:
		for line in openfile2:
			read = line.split()
			for part in range(len(read) - 3):
				if "2019" in read[part - 1] and "chainerrl" in read[part + 2] and "evaluat" not in read[part + 3] and "save" not in read[part + 3]:
					temp = read[part].split(":")
					temp2 = read[part - 1].split("-")
					newDate = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))
					print(newDate - oldDate)
					if newDate - oldDate == datetime.timedelta(0):
						pass
					else:
						delta = newDate - oldDate
						diff = divmod(delta.total_seconds(), 60)
						timediff.append(diff)
						oldDate = datetime.datetime(int(temp2[0]), int(temp2[1]), int(temp2[2]), int(temp[0]), int(temp[1]), int(temp[2][:2]))

	# with open('log1r_92.txt') as openfile:
	# 	for line in openfile:
	# 		read = line.split()
	# 		for part in range(len(read)):
	# 			if "R:" in read[part]:
	# 				print(read[part][2:9])
	# 				reward2.append(float(read[part][2:5]))
	# 			elif "\'policy_average_value\'" in read[part]:
	# 				print(read[part + 1][:5])
	# 				policy_average2.append(float(read[part + 1][:5]))

	print(sum(reward) / len(reward))
	print(len(timediff))

	f1 = plt.figure('Reward')
	plt.plot(range(0, 945), reward, color = 'g', label = 'Baseline GAIL')
	# plt.plot(range(0, 93), reward2, color = 'r', label = 'Improved GAIL')
	plt.title("Episodic Rewards")
	plt.xlabel("Episode")
	plt.ylabel("Reward")
	plt.legend()

	f2 = plt.figure('Policy Average')
	plt.plot(range(0, 945), policy_average, color = 'g', label = 'Baseline GAIL')
	# plt.plot(range(0, 93), policy_average2, color = 'r', label = 'Improved GAIL')
	plt.title("Episodic Reward Average")
	plt.xlabel("Episode")
	plt.ylabel("Average Reward")
	plt.legend()
	plt.show()

if __name__ == "__main__": 
    main()