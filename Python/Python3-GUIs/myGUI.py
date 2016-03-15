import wx

class windowClass(wx.Frame):
    
    def __init__(self, parent, title):
        super(windowClass, self).__init__(parent, title=title, size =(300,100))

        self.Move((500, 250)) # sets postion of window when opened # try also self.Centre
        self.Show()

app = wx.App()
windowClass(None, title = 'QuickSocialNetwork ')
app.MainLoop()
