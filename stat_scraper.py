import sys
from urllib import urlopen
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")
 
third_down_durl = 'http://stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=14.0&amp;sport_code=MFB&amp;stat_seq=22.0'
third_down_dpage = urlopen(third_down_durl)

soup = BeautifulSoup(third_down_dpage)

print soup.find_all('table')

''' 
stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=14.0&amp;sport_code=MFB&amp;stat_seq=21.0

<option value="699.0">3rd Down Conversion Pct</option>
<option value="701.0">3rd Down Conversion Pct Defense</option>
<option value="700.0">4th Down Conversion Pct</option>
<option value="702.0">4th Down Conversion Pct Defense</option>
<option value="785.0">Blocked Kicks</option>
<option value="786.0">Blocked Kicks Allowed</option>
<option value="790.0">Blocked Punts</option>
<option value="791.0">Blocked Punts Allowed</option>
<option value="756.0">Completion Percentage</option>
<option value="926.0">Defensive TDs</option>
<option value="876.0">Fewest Penalties</option>
<option value="697.0">Fewest Penalties Per Game</option>
<option value="877.0">Fewest Penalty Yards</option>
<option value="698.0">Fewest Penalty Yards Per Game</option>
<option value="694.0">First Downs Defense</option>
<option value="693.0">First Downs Offense</option>
<option value="458.0">Fumbles Lost</option>
<option value="456.0">Fumbles Recovered</option>
<option value="463.0">Kickoff Return Defense</option>
<option value="96.0">Kickoff Returns</option>
<option value="98.0">Net Punting</option>
<option value="459.0">Passes Had Intercepted</option>
<option value="457.0">Passes Intercepted</option>
<option value="25.0">Passing Offense</option>
<option value="695.0">Passing Yards Allowed</option>
<option value="741.0">Passing Yards per Completion</option>
<option value="462.0">Punt Return Defense</option>
<option value="97.0">Punt Returns</option>
<option value="704.0">Red Zone Defense</option>
<option value="703.0">Red Zone Offense</option>
<option value="24.0">Rushing Defense</option>
<option value="23.0">Rushing Offense</option>
<option value="468.0">Sacks Allowed</option>
<option value="28.0">Scoring Defense</option>
<option value="27.0">Scoring Offense</option>
<option value="696.0">Tackles for Loss Allowed</option>
<option value="465.0">Team Passing Efficiency</option>
<option value="40.0">Team Passing Efficiency Defense</option>
<option value="466.0">Team Sacks</option>
<option value="467.0">Team Tackles for Loss</option>
<option value="705.0">Time of Possession</option>
<option value="22.0" selected="selected">Total Defense</option>
<option value="21.0">Total Offense</option>
<option value="29.0">Turnover Margin</option>
<option value="460.0">Turnovers Gained</option>
<option value="461.0">Turnovers Lost</option>
<option value="742.0">Winning Percentage</option></select>
'''
