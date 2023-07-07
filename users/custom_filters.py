from django import template

register = template.Library()

@register.filter
def is_booked_by_user(appointment, user):
    return appointment.is_booked(user)