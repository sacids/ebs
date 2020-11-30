from django.http import HttpResponse

# check if user is reviewer
def is_reviewer(user):
    return user.groups.filter(name='Reviewers').exists()


# check if user is respondents
def is_respondent(user):
    return user.groups.filter(name='Respondents').exists()
