#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Plecost: Wordpress vulnerabilities finder
#
# @url: http://iniqua.com/labs/
# @url: https://github.com/iniqua/plecost
#
# @author:Francisco J. Gomez aka ffranz (http://iniqua.com/)
# @author:Daniel Garcia aka cr0hn (http://www.cr0hn.com/me/)
#
# Copyright (c) 2015, Iniqua Team
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
# following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
# products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

"""
This file manage word list
"""

__all__ = ["list_wordlists", "get_wordlist"]

from os import listdir
from os.path import join

from .exceptions import PlecostWordListNotFound
from .utils import get_data_folder


# ----------------------------------------------------------------------
def list_wordlists():
    """
    List internal word list.

    :return: list with file names
    :rtype: list(str)
    """
    return [x for x in listdir(get_data_folder()) if x.endswith("txt")]


# ----------------------------------------------------------------------
def get_wordlist(wordlist_name):
    """
    Get and iterator of specified word list.

    :param wordlist_name: Word list name
    :type wordlist_name: basestring

    :return: iterator with each line of file.
    :rtype: str
    """
    if not isinstance(wordlist_name, str):
        raise TypeError("Expected basestring, got '%s' instead" % type(wordlist_name))

    word_list_name = join(get_data_folder(), wordlist_name)

    try:
        with open(word_list_name, "rU") as f:
            for word in f:
                yield word.replace("\n", "").replace("\r", "")
    except IOError as e:
        raise PlecostWordListNotFound("Wordlist '%s' not found. Error: %s" % (wordlist_name, e))
