import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

file_name = 'fplrecord.txt'
data = []
with open (file_name, 'r') as f:
	lines = f.readlines()
	for line in lines:
		stripped_line = line.strip()
		line_list = stripped_line.split()

		data.append(line_list)

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
x=[]
y=[]
count =0
def animate(i):
	global count
	x.append(count)
	y.append(oarank[count])
	count += 1
	plt.plot(x,y, color = 'orange')
	plt.yscale('log')
	ticks= (1000000, 300000, 100000, 30000, 10000, 3000, 1000)
	plt.yticks(ticks)
	ax.set_yticklabels(["1M", "300k", "100k", "30k", "10k", '3k', '1k'])

	plt.locator_params(axis="x", nbins=count)

ax.set_title("OR 2021/2022 Season", fontsize= 24)
ax.tick_params(axis='both', labelsize= 14)
ax.set_xlabel("GameWeek ", fontsize= 14)
ax.set_ylabel("Overall Rank", fontsize = 14)
ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)
plt.gca().invert_yaxis()
ax.yaxis.tick_right()
plt.show()