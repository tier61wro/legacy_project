from django import template
from django.db import connection

register = template.Library()

@register.simple_tag
def get_comment_count(article_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM articles_comment WHERE article_id = %s", [article_id])
        row = cursor.fetchone()
    return row[0]
