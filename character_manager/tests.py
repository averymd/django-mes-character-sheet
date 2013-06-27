from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from datetime import datetime
from models import GeistCharacterSheet
from game_manager.models import Trait
#from django.db.models import Count
import json

