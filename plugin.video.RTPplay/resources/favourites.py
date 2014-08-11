#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
 Author: enen92 

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 
"""
import xbmc,xbmcgui,xbmcplugin,xbmcaddon,sys,os,re,xbmcvfs
from webutils import *
from common_variables import *
from directory import *
from utilities import *
from directory import *
from iofile import *


def list_favourites():
	if not xbmcvfs.exists(programafav): xbmcvfs.mkdir(programafav)
	dirs,files = xbmcvfs.listdir(programafav)
	if files:
		totalit = len(files)
		for fich in files:
			text = readfile(os.path.join(programafav,fich))
			data = text.split('|')
			try: 
				information = { "Title": data[0],"plot":data[3] }
				if 'arquivo/' not in data[1]: mode = 16
				else: mode = 11
				addprograma(data[0],data[1],mode,data[2],totalit,information)
			except: pass
		xbmcplugin.setContent(int(sys.argv[1]), 'tvshows')
		setview('show-view')
	else: msgok(translate(40000),translate(40023));sys.exit(0)
			
	
def add_favourite(name,url,iconimage,plot):
	if not xbmcvfs.exists(programafav): xbmcvfs.mkdir(programafav)
	text = name + '|' + url + '|' + iconimage + '|' + plot
	favfile=os.path.join(programafav,removeNonAscii(name.lower())+'.txt')
	save(favfile,text)
	xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % (translate(40000), translate(40022), 1,os.path.join(addonfolder,"icon.png")))
	xbmc.executebuiltin("XBMC.Container.Refresh")
	
def remove_favourite(name):
	favfile=os.path.join(programafav,removeNonAscii(name.lower())+'.txt')
	xbmcvfs.delete(favfile)
	xbmc.executebuiltin("Notification(%s,%s,%i,%s)" % (translate(40000), translate(), 1,os.path.join(addonfolder,"icon.png")))
	dirs,files = xbmcvfs.listdir(programafav)
	if files:
		xbmc.executebuiltin("XBMC.Container.Refresh")
	
	
	
