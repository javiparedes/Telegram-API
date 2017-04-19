#!/usr/bin/python

# Copyright (C) 2017 Javier Paredes javi.paredes@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import json
import requests

class TelegramBot(object):

	def __init__(self,token):
		self.token=token
		self.url="https://api.telegram.org/bot"+self.token+"/"

	def getMe(self):
		r=requests.get(self.url+"getMe")
		return r.json()

	def getUpdates(self):
		r=requests.get(self.url+"getUpdates")
		return r.json()

	def sendMessage(self,chat_id,text,parse_mode="",disable_web_page_preview=False,disable_notification=False,reply_to_message_id=-1,reply_markup={}):
		parameters={}
		parameters["chat_id"]=chat_id
		parameters["text"]=text
		if parse_mode != "":
			parameters["parse_mode"]=parse_mode
		parameters["disable_web_page_preview"]=disable_web_page_preview
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendMessage",json=parameters)
		return r.status_code

	def forwardMessage(self,chat_id,from_chat_id,message_id,disable_notification=False):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["from_chat_id"]=from_chat_id
		parameters["disable_notification"]=disable_notification
		parameters["message_id"]=message_id
		r=requests.post(self.url+"forwardMessage",json=parameters)
		return r.status_code

	def sendPhoto(self,chat_id,photo,caption="",disable_notification=False,reply_to_message_id=-1,reply_markup={}):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["photo"]=photo
		if caption != "":
			parameters["caption"]=caption
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendPhoto",json=parameters)
		return r.status_code

	def sendAudio(self,chat_id,audio,duration=-1,performer="",title="",disable_notification=False,reply_to_message_id=-1,reply_markup={}):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["audio"]=audio
		if performer != "":
 			parameters["performer"]=performer
		if title != "":
 			parameters["title"]=title			
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendAudio",json=parameters)
		return r.status_code

	def sendDocument(self,chat_id,document,caption="",disable_notification=False,reply_to_message_id=-1,reply_markup={}):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["document"]=document
		if caption != "":
			parameters["caption"]=caption
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendDocument",json=parameters)
		return r.status_code

	def sendSticker(self,chat_id,sticker,disable_notification=False,reply_to_message_id=-1,reply_markup={}):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["sticker"]=sticker
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendSticker",json=parameters)
		return r.status_code

	def sendVideo(self,chat_id,video,duration=-1,width=-1,height=-1,caption="",disable_notification=False,reply_to_message_id=-1,reply_markup={}):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["video"]=video
		if duration > -1:
 			parameters["duration"]=duration
		if width > -1:
 			parameters["width"]=width
		if height > -1:
			parameters["height"]=height
		if caption != "":
 			parameters["caption"]=caption
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendVideo",json=parameters)
		return r.status_code
	
	def sendVoice(self,chat_id,voice,duration=-1,disable_notification=False,reply_to_message_id=-1,reply_markup={}):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["voice"]=voice
		if duration > -1:
 			parameters["duration"]=duration
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendVoice",json=parameters)
		return r.status_code

	def sendLocation(self,chat_id,latitude,longitude,disable_notification=False,reply_to_message_id=-1,reply_markup={}):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["latitude"]=latitude
		parameters["longitude"]=longitude
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendLocation",json=parameters)
		return r.status_code

	def sendVenue(self,chat_id,latitude,longitude,title,address,foursquare_id="",disable_notification=False,reply_to_message_id=-1,reply_markup={}):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["latitude"]=latitude
		parameters["longitude"]=longitude
		parameters["title"]=title
		parameters["address"]=address
		if foursquare_id != "":
 			parameters["foursquare_id"]=foursquare_id
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendVenue",json=parameters)
		return r.status_code

	def sendContact(self,chat_id,phone_number,first_name,last_name="",disable_notification=False,reply_to_message_id=-1,reply_markup={}):
		parameters={}
		parameters["chat_id"]=chat_id
		parameters["phone_number"]=phone_number
		parameters["first_name"]=first_name
		if last_name != "":
 			parameters["last_name"]=last_name
		parameters["disable_notification"]=disable_notification
		if reply_to_message_id > -1:
			parameters["reply_to_message_id"]=reply_to_message_id
		if reply_markup != {}:
			parameters["reply_markup"]=reply_markup
		r=requests.post(self.url+"sendContact",json=parameters)
		return r.status_code

	def sendChatAction(self,chat_id,action):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["action"]=action
		r=requests.post(self.url+"sendChatAction",json=parameters)
		return r.status_code

	def getUserProfilePhotos(self,user_id,offset=-1,limit=-1):
 		parameters={}
		parameters["user_id"]=user_id
		if offset > -1:
			parameters["offset"]=offset
		if limit > -1:
			parameters["limit"]=limit	
 		r=requests.get(self.url+"getUserProfilePhotos")
		return r.json()
	
	def getFile(self,file_id):
 		parameters={}
		parameters["file_id"]=file_id
		r=requests.get(self.url+"getFile")
		return r.json()

	def kickChatMember(self,chat_id,user_id):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["user_id"]=user_id
		r=requests.post(self.url+"kickChatMember",json=parameters)
		return r.status_code

	def leaveChat(self,chat_id):
 		parameters={}
		parameters["chat_id"]=chat_id
		r=requests.post(self.url+"leaveChat",json=parameters)
		return r.status_code
	
	def unbanChatMember(self,chat_id,user_id):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["user_id"]=user_id
		r=requests.post(self.url+"unbanChatMember",json=parameters)
		return r.status_code

	def getChat(self,chat_id):
 		parameters={}
		parameters["chat_id"]=chat_id
		r=requests.get(self.url+"getChat")
		return r.json()

	def getChatAdministrators(self,chat_id):
 		parameters={}
		parameters["chat_id"]=chat_id
		r=requests.get(self.url+"getChatAdministrators")
		return r.json()

	def getChatMembersCount(self,chat_id):
 		parameters={}
		parameters["chat_id"]=chat_id
		r=requests.get(self.url+"getChatMembersCount")
		return r.json()

	def getChatMember(self,chat_id,user_id):
 		parameters={}
		parameters["chat_id"]=chat_id
		parameters["user_id"]=user_id
		r=requests.get(self.url+"getChatMember")
		return r.json()

	def answerCallbackQuery(self,callback_query_id,text="",show_alert=False):
 		parameters={}
		parameters["callback_query_id"]=callback_query_id
		if text != "":
 			parameters["text"]=text
		parameters["show_alert"]=show_alert
		r=requests.post(self.url+"answerCallbackQuery",json=parameters)
		return r.status_code
