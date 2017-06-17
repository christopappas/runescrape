from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.forms.models import model_to_dict

#####
# Custom field from stack overflow (http://stackoverflow.com/questions/2350681/django-lowercasecharfield)
#####

class ModifyingFieldDescriptor(object):
    """ Modifies a field when set using the field's (overriden) .to_python() method. """
    def __init__(self, field):  
        self.field = field  
    def __get__(self, instance, owner=None):
        if instance is None:
            raise AttributeError('Can only be accessed via an instance.')  
        return instance.__dict__[self.field.name]
    def __set__(self, instance, value):
        instance.__dict__[self.field.name] = self.field.to_python(value)

class LowerCaseCharField(models.CharField):
    def to_python(self, value):
        value = super(LowerCaseCharField, self).to_python(value)
        if isinstance(value, basestring):
            return value.lower()
        return value
    def contribute_to_class(self, cls, name):
        super(LowerCaseCharField, self).contribute_to_class(cls, name)
        setattr(cls, self.name, ModifyingFieldDescriptor(self))

### End Custom field

class BaseModel(models.Model):
    created_time = models.DateTimeField('date-created', auto_now_add=True)
    last_modified_time = models.DateTimeField('last-modified', auto_now=True, db_index=True)

    class Meta:
        abstract = True

    def as_dict(self):
        ''' convert this model into a dict '''
        return model_to_dict(self)
   
class Character(BaseModel):
    name = LowerCaseCharField(null=False, max_length=255, unique=True)

    class Meta:
        ordering = '-created_time',

    def __unicode__(self):
        return u'{}'.format(self.name)

    # Reminds me of a serializer in a way...
    @property
    def latest_stats(self):
        latest_stat_dict = {}
        sk_list = [i[0] for i in Skill.OSRS_SKILL_CHOICES]
        for item in sk_list:
            sk = Skill.objects.filter(character=self, name=item).latest('created_time')
            latest_stat_dict[item] = {
                'rank': sk.rank,
                'level': sk.level,
                'xp': sk.xp,
                }

        return latest_stat_dict

class Skill(BaseModel):

    OSRS_SKILL_CHOICES = (
        ('Overall', 'Overall'),
        ('Attack', 'Attack'),
        ('Defence', 'Defence'),
        ('Strength', 'Strength'),
        ('Hitpoints', 'Hitpoints'),
        ('Ranged', 'Ranged'),
        ('Prayer', 'Prayer'),
        ('Magic', 'Magic'),
        ('Cooking', 'Cooking'),
        ('Woodcutting', 'Woodcutting'),
        ('Fletching', 'Fletching'),
        ('Fishing', 'Fishing'),
        ('Firemaking', 'Firemaking'),
        ('Crafting', 'Crafting'),
        ('Smithing', 'Smithing'),
        ('Mining', 'Mining'),
        ('Herblore', 'Herblore'),
        ('Agility', 'Agility'),
        ('Thieving', 'Thieving'),
        ('Slayer', 'Slayer'),
        ('Farming', 'Farming'),
        ('Runecraft', 'Runecraft'),
        ('Hunter', 'Hunter'),
        ('Construction', 'Construction'),
    ) 

    character = models.ForeignKey(Character, related_name='skills', blank=False, on_delete=models.CASCADE, default='', db_column='character')
    name = models.CharField(max_length=255, choices=OSRS_SKILL_CHOICES)
    rank = models.IntegerField()
    level = models.IntegerField(validators=[MinValueValidator(1)])
    xp = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    def __unicode__(self):
        return u'{}'.format(self.name)
