from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError
from datetime import datetime

def data_processing (team_data: dict):
    if team_data["titles"] < 0:
            raise NegativeTitlesError("titles cannot be negative")
    
    cup_date = team_data["first_cup"]
    date_split = cup_date.split("-")
    year = int(date_split[0])
    year_now = int(datetime.now().year)

    wc_list = [wc for wc in range(1930, year_now, 4)]
    
    if year not in wc_list:
        raise InvalidYearCupError("there was no world cup this year")
        
    if team_data["titles"] > (len(wc_list) - wc_list.index(year)):
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
