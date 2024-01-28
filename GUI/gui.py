import wx



class Calculator(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Calculator.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.FRAME_NO_TASKBAR | wx.MINIMIZE_BOX
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((321, 318))
        self.SetTitle("Calculator")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.Numbers = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.Numbers.SetMinSize((350, 40))
        self.Numbers.SetBackgroundColour(wx.NullColour)
        self.Numbers.SetForegroundColour(wx.NullColour)
        self.Numbers.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_1.Add(self.Numbers, 0, 0, 0)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)

        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_8, 1, wx.EXPAND, 0)

        self.button_27 = wx.Button(self.panel_1, wx.ID_ANY, "(")
        self.button_27.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_8.Add(self.button_27, 0, 0, 0)

        self.button_26 = wx.Button(self.panel_1, wx.ID_ANY, ")")
        self.button_26.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_8.Add(self.button_26, 0, 0, 0)

        self.list_box_1 = wx.ListBox(self.panel_1, wx.ID_ANY, choices=[])
        self.list_box_1.SetMinSize((75, 45))
        self.list_box_1.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_8.Add(self.list_box_1, 0, 0, 0)

        self.divinate = wx.Button(self.panel_1, wx.ID_ANY, u"÷")
        self.divinate.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_8.Add(self.divinate, 0, 0, 0)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)

        self.button_7 = wx.Button(self.panel_1, wx.ID_ANY, "7")
        self.button_7.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_4.Add(self.button_7, 0, 0, 0)

        self.button_8 = wx.Button(self.panel_1, wx.ID_ANY, "8")
        self.button_8.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_4.Add(self.button_8, 0, 0, 0)

        self.button_9 = wx.Button(self.panel_1, wx.ID_ANY, "9")
        self.button_9.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_4.Add(self.button_9, 0, 0, 0)

        self.button_multi = wx.Button(self.panel_1, wx.ID_ANY, u"×")
        self.button_multi.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_4.Add(self.button_multi, 0, 0, 0)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)

        self.button_4 = wx.Button(self.panel_1, wx.ID_ANY, "4")
        self.button_4.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_5.Add(self.button_4, 0, 0, 0)

        self.button_5 = wx.Button(self.panel_1, wx.ID_ANY, "5")
        self.button_5.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_5.Add(self.button_5, 0, 0, 0)

        self.button_6 = wx.Button(self.panel_1, wx.ID_ANY, "6")
        self.button_6.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_5.Add(self.button_6, 0, 0, 0)

        self.button_minus = wx.Button(self.panel_1, wx.ID_ANY, "-")
        self.button_minus.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_5.Add(self.button_minus, 0, 0, 0)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)

        self.button_1 = wx.Button(self.panel_1, wx.ID_ANY, "1")
        self.button_1.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(self.button_1, 0, 0, 0)

        self.button_2 = wx.Button(self.panel_1, wx.ID_ANY, "2")
        self.button_2.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(self.button_2, 0, 0, 0)

        self.button_3 = wx.Button(self.panel_1, wx.ID_ANY, "3")
        self.button_3.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(self.button_3, 0, 0, 0)

        self.button_plus = wx.Button(self.panel_1, wx.ID_ANY, "+")
        self.button_plus.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_6.Add(self.button_plus, 0, 0, 0)

        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)

        self.button_clear = wx.Button(self.panel_1, wx.ID_ANY, "CE")
        self.button_clear.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_7.Add(self.button_clear, 0, 0, 0)

        self.button_delete = wx.Button(self.panel_1, wx.ID_ANY, u"⌫")
        self.button_delete.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_7.Add(self.button_delete, 0, 0, 0)

        self.button_0 = wx.Button(self.panel_1, wx.ID_ANY, "0")
        self.button_0.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_7.Add(self.button_0, 0, 0, 0)

        self.button_equal = wx.Button(self.panel_1, wx.ID_ANY, "=")
        self.button_equal.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizer_7.Add(self.button_equal, 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()


        self.Bind(wx.EVT_BUTTON, self.on_push_bracket_open, self.button_27)
        self.Bind(wx.EVT_BUTTON, self.on_push_bracket_close, self.button_26)
        self.Bind(wx.EVT_BUTTON, self.on_push_divinate, self.divinate)
        self.Bind(wx.EVT_BUTTON, self.on_push_7, self.button_7)
        self.Bind(wx.EVT_BUTTON, self.on_push_8, self.button_8)
        self.Bind(wx.EVT_BUTTON, self.on_push_9, self.button_9)
        self.Bind(wx.EVT_BUTTON, self.on_push_multi, self.button_multi)
        self.Bind(wx.EVT_BUTTON, self.on_push_4, self.button_4)
        self.Bind(wx.EVT_BUTTON, self.on_push_5, self.button_5)
        self.Bind(wx.EVT_BUTTON, self.on_push_6, self.button_6)
        self.Bind(wx.EVT_BUTTON, self.on_push_minus, self.button_minus)
        self.Bind(wx.EVT_BUTTON, self.on_push_1, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.on_push_2, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.on_push_3, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.on_push_plus, self.button_plus)
        self.Bind(wx.EVT_BUTTON, self.on_push_clear, self.button_clear)
        #self.Bind(wx.EVT_BUTTON, self.on_push_delete, self.button_delete)
        self.Bind(wx.EVT_BUTTON, self.on_push_0, self.button_0)
        self.Bind(wx.EVT_BUTTON, self.on_push_equal, self.button_equal)
        # end wxGlade

    # start define the buttons
    def on_push_plus(self, _):
        button = "+"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_9(self, _):
        button = "9"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_8(self, _):
        button = "8"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_7(self, _):
        button = "7"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_6(self, _):
        button = "6"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_5(self, _):
        button = "5"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_4(self, _):
        button = "4"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_3(self, _):
        button = "3"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_2(self, _):
        button = "2"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_1(self, _):
        button = "1"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)
    
    def on_push_divinate(self, _):
        button = "/"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_multi(self, _):
        button = "*"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_minus(self, _):
        button = "-"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_bracket_open(self, _):
        button = "("
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)
    
    def on_push_bracket_close(self, _):
        button = ")"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_0(self, _):
        button = "0"
        data = self.Numbers.GetValue()
        self.Numbers.SetValue(data + button)

    def on_push_clear(self, _):
        self.Numbers.SetValue("")

    def on_push_equal(self, _):
        data = self.Numbers.GetValue()
        res = str(eval(data))
        self.Numbers.SetValue(res)
        self.list_box_1.AppendItems([f"{data}={res}"])



        # end of class Calculator


class MyApp(wx.App):
    def OnInit(self):
        self.Calculator = Calculator(None, wx.ID_ANY, "")
        self.SetTopWindow(self.Calculator)
        self.Calculator.Show()
        return True