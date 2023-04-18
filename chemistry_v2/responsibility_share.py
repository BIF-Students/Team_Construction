import pandas as pd

from chemistry_v2.chemistry_helpers import *
from chemistry_v2.chemistry_helpers import compute_relative_player_impact_v2
from helpers.helperFunctions import non_possession_action

def get_responsibility_share(df):
    df.insert(57, 'nonPosAction', df.apply(lambda row: non_possession_action(row), axis=1), allow_duplicates=True) # Mark if action is defensive
    df_def_actions_player = df[df['nonPosAction'] == 1] # Filter dataframe for defensive actions
    df_def_actions_player['zone'] = df_def_actions_player.apply(lambda row: find_zone_chemistry(row), axis = 1) # Filter dataframe for defensive actions
    df_players_actions = get_zones_count_pl(df_def_actions_player)
    df_team_actions = get_zones_count_t(df_def_actions_player)
    print("df_players_actions.columns")
    print(df_players_actions.columns)
    print("df_team_actions.columns")
    print(df_team_actions.columns)

    df_player_share = compute_relative_player_impact(df_players_actions, df_team_actions)
    print(df_player_share.columns)
    return df_player_share


def getResponsibilityShare_v2(df):
    df.insert(57, 'nonPosAction', df.apply(lambda row: non_possession_action(row), axis=1),
              allow_duplicates=True)  # Mark if action is defensive
    df_def_actions_player = df[df['nonPosAction'] == 1]  # Filter dataframe for defensive actions
    df_def_actions_player['zone'] = df_def_actions_player.apply(lambda row: find_zone_chemistry(row),axis=1)  # Filter dataframe for defensive actions
    df_players_actions = find_zones_and_counts_pl(df_def_actions_player)
    df_players_actions['def_actions_count_pl'] = df_players_actions.zone_1_pl + df_players_actions.zone_2_pl + df_players_actions.zone_3_pl +  df_players_actions.zone_4_pl+ df_players_actions.zone_5_pl +  df_players_actions.zone_6_pl
    df_team_actions = find_zones_and_counts_t(df_def_actions_player)
    df_team_actions['def_actions_count_t'] = df_team_actions.zone_1_t + df_team_actions.zone_2_t + df_team_actions.zone_3_t +  df_team_actions.zone_4_t + df_team_actions.zone_5_t +  df_team_actions.zone_6_t
    df_player_share = compute_relative_player_impact_v2(df_players_actions, df_team_actions)

    return df_player_share


def getResponsibilityShare_v3(df):
    df.insert(57, 'nonPosAction', df.apply(lambda row: non_possession_action(row), axis=1),
              allow_duplicates=True)  # Mark if action is defensive
    df_def_actions_player = df[df['nonPosAction'] == 1]  # Filter dataframe for defensive actions
    df_def_actions_player['zone'] = df_def_actions_player.apply(lambda row: find_zone_chemistry(row),axis=1)  # Filter dataframe for defensive actions
    df_players_actions = find_zones_and_counts_pl(df_def_actions_player)
    df_players_actions['def_actions_count_pl'] = df_players_actions.zone_1_pl + df_players_actions.zone_2_pl + df_players_actions.zone_3_pl +  df_players_actions.zone_4_pl+ df_players_actions.zone_5_pl +  df_players_actions.zone_6_pl
    df_team_actions = find_zones_and_counts_t(df_def_actions_player)
    df_team_actions['def_actions_count_t'] = df_team_actions.zone_1_t + df_team_actions.zone_2_t + df_team_actions.zone_3_t +  df_team_actions.zone_4_t + df_team_actions.zone_5_t +  df_team_actions.zone_6_t
    df_player_share = compute_relative_player_impact_v3(df_players_actions, df_team_actions)

    return df_player_share