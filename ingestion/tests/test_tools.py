from mock import patch
import requests

import ingestion.tools

class TestTools(object):

    @patch('ingestion.tools._parse_scraped_text')
    @patch('requests.get')
    def test_scrape_by_user1(self, mockrequest, mockparse):
        """
        scrape_by_user should return skill_dict if parse is successful
        """
        mockrequest.text.return_value = 'some string'
        mockparse.return_value = {'skill': 'dict'}
        
        user = 'anyone'
        actual = ingestion.tools.scrape_by_user(user)
        expected = {'skill': 'dict'}
        assert actual == expected

    @patch('ingestion.tools._parse_scraped_text')
    @patch('requests.get')
    def test_scrape_by_user2(self, mockrequest, mockparse):
        """
        scrape_by_user should return an empty dict if parse is unsuccessful
        """

        mockrequest.text.return_value = 'some string'
        mockparse.side_effect = KeyError
        
        user = 'anyone'
        actual = ingestion.tools.scrape_by_user(user)
        expected = {}
        assert actual == expected

    def test_parse_scraped_text(self):
        """
        _parse_scraped_text correctly parses csv response from osrs api
        """
        user = 'anyone'
        text = (u'284116,1316,27787204 335745,72,900652 '
                u'393938,66,496759 394043,75,1213756 '
                u'462423,72,929118 597658,62,361046 '
                u'248029,60,292126 632097,58,237931 '
                u'20842,99,13366950 391815,63,378229 '
                u'341381,61,311618 55089,84,3085769 '
                u'114468,73,1042368 402314,55,166893 '
                u'266444,55,181928 11699,87,4211860 '
                u'226504,55,169665 288796,58,235512 '
                u'614995,30,13523 615728,34,21933 -1,1,0 '
                u'218826,44,57039 252485,51,112529 -1,1,0 '
                u'356675,1 257705,2 439998,3 -1,-1 -1,-1 -1,-1 '
                u'-1,-1 -1,-1 -1,-1')

        skill_dict = ingestion.tools._parse_scraped_text(text, user=user)

        # Test some of the values
        actual = skill_dict['Cooking']['level']
        expected = u'99'
        assert actual == expected

        actual = skill_dict['Overall']['rank']
        expected = u'284116'
        assert actual == expected

        actual = skill_dict['Mining']['xp']
        expected = u'4211860'
        assert actual == expected
