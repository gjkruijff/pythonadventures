## wiki.wxpython.org/Getting%20Started

import wx

xSize = 300
ySize = 400

class MainWindow (wx.Frame):
    def __init__ (self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(xSize, ySize))
        self.control = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        self.CreateStatusBar() # A status bar at the bottom of the window

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, "&New", "Start a new game")
        fileMenu.AppendSeparator()
        fileMenu.Append(wx.ID_OPEN, "&Load", "Load a previously stored game")
        fileMenu.Append(wx.ID_SAVE, "&Save", "Save the current game")
        fileMenu.AppendSeparator() # The next things get displayed elsewhere ... Mac-style
        fileMenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        fileMenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")



        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        self.SetMenuBar(menuBar)
        self.Show(True)


class MyFrame (wx.Frame):
    # Derive a new class of Frame
    def __init__ (self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(xSize, ySize))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)

app = wx.App(False)
frame = MainWindow(None, "Small Editor")
app.MainLoop()
