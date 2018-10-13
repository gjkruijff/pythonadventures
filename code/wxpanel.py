import wx

class ExampleFrame(wx.Frame):
    def __init__ (self, parent):
        wx.Frame.__init__(self, parent)
        panel = wx.Panel(self)
        self.quote = wx.StaticText(panel, label = "Your quote: Go fast and break stuff", pos=(20,30))
        self.Show()

        # A multiline TextCtrl (again)
        self.logger = wx.TextCtrl(self, pos=(300,20), size = (200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A button
        self.button = wx.Button(self, label="Save", pos=(200,325))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)

        # The edit control, one-line version
        self.lblname = wx.StaticText(self, label="Your name: ", pos=(20,60))
        self.editname = wx.TextCtrl(self, value="Enter here your name", pos=(150,60), size=(140,-1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # The combobox control
        self.sampleList = ['friends', 'advertising', 'web search', 'Yellow pages']
        self.lblhear = wx.StaticText(self, label="How did you hear from us?", pos=(20,90))
        self.edithear = wx.ComboBox(self, pos=(150,90), size=(95,-1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.edithear)

        # Checkbox
        self.insure = wx.CheckBox(self, label="Do you want insured shipment?", pos=(20,180))
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # Radio boxes
        radioList = ['blue', 'red', 'yellow', 'orange', 'green', 'purple', 'navy blue']
        rb = wx.RadioBox(self, label="what color would you like?", pos=(20,210), choices=radioList, mahorDimension=3, style=wx.RA_SPECIFY_COLS)
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

    def EvtRadioBox(self, event): self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())
    def EvtComboBox(self, event): self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())
    def OnClick(self, event): self.logger.AppendText('Click on object Id %d\n' % event.GetId())
    def EvtText(self, event): self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event): self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())


app = wx.App(False)
frame = wx.Frame(None)

panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()




app = wx.App(False)
ExampleFrame(None)
app.MainLoop()
