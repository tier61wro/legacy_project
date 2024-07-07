from django.core.management.base import BaseCommand
from articles.models import Article, Comment
import random


class Command(BaseCommand):
    help = 'Create test data for articles and comments'

    def handle(self, *args, **kwargs):
        Article.objects.all().delete()
        Comment.objects.all().delete()

        for i in range(10):
            article = Article.objects.create(title=f'Article {i}', content='Some content')
            for j in range(random.randint(0, 10)):
                Comment.objects.create(article=article, content=f'Comment {j} for Article {i}')
        self.stdout.write(self.style.SUCCESS('Test data created successfully'))