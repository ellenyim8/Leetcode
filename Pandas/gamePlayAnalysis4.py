import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # determine first date each player logged in
    first = activity.groupby('player_id')['event_date'].min().reset_index()
    # calculate day before each event date
    activity['day_before_event'] = activity['event_date'] - pd.to_timedelta(1, unit='D')
    # merge dataframes to identify potential consecutive logins
    merged = activity.merge(first, on='player_id', suffixes=('_actual', '_first'))
    # identify consecutive logins
    consec_login = merged[merged['day_before_event'] == merged['event_date_first']] 
    # compute fractions
    fraction = round(consec_login['player_id'].nunique() / activity['player_id'].nunique(), 2)

    output = pd.DataFrame({'fraction':[fraction]})
    return output
