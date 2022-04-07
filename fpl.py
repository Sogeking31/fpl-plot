import webbrowser
import requests
import bs4
from selenium import webdriver
path = "C:/Users/q8_a7/Desktop/fpl/driver_file/geckodriver.exe"
driver = webdriver.Firefox(executable_path= r'C:/Users/q8_a7/Desktop/fpl/driver_file/geckodriver.exe')

team_id = '1014'
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




