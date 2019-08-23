from tkinter import *
import time

from nlu import nlu_reply


class ChatUI:
    def __init__(self):
        # create UI window
        self.t = Tk()
        self.t.title('Chatting with GeoBot')

        # build 'frame' container(width, height, background
        self.frmLT = Frame(width=500, height=320, bg='white')
        self.frmLC = Frame(width=500, height=150, bg='white')
        self.frmLB = Frame(width=500, height=30)
        self.frmRT = Frame(width=350, height=500)

        # build 'controllers'
        self.txtMsgList = Text(self.frmLT)
        self.txtMsgList.tag_config('greencolor', foreground='#008C00')  # 创建tag
        self.txtMsg = Text(self.frmLC);
        # send message event
        self.txtMsg.bind("<KeyPress-Up>", self._sendMsgEvent)
        self.btnSend = Button(self.frmLB, text='Send', width=8, command=self._sendMsg)
        self.btnCancel = Button(self.frmLB, text='Cancel', width=8, command=self._cancelMsg)
        self.imgInfo = PhotoImage(file="assets/robot1.png")
        self.lblImage = Label(self.frmRT, image=self.imgInfo)
        self.lblImage.image = self.imgInfo

        # 窗口布局(span为跨越数，LT中columnspan(2)意为LT跨越两列，padx/pady意为分割比例为1/3)
        self.frmLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
        self.frmLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
        self.frmLB.grid(row=2, column=0, columnspan=2)
        self.frmRT.grid(row=0, column=2, rowspan=3, padx=2, pady=3)
        # 固定大小
        self.frmLT.grid_propagate(0)
        self.frmLC.grid_propagate(0)
        self.frmLB.grid_propagate(0)
        self.frmRT.grid_propagate(0)
        # 第3行第1列插入按钮Send
        self.btnSend.grid(row=2, column=0)
        self.btnCancel.grid(row=2, column=1)
        self.lblImage.grid()
        self.txtMsgList.grid()
        self.txtMsg.grid()

    def _sendMsg(self):  # send your message
        strMsg = 'Me:' + time.strftime("%Y-%m-%d %H:%M:%S",
                                      time.localtime()) + '\n '
        self.txtMsgList.insert(END, strMsg, 'greencolor')
        new_message = self.txtMsg.get('0.0', END)
        self.txtMsgList.insert(END, new_message)
        self.txtMsgList.insert(END, '\n')
        self.txtMsg.delete('0.0', END)

        self._replyMsg(new_message)

    def _replyMsg(self, new_message):  # make reply
        strMsg2 = 'Bot:' + time.strftime("%Y-%m-%d %H:%M:%S",
                                         time.localtime()) + '\n '
        self.txtMsgList.tag_config('redcolor', foreground='red')
        self.txtMsgList.insert(END, strMsg2, 'redcolor')
        replyMsg = nlu_reply(new_message)
        self.txtMsgList.insert(END, replyMsg)
        self.txtMsgList.insert(END, "\n")
        self.txtMsgList.insert(END, self.txtMsg.get('0.0', END))
        self.txtMsg.delete('0.0', END)

    def _cancelMsg(self):  # cancel your message
        self.txtMsg.delete('0.0', END)

    def _sendMsgEvent(self, event):  # send message event
        if event.keysym == "Up":
            self._sendMsg()

    def build_bot(self):
        return self.t