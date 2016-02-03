### Widget - CheckBox


import wx

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(300,250))
        panel = wx.Panel(self)
        
        wx.CheckBox(panel, label='Male', pos=(100, 50))
        wx.CheckBox(panel, label='Female', pos=(100, 80))

app = wx.App()
frame = Frame("wxPython Widgets!")
frame.Show()
app.MainLoop()
