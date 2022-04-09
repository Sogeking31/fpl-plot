import matplotlib.animation as animation
import matplotlib.pyplot as plt
import json

file_name = 'fplrecord.txt'
data = []
with open (file_name, 'r') as f:
	lines = f.readlines()
	for line in lines:
		stripped_line = line.strip()
		line_list = stripped_line.split()
		data.append(line_list)

file_name2 = 'chipsrecord.txt'
with open(file_name2, 'r') as f2:
	data2 = f2.read()
chips = json.loads(data2)

oarank = data[1]
gwrank = data[3]
gwpoints = data[5]
oapoints = data[7]
tv = data[9]

oarank = [x.replace(',','') for x in oarank]
oarank = [x.replace('[','') for x in oarank]
oarank = [x.replace(']','') for x in oarank]
oarank = [x.replace("'","") for x in oarank]

oarank = [int(x) for x in oarank]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots(1,1,figsize=(12,6))
x=[0]
y=[oarank[0]]
count =1

def animate(i):
	global count
	x.append(count)
	y.append(oarank[count-1])
	s= line_slope(y[count-1], y[count])

	if -0.15 >= s > -0.3:
		color = "#FF9999"
	elif -0.3 >= s > -0.75:
		color = "#FF3333"
	elif s <= -0.75:
		color = "#CC0000"
	elif 0.1 <= s < 0.2:
		color = "#99FF99"
	elif 0.2 <= s < 0.5:
		color = "#33FF33"
	elif s >= 0.5:
		color = "#00CC00"
	else:
		color = "#A0A0A0"
	
	plt.plot([x[count-1], x[count]], [y[count-1],y[count]], color = color)

	for key in chips:
		if f'GW{x[-1]}' == key:
			if chips[key] == 'Wildcard':
				plt.text(x[-1], y[-1], 'WC')
			elif chips[key] == 'FreeHit':
				plt.text(x[-1], y[-1], 'FH')
			if chips[key] == 'BenchBoost':
				plt.text(x[-1], y[-1], 'BB')
			if chips[key] == 'TripleCaptain':
				plt.text(x[-1], y[-1], 'TC')

	plt.yscale('log')
	ticks= (1000000, 300000, 100000, 30000, 10000, 3000, 1000)
	plt.yticks(ticks)
	ax.set_yticklabels(["1M", "300k", "100k", "30k", "10k", '3k', '1k'])
	plt.locator_params(axis="x", nbins=count)
	count += 1

def line_slope(y1, y2):
    s = ((y1 - y2)/y1)
    return s

ax.set_title("OR 2021/2022 Season", fontsize= 24)
ax.tick_params(axis='both', labelsize= 14)
ax.set_xlabel("GameWeek ", fontsize= 14)
ax.set_ylabel("Overall Rank", fontsize = 14)

ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)
plt.gca().invert_yaxis()
ax.yaxis.tick_right()
plt.show()