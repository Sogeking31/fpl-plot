import matplotlib.animation as animation
import matplotlib.pyplot as plt
import json
plt.rcParams['animation.ffmpeg_path'] = r'C:\\Users\\q8_a7\\Desktop\\ffmpeg\\bin\\ffmpeg.exe'

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
textboxes2=[]
x=[1]
y=[team_data['oarank'][0]]
gw_list=[]
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
	ticks= (1000000, 500000, 250000, 100000, 50000, 25000, 10000)
	plt.yticks(ticks)
	ax.set_yticklabels(["1M", "500k", "250k", "100k", "50k", '25k', '10k'])
	plt.locator_params(axis="x", nbins=count)

	try:
		textboxes[-1].remove()
	except IndexError:
		pass

	text = f"GW# {x[-1]}\nOR: {y[-1]:,}\nGW rank: {team_data['gwrank'][count-1]:,}\nTeam Value: {team_data['tv'][count-1]}"
	props = dict(boxstyle='round', facecolor='#00CC00', alpha=0.3)
	textbox = ax.text(0.025, 0.95, text, transform=ax.transAxes,
	 fontsize=12, verticalalignment='top', bbox=props)
	textboxes.append(textbox)

	gw_list.append(team_data['gwrank'][count-1])
	b = min(y)
	b2 = min(gw_list)
	location_b = y.index(b)
	location_b2 = gw_list.index(b2)

	try:
		textboxes2[-1].remove()
	except IndexError:
		pass

	text2 = f"Best OR: {b:,} in GW# {x[location_b]}\nBest GW Rank: {b2:,} in GW# {x[location_b2]+1}"
	props2 = dict(boxstyle='round', facecolor='#00CC00', alpha=0.3)
	textbox2 = ax.text(0.2, 0.95, text2, transform=ax.transAxes,
	 fontsize=12, verticalalignment='top', bbox=props2)
	textboxes2.append(textbox2)

	count += 1	

def line_slope(y1, y2):
    s = ((y1 - y2)/y1)
    return s

ax.set_title(f"{team_name} 2021/2022 Season Rank Progression",
 fontsize= 24, color = ('Purple'))
ax.tick_params(axis='both', labelsize= 12)
ax.set_xlabel("Gameweek", fontsize= 18, color= 'Purple')
ax.set_ylabel("Overall Rank", fontsize = 18, color= 'Purple')

ani = animation.FuncAnimation(plt.gcf(), animate,frames=len(team_data['gwrank'])-1, interval=1000, repeat = False)
plt.gca().invert_yaxis()
ax.tick_params(labeltop=False, labelright=True)

f5 = r"c://Users/q8_a7/Desktop/animation5.mp4" 
writervideo = animation.FFMpegWriter(fps=60)  
plt.show()

fig.canvas.draw()
ani.event_source.stop()
ani.save(f5, writer=writervideo)