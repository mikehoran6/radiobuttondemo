'''
Program: radiobuttondemo.py
Author: Mike Horan
Date: 10/19/20
p.281-282

Simple python GUI application highlighting the use of radio buttons and groups
'''

from breezypythongui import EasyFrame

class RadioButtonDemo(EasyFrame):
	#Allows the user to place a restaurant order from a set of radio button options

	def __init__(self):
		#sets up window and widgets
		EasyFrame.__init__(self, title = 'Radio Button Demo', background = '#f0f0f0')
		
		#Add label,button group and radio buttons for meats
		self.addLabel(text = 'Meat', row = 0, column = 0, sticky = 'NSEW', background = '#f0f0f0')
		self.meatGroup = self.addRadiobuttonGroup(row = 1, column = 0, rowspan = 2)
		defaultRB = self.meatGroup.addRadiobutton(text = 'Chicken')
		#Make chicken the pre-selected radio button
		self.meatGroup.setSelectedButton(defaultRB)
		self.meatGroup.addRadiobutton(text = 'Beef')

		#Add label,button group and radio buttons for potatoes
		self.addLabel(text = 'Potato', row = 0, column = 1, sticky = 'NSEW', background = '#f0f0f0')
		self.taterGroup = self.addRadiobuttonGroup(row = 1, column = 1, rowspan = 2)
		defaultRB = self.taterGroup.addRadiobutton(text = 'French Fries')
		#Make french fries the pre-selected radio button
		self.taterGroup.setSelectedButton(defaultRB)
		self.taterGroup.addRadiobutton(text = 'Baked Potato')

		#Add label,button group and radio buttons for meats
		self.addLabel(text = 'Vegetable', row = 0, column = 2, sticky = 'NSEW', background = '#f0f0f0')
		self.vegGroup = self.addRadiobuttonGroup(row = 1, column = 2, rowspan = 2)
		defaultRB = self.vegGroup.addRadiobutton(text = 'Applesauce')
		#Make applesauce the pre-selected radio button
		self.vegGroup.setSelectedButton(defaultRB)
		self.vegGroup.addRadiobutton(text = 'Green Beans')



		#add command button
		self.addButton(text = 'Place Order', row = 3, column = 0, columnspan = 3, command = self.placeOrder)

	def placeOrder(self):
		#display message box with the order summary
		message = ''
		message += self.meatGroup.getSelectedButton()['text'] + '\n\n'
		message += self.taterGroup.getSelectedButton()['text'] + '\n\n'
		message += self.vegGroup.getSelectedButton()['text'] + '\n\n'
		#generate message dialog with message varibale text inside
		self.messageBox(title = 'Customer Order', message = message)



def main():
	#instantiates and pops up window
	RadioButtonDemo().mainloop()

main()