# 626: Exchange Seats 

import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    # iterate every 2 students
    for i in range(0, len(seat), 2):
        seat.loc[i:i+1, 'student'] = seat.loc[i+1:i:-1, 'student'].values

    return seat

    