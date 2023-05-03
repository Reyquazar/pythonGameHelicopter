# 🌲 🏥 🧡 🚁 🌊 🔥 🟩 🛢️ 🛒 ☁️ 🗲 🏆

from map import Map
import time
import os

TICK_SLEEP = 0.5

tmp = Map(20, 10)
tmp.generate_forest(3, 10)
tmp.generate_river(10)
tmp.generate_river(10)
tmp.generate_river(10)
tmp.print_map()

tick = 1

while True:
    print("\n" * 99999)
    print('TICK', tick)
    tmp.print_map()
    tick += 1
    time.sleep(TICK_SLEEP)
