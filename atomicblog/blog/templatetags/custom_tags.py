from django import template
from django.template.loader_tags import do_include
from django.template.base import TemplateSyntaxError, Token

# Taken from https://stackoverflow.com/questions/42237732/using-context-variables-inside-text-inside-template-tag-in-django
# to solve the issue of inserting each articles slug into the template name used in "article_detail.html"

# register = template.Library()

# @register.tag(takes_context=True)
# def include_article_text(parser, token):
# 	return articles/{{article.slug}}.html