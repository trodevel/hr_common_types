#!/usr/bin/python3

'''
Social Media Communities.

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

##########################################################

class Community(int, Enum):
    behance = 1
    codeproject = 2
    devto = 3
    discord = 4
    douyin = 5
    dribbble = 6
    facebook = 7
    github = 8
    gitlab = 9
    habr = 10
    habr_qa = 11
    hackernoon = 12
    hashnode = 13
    imo = 14
    instagram = 15
    josh = 16
    kuaishou = 17
    likee = 18
    line = 19
    linkedin = 20
    mastodon = 21
    messenger = 22
    picsart = 23
    pinterest = 24
    qq = 25
    quora = 26
    qzone = 27
    reddit = 28
    skype = 29
    slack = 30
    snapchat = 31
    stackoverflow = 32
    teams = 33
    telegram = 34
    threads = 35
    tieba = 36
    tiktok = 37
    tumblr = 38
    twitch = 39
    vevo = 40
    viber = 41
    vk = 42
    wechat = 43
    weibo = 44
    whatsapp = 45
    xiaohongshu = 46
    xing = 47
    x_twitter = 48
    youtube = 49
