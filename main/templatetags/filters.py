from django import template

register = template.Library()

def get_total(obj):
    total, grade = obj.performance()
    return total

def get_grade(obj):
    total, grade = obj.performance()
    return grade


register.filter('get_total', get_total)
register.filter('get_grade', get_grade)