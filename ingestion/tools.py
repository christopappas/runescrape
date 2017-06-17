from collections import OrderedDict
import requests

# Coming soon!
# def scrape_by_rank(rank='1'):
#     """
#     Grab info from high scores using character rank
#     """
#     pass

def scrape_by_user(user='girisking'):
    """
    Grab info from high scores using character name
    """

    r = requests.get("http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player={}".format(user))
    text = r.text.replace('\n', ' ')
    try:
        skill_dict = _parse_scraped_text(text, user='girisking')
    except (IndexError, KeyError):
        skill_dict = {}
        
    return skill_dict

def _parse_scraped_text(text, user='girisking'):
    """
    Parses the text grabbed from OSRS API and then drops it into 
    a dictionary. Expects something like:

      (Rank) (Lvl) (XP)
    u'334881,1206,23983020 484938,62,341722 392806,64,432194 685962,60,277770'
    """

    skill_dict = OrderedDict()
    skill_chunks_from_api = text.split() # a list
    skillnames = [
        'Overall',
        'Attack',
        'Defence',
        'Strength',
        'Hitpoints',
        'Ranged',
        'Prayer',
        'Magic',
        'Cooking',
        'Woodcutting',
        'Fletching',
        'Fishing',
        'Firemaking',
        'Crafting',
        'Smithing',
        'Mining',
        'Herblore',
        'Agility',
        'Thieving',
        'Slayer',
        'Farming',
        'Runecraft',
        'Hunter',
        'Construction',
        ]

    # There are 24 skills (tables 0-23), process data for each
    for index in range(0, 24):
        skillname = skillnames[index]

        skilldata = skill_chunks_from_api[index].split(",")
        rank = skilldata[0]
        level = skilldata[1]
        xp = skilldata[2]

        skill_dict[skillname] = {
            'rank': rank,
            'level': level,
            'xp': xp,
            }
            
    return skill_dict

