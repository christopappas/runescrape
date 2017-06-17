# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

import models

class SkillInline(admin.TabularInline):
    model = models.Skill
    fk_name = "character"

class CharacterAdmin(admin.ModelAdmin):
    model = models.Character
    list_display = ['name',]
    inlines = [SkillInline,]

class SkillAdmin(admin.ModelAdmin):
	model = models.Skill
	list_display = ['name', 'character', 'level', 'xp', 'rank']

# Register your models here.
admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.Skill, SkillAdmin)