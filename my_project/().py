# coding: utf-8
from datetime import date
from blog.models import Post
from organizer.models import Tag, Startup, NewsLink
Tag.objects.create(name = 'Video Games', slug = 'video-games')
Tag.objects.create(name='Video Games', slug='video-games')
Tag.objects.bulk_create([
Tag(name='Django', slug='django'),
Tag(name='Mobile', slug='mobile'),
Tag(name='Web', slug='web'),
])
Tag.objects.all()
Tag.objects.all()[0]
Tag.objects.all()[1]
Tag.objects.all()[2]
edut
edut = Tag(name='Education', slug='education')
edut
# get == SELECT 
Tag.objects.get(slug='django')
Tag.objects.get(name = 'Django')
type(Tag.objects.all())
type(Tag.objects.get(slug='django'))
try:
    Tag.objects.get(slug='not-exist')
except Tag.DoesNotExist as e:
    print(e)
    
# insensitive 
Tag.objects.get(slug__iexact='DJANGO')
Tag.objects.get(slug__iexact='DjAnGo')
Tag.objects.get(slug__istartwith='DJ')
Tag.objects.get(slug__istartswith='DJ')
Tag.objects.get(slug__contains='go')
try:
    #djangO - mObile - videO-games
    Tag.objects.get(slug__contains='o')
except Tag.MultipleObjectsReturned as e:
    print(e)
    
Tag.objects.filter(slug__contains='o')
Tag.objects.filter(slug__contains='o').order_by('name')
Tag.objects.filter(slug__contains='o').order_by('-name')
Tag.objects.oreder_by('-name')
Tag.objects.order_by('-name')
Tag.objects.values_list()
Tag.objects.values_list('name', 'slug')
Tag.objects.values_list('name')
Tag.objects.values_list('name', flat=True)
jb = Startup.objects.create()
jb = Startup.objects.create(
name='JamBon Software',
slug='jambon-software',
contact='django@jambonsw.com',
description='Web and Mobile Con.\n'
            'Django Tut.\n',
founded_date=date(2013, 1, 18),
website='www.jambonsw.com',
)
jb
# str method -> self.name
jb
jb.founded_date
jb.founded_date = date(2014,1,1)
jb.founded_date
jb = Startup.objects.get(slug='jambon-software')
jb.founded_date
djt = Post.objects.create(
title='Django Training',
slug='django-training',
text=(
    'learn django in a classroom setting '
    'with jambon software.'),
)
djt = Post.objects.create(
title='Django Training',
slug='django-training',
text=(
    'learn django in a classroom setting '
    'with jambon software.'),
pub_date=date(2022,1,1)
)
djt.pub_date = date(2013, 1, 18)
djt.save()
djt
type(djt.tags)
type(djt.startups)
djt.tags.all()
djt.startups.all()
django = Tag.objects.get(slug__contains='django')
djt.tags.add(django)
djt.tags.all()
django.blog_posts.all()
django.blog_posts.all()
django.blog_post.all()
django.startup_set.add(jb)
django.startup_set.all()
djt
djt.startups.add(jb)
djt.startups.all()
jb.blog_posts.all()
