"Plugin module for Meek STV with RON"

## Copyright (C) 2003-2010 Jeffrey O'Neill
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## Lee Maguire <lee@openrightsgroup.org>
##  based on http://web.archive.org/web/20130126132333/http://www.kusu.net/voting-technical.html

__revision__ = "$Id: $"

from openstv.MethodPlugins.MeekSTV import MeekSTV
from openstv.plugins import MethodPlugin

##################################################################

class MeekSTVRon(MeekSTV, MethodPlugin):
  "Meek STV with RON"

  methodName = "Meek STV RON"
  longMethodName = "Meek STV with RON"
  status = 2
  
  htmlBody = """
<p>Meek STV but candidate RON (re-open nominations) is exempt from elimination.</p>
"""
  
  htmlHelp = (MethodPlugin.htmlBegin % (longMethodName, longMethodName)) +\
             htmlBody + MethodPlugin.htmlEnd

  def __init__(self, b): 
    MeekSTV.__init__(self, b)

  def getSureLosers(self, R=None):
    losers = MeekSTV.getSureLosers(self, R=None)
    try:
      ronIndex = self.b.names.index('RON')
    except ValueError:
      return losers
    if ronIndex in losers:
      losers.remove(ronIndex)
    return losers

  def breakWeakTie(self, R, candidateList, mostfewest, what=""):
    try:
      ronIndex = self.b.names.index('RON')
    except ValueError:
      return MeekSTV.breakWeakTie(self, R, candidateList, mostfewest, what)

    if ronIndex in candidateList:
      candidateList.remove(ronIndex)
    return MeekSTV.breakWeakTie(self, R, candidateList, mostfewest, what)

