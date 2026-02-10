import pandas as pd


def readplayers():
    import pandas as pd

    players = pd.read_excel("players.xlsx")
    player1 = pd.read_excel("players1.xlsx")
    selected_columns = ["Name", "Team", "OVR", "POT", "POS", "AGE"]

    player_dict = {}

    combined = pd.concat([players[selected_columns], player1[selected_columns]], ignore_index=True)

    for _, row in combined.iterrows():
        player_name = row["Name"]
        team_raw = str(row["Team"]).strip()

        # Remove trailing " |" and clean whitespace
        if "|" in team_raw:
            team_clean = team_raw.split("|")[0].strip()
        else:
            team_clean = team_raw

        # Replace empty or invalid values with "Free Agents"
        if team_clean.lower() in ["", "nan", "none"]:
            team_clean = "Free Agents"

        player_dict[player_name] = {
            "Team": team_clean,
            "OVR": row["OVR"],
            "POT": row["POT"],
            "POS": row["POS"],
            "AGE": row["AGE"],
        }

    for player in player_dict:
        print(f"Loaded player: {player}")
    return player_dict



def getplayerovr(player_dict, player_name):
    if player_name in player_dict:
        return player_dict[player_name]["OVR"]
    else:
        raise ValueError(f"Player '{player_name}' not found in the dictionary.")


def getplayerpot(player_dict, player_name):
    if player_name in player_dict:
        return player_dict[player_name]["POT"]
    else:
        raise ValueError(f"Player '{player_name}' not found in the dictionary.")


def getplayerpos(player_dict, player_name):
    if player_name in player_dict:
        return player_dict[player_name]["POS"]
    else:
        raise ValueError(f"Player '{player_name}' not found in the dictionary.")


def getplayerage(player_dict, player_name):
    if player_name in player_dict:
        return player_dict[player_name]["AGE"]
    else:
        raise ValueError(f"Player '{player_name}' not found in the dictionary.")


def getplayerteam(player_dict, player_name):
    if player_name in player_dict:
        return player_dict[player_name]["Team"]
    else:
        raise ValueError(f"Player '{player_name}' not found in the dictionary.")


def getplayersbyteam(player_dict, team_name):
    players_in_team = []
    for player_name, details in player_dict.items():
        if details["Team"] == team_name:
            players_in_team.append(player_name)
    return players_in_team


def getplayersbyage(player_dict, age):
    players_of_age = []
    for player_name, details in player_dict.items():
        if details["AGE"] == age:
            players_of_age.append(player_name)
    return players_of_age


def getplayersbyovr(player_dict, ovr):
    players_with_ovr = []
    for player_name, details in player_dict.items():
        if details["OVR"] == ovr:
            players_with_ovr.append(player_name)
    return players_with_ovr


def getplayersbypot(player_dict, pot):
    players_with_pot = []
    for player_name, details in player_dict.items():
        if details["POT"] == pot:
            players_with_pot.append(player_name)
    return players_with_pot


def getplayersbyteamandpos(player_dict, team_name, position):
    players_in_team_and_pos = []
    for player_name, details in player_dict.items():
        if details["Team"] == team_name and details["POS"] == position:
            players_in_team_and_pos.append(player_name)
    return players_in_team_and_pos


def playercompare(player_dict, player1, player2):
    if player1 not in player_dict or player2 not in player_dict:
        raise ValueError("One or both players not found in the dictionary.")

    details1 = player_dict[player1]
    details2 = player_dict[player2]

    comparison = {
        "Player 1": player1,
        "Player 2": player2,
        "OVR Player 1": details1["OVR"],
        "OVR Player 2": details2["OVR"],
        "POT Player 1": details1["POT"],
        "POT Player 2": details2["POT"],
        "POS Player 1": details1["POS"],
        "POS Player 2": details2["POS"],
        "AGE Player 1": details1["AGE"],
        "AGE Player 2": details2["AGE"],
    }

    return comparison
