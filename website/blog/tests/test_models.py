import pytest

from django.contrib.auth.models import User

from ..models import Post


@pytest.mark.django_db
def test_user_create():
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    post = Post.objects.create(
        title='Сессии',
        content="""Все взаимодействия между браузерами и серверами осуществляются при помощи протокола HTTP, который
                  не сохраняет своё состояние (stateless). Данный факт означает, что сообщения между клиентом и 
                  сервером являются полностью независимыми один от другого — то есть не существует какого-либо 
                  представления "последовательности", или поведения в зависимости от предыдущих сообщений. 
                  В результате, если вы хотите создать сайт который будет отслеживать взаимодействие с клиентом 
                  (браузером), вам нужно реализовать это самостоятельно.""",
        category='django',
        author=user,
    )
    assert Post.objects.count() == 1
    assert post.title == 'Сессии'
    assert post.category == 'django'
