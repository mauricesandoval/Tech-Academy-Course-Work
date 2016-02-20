# Maurice Sandoval

# Social Network Access Panel

# A small window panel that provides quick access to your entire social network



import wx

class windowClass(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()
        
    def basicGUI(self):

        panel = wx.Panel(self)
        
        menuBar = wx.MenuBar()
        
        
        fileButton = wx.Menu()
        editButton = wx.Menu()
        importItem = wx.Menu()                               ####
                                                             ####  sub-menu 
        importItem.Append(wx.ID_ANY, 'Blog Entry')           ####
        importItem.Append(wx.ID_ANY, 'Resume')               ####
        importItem.Append(wx.ID_ANY, 'My Projects')

        fileButton.AppendMenu(wx.ID_ANY, 'mauricesandoval.com', importItem)
        

        toolBar = self.CreateToolBar()
        

        importToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Import', wx.Bitmap('C:/Python27/TwitterButton.png'))
        importToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Import', wx.Bitmap('C:/Python27/facebookIcon.png'))
        importToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Import', wx.Bitmap('C:/Python27/blogButton.jpg'))
        importToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Import', wx.Bitmap('C:/Python27/snapchatIcon.png'))
        importToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Import', wx.Bitmap('C:/Python27/linkedinButton.jpg'))
        importToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Import', wx.Bitmap('C:/Python27/youtube.png'))
        
        quitToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('C:/Python27/Actions-exit-icon.png'))
        
        toolBar.Realize()
        
        self.Bind(wx.EVT_TOOL, self.Quit, quitToolButton)

        
        exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit\tCtrl-Q') #### or 'Quit\tDon\'t do it!')
        exitItem.SetBitmap(wx.Bitmap('C:/Python27/Actions-exit-icon.png'))
        fileButton.AppendItem(exitItem)


        
        menuBar.Append(fileButton, 'Website')
        menuBar.Append(editButton, 'GitHub')
        

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)
 

        wx.TextCtrl(panel, pos=(66, 18), size=(250, 50))

        aweText = wx.StaticText(panel, -1, 'Blog Entry', (175,3))
        aweText.SetForegroundColour('black')
        aweText.SetBackgroundColour('white')



        self.SetTitle('Social Network Access Panel')
        self.Show(True)

    def Quit(self, e):
        self.Close()

def main():
    app = wx.App()
    windowClass(None)

    app.MainLoop()


main()

