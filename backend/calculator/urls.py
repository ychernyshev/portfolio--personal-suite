# SPDX-License-Identifier: AGPL-3.0-or-later
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('dashboard/', index, name='dashboard'),
    path('add_entry/', add_entry, name='add_entry'),
    path('settings/', settings, name='settings'),
]