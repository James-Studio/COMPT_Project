from transitions.extensions import GraphMachine

from utils import visit_link, send_text_message, send_button_message

from linebot.models import MessageTemplateAction

import webbrowser




class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_help(self, event):
        text = event.message.text
        if text.lower() == "help":
            return True
        return False 
            
    def is_going_to_laptop(self, event):
        text = event.message.text
        if text.lower() == "laptop":
            return True
        return False

    def is_going_to_desktop(self, event):
        text = event.message.text
        if text.lower() == "desktop":
            return True
        return False

    def is_going_to_phone(self, event):
        text = event.message.text
        if text.lower() == "phone":
            return True
        return False

    def is_going_to_info(self, event):
        text = event.message.text
        if text.lower() == "info":
            return True
        return False 
    
    def is_going_to_apple_phone(self, event):
        text = event.message.text
        if text.lower() == "apple":
            return True
        return False
    
    def is_going_to_apple_desktop(self, event):
        text = event.message.text
        if text.lower() == "apple":
            return True
        return False
    
    def is_going_to_apple_laptop(self, event):
        text = event.message.text
        if text.lower() == "apple":
            return True
        return False

    def is_going_to_samsung(self, event):
        text = event.message.text
        if text.lower() == "samsung":
            return True
        return False

    def is_going_to_asus_laptop(self, event):
        text = event.message.text
        if text.lower() == "asus":
            return True
        return False
    
    def is_going_to_asus_desktop(self, event):
        text = event.message.text
        if text.lower() == "asus":
            return True
        return False

    def is_going_to_msi_laptop(self, event):
        text = event.message.text
        if text.lower() == "msi":
            return True
        return False

    def is_going_to_msi_desktop(self, event):
        text = event.message.text
        if text.lower() == "msi":
            return True
        return False

    def is_going_to_hwawei(self, event):
        text = event.message.text
        if text.lower() == "hwawei":
            return True
        return False

    def is_going_to_microsoft(self, event):
        text = event.message.text
        if text.lower() == "microsoft":
            return True
        return False

    def is_going_to_youtuber(self, event):
        text = event.message.text
        if text.lower() == "youtuber":
            return True
        return False
    
    def is_going_to_ted(self, event):
        text = event.message.text
        if text.lower() == "ted":
            return True
        return False 
    
    def is_going_to_report(self, event):
        text = event.message.text
        if text.lower() == "report":
            return True
        return False


# write activation function here !

    def on_enter_help(self, event):
        print("enter help")
        title = "Help Center"
        text = "Press the service you need !"
        # Remember the button should not be more than 4 items !!!
        btn = [
	            MessageTemplateAction(
	                label = 'Laptop',
	                text ='Laptop'
	            ),
                MessageTemplateAction(
	                label = 'Desktop',
	                text = 'Desktop'
	            ),
	            MessageTemplateAction(
	                label = 'Phone',
	                text = 'Phone'
	            ),
	            MessageTemplateAction(
	                label = 'Tech Info',
	                text ='Info'
	            )
	        ]
        url = "https://images.unsplash.com/photo-1461958508236-9a742665a0d5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80"
        reply_token = event.reply_token
        send_button_message(reply_token, title, text, btn, url)

    def on_enter_laptop(self, event):
        print("enter laptop")
        title = "Which brand do you prefer ?"
        text = "Press the brand you would like to know more about !!!"
        # Remember the button should not be more than 4 items !!!
        btn = [
	            MessageTemplateAction(
	                label = 'Apple',
	                text ='Apple'
	            ),
                MessageTemplateAction(
	                label = 'Microsoft',
	                text = 'Microsoft'
	            ),
	            MessageTemplateAction(
	                label = 'Asus',
	                text = 'Asus'
	            ),
	            MessageTemplateAction(
	                label = 'Msi',
	                text ='Msi'
	            )
	            
	        ]
        url = "https://images.unsplash.com/photo-1531297484001-80022131f5a1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1420&q=80"
        reply_token = event.reply_token
        send_button_message(reply_token, title, text, btn, url)

    def on_enter_desktop(self, event):
        print("enter desktop")
        title = "Which brand do you prefer ?"
        text = "Press the brand you would like to know more about !!!"
        # Remember the button should not be more than 4 items !!!
        btn = [
	            MessageTemplateAction(
	                label = 'Apple',
	                text ='Apple'
	            ),
	            MessageTemplateAction(
	                label = 'Asus',
	                text = 'Asus'
	            ),
	            MessageTemplateAction(
	                label = 'Msi',
	                text ='Msi'
	            )
	        ]
        url = "https://images.unsplash.com/photo-1529336953128-a85760f58cb5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
        reply_token = event.reply_token
        send_button_message(reply_token, title, text, btn, url)
        
    def on_enter_phone(self, event):
        print("enter phone")
        title = "Which brand do you prefer ?"
        text = "Press the brand you would like to know more about !!!"
        # Remember the button should not be more than 4 items !!!
        btn = [
	            MessageTemplateAction(
	                label = 'Apple',
	                text ='Apple'
	            ),
                MessageTemplateAction(
	                label = 'Samsung',
	                text = 'Samsung'
	            ),
	            MessageTemplateAction(
	                label = 'Hwawei',
	                text = 'Hwawei'
                )
	        ]
        url = "https://images.unsplash.com/photo-1585060544812-6b45742d762f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1481&q=80"
        reply_token = event.reply_token
        send_button_message(reply_token, title, text, btn, url)

    def on_enter_info(self, event):
        print("enter tech_info")
        title = "Latest Tech Information"
        text = "Press the oner you prefer !"
        # Remember the button should not be more than 4 items !!!
        btn = [
	            MessageTemplateAction(
	                label = 'Youtuber',
	                text ='Youtuber'
	            ),
                MessageTemplateAction(
	                label = 'Report',
	                text = 'Report'
	            ),
                MessageTemplateAction(
                    label = 'TED',
                    text = 'TED'
                )
	        ]
        url = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1472&q=80"
        reply_token = event.reply_token
        send_button_message(reply_token, title, text, btn, url)
    
    def on_enter_apple_phone(self,event):
        url = "https://www.apple.com/iphone-13/"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token
    
    def on_enter_apple_laptop(self,event):
        url = "https://www.apple.com/macbook-pro-14-and-16/"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token

    def on_enter_apple_desktop(self, event):
        url = "https://www.apple.com/imac/"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token
    
    def on_enter_samsung(self, event):
        url = "https://www.samsung.com/global/galaxy/"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token

    def on_enter_msi_laptop(self, event):
        url = "https://www.msi.com/Laptops/Products#?tag=GE-Raider-Series"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token
        
    def on_enter_msi_desktop(self, event):
        url = "https://www.msi.com/Desktops/Products#?tag=Nightblade-Series"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token
           
    def on_enter_asus_laptop(self,event):
        url = "https://www.asus.com/us/Laptops/For-Gaming/All-series/"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token

    def on_enter_asus_desktop(self,event):
        url = "https://www.asus.com/us/Displays-Desktops/Gaming-Tower-PCs/All-series/"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token
     
    def on_enter_hwawei(self,event):
        url = "https://www.huawei.com/en/"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token

    def on_enter_microsoft(self,event):
        url = "https://www.microsoft.com/zh-tw/"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token

# tech info
    def on_enter_youtuber(self, event):
        url = "https://www.youtube.com/c/mkbhd"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token

    def on_enter_ted(self, event):
        url = "https://www.ted.com/topics/technology"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token

    def on_enter_report(self, event):
        url = "https://www.cnbc.com/technology/"
        send_text_message(event.reply_token, url)
        reply_token = event.reply_token
