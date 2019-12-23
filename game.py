# -*- coding: utf-8 -*-

from astrobox.space_field import SpaceField
from KhizhovDrone import KhizhovDrone
from stage_03_harvesters.reaper import ReaperDrone
from stage_03_harvesters.driller import DrillerDrone
from stage_03_harvesters.vader import VaderDrone
DRONE_COUNT = 5

if __name__ == '__main__':
    scene = SpaceField(
        field=(1000, 900),
        speed=3,
        asteroids_count=10,
        can_fight=False,
    )
    my_team = []
    enemy_team = []
    my_drones = [KhizhovDrone() for i in range(DRONE_COUNT)]
    for drone in my_drones:
        my_team.append(drone)
    enemy_drones = [DrillerDrone() for i in range(DRONE_COUNT)]
    # enemy_drones2 = [ReaperDrone() for i in range(DRONE_COUNT)]
    # enemy_drones3 = [VaderDrone() for i in range(DRONE_COUNT)]

    scene.go()
    my_drones[0].game_over()

#  на Windows 1.3.0 Теперь не вылетаетет,выдает GameOver при завешении игры, а мою статистику не выдает.
#  Процесс не завершается
#  А на убунту всё норм, выдает GameOver и при закрытии окна выдает мою статистику

# - тестирую на Ubuntu, поэтому могу не заметить, что есть косяки в Windows

# Второй этап: зачёт!
