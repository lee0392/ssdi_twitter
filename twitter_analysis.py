import re
import operator
import datetime

data = [[]]
count1 = {}
count2 = {}
interval = {}

def getData():
	global data
	file = open("'charlotte'.txt", 'r')
	matches = re.findall('(\w+) \\[([^\\]]*)\\] "([^"]*)" ([^ ]*) ([^ ]*\n)',file.read())
	for match in matches:
		data.append(match)
	return

def findHighestTweeter1():
	global data
	for i in range(len(data)):
		x = 1
		y = int(data[i][3])
		if data[i][0] not in count1:
			for j in range(i+1, len(data)):
				if data[j][0]==data[i][0]:
					x = x + 1
			count1[data[i][0]] = [x,0,y]
	return


def findHighestTweets():
	global data
	global count2
	temp = {}
	for i in range(len(data)):
		temp[i] = int(data[i][4].replace('\n',''))
	count2 = sorted(temp.items(), key=operator.itemgetter(1),reverse=True)
	return

def displayDict(dict,n,index):
	#iterator = iter(dict.items())
	print('\nResult:\n')
	for i in range(n):
		print(dict[i][0]+" : "+str(dict[i][1][index]))
	print('\n')

def displayTweets(dict,n):
	#iterator = iter(dict.items())
	print('\nResult:\n')
	for i in range(n):
		print(data[dict[i][0]][2]+" : "+str(dict[i][1]))
	print('\n')


def disp_perhr_tweet(n):
	for i in range(len(interval)):
		sorted_dict = sorted(interval[i][2].items(), key=operator.itemgetter(1),reverse=True)
		print("Top users for time Interval: From " + interval[i][0].strftime("%Y-%m-%d %H:%M:%S")+" till "+interval[i][1].strftime("%Y-%m-%d %H:%M:%S"))
		for j in range(n):
			print(sorted_dict[j][0]+" : "+str(sorted_dict[j][1]))
			

def gettime(str):
	dt = datetime.datetime.strptime(str, "%d/%b/%Y:%H:%M:%S ")
	return dt

def timediff(diff):
	days = diff.days
	temp = days * 24
	diff2 = (diff.seconds) / 3600
	tot_hrs = temp + diff2
	return tot_hrs

def findHighestTweeter2(start,last):
	global data
	count3 = {}
	for i in range(start,last):
		x = 1
		if data[i][0] not in count3:
			for j in range(i+1, last):
				if data[j][0]==data[i][0]:
					x = x + 1
			count3[data[i][0]] = x
	return count3

def getEveryHourTweets():
	global data
	global interval
	c = 0
	i = 0
	new_s = 0
	while (i + new_s)<len(data):
		i = i + new_s
		parent_time = gettime(data[i][1])
		for j in range(i+1, len(data)):
			cur_time = gettime(data[j][1])
			if timediff(cur_time-parent_time)>1 or j==(len(data)-1):
				temp = findHighestTweeter2(i,j)
				interval[c] = [parent_time,gettime(data[j-1][1]),temp]
				c = c + 1
				new_s = j
				


getData()
del data[0]
findHighestTweeter1()
findHighestTweets()
getEveryHourTweets()


while 1:
	query = int(input("\nChoose Options:\npress 0 for top n users who have tweeted the most for the entire timeline\npress 1 for top n users who have tweeted the most for every hour\npress 2 for top n users who have the maximum followers\npress 3 for top n tweets which have the maximum retweet count\npress 4 for exit\n\n"));


	if query==0:
		n1 = int(input("Enter n to know top n users who have tweeted the most for the entire timeline : "))
		sorted_dict = sorted(count1.items(), key=lambda i: i[1][0], reverse=True)
		displayDict(sorted_dict,n1,0)

	elif query==1:
		n1 = int(input("Enter n to know top n users who have tweeted the most for every hour : "))
		disp_perhr_tweet(n1)
		

	elif query==2:
		n1 = int(input("Enter n to know top n users who have the maximum followers : "))
		sorted_dict = sorted(count1.items(), key=lambda i: i[1][2], reverse=True)
		displayDict(sorted_dict,n1,2)

	elif query==3:
		n1 = int(input("Enter n to know top n tweets which have the maximum retweet count : "))
		displayTweets(count2,n1)
	else:
		break

