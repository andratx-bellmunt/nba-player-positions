"""Connection with NBA API"""

import time
import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats, commonteamroster
from nba_api.stats.static import teams


def get_player_stats(first_season: int, last_season: int) -> pd.DataFrame:
    assert first_season <= last_season, 'Last season must be later than first season'

    # Initialize a list to append data for each season
    list_seasons_data = []

    for season in range(first_season, last_season + 1):
        print(f"Fetching {season}...")

        # Call API
        stats = leaguedashplayerstats.LeagueDashPlayerStats(
            season=season,
            season_type_all_star='Regular Season',
            measure_type_detailed_defense='Base'
        )

        # Store the data
        df_stats = stats.get_data_frames()[0]

        # Drop _RANK columns
        # since they just represent position by different criteria
        for col in df_stats.columns:
            if "RANK" in col:
                df_stats.drop(col, axis=1, inplace=True)

        # Sleep to not overload API calls
        time.sleep(0.5)

        # Add SEASON column to identify data when we concatenate all seasons together
        df_stats['SEASON'] = season

        # Append data to the list of dataframes for all seasons
        list_seasons_data.append(df_stats)

    # Concatenate the data together and set an ID for each player + season combination  
    df = pd.concat(list_seasons_data, ignore_index=True)
    df['ID'] = df['PLAYER_ID'].astype(str) + '_' + df['SEASON'].astype(str)

    return df


def get_player_positions(first_season: int, last_season: int) -> pd.DataFrame:
    all_teams = teams.get_teams()
    rosters = []

    for team in all_teams:
        for season in range(first_season, last_season + 1):
            roster = commonteamroster.CommonTeamRoster(
                team_id=team['id'],
                season=season
            )
            df_roster = roster.get_data_frames()[0]
            df_roster['SEASON'] = season

            rosters.append(roster.get_data_frames()[0])
            time.sleep(0.5)  # avoid rate limiting

    df = pd.concat(rosters)[['PLAYER_ID', 'SEASON', 'POSITION']]
    df['ID'] = df['PLAYER_ID'].astype(str) + '_' + df['SEASON'].astype(str)

    return df[['ID', 'POSITION']]
