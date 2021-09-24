import moment
from datetime import datetime
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import csv
import sys


def dates_bwn_twodates(start_date, end_date):
    diff = abs(start_date.diff(end_date).days)
    
    for n in range(0,diff+1):
        yield start_date.strftime("%Y-%m-%d")
        start_date = (start_date).add(days=1)


def create_data_table(dates):
    df_total = pd.DataFrame()

    for date in dates:
        url = f"{base_url}/odds?dateEnd={date}"
        r = requests.get(url)

        data = r.json()

        df_single_date = pd.json_normalize(data)
        df_single_date['date'] = date
        
        df_total = df_total.append(df_single_date)

    return df_total


if __name__ == "__main__":

    team = sys.argv[1]
    stat = sys.argv[2]

    filename = "team_stats.csv"

    if sys.argv[-1] == 'download':

        today = datetime.today().strftime('%Y-%m-%d')
        sdate = moment.date('2021-04-01')
        edate = moment.date(today)
        base_url = 'https://www.fangraphs.com/api/playoff-odds'

        dates = list(dates_bwn_twodates(sdate,edate))

        team_data = create_data_table(dates)
        team_data.to_csv(filename, index=False)

    team_data = pd.read_csv(filename, sep=',')
    team_data = team_data.loc[team_data['shortName'] == team]

    tick_spacing = 30

    fig, ax = plt.subplots(1,1)
    ax.plot(team_data['date'], team_data[stat])

    plt.xlabel('date', fontsize=18)
    plt.ylabel(stat, fontsize=16)

    fig.suptitle(team, fontsize=12)

    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))

    plt.show()

