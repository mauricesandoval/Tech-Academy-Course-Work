### Widget - Static Box

import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,250))
        panel = wx.Panel(self)
        
        wx.StaticBox(panel, label='Static Box Title', pos=(10,10), size=(280,200))
        wx.StaticText(panel, label='Single line', pos=(100,100))

app = wx.App()
frame = Frame("wxPython Widgets!")
frame.Show()
app.MainLoop()
