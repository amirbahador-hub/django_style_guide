from .models import Profile, BaseUser

def get_profile(user:BaseUser) -> Profile:
    return Profile.objects.get(user=user)
