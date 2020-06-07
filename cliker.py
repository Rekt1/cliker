import pyautogui as pg
from time import sleep
pg.failsafe = True

i = 0
pg.alert("Привет, это кликер", "Кликер", button="ОК")
while i in range(1):
	num = pg.prompt("Сколько надо сделать кликов?","Кликер","10")
	time_click = pg.prompt("С каким интервалом кликать(в секундах)?","Кликер","1")
	time = pg.prompt("Через сколько начать кликать(в секундах)?","Кликер","5")
	pg.click(clicks=int(num), interval=int(time_click))