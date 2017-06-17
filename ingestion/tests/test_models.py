from django.test import TestCase

import ingestion.models

class TestCharacter(TestCase):

    def setUp(self):
        self.name = 'girisking'
        self.char = ingestion.models.Character.objects.create(name=self.name)

    def test_as_dict_with_character(self):
        """
        as_dict() should return dictionary form of model instance

        BaseModel has an as_dict method which Character inherits. Testing
        with Character model instance as BaseModel is sort of an abstract
        class
        """
        
        actual = self.char.as_dict()
        expected = {u'id': 1, 'name': u'girisking'}
        assert actual == expected

    def test_char_unicode_name(self):
        """__unicode__ method should return unicode name of character"""
        
        name = self.char.__unicode__()

        actual = type(name)
        expected = unicode

        assert actual == expected
        assert name == u'girisking'

    def test_char_latest_stats(self):
        """
        latest_stats property should be able to return most recently added
        stats to a particular character model
        """

        skillnames = ['Overall', 'Attack', 'Defence', 'Strength',
                      'Hitpoints', 'Ranged', 'Prayer', 'Magic',
                      'Cooking', 'Woodcutting', 'Fletching',
                      'Fishing', 'Firemaking', 'Crafting',
                      'Smithing', 'Mining', 'Herblore', 'Agility',
                      'Thieving','Slayer', 'Farming',
                      'Runecraft', 'Hunter', 'Construction',]

        # Add first round of skills with all values at 1
        for sk in skillnames:
            skill = ingestion.models.Skill.objects.create(character=self.char,
                                                          name=sk,
                                                          rank=1,
                                                          level=1,
                                                          xp=1)
        # Add another round of skills with values at 2
        for sk in skillnames:
            skill = ingestion.models.Skill.objects.create(character=self.char,
                                                          name=sk,
                                                          rank=2,
                                                          level=2,
                                                          xp=2)
        # Assert values are 2
        skill_dict = self.char.latest_stats
        assert skill_dict['Firemaking']['rank'] == 2

class TestSkill(TestCase):

    def setUp(self):
        self.charname = 'girisking'
        self.char = ingestion.models.Character.objects.create(name=self.charname)
        self.skill = ingestion.models.Skill.objects.create(character=self.char,
                                                           name='Attack',
                                                           rank=1,
                                                           level=1,
                                                           xp=1)

    def test_skill_unicode_name(self):
        """__unicode__ method should return unicode name of skill"""
        
        name = self.skill.__unicode__()

        actual = type(name)
        expected = unicode

        assert actual == expected
        assert name == u'Attack'

