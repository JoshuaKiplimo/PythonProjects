from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time
import random


class SpotifyBot:

	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot = webdriver.Chrome(executable_path = "path to driver")#instance of the bot

	def login(self):
		BOT = self.bot
		BOT.maximize_window()
		BOT.get("https://open.spotify.com/album/6trNtQUgC8cgbWcqoMYkOR")
		time.sleep(10) #pause as the page loads
		BOT.find_element('xpath', "//button[contains(.,'Log in')]").click()
		time.sleep(10)
		email = BOT.find_element_by_name("username")
		password = BOT.find_element_by_name("password")
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(20)
		BOT.find_element('xpath', '//header[@class="TrackListHeader"]//button[contains(@class,"btn-green") and .= "PLAY"]').click()

ed = SpotifyBot("username", "password")

ed.login()


