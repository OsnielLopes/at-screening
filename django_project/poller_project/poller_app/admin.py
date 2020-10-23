from django.contrib import admin

from .models import Question, Choice, Answer


class PollerAdminSite(admin.AdminSite):
    login_template = 'login.html'

    class Meta:
        pass


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ('choice_text', )


class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = [ChoiceInline]
    fields = ('question_text', 'answers')
    readonly_fields = ('answers', )
    list_display = ('question_text', )

    def save_model(self, request, obj: Question, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(user=request.user)
        return qs

    def answers(self, obj):
        return "\n".join([f'{choice.choice_text}: {len(choice.answer_set.all())}' for choice in obj.choice_set.all()])


class AnswerAdmin(admin.ModelAdmin):
    model = Answer
    fields = ('question_text', 'choice')
    readonly_fields = ('question_text', )
    list_display = ('question_text', 'answer')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(user=request.user)
        return qs

    def question_text(self, obj):
        return obj.question.question_text

    def answer(self, obj):
        return obj.choice.choice_text

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context['adminform'].form.fields['choice'].queryset = Choice.objects.filter(question=obj.question)
        return super().render_change_form(request, context, add=add, change=change, form_url=form_url, obj=obj)



site = PollerAdminSite()
site.register(Question, QuestionAdmin)
site.register(Answer, AnswerAdmin)
