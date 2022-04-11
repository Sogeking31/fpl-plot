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

with open('team_name.txt', 'r') as f3:
	team_name = f3.read()
	team_name =team_name[2:]
	team_name =team_name[:-2]
	team_name.strip()

team_data ={
	'oarank' : data[1],
	'gwrank' : data[3],
	'gwpoints' : data[5],
	'oapoints' : data[7],
	'tv' : data[9],
}
for key in team_data:
	team_data[key] = [x.replace(',','') for x in team_data[key]]
	team_data[key] = [x.replace('[','') for x in team_data[key]]
	team_data[key] = [x.replace(']','') for x in team_data[key]]
	team_data[key] = [x.replace("'","") for x in team_data[key]]
	try:
		team_data[key] = [int(x) for x in team_data[key]]
	except ValueError:
		team_data[key] = [float(x) for x in team_data[key]]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots(1,1,figsize=(12,6))
fig.patch.set_facecolor('White')
plt.margins(0)
plt.subplots_adjust(left=0.075, right=0.95, top=0.925, bottom=0.1)

textboxes=[]
x=[1]
y=[team_data['oarank'][0]]
count =1

def animate(i):
	global count
	x.append(count)
	y.append(team_data['oarank'][count-1])
	s= line_slope(y[-2], y[-1])

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
	
	plt.plot([x[-2], x[-1]], [y[-2],y[-1]], color = color)

	for key in chips:
		if f'GW{x[-1]}' == key:
			if chips[key] == 'Wildcard':
				plt.text(x[-1], y[-1], 'WC', color = ('Purple'))
			elif chips[key] == 'FreeHit':
				plt.text(x[-1], y[-1], 'FH', color = ('Purple'))
			elif chips[key] == 'BenchBoost':
				plt.text(x[-1], y[-1], 'BB', color = ('Purple'))
			elif chips[key] == 'TripleCaptain':
				plt.text(x[-1], y[-1], 'TC', color = ('Purple'))

	plt.yscale('log')
	ticks= (1000000, 300000, 100000, 30000, 10000, 3000, 1000)
	plt.yticks(ticks)
	ax.set_yticklabels(["1M", "300k", "100k", "30k", "10k", '3k', '1k'])
	plt.locator_params(axis="x", nbins=count)

	try:
		textboxes[-1].remove()
	except IndexError:
		pass

	text = f"GW# {x[-1]}\nOR: {y[-1]:,}\nGW rank: {team_data['gwrank'][count-1]:,}\nTeam Value: {team_data['tv'][count-1]}"
	props = dict(boxstyle='round', facecolor='Green', alpha=0.4)
	textbox = ax.text(0.05, 0.95, text, transform=ax.transAxes,
	 fontsize=12, verticalalignment='top', bbox=props)
	textboxes.append(textbox)

	count += 1	

def line_slope(y1, y2):
    s = ((y1 - y2)/y1)
    return s

print(f'{123456789:,}')
ax.set_title(f"{team_name} 2021/2022 Season Rank Progression",
 fontsize= 24, color = ('Purple'))
ax.tick_params(axis='both', labelsize= 12)
ax.set_xlabel("Gameweek", fontsize= 18)
ax.set_ylabel("Overall Rank", fontsize = 18)

ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)
plt.gca().invert_yaxis()
ax.tick_params(labeltop=False, labelright=True)
plt.show()