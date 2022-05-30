from asyncio.windows_events import NULL
from re import I
from tkinter import *
from tkinter import ttk

from datetime import datetime
import time

import json
from data import dex
from functools import partial

import sim.sim as sim
from tools.pick_six import generate_team

with open('data/domains/all.json') as f:
    domain_all = json.load(f)

uber = [94, 115, 150, 249, 250, 257, 373, 376, 382, 383, 384, 386, 448, 483, 484, 487, 491, 492, 493, 643, 644, 645, 646, 649, 681, 716, 717, 718, 791, 792, 795, 800, 802, 804]
ou = [3, 6, 36, 38, 65, 94, 105, 113, 127, 130, 145, 149, 151, 212, 227, 230, 248, 260, 279, 302, 303, 308, 381, 428, 445, 462, 465, 485, 490, 494, 530, 598, 625, 637, 645, 646, 647, 658, 701, 718, 719, 745, 748, 778, 785, 786, 787, 788, 797, 798, 801] # 2500 sec
uu = [9, 15, 18, 34, 59, 73, 82, 89, 121, 142, 169, 184, 205, 212, 214, 226, 242, 243, 244, 245, 251, 254, 260, 306, 310, 319, 334, 342, 376, 380, 392, 395, 450, 468, 472, 473, 479, 482, 497, 553, 555, 591, 594, 609, 612, 620, 630, 635, 638, 639, 700, 707, 721, 730, 793] # 2700 sec
ru = [3, 9, 31, 51, 68, 91, 135, 142, 143, 146, 160, 181, 195, 196, 197, 207, 208, 232, 233, 235, 264, 277, 282, 323, 324, 330, 350, 354, 362, 379, 407, 430, 437, 452, 460, 464, 479, 488, 492, 526, 589, 596, 632, 648, 652, 671, 675, 680, 691, 695, 697, 706, 718, 719, 720, 724, 752, 758, 760, 763, 764, 768, 779, 781, 784] # 3269 sec
nu = [28, 42, 45, 80, 85, 106, 112, 123, 134, 139, 157, 178, 199, 208, 213, 215, 221, 229, 237, 254, 297, 344, 424, 429, 442, 454, 478, 479, 479, 480, 500, 503, 531, 537, 547, 560, 561, 569, 573, 584, 593, 615, 617, 621, 628, 640, 655, 666, 683, 687, 693, 699, 727, 738, 774, 799] # 2366 sec


# print(f"uber: {len(uber)}, ou: {len(ou)}, uu: {len(uu)}, ru: {len(ru)}, nu: {len(nu)}\n")
# uber: 34, ou: 51, uu: 55, ru: 65, nu: 56


def launch_battle():

    tps1 = time.process_time()
    logname = "uber.csv"
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Starting : {current_time}\n")
    mat = []

    f = open(logname,"a")

    for i in uber :
        
        tpsline1 = time.process_time()
        
        print(f"Fights versus {i} started..\n")
        line = []

        for j in uber:

            pokemons = [[i-1], [j-1]]

            p1 = 0
            p2 = 0
            match = 0

            for k in range(1000) :

                teams = []
                teams.append(sim.dict_to_team_set(generate_team(num_pokemon=1,pokemon_list=pokemons[0])))
                teams.append(sim.dict_to_team_set(generate_team(num_pokemon=1,pokemon_list=pokemons[1])))
                
                battle = sim.Battle('single', 'Nic', teams[0], 'Sam', teams[1], debug=False)

                sim.run(battle)
                winner = battle.winner

                # stats for logs
                if winner == 'p2':
                    p2 += 1
                elif winner == 'p1':
                    p1 +=1

                match+=1
                
            # stats for logs                    
            f.write(f"{i}, {j}, {p1/match}\n")

        
        tpsline2 = time.process_time()
        print(f"Duration : {tpsline2 - tpsline1} sec")

        mat.append(line)

    tps2 = time.process_time()
    print(f"\nDuration : {tps2 - tps1} sec")

if __name__ == "__main__" :

    print("MAIN :\n")

    print("battle started")
    launch_battle()

