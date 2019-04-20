from ui import ChatUI

if __name__ == '__main__':
    chat_ui = ChatUI()
    bot = chat_ui.build_bot()
    bot.mainloop()
