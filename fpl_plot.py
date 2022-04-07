import matplotlib.pyplot as plt
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

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(range(31), oarank, linewidth = 2)
ax.set_title("FPL Rank", fontsize= 24)
ax.set_xlabel("GW", fontsize= 14)
ax.set_ylabel("rank", fontsize = 14)
ax.tick_params(axis='both', labelsize= 14)
plt.xticks(range(31))
plt.yscale('log')
ticks= (500000, 250000, 100000, 50000, 25000, 10000, 5000)
plt.yticks(ticks)
ax.set_yticklabels(["500k", "250k", "100k", "50k", '25k', '10k', '5k'])
plt.show()

