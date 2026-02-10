import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from teams import *
from players import *

#get randomteam based on difficulty level
def get_random_team(team_dict, choice):
    if not team_dict:
        raise ValueError("The team dictionary is empty.")

    if choice == "Easy":
        es_ovr_get = random.randint(80, 90)
        es_teams = getteamsbyovr(team_dict, es_ovr_get)
        if not es_teams:
            raise ValueError(f"No teams found with OVR {es_ovr_get}.")
        team_name = random.choice(es_teams)

    elif choice == "Medium":
        md_ovr_get = random.randint(70, 80)
        md_teams = getteamsbyovr(team_dict, md_ovr_get)
        if not md_teams:
            raise ValueError(f"No teams found with OVR {md_ovr_get}.")
        team_name = random.choice(md_teams)

    elif choice == "Hard":
        hd_ovr_get = random.randint(60, 70)
        hd_teams = getteamsbyovr(team_dict, hd_ovr_get)
        if not hd_teams:
            raise ValueError(f"No teams found with OVR {hd_ovr_get}.")
        team_name = random.choice(hd_teams)

    else:
        raise ValueError("Invalid choice. Please select 'Easy', 'Medium', or 'Hard'.")

    return team_name


#
def get_random_player(player_dict, ovr_range, age_range, pot_range, pos):
    position = pos
    players = []

    for player_name, details in player_dict.items():
        ovr_match = isinstance(ovr_range, (list, tuple, range)) and details["OVR"] in ovr_range or details["OVR"] == ovr_range
        age_match = isinstance(age_range, (list, tuple, range)) and details["AGE"] in age_range or details["AGE"] == age_range
        pot_match = isinstance(pot_range, (list, tuple, range)) and details["POT"] in pot_range or details["POT"] == pot_range
        
        if ovr_match and age_match and pot_match and details["POS"] == position:
            players.append(player_name)
    
    if not players:
        raise ValueError(
            "No players found matching the criteria in the player dictionary."
        )

    return random.choice(players)


def get_random_wonderkid(player_dict):
    age_min = 16
    age_max = 21
    pot_min = 82
    pot_max = 90
    ovr_min = 60
    ovr_max = 80
    wonderkids = []
    for player_name, details in player_dict.items():
        if (
            age_min <= details["AGE"] <= age_max
            and pot_min <= details["POT"] <= pot_max
            and ovr_min <= details["OVR"] <= ovr_max
        ):
            wonderkids.append(player_name)

    if not wonderkids:
        raise ValueError("No wonderkids found in the player dictionary.")

    return random.choice(wonderkids)


def get_youthacademypos():
    positions = [
        "GK",
        "CB",
        "RB",
        "LB",
        "CDM",
        "CM",
        "CAM",
        "RW",
        "LW",
        "RF",
        "LF",
        "ST",
    ]
    return random.choice(positions)

def get_youthcountry(continent):
    yafile = "yacountry.txt"
    dic_country = {}
    try:
        with open(yafile, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) >= 2:
                    country, cont = parts[0], parts[1]
                    if cont not in dic_country:
                        dic_country[cont] = []
                    dic_country[cont].append(country)
    except FileNotFoundError:
        raise ValueError(f"Youth academy country file '{yafile}' not found.")
    
    if continent not in dic_country:
        raise ValueError(f"No countries found for continent '{continent}'.")
    else:
        return random.choice(dic_country[continent])

def getpositionspeciality(pos):
    pos = pos.upper()  # Convert to uppercase for consistency
    if pos == "GK":
        random_speciality = random.choice(['Goalkeeper', 'Sweeper Keeper'])

    elif pos == "CB":
        random_speciality = random.choice(['Defender', 'Stopper', 'Ball-Playing Defender'])

    elif pos in ['LB', 'RB']:
        random_speciality = random.choice(['Fullback', 'Wingback', 'Falseback', 'Attacking Wingback'])

    elif pos == 'CM':
        random_speciality = random.choice(['Box-to-Box', 'Holding', 'Deep-Lying Playmaker', 'Playmaker', 'Half-Winger'])

    elif pos == 'CDM':
        random_speciality = random.choice(['Holding', 'Centre-Half', 'Deep-Lying Playmaker', 'Wide Half'])

    elif pos in ['LM', 'RM']:
        random_speciality = random.choice(['Winger', 'Wide Midfielder', 'Wide Playmaker', 'Inside Forward'])

    elif pos == 'CAM':
        random_speciality = random.choice(['Playmaker', 'Shadow Striker', 'Half-Winger', 'Classic 10'])

    elif pos in ['LW', 'RW']:
        random_speciality = random.choice(['Winger', 'Inside Forward', 'Wide Playmaker'])

    elif pos == 'ST':
        random_speciality = random.choice(['Advanced Forward', 'Poacher', 'False 9', 'Target Forward'])
    else:
        random_speciality = "Unknown Position"

    return random_speciality


def get_random_budget(team_dict, team, givenovr):
    if givenovr == "None" or givenovr is None:
        ovr_calc = getovr(team_dict, team)
    else:
        ovr_calc = givenovr
    if ovr_calc < 60:
        return random.randint(1, 5) * 1000000
    elif ovr_calc < 70:
        return random.randint(15, 30) * 1000000
    elif ovr_calc < 80:
        return random.randint(30, 50) * 1000000
    elif ovr_calc < 90:
        return random.randint(50, 150) * 1000000
    else:
        return random.randint(150, 300) * 1000000


def get_random_formation(defender_count):
    formation_3 = {}
    formation_4 = {}
    formation_5 = {}
    try:
        formations = pd.read_excel("formations.xlsx")
        selected_columns = ["FORMATION", "MODE", "BASE"]
        formations = formations[selected_columns]
        for index, row in formations.iterrows():
            if str(row["BASE"]) == "3" or str(row["BASE"]) == "3.0":
                formation_3[row["FORMATION"]] = row["MODE"]
            elif str(row["BASE"]) == "4" or str(row["BASE"]) == "4.0":
                formation_4[row["FORMATION"]] = row["MODE"]
            elif str(row["BASE"]) == "5" or str(row["BASE"]) == "5.0":
                formation_5[row["FORMATION"]] = row["MODE"]
    except FileNotFoundError:
        raise ValueError("formations.xlsx file not found.")
    
    if defender_count == 3:
        if not formation_3:
            raise ValueError("No 3-defender formations found.")
        return random.choice(list(formation_3.keys()))
    elif defender_count == 4:
        if not formation_4:
            raise ValueError("No 4-defender formations found.")
        return random.choice(list(formation_4.keys()))
    elif defender_count == 5:
        if not formation_5:
            raise ValueError("No 5-defender formations found.")
        return random.choice(list(formation_5.keys()))
    else:
        combined_formations = {**formation_3, **formation_4, **formation_5}
        if not combined_formations:
            raise ValueError("No formations found.")
        return random.choice(list(combined_formations.keys()))


def getcareeridea(storyline):
    realistic = []
    challenging = []
    fun = []
    creative = []
    specific = []

    try:
        ideas = pd.read_excel("ideas.xlsx")
        selected_columns = ["Category", "Idea Description"]
        ideas = ideas[selected_columns]
        for index, row in ideas.iterrows():
            if row["Category"] == "Realistic & Grounded":
                realistic.append(row["Idea Description"])
            elif row["Category"] == "Challenging & Hardcore":
                challenging.append(row["Idea Description"])
            elif row["Category"] == "Fun & Unique Concepts":
                fun.append(row["Idea Description"])
            elif row["Category"] == "Creative & Story-Driven":
                creative.append(row["Idea Description"])
            elif row["Category"] == "Specific & Niche":
                specific.append(row["Idea Description"])
    except FileNotFoundError:
        raise ValueError("ideas.xlsx file not found.")

    if storyline == "Realistic":
        if not realistic:
            raise ValueError("No realistic career ideas found.")
        return random.choice(realistic)

    elif storyline == "Challenging":
        if not challenging:
            raise ValueError("No challenging career ideas found.")
        return random.choice(challenging)

    elif storyline == "Fun":
        if not fun:
            raise ValueError("No fun career ideas found.")
        return random.choice(fun)

    elif storyline == "Creative":
        if not creative:
            raise ValueError("No creative career ideas found.")
        return random.choice(creative)

    elif storyline == "Specific":
        if not specific:
            raise ValueError("No specific career ideas found.")
        return random.choice(specific)

    else:
        return False

def seasonsstats():
    print("Welcome to the Seasons Stats section!")
    print("This feature is currently under development.")
    print("Please enter your team name and season year to proceed.")
    team_name = input("Enter your team name: ")
    season_year = input("Enter the season year (e.g., 2023/2024): ")
    print(
        "Enter your players goals, assists,appearances,average match rarting and clean sheets for the season with '-' seperating them"
    )
    print("input done, type 'done' to finish.")
    player_stats = {}
    players_in = input("Enter your players")
    while players_in != "done":
        try:
            goals = int(input("Enter the number of goals scored: "))
            assists = int(input("Enter the number of assists made: "))
            appearances = int(input("Enter the number of appearances made: "))
            average_rating = float(input("Enter the average match rating: "))
            clean_sheets = int(input("Enter the number of clean sheets kept: "))
            
            # Validate inputs
            if goals < 0 or assists < 0 or appearances < 0 or clean_sheets < 0:
                print("Stats cannot be negative. Please re-enter.")
                continue
            if average_rating < 0 or average_rating > 10:
                print("Average rating must be between 0 and 10. Please re-enter.")
                continue
            
            player_stats[players_in] = {
                "Goals": goals,
                "Assists": assists,
                "Clean Sheets": clean_sheets,
                "Appearances": appearances,
                "Average Rating": average_rating,
            }
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
            
        players_in = input('Enter your players or type "done" to finish: ')
    
    if not player_stats:
        raise ValueError("No player stats were entered.")
    
    print("Player stats for the season:")
    for player, stats in player_stats.items():
        print(f"{player}: {stats}")
    print("Time to show the visual representation of the stats on a histogram")
    plot_season_stats(player_stats)
    writing = input("Do you want to save the stats to a file? (yes/no): ")
    if writing.lower() == "yes":
        safe_season_year = season_year.replace("/", "_")
        filename = f"{team_name}_{safe_season_year}_stats.csv"
        df = pd.DataFrame(player_stats).T
        df.to_csv(filename, index_label="Player")
        print(f"Stats saved to {filename}")
    else:
        print("Stats not saved to a file. Exiting the feature.")


def plot_season_stats(player_stats):
    if not player_stats:
        raise ValueError("No player stats to plot.")

    players = list(player_stats.keys())
    goals = [stats["Goals"] for stats in player_stats.values()]
    assists = [stats["Assists"] for stats in player_stats.values()]
    appearances = [stats["Appearances"] for stats in player_stats.values()]
    average_rating = [stats["Average Rating"] for stats in player_stats.values()]
    clean_sheets = [stats["Clean Sheets"] for stats in player_stats.values()]

    x = np.arange(len(players))  # the label locations
    stats = [
        ("Goals", goals),
        ("Assists", assists),
        ("Appearances", appearances),
        ("Average Rating", average_rating),
        ("Clean Sheets", clean_sheets),
    ]

    # Create a separate figure for each statistic
    for stat_name, stat_values in stats:
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(x, stat_values, label=stat_name)

        ax.set_xlabel("Players")
        ax.set_ylabel(stat_name)
        ax.set_title(f"{stat_name} by Player")
        ax.set_xticks(x)
        ax.set_xticklabels(players)
        ax.legend()

        plt.tight_layout()
        plt.show()
        
        # Close figure to prevent memory leaks
        plt.close(fig)
