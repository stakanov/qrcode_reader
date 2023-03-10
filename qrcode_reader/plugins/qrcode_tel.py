import re
import webbrowser
from tkinter import messagebox
import plugins 



class CodeQRTel(plugins.Code):
	def __init__(self, _type, _subtype, _data):
		self.type = _type
		self.subtype = 'tel'
		self.data = _data
		self.tel = None
		self.name = "Telephone"
		super().__init__(self.type, self.subtype, self.data)


	def check(self):    
		try:
			if result := re.search(r'^tel:(.*)$', self.data):
				self.tel = result.groups()[0]
			else: 
				return False
			return True
		except Exception as e:
			print(e)


	def actions(self):
		res = messagebox.askyesno(self.name, f"Call {self.tel} ?")
		if res:
			webbrowser.open(self.tel)	