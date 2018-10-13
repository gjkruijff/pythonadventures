## wiki.wxpython.org/Getting%20Started

import os 
import wx

xSize = 300
ySize = 400

class MainWindow (wx.Frame):
    def __init__ (self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(xSize, ySize))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.CreateStatusBar() # A status bar at the bottom of the window

        fileMenu = wx.Menu()
        menuNew = fileMenu.Append(wx.ID_NEW, "&New", "Start a new game")
        fileMenu.AppendSeparator()
        menuOpen = fileMenu.Append(wx.ID_OPEN, "&Load", "Load a previously stored game")
        menuSave = fileMenu.Append(wx.ID_SAVE, "&Save", "Save the current game")
        fileMenu.AppendSeparator() # The next things get displayed elsewhere ... Mac-style
        menuAbout = fileMenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        menuExit  = fileMenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        self.SetMenuBar(menuBar)

        # Set event bindings
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnAbout (self, event):
        dlg = wx.MessageDialog(self, "A Small Text Editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy()   # Destroy when finished

    def OnExit (self, event):
        self.Close(True)

    def OnOpen (self, event):
        self.dirname = ''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()




class MyFrame (wx.Frame):
    # Derive a new class of Frame
    def __init__ (self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(xSize, ySize))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = MainWindow(None, "Small Editor")
app.MainLoop()
