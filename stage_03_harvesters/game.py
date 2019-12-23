# -*- coding: utf-8 -*-

# pip install -r requirements.txt

from astrobox.space_field import SpaceField

from KhizhovDrone import KhizhovDrone
from stage_03_harvesters.driller import DrillerDrone
from stage_03_harvesters.reaper import ReaperDrone

NUMBER_OF_DRONES = 5

if __name__ == '__main__':
    scene = SpaceField(
        speed=5,
        field=(1000, 900),
        asteroids_count=20,
    )
    team_1 = [KhizhovDrone() for _ in range(NUMBER_OF_DRONES)]
    # team_2 = [ReaperDrone() for _ in range(NUMBER_OF_DRONES)]
    team_3 = [DrillerDrone() for _ in range(NUMBER_OF_DRONES)]
    scene.go()

