# general link to stats
def build_links(stat):
    links = []

    link = "http://www.ncaa.com/stats/football/fbs/current/team/"

    stats_dict = {
                  'Total Offense': '21', 'Total Defense': '22', 
                  'Rushing Offense': '23', 'Rushing Defense': '24', 
                  'Passing Offense': '25', 'Passing Yards Allowed': '695', 
                  'Passing Yards Per Completion': '741','Scoring Offense': '27', 
                  'Scoring Defense': '28', 'Team Passing Efficiency': '465', 
                  'Team Passing Efficiency Defense': '40', '3rd Down Conversion Pct': '699', 
                  '3rd Down Conversion Pct Defense': '701', 'Red Zone Offense': '703', 
                  'Red Zone Defense': '704', 'Turnover Margin': '29', 
                  'Tackles for Loss Allowed': '696', 'Team Tackles for Loss': '467', 
                  'Sacks Allowed': '468', 'Team Sacks': '466'
                 }

    more_pgs = ['', '/p2', '/p3']

    for i in more_pgs:
        if stat in stats_dict:
            links.append(link + stats_dict[stat] + i)
        else:
            print("Stat not found")
            break

    return links     
