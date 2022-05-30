from asyncio.windows_events import NULL
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

def ending() :
    """ Ending function, called at the end of the process"""

    root.quit()


def launch_battle():

    tps1 = time.process_time()
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Starting : {current_time}\n")

    battle_number = int(battle_number_entry.get())

    pokemons = get_entry()

    # battle stats 
    match = 0
    player2 = 0
    player1 = 0 

    for i in range(battle_number):

        teams = []
        teams.append(sim.dict_to_team_set(generate_team(pokemon_list=pokemons[0])))
        teams.append(sim.dict_to_team_set(generate_team(pokemon_list=pokemons[1])))
        
        battle = sim.Battle('single', 'Nic', teams[0], 'Sam', teams[1], debug=False)
        # print(battle.p1.pokemon)
        # print(teams)

        sim.run(battle)
        winner = battle.winner

        # stats for logs
        if winner == 'p2':
            player2 += 1
        if winner == 'p1':
            player1 += 1
        
        match += 1

    team_p1 = []
    team_p2 = []

    n=0
    for n in range(6) :
        pokemon_p1 = battle.p1.pokemon[n] 
        pokemon_p2 = battle.p2.pokemon[n]
        team_p1.append(pokemon_p1.name)
        team_p2.append(pokemon_p2.name)

    print("Teams : \n")
    print("Player 1 :  " + str(team_p1))
    print("Player 2 :  " + str(team_p2) + "\n\n")

    print("Win poucentage : \n")
    print("Player 1 : " + str(float((player1*100)/match)) + " (" + str(player1) + "/" + str(match) +").")
    print("Player 2 : " + str(float((player2*100)/match)) + " (" + str(player2) + "/" + str(match) +").")

    tps2 = time.process_time()
    print(f"\nDuration : {tps2 - tps1} sec")

    ending()


def get_entry():

    try:
        teams_a_b = []

        team_a = [int(team_a_1.get()), int(team_a_2.get()), int(team_a_3.get()), int(team_a_4.get()), int(team_a_5.get()), int(team_a_6.get())]
        team_b = [int(team_b_1.get()), int(team_b_2.get()), int(team_b_3.get()), int(team_b_4.get()), int(team_b_5.get()), int(team_b_6.get())]

        teams_a_b.append(team_a)
        teams_a_b.append(team_b)

        return teams_a_b

    except ValueError:
        pass
  

def actualise() :

    teams = get_entry()

    team_a = teams[0]
    team_b = teams[1]

    pokedex = list(domain_all)

    team_a_variables = [pokemon_a_1, pokemon_a_2, pokemon_a_3, pokemon_a_4, pokemon_a_5, pokemon_a_6]
    team_b_variables = [pokemon_b_1, pokemon_b_2, pokemon_b_3, pokemon_b_4, pokemon_b_5, pokemon_b_6]

    k=0
    for j in team_b_variables :
        if team_b[k] == -1 :
            pass
        else :
            text_variable = pokedex[team_b[k]]
            j.configure(text=text_variable)
        k+=1

    k=0
    for i in team_a_variables :
        if team_a[k] == -1 :
            pass
        else :
            text_variable = pokedex[team_a[k]]
            i.configure(text=text_variable)
        k+=1

    


# ________TKINTER_________

root = Tk()
root.title("Pokemon Battle")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

team_a_1 = StringVar()
teams_a_entry_1 = ttk.Entry(mainframe, width=7, textvariable=team_a_1)
teams_a_entry_1.grid(column=2, row=1, sticky=(W, E))
pokemon_a_1 = ttk.Label(mainframe, text="pokemon 1")
pokemon_a_1.grid(column=1, row=1, sticky=(W, E))

team_a_2 = StringVar()
teams_a_entry_2 = ttk.Entry(mainframe, width=7, textvariable=team_a_2)
teams_a_entry_2.grid(column=2, row=2, sticky=(W, E))
pokemon_a_2 = ttk.Label(mainframe, text= "pokemon 2")
pokemon_a_2.grid(column=1, row=2, sticky=(W, E))

team_a_3 = StringVar()
teams_a_entry_3 = ttk.Entry(mainframe, width=7, textvariable=team_a_3)
teams_a_entry_3.grid(column=2, row=3, sticky=(W, E))
pokemon_a_3 = ttk.Label(mainframe, text= "pokemon 3")
pokemon_a_3.grid(column=1, row=3, sticky=(W, E))

team_a_4 = StringVar()
teams_a_entry_4 = ttk.Entry(mainframe, width=7, textvariable=team_a_4)
teams_a_entry_4.grid(column=2, row=4, sticky=(W, E))
pokemon_a_4 = ttk.Label(mainframe, text= "pokemon 4")
pokemon_a_4.grid(column=1, row=4, sticky=(W, E))

team_a_5 = StringVar()
teams_a_entry_5 = ttk.Entry(mainframe, width=7, textvariable=team_a_5)
teams_a_entry_5.grid(column=2, row=5, sticky=(W, E))
pokemon_a_5 = ttk.Label(mainframe, text= "pokemon 5")
pokemon_a_5.grid(column=1, row=5, sticky=(W, E))

team_a_6 = StringVar()
teams_a_entry_6 = ttk.Entry(mainframe, width=7, textvariable=team_a_6)
teams_a_entry_6.grid(column=2, row=6, sticky=(W, E))
pokemon_a_6 = ttk.Label(mainframe, text= "pokemon 6")
pokemon_a_6.grid(column=1, row=6, sticky=(W, E))

team_b_1 = StringVar()
teams_b_entry_1 = ttk.Entry(mainframe, width=7, textvariable=team_b_1)
teams_b_entry_1.grid(column=3, row=1, sticky=(W, E))
pokemon_b_1 = ttk.Label(mainframe, text= "pokemon 1")
pokemon_b_1.grid(column=4, row=1, sticky=(W, E))

team_b_2 = StringVar()
teams_b_entry_2 = ttk.Entry(mainframe, width=7, textvariable=team_b_2)
teams_b_entry_2.grid(column=3, row=2, sticky=(W, E))
pokemon_b_2 = ttk.Label(mainframe, text= "pokemon 2")
pokemon_b_2.grid(column=4, row=2, sticky=(W, E))

team_b_3 = StringVar()
teams_b_entry_3 = ttk.Entry(mainframe, width=7, textvariable=team_b_3)
teams_b_entry_3.grid(column=3, row=3, sticky=(W, E))
pokemon_b_3 = ttk.Label(mainframe, text= "pokemon 3")
pokemon_b_3.grid(column=4, row=3, sticky=(W, E))

team_b_4 = StringVar()
teams_b_entry_4 = ttk.Entry(mainframe, width=7, textvariable=team_b_4)
teams_b_entry_4.grid(column=3, row=4, sticky=(W, E))
pokemon_b_4 = ttk.Label(mainframe, text= "pokemon 4")
pokemon_b_4.grid(column=4, row=4, sticky=(W, E))

team_b_5 = StringVar()
teams_b_entry_5 = ttk.Entry(mainframe, width=7, textvariable=team_b_5)
teams_b_entry_5.grid(column=3, row=5, sticky=(W, E))
pokemon_b_5 = ttk.Label(mainframe, text= "pokemon 5")
pokemon_b_5.grid(column=4, row=5, sticky=(W, E))

team_b_6 = StringVar()
teams_b_entry_6 = ttk.Entry(mainframe, width=7, textvariable=team_b_6)
teams_b_entry_6.grid(column=3, row=6, sticky=(W, E))
pokemon_b_6 = ttk.Label(mainframe, text= "pokemon 6")
pokemon_b_6.grid(column=4, row=6, sticky=(W, E))

battle_number = StringVar()
battle_number_entry = ttk.Entry(mainframe, width=7, textvariable=battle_number)
battle_number_entry.grid(column=4, row=9, columnspan=1, sticky=(W, E))
battle_number_entry.insert(0,"1")

ttk.Label(mainframe, text= "Nombres de combats").grid(column=1, row=9, columnspan=2, sticky=(W, E))


# insert default value

team_a_entry = [teams_a_entry_1, teams_a_entry_2, teams_a_entry_3, teams_a_entry_4, teams_a_entry_5, teams_a_entry_6]
team_b_entry = [teams_b_entry_1, teams_b_entry_2, teams_b_entry_3, teams_b_entry_4, teams_b_entry_5, teams_b_entry_6]

k=0
for i in team_a_entry :
    i.insert(-1,"-1")
    k+=1

k=0
for i in team_b_entry :
    i.insert(-1, "-1")
    k+=1


ttk.Label(mainframe, text= "Team 1").grid(column=1, row=7, sticky=(W, E))
ttk.Label(mainframe, text= "Team 2").grid(column=4, row=7, sticky=(W, E))

ttk.Button(mainframe, text="Launch battle", command=launch_battle).grid(column=2, row=7, columnspan=2, sticky=(W, E))


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

ttk.Button(mainframe, text="Actualise", command=actualise).grid(column=2, row=8, columnspan=2, sticky=(W, E))
teams_a_entry_1.focus()
root.bind("<Return>", actualise)

root.mainloop()