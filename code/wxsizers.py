import wx
import os

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname = ''

        # A '-1' in the size parameter instructs wxWidgets to use the default size
        wx.Frame.__init__(self, parent, title=title, size=(200,-1))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        # Setting up the menu
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open a file to edit")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        menuExit  = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")

        # Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)

        # Create the event bindings
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range (0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)

        # Use some sizers to see layour options
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)

        # Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self, event):
        dlg = wx.MessageDialog(self, "A sample editor \n in wxPython", "About ...", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit (self, event):
        self.Close(True)

    def OnOpen(self, event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname  = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

app = wx.App(False)
frame = MainWindow(None, "Small editor")
app.MainLoop()
