from django.db import transaction 
from .models import BaseUser, Profile


def create_profile(*, user:BaseUser, bio:str | None) -> Profile:
    return Profile.objects.create(user=user, bio=bio)

def create_user(*, email:str, password:str) -> BaseUser:
    return BaseUser.objects.create_user(email=email, password=password)


@transaction.atomic
def register(*, bio:str|None, email:str, password:str) -> BaseUser:

    user = create_user(email=email, password=password)
    create_profile(user=user, bio=bio)

    return user
