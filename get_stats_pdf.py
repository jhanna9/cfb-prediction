from pathlib import Path
import requests


with open('stat_num.txt', 'r') as f:
    for line in f:
        stat_name, stat_num = line.split()

        filename = Path(stat_name + '.pdf')

        url = 'http://web1.ncaa.org/stats/StatsSrv/pdf/rankings?rptWeeks=69&statSeq=' + stat_num + '&div=11&sportCode=MFB&academicYear=2019&rptType=PDF&doWhat=showrankings'

        r = requests.get(url)

        filename.write_bytes(r.content)
