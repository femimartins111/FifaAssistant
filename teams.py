import pandas as pd


def readteams(teamsfile):
    teams = pd.read_excel(teamsfile)
    selected_columns = ["Name", "OVR", "ATT", "MID", "DEF", "AVAGE"]
    team_dict = {}
    for index, row in teams.iterrows():
        team_name = row["Name"]
        team_dict[team_name] = {
            "OVR": row["OVR"],
            "ATT": row["ATT"],
            "MID": row["MID"],
            "DEF": row["DEF"],
            "AVG AGE": row["AVAGE"],
        }

    return team_dict


def getovr(team_dict, team_name):
    if team_name in team_dict:
        return team_dict[team_name]["OVR"]
    else:
        raise ValueError(f"Team '{team_name}' not found in the dictionary.")


def getatt(team_dict, team_name):
    if team_name in team_dict:
        return team_dict[team_name]["ATT"]
    else:
        raise ValueError(f"Team '{team_name}' not found in the dictionary.")


def getmid(team_dict, team_name):
    if team_name in team_dict:
        return team_dict[team_name]["MID"]
    else:
        raise ValueError(f"Team '{team_name}' not found in the dictionary.")


def getdef(team_dict, team_name):
    if team_name in team_dict:
        return team_dict[team_name]["DEF"]
    else:
        raise ValueError(f"Team '{team_name}' not found in the dictionary.")


def getavgage(team_dict, team_name):
    if team_name in team_dict:
        return team_dict[team_name]["AVG AGE"]
    else:
        raise ValueError(f"Team '{team_name}' not found in the dictionary.")


def getteamsbyovr(team_dict, ovr):
    teams_by_ovr = []
    for team_name, details in team_dict.items():
        if details["OVR"] == ovr:
            teams_by_ovr.append(team_name)

    if not teams_by_ovr:
        raise ValueError(f"No teams found with OVR {ovr}.")

    return teams_by_ovr


readteams("allteams.xlsx")
