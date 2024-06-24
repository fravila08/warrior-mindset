from django.urls import path

from typing import List
from .views import Registration
#, LogOut, Profile, Details

urlpatterns: List[path] = [
    path("login/", Registration.as_view(), name="login_signup")
    # path("", Details.as_view(), "details"),
    # path("profile/", Profile.as_view(), "profile"),
    # path("logout/", LogOut.as_view(), "logout"),
]
