# -*- coding: utf-8 -*-

# pip install -r requirements.txt

from astrobox.space_field import SpaceField
from stage_03_harvesters.driller import DrillerDrone
from stage_03_harvesters.reaper import ReaperDrone
from stage_04_soldiers.devastator import DevastatorDrone
from KhizhovDrone import KhizhovDrone

NUMBER_OF_DRONES = 5

if __name__ == '__main__':
    scene = SpaceField(
        field=(1500, 900),
        speed=3,
        asteroids_count=10,
        can_fight=True,
        max_drones_at_team=12,
        # headless=True,
    )

    team_2 = [ReaperDrone() for _ in range(NUMBER_OF_DRONES)]
    team_1 = [KhizhovDrone() for _ in range(NUMBER_OF_DRONES)]
    team_3 = [DrillerDrone() for _ in range(NUMBER_OF_DRONES)]
    team_4 = [DevastatorDrone() for _ in range(NUMBER_OF_DRONES)]


    scene.go()
    team_1[0].game_over()


# Четвертый этап: зачёт!
