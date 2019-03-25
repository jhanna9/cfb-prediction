from pathlib import Path
import requests

filename = Path('total_offense.pdf')

url = 'http://web1.ncaa.org/stats/StatsSrv/pdf/rankings?rptWeeks=69&statSeq=21&div=11&sportCode=MFB&academicYear=2019&rptType=PDF&doWhat=showrankings'

r = requests.get(url)

print(r.status_code)

filename.write_bytes(r.content)
