from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline): #Use Tabular to have a table of entries, stacked to have them stacked on one another.
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']})
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
