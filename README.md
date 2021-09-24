## MLB Playoff Odds (and other stats) Visualizer

#### Install Requirements

This project was built with the following:
```
Python 3.9.5
pip 21.1.1
```

Install libraries:
```
pip install -r requirements.txt
```

#### Example usage

The syntax is:
```
python run.py <team-name> <stat> <download (optional)>
```

For example, to get the Mariners' playoff odds over the course of the 2021 season
```
python run.py Mariners endData.poffTitle download
```

Get the Mariners' win percentage over the course of the 2021 season, but don't re-download the data
```
python run.py Mariners Wpct
```

#### List of stats you can use

```
W - wins

L - losses

Wpct - win percentage

GB - games back in the division

WCGB - games back in the wildcard

endData.ExpW - expected wins

endData.ExpL - expected losses

endData.rosW - rest of season win percentage

endData.divTitle - odds of winning the division

endData.wcTitle - odds of winning the wildcard

endData.poffTitle - odds of making the playoffs

endData.wcWin - odds of advancing to the division series

endData.dsWin - odds of advancing to the league championship series

endData.csWin - odds of advancing to the world series

endData.wsWin - odds of winning the world series

endData.sos - strength of schedule
```

#### Example Output

![alt text](image.png "Mariners Playoff Odds")
