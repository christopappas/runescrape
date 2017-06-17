from django.db import transaction

import ingestion.tools
from ingestion.models import Character, Skill
from ingestion.validators import validate_skill_dict as valid
from runescrape.celery_app import app

# TODO - import logger


def ingest_data_by_user_wrapper(username):
    """
    Wraps scraping and ingestion code so we can queue up multiple calls
    in the celery queue
    """
    # Consider putting this inside the async bit
    skill_data = ingestion.tools.scrape_by_user(username)
    # This if protects us from creating a character without any skills
    if skill_data:
        ingest_data_by_user.delay(username, skill_data)
        return True
    return False
    
# else:
    #      # LOG SOME ERROR!

# If we ingest by rank too, have the absracted to do both
@app.task()
def ingest_data_by_user(username, skill_data):

    try:
        inst_char = Character.objects.get(name=username)
    except ingestion.models.Character.DoesNotExist:
        inst_char = Character.objects.create(name=username)

    # Add skills to db associated with user
    # Using atomic transaction to make sure all skills can be added
    # because I don't want fragmented data
    # Don't create Character object if skills don't pan out
    with transaction.atomic():
        # Check if user exists in DB, if not, create it
        
        for skillname in skill_data:
            inst_rank = skill_data[skillname]['rank']
            inst_level = skill_data[skillname]['level']
            inst_xp = skill_data[skillname]['xp']
            # Create the object
            inst_skill = Skill.objects.create(character=inst_char,
                                              name=skillname,
                                              rank=inst_rank,
                                              level=inst_level,
                                              xp=inst_xp,)


