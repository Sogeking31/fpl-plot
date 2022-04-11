import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
import json

path = "C:/Users/q8_a7/Desktop/fpl/driver_file/geckodriver.exe"
driver = webdriver.Firefox(executable_path= r'C:/Users/q8_a7/Desktop/fpl/driver_file/geckodriver.exe')

team_id = '3371560'
headers={'user-agent': 'Mozilla/5.0'}
driver.get(f"https://fantasy.premierleague.com/entry/{team_id}/history")
soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
i = 1
oarank, gwrank, gwpoints, oapoints, tv= [], [], [], [], []
for x in range(38):
	try:
		elems_gwp = soup.select(f'table.Table-ziussd-1:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(2)')
		elems_oap = soup.select(f'table.Table-ziussd-1:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(7)')
		elems_tv = soup.select(f'table.Table-ziussd-1:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(9)')
		elems_oar = soup.select(f'table.Table-ziussd-1:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(8)')
		elems_gwr = soup.select(f'table.Table-ziussd-1:nth-child(1) > tbody:nth-child(2) > tr:nth-child({i}) > td:nth-child(4)')
		oarank.append(elems_oar[0].text)
		gwrank.append(elems_gwr[0].text)
		gwpoints.append(elems_gwp[0].text)
		oapoints.append(elems_oap[0].text)
		tv.append(elems_tv[0].text)

		i += 1
	except IndexError:
		break

def remove_tags(html):
	soup = BeautifulSoup(html, "html.parser")
	for data in soup(['style', 'script']):
		data.decompose()
	return ' '.join(soup.stripped_strings)

c = 1
chips_gw=[]
chips=[]
used_chips={}
for x in range(6):
	try:
		elems_chp = soup.select(f'div.gdTvZ:nth-child(3) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child({c}) > td:nth-child(2)')
		elems_gwc = soup.select(f'div.gdTvZ:nth-child(3) > table:nth-child(2) > tbody:nth-child(2) > tr:nth-child({c}) > td:nth-child(3)')

		html_doc = f"""{elems_chp}""" 
		html_doc2 = f"""{elems_gwc}""" 
		chips_gw.append(remove_tags(html_doc2))
		chips.append(remove_tags(html_doc))
		chips = [x.replace('[','') for x in chips]
		chips = [x.replace(']','') for x in chips]
		chips = [x.replace(' ','') for x in chips]

		chips_gw = [x.replace('[','') for x in chips_gw]
		chips_gw = [x.replace(']','') for x in chips_gw]
		chips_gw = [x.replace(' ','') for x in chips_gw]
		
		c += 1
	except IndexError:
		break

elems_nm = soup.select(f'.eQebeb > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(1)')
html_nm = f"""{elems_nm}"""
team_name = remove_tags(html_nm)
with open('team_name.txt', 'w') as f:
	f.write(team_name)

lines =[oarank, gwrank, gwpoints, oapoints, tv]
with open('fplrecord.txt', 'w') as f:
    f.write(f"oarank:\n{oarank} \n")
    f.write(f"gwrank:\n{gwrank} \n")
    f.write(f"gwpoints:\n{gwpoints} \n")
    f.write(f"oapoints:\n{oapoints} \n")
    f.write(f"tv:\n{tv} \n")

g = 0
for gw in chips_gw:
	used_chips[gw] = chips[g]
	g += 1
with open('chipsrecord.txt', 'w') as f:
	f.write(json.dumps(used_chips))







