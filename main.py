import django_setup
from app_construct.models import Post, Commentary

post1 = Post(name='Apples', text='Are you know? Apples is...')
post1.save()
comment1 = Commentary(post=Post.objects.get(id=4), text='Really? I`m don`t know this!', author=2).save()
