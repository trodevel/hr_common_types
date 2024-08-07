#!/usr/bin/python3

'''
Types.

Copyright (C) 2023 Dr. Sergey Kolevatov

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

'''

from enum import Enum
from languages.python.languages import Language
from typing import Optional
from pydantic.dataclasses import dataclass

##########################################################

class Gender(int, Enum):
    undef = 0
    male = 1
    female = 2
    other = 3

class OfficePresenceType(int, Enum):
    UNDEF = 0
    OFFICE_ONLY = 1
    OFFICE_AND_REMOTE = 2
    REMOTE_ONLY = 3

class Qualification(int, Enum):
    undef = 0
    intern = 1
    junior = 2
    middle = 3
    senior = 4
    lead = 5

class HigherEducationLevel(int, Enum):
    UNDEF = 0
    BACHELOR = 1
    MASTER = 2
    PHD = 3

class LanguageLevel(int, Enum):
    undef = 0
    beginner = 1
    intermediate = 2
    advanced = 3
    native = 4

class JobSearchStatus(int, Enum):
    not_looking = 0
    passively_looking = 1
    actively_looking = 2

@dataclass
class LanguageWithLevel:
    language: Language        = None
    level: LanguageLevel      = None

    def __init__( self, language, level ):
        self.language          = language
        self.level             = level

    def __str__(self):
        return str( self.language ) + ";" + str( self.level )

@dataclass
class ContactType(int, Enum):
    UNDEF = 0
    EMAIL = 1
    PHONE = 2
    WHATSAPP = 3
    TELEGRAM = 4
    SKYPE = 5

##########################################################
