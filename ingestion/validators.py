from collections import OrderedDict

# TODO: Put skillnames in one central place in repo
def validate_skill_dict(skill_dict):
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

    try:
        # Check Type
        assert type(skill_dict) == OrderedDict
        # Check keys and Values
        for skill in skillnames:
            assert skill in skill_dict
            assert skill_dict[skill] != None
        # Return true if we're happy
        return True 
    except AssertionError:
        return False

