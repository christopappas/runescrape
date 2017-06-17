from collections import OrderedDict

import ingestion.validators

class TestValidators(object):

	def test_validate_skill_dict_good(self):
		"""
		A valid skill_dict should validate and return True
		"""
		good_dict = OrderedDict()
		good_dict['Strength'] = {'xp': 557958, 'rank': 541254, 'level': 67}
		good_dict['Herblore'] = {'xp': 103152, 'rank': 262658, 'level': 50}
		good_dict['Smithing'] = {'xp': 149226, 'rank': 286247, 'level': 53}
		good_dict['Hunter'] = {'xp': 1000, 'rank': 577598, 'level': 9}
		good_dict['Cooking'] = {'xp': 13322500, 'rank': 21109, 'level': 99}
		good_dict['Woodcutting'] = {'xp': 156729, 'rank': 614090, 'level': 54}
		good_dict['Defence'] = {'xp': 450002, 'rank': 389709, 'level': 65}
		good_dict['Farming'] = {'xp': 0, 'rank': -1, 'level': 1}
		good_dict['Agility'] = {'xp': 200978, 'rank': 301569, 'level': 56}
		good_dict['Ranged'] = {'xp': 345478,'rank': 585065, 'level': 62}
		good_dict['Thieving'] = {'xp': 13388, 'rank': 601323, 'level': 30}
		good_dict['Overall'] = {'xp': 24661261, 'rank': 326348, 'level': 1223}
		good_dict['Construction'] = {'xp': 0, 'rank': -1, 'level': 1}
		good_dict['Crafting'] = {'xp': 112476, 'rank': 449576, 'level': 51}
		good_dict['Magic'] = {'xp': 211508, 'rank': 631691, 'level': 57}
		good_dict['Mining'] = {'xp': 3342797, 'rank': 15620, 'level': 85}
		good_dict['Runecraft'] = {'xp': 56599, 'rank': 211684, 'level': 44}
		good_dict['Slayer'] = {'xp': 14273, 'rank': 642826, 'level': 30}
		good_dict['Firemaking'] = {'xp': 843853, 'rank': 116727, 'level': 71}
		good_dict['Attack'] = {'xp': 551598, 'rank': 443770, 'level': 67}
		good_dict['Fletching'] = {'xp': 300468, 'rank': 333179, 'level': 60}
		good_dict['Fishing'] = {'xp': 3062779, 'rank': 52491, 'level': 84}
		good_dict['Prayer'] = {'xp': 289786, 'rank': 239217, 'level': 60}
		good_dict['Hitpoints'] = {'xp': 574713, 'rank': 545939, 'level': 67}
		
		actual = ingestion.validators.validate_skill_dict(good_dict)
		expected = True
		assert actual == expected

	def test_validate_skill_dict_bad(self):
		"""
		An invalid skill_dict should return False when validated
		"""

		# Missing a skill (strength)
		bad_dict = OrderedDict()
		bad_dict['Herblore'] = {'xp': 103152, 'rank': 262658, 'level': 50}
		bad_dict['Smithing'] = {'xp': 149226, 'rank': 286247, 'level': 53}
		bad_dict['Hunter'] = {'xp': 1000, 'rank': 577598, 'level': 9}
		bad_dict['Cooking'] = {'xp': 13322500, 'rank': 21109, 'level': 99}
		bad_dict['Woodcutting'] = {'xp': 156729, 'rank': 614090, 'level': 54}
		bad_dict['Defence'] = {'xp': 450002, 'rank': 389709, 'level': 65}
		bad_dict['Farming'] = {'xp': 0, 'rank': -1, 'level': 1}
		bad_dict['Agility'] = {'xp': 200978, 'rank': 301569, 'level': 56}
		bad_dict['Ranged'] = {'xp': 345478,'rank': 585065, 'level': 62}
		bad_dict['Thieving'] = {'xp': 13388, 'rank': 601323, 'level': 30}
		bad_dict['Overall'] = {'xp': 24661261, 'rank': 326348, 'level': 1223}
		bad_dict['Construction'] = {'xp': 0, 'rank': -1, 'level': 1}
		bad_dict['Crafting'] = {'xp': 112476, 'rank': 449576, 'level': 51}
		bad_dict['Magic'] = {'xp': 211508, 'rank': 631691, 'level': 57}
		bad_dict['Mining'] = {'xp': 3342797, 'rank': 15620, 'level': 85}
		bad_dict['Runecraft'] = {'xp': 56599, 'rank': 211684, 'level': 44}
		bad_dict['Slayer'] = {'xp': 14273, 'rank': 642826, 'level': 30}
		bad_dict['Firemaking'] = {'xp': 843853, 'rank': 116727, 'level': 71}
		bad_dict['Attack'] = {'xp': 551598, 'rank': 443770, 'level': 67}
		bad_dict['Fletching'] = {'xp': 300468, 'rank': 333179, 'level': 60}
		bad_dict['Fishing'] = {'xp': 3062779, 'rank': 52491, 'level': 84}
		bad_dict['Prayer'] = {'xp': 289786, 'rank': 239217, 'level': 60}
		bad_dict['Hitpoints'] = {'xp': 574713, 'rank': 545939, 'level': 67}
		
		actual = ingestion.validators.validate_skill_dict(bad_dict)
		expected = False
		assert actual == expected


