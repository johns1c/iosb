#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0pre on Fri Sep 17 13:52:39 2021 from "D:\CJWork\Python\iosb\IOSb.wxg"
#

import wx





class IOSb_View(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((593, 600))
        self.SetTitle("iOS Device Backup")
        self.SetBackgroundColour(wx.Colour(171, 171, 44031))
        self.SetFocus()

        # Menu Bar
        self.Main_Frame_Menubar = wx.MenuBar()
        self.File = wx.Menu()
        self.Main_Frame_Menubar.Open = self.File.Append(wx.ID_ANY, "Open", "")
        self.Bind(wx.EVT_MENU, self.DoOpen, self.Main_Frame_Menubar.Open)
        self.Main_Frame_Menubar.Export = self.File.Append(wx.ID_ANY, "Export", "Save list of files")
        self.Bind(wx.EVT_MENU, self.DoExport, self.Main_Frame_Menubar.Export)
        self.Main_Frame_Menubar.Import = self.File.Append(wx.ID_ANY, "Import", "Copy new files from a given source location")
        self.Bind(wx.EVT_MENU, self.DoImport, self.Main_Frame_Menubar.Import)
        self.Main_Frame_Menubar.Quit = self.File.Append(wx.ID_ANY, "Quit", "")
        self.Bind(wx.EVT_MENU, self.DoQuit, self.Main_Frame_Menubar.Quit)
        self.Main_Frame_Menubar.Append(self.File, "File")
        self.Query = wx.Menu()
        self.Main_Frame_Menubar.QueryEnter = self.Query.Append(wx.ID_ANY, "Enter Query", "Enter Fields to be searched for")
        self.Bind(wx.EVT_MENU, self.OnEnterQuery, self.Main_Frame_Menubar.QueryEnter)
        self.Main_Frame_Menubar.QueryPrevious = self.Query.Append(wx.ID_ANY, "Last Query", "Paste in last query criteria")
        self.Bind(wx.EVT_MENU, self.OnLastQuery, self.Main_Frame_Menubar.QueryPrevious)
        self.Main_Frame_Menubar.QueryExec = self.Query.Append(wx.ID_ANY, "Execute Query", "Apply the defined filter")
        self.Bind(wx.EVT_MENU, self.OnRunQuery, self.Main_Frame_Menubar.QueryExec)
        self.Main_Frame_Menubar.QueryAll = self.Query.Append(wx.ID_ANY, "Show All", "Shows all entries in the Data Base")
        self.Bind(wx.EVT_MENU, self.OnQueryAll, self.Main_Frame_Menubar.QueryAll)
        self.Main_Frame_Menubar.QueryCncl = self.Query.Append(wx.ID_ANY, "Cancel Query", "Back to showing results")
        self.Bind(wx.EVT_MENU, self.OnCnclQuery, self.Main_Frame_Menubar.QueryCncl)
        self.Main_Frame_Menubar.Append(self.Query, "Query")
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Run Queued Actions", "")
        self.Bind(wx.EVT_MENU, self.OnRunActions, item)
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "View Queue", "")
        self.Bind(wx.EVT_MENU, self.On_View_Actions, item)
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Clear Queue", "Remove any queued Actions")
        self.Bind(wx.EVT_MENU, self.OnClearActions, item)
        self.Main_Frame_Menubar.Append(wxglade_tmp_menu, "Process")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ANY, "Application", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "PDF Viewer", "")
        wxglade_tmp_menu.Append(wx.ID_ANY, "File Locations", "")
        self.Main_Frame_Menubar.Append(wxglade_tmp_menu, "Settings")
        self.Help = wx.Menu()
        self.Main_Frame_Menubar.Append(self.Help, "Help")
        self.SetMenuBar(self.Main_Frame_Menubar)
        # Menu Bar end

        sizer_s1 = wx.FlexGridSizer(7, 1, 0, 0)

        self.Directory_text = wx.StaticText(self, wx.ID_ANY, "Backup Directory")
        sizer_s1.Add(self.Directory_text, 0, 0, 0)

        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_s1.Add(static_line_1, 0, wx.EXPAND, 0)

        self.domain_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.domain_list.SetFocus()
        self.domain_list.AppendColumn("Domain", format=wx.LIST_FORMAT_LEFT, width=-1)
        sizer_s1.Add(self.domain_list, 1, wx.EXPAND, 0)

        static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        sizer_s1.Add(static_line_2, 0, wx.EXPAND, 0)

        self.file_list = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.file_list.AppendColumn("A", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.file_list.AppendColumn("B", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.file_list.AppendColumn("C", format=wx.LIST_FORMAT_LEFT, width=-1)
        sizer_s1.Add(self.file_list, 1, wx.EXPAND, 0)

        static_line_3 = wx.StaticLine(self, wx.ID_ANY)
        sizer_s1.Add(static_line_3, 0, wx.EXPAND, 0)

        self.window_3 = IOSb_File_Properties(self, wx.ID_ANY)
        sizer_s1.Add(self.window_3, 1, wx.EXPAND, 0)

        sizer_s1.AddGrowableCol(0)
        self.SetSizer(sizer_s1)

        self.Layout()

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.On_Select_Domain, self.domain_list)

    def DoOpen(self, event):
        print("Event handler 'DoOpen' not implemented!")
        event.Skip()

    def DoExport(self, event):
        print("Event handler 'DoExport' not implemented!")
        event.Skip()

    def DoImport(self, event):
        print("Event handler 'DoImport' not implemented!")
        event.Skip()

    def DoQuit(self, event):
        print("Event handler 'DoQuit' not implemented!")
        event.Skip()

    def OnEnterQuery(self, event):
        print("Event handler 'OnEnterQuery' not implemented!")
        event.Skip()

    def OnLastQuery(self, event):
        print("Event handler 'OnLastQuery' not implemented!")
        event.Skip()

    def OnRunQuery(self, event):
        print("Event handler 'OnRunQuery' not implemented!")
        event.Skip()

    def OnQueryAll(self, event):
        print("Event handler 'OnQueryAll' not implemented!")
        event.Skip()

    def OnCnclQuery(self, event):
        print("Event handler 'OnCnclQuery' not implemented!")
        event.Skip()

    def OnRunActions(self, event):
        print("Event handler 'OnRunActions' not implemented!")
        event.Skip()

    def On_View_Actions(self, event):
        print("Event handler 'On_View_Actions' not implemented!")
        event.Skip()

    def OnClearActions(self, event):
        print("Event handler 'OnClearActions' not implemented!")
        event.Skip()

    def DoHelp(self, event):
        print("Event handler 'DoHelp' not implemented!")
        event.Skip()

    def On_Select_Domain(self, event):
        print("Event handler 'On_Select_Domain' not implemented!")
        event.Skip()


class IOSb_Open(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.STAY_ON_TOP
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((620, 480))
        self.SetTitle("File  /  Catalog Open")
        self.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.SetToolTip("Please supply location of files and the supporting sqllite catalogue")
        self.SetFocus()

        grid_sizer_2 = wx.FlexGridSizer(11, 4, 2, 2)

        self.label_1 = wx.StaticText(self, wx.ID_ANY, "Directory")
        grid_sizer_2.Add(self.label_1, 1, 0, 0)

        grid_sizer_2.Add((240, 20), 7, wx.ALIGN_RIGHT | wx.EXPAND | wx.FIXED_MINSIZE, 0)

        grid_sizer_2.Add((120, 20), 1, wx.EXPAND | wx.FIXED_MINSIZE, 0)

        grid_sizer_2.Add((120, 20), 1, wx.EXPAND | wx.FIXED_MINSIZE, 0)

        self.label_2 = wx.StaticText(self, wx.ID_ANY, "Path", style=wx.ALIGN_RIGHT)
        grid_sizer_2.Add(self.label_2, 1, wx.ALIGN_RIGHT | wx.EXPAND, 0)

        self.path_combo = wx.ComboBox(self, wx.ID_ANY, choices=[], style=0)
        self.path_combo.SetMinSize((200, -1))
        grid_sizer_2.Add(self.path_combo, 7, wx.EXPAND, 0)

        self.PathBrowseButton = wx.Button(self, wx.ID_ANY, "Browse")
        grid_sizer_2.Add(self.PathBrowseButton, 1, 0, 0)

        grid_sizer_2.Add((120, 20), 1, wx.EXPAND | wx.FIXED_MINSIZE, 0)

        self.status_label = wx.StaticText(self, wx.ID_ANY, "Status")
        self.status_label.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_2.Add(self.status_label, 0, wx.ALIGN_BOTTOM, 0)

        grid_sizer_2.Add((0, 0), 0, 0, 0)

        self.target_label = wx.StaticText(self, wx.ID_ANY, "Device")
        self.target_label.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        grid_sizer_2.Add(self.target_label, 1, wx.ALIGN_BOTTOM, 0)

        grid_sizer_2.Add((0, 0), 0, 0, 0)

        self.date_label = wx.StaticText(self, wx.ID_ANY, "Date")
        grid_sizer_2.Add(self.date_label, 1, wx.ALIGN_RIGHT, 0)

        self.date_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.date_text, 0, 0, 0)

        self.device_name_label = wx.StaticText(self, wx.ID_ANY, "Device Name")
        grid_sizer_2.Add(self.device_name_label, 1, wx.ALIGN_RIGHT, 0)

        self.device_name_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.device_name_text, 0, 0, 0)

        self.ifb_label = wx.StaticText(self, wx.ID_ANY, "Is Full Backup")
        grid_sizer_2.Add(self.ifb_label, 0, wx.ALIGN_RIGHT, 0)

        self.ifb_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.ifb_text, 0, 0, 0)

        product_name_label = wx.StaticText(self, wx.ID_ANY, "Product Name")
        grid_sizer_2.Add(product_name_label, 0, wx.ALIGN_RIGHT, 0)

        self.product_name_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.product_name_text, 0, 0, 0)

        self.ss_label = wx.StaticText(self, wx.ID_ANY, "Snapshot State")
        grid_sizer_2.Add(self.ss_label, 0, wx.ALIGN_RIGHT, 0)

        self.ss_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.ss_text, 0, 0, 0)

        product_version_label = wx.StaticText(self, wx.ID_ANY, "Product Version", style=wx.ALIGN_RIGHT)
        grid_sizer_2.Add(product_version_label, 0, wx.ALIGN_RIGHT, 0)

        self.product_version_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.product_version_text, 0, 0, 0)

        uuid_label = wx.StaticText(self, wx.ID_ANY, "UUID")
        grid_sizer_2.Add(uuid_label, 0, wx.ALIGN_RIGHT, 0)

        self.uuid_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.uuid_text, 0, wx.EXPAND, 0)

        serial_number_label = wx.StaticText(self, wx.ID_ANY, "Serial Number")
        grid_sizer_2.Add(serial_number_label, 0, wx.ALIGN_RIGHT, 0)

        self.serial_number_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.serial_number_text, 0, 0, 0)

        label_3 = wx.StaticText(self, wx.ID_ANY, "Version")
        grid_sizer_2.Add(label_3, 0, wx.ALIGN_RIGHT, 0)

        self.version_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.version_text, 0, 0, 0)

        label_6 = wx.StaticText(self, wx.ID_ANY, "IMEI")
        grid_sizer_2.Add(label_6, 0, wx.ALIGN_RIGHT, 0)

        self.imei_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.imei_text, 0, 0, 0)

        grid_sizer_2.Add((5, 10), 0, 0, 0)

        grid_sizer_2.Add((5, 10), 0, 0, 0)

        grid_sizer_2.Add((2, 40), 0, 0, 0)

        grid_sizer_2.Add((2, 40), 0, 0, 0)

        grid_sizer_2.Add((0, 0), 0, 0, 0)

        self.button_1 = wx.Button(self, wx.ID_CANCEL, "")
        grid_sizer_2.Add(self.button_1, 0, wx.ALIGN_BOTTOM, 0)

        self.Open_OK = wx.Button(self, wx.ID_OK, "")
        grid_sizer_2.Add(self.Open_OK, 0, wx.ALIGN_BOTTOM, 0)

        grid_sizer_2.Add((2, 40), 0, 0, 0)

        grid_sizer_2.Add((0, 0), 0, 0, 0)

        grid_sizer_2.Add((0, 0), 0, 0, 0)

        grid_sizer_2.AddGrowableCol(1)
        self.SetSizer(grid_sizer_2)
        grid_sizer_2.SetSizeHints(self)

        self.Layout()

        self.Bind(wx.EVT_COMBOBOX, self.OnPathChosen, self.path_combo)
        self.Bind(wx.EVT_BUTTON, self.DoBrowsePath, self.PathBrowseButton)
        self.Bind(wx.EVT_BUTTON, self.Cancel_Open, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.DoOpen, self.Open_OK)
        self.Bind(wx.EVT_INIT_DIALOG, self.DoPopen, self)

    def OnPathChosen(self, event):
        print("Event handler 'OnPathChosen' not implemented!")
        event.Skip()

    def DoBrowsePath(self, event):
        print("Event handler 'DoBrowsePath' not implemented!")
        event.Skip()

    def Cancel_Open(self, event):
        print("Event handler 'Cancel_Open' not implemented!")
        event.Skip()

    def DoOpen(self, event):
        print("Event handler 'DoOpen' not implemented!")
        event.Skip()

    def DoPopen(self, event):
        print("Event handler 'DoPopen' not implemented!")
        event.Skip()


class Cat_Move(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((1700, 800))
        self.SetTitle("Move file or catalogue entry")
        self.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.SetToolTip("Provide type of Move or Copy Action and Destination")
        self.SetFocus()

        grid_sizer_3 = wx.GridBagSizer(2, 2)

        self.label_source = wx.StaticText(self, wx.ID_ANY, "Source")
        grid_sizer_3.Add(self.label_source, (0, 0), (1, 1), 0, 0)

        grid_sizer_3.Add(120, 20, (0, 1), (1, 1), wx.ALIGN_RIGHT | wx.EXPAND | wx.FIXED_MINSIZE, 0)

        grid_sizer_3.Add(120, 20, (0, 2), (1, 1), wx.ALIGN_RIGHT | wx.EXPAND | wx.FIXED_MINSIZE, 0)

        self.label_file = wx.StaticText(self, wx.ID_ANY, "File", style=wx.ALIGN_RIGHT)
        grid_sizer_3.Add(self.label_file, (1, 0), (1, 1), wx.ALIGN_RIGHT | wx.EXPAND, 0)

        self.Source_File = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_3.Add(self.Source_File, (1, 1), (1, 1), wx.EXPAND, 0)

        self.label_location = wx.StaticText(self, wx.ID_ANY, "Location", style=wx.ALIGN_RIGHT)
        grid_sizer_3.Add(self.label_location, (2, 0), (1, 1), wx.ALIGN_RIGHT | wx.EXPAND, 0)

        self.Source_Location = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_3.Add(self.Source_Location, (2, 1), (1, 1), wx.EXPAND, 0)

        grid_sizer_3.Add(5, 10, (2, 2), (1, 1), 0, 0)

        Catalog = wx.StaticText(self, wx.ID_ANY, "Catalogue")
        grid_sizer_3.Add(Catalog, (3, 0), (1, 1), wx.ALIGN_RIGHT, 0)

        self.DB_Location = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_3.Add(self.DB_Location, (3, 1), (1, 1), wx.EXPAND, 0)

        grid_sizer_3.Add(5, 10, (3, 2), (1, 1), 0, 0)

        self.label_destination = wx.StaticText(self, wx.ID_ANY, "\nDestination\n")
        grid_sizer_3.Add(self.label_destination, (4, 0), (1, 1), 0, 0)

        grid_sizer_3.Add(5, 5, (4, 1), (1, 1), 0, 0)

        grid_sizer_3.Add(5, 10, (4, 2), (1, 1), 0, 0)

        self.label_destlocn = wx.StaticText(self, wx.ID_ANY, "Location")
        grid_sizer_3.Add(self.label_destlocn, (5, 0), (1, 1), wx.ALIGN_RIGHT, 0)

        self.Dest_Location = wx.ComboBox(self, wx.ID_ANY, choices=[], style=0)
        grid_sizer_3.Add(self.Dest_Location, (5, 1), (1, 1), wx.EXPAND, 0)

        self.CatBrowseButton = wx.Button(self, wx.ID_ANY, "Browse")
        grid_sizer_3.Add(self.CatBrowseButton, (5, 2), (1, 1), 0, 0)

        label_Name = wx.StaticText(self, wx.ID_ANY, "Name", style=wx.ALIGN_RIGHT)
        label_Name.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_3.Add(label_Name, (6, 0), (1, 1), wx.EXPAND, 0)

        self.Dest_Name = wx.TextCtrl(self, wx.ID_ANY, "")
        grid_sizer_3.Add(self.Dest_Name, (6, 1), (1, 1), wx.EXPAND, 0)

        self.Dest_Modify = wx.Button(self, wx.ID_ANY, "Toggle Name")
        grid_sizer_3.Add(self.Dest_Modify, (6, 2), (1, 1), 0, 0)

        grid_sizer_3.Add(5, 10, (7, 1), (1, 1), 0, 0)

        self.Label_Action = wx.StaticText(self, wx.ID_ANY, "Action", style=wx.ALIGN_RIGHT)
        grid_sizer_3.Add(self.Label_Action, (8, 0), (1, 1), wx.ALIGN_RIGHT | wx.ALL, 5)

        self.Move_Action = wx.Choice(self, wx.ID_ANY, choices=["Copy", "Move"])
        self.Move_Action.SetSelection(0)
        grid_sizer_3.Add(self.Move_Action, (8, 1), (1, 1), 0, 0)

        self.Catalog_Update_Checkbox = wx.CheckBox(self, wx.ID_ANY, "Update Catalogue")
        self.Catalog_Update_Checkbox.SetValue(1)
        grid_sizer_3.Add(self.Catalog_Update_Checkbox, (9, 1), (1, 1), 0, 0)

        self.Move_Option = wx.Choice(self, wx.ID_ANY, choices=["Defer", "Immediate"])
        self.Move_Option.SetSelection(0)
        grid_sizer_3.Add(self.Move_Option, (9, 2), (1, 1), 0, 0)

        grid_sizer_3.Add(5, 20, (10, 0), (1, 1), 0, 0)

        self.Move_Cancel = wx.Button(self, wx.ID_CANCEL, "")
        grid_sizer_3.Add(self.Move_Cancel, (11, 1), (1, 1), wx.ALIGN_BOTTOM, 0)

        self.Move_OK = wx.Button(self, wx.ID_OK, "")
        grid_sizer_3.Add(self.Move_OK, (11, 2), (1, 1), wx.ALIGN_BOTTOM, 0)

        self.Move_Message = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.Move_Message.SetMinSize((500, -1))
        grid_sizer_3.Add(self.Move_Message, (12, 0), (1, 3), wx.BOTTOM | wx.EXPAND | wx.TOP, 0)

        grid_sizer_3.AddGrowableCol(1)
        self.SetSizer(grid_sizer_3)
        grid_sizer_3.SetSizeHints(self)

        self.Layout()

        self.Bind(wx.EVT_COMBOBOX, self.DoNewDest, self.Dest_Location)
        self.Bind(wx.EVT_TEXT, self.DoNewDest, self.Dest_Location)
        self.Bind(wx.EVT_BUTTON, self.DoBrowseDest, self.CatBrowseButton)
        self.Bind(wx.EVT_TEXT, self.DoNewDest, self.Dest_Name)
        self.Bind(wx.EVT_BUTTON, self.DoToggleDest, self.Dest_Modify)
        self.Bind(wx.EVT_CHOICE, self.DoNewAction, self.Move_Action)
        self.Bind(wx.EVT_BUTTON, self.Cancel_Open, self.Move_Cancel)
        self.Bind(wx.EVT_BUTTON, self.DoMove, self.Move_OK)

    def DoNewDest(self, event):
        print("Event handler 'DoNewDest' not implemented!")
        event.Skip()

    def DoBrowseDest(self, event):
        print("Event handler 'DoBrowseDest' not implemented!")
        event.Skip()

    def DoToggleDest(self, event):
        print("Event handler 'DoToggleDest' not implemented!")
        event.Skip()

    def DoNewAction(self, event):
        print("Event handler 'DoNewAction' not implemented!")
        event.Skip()

    def Cancel_Open(self, event):
        print("Event handler 'Cancel_Open' not implemented!")
        event.Skip()

    def DoMove(self, event):
        print("Event handler 'DoMove' not implemented!")
        event.Skip()


class IOSb_File_Properties(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetTitle("dialog")

        grid_sizer_2 = wx.FlexGridSizer(9, 3, 2, 2)

        self.label_1 = wx.StaticText(self, wx.ID_ANY, "Directory")
        grid_sizer_2.Add(self.label_1, 1, 0, 0)

        grid_sizer_2.Add((240, 20), 7, wx.ALIGN_RIGHT | wx.EXPAND | wx.FIXED_MINSIZE, 0)

        grid_sizer_2.Add((120, 20), 1, wx.EXPAND | wx.FIXED_MINSIZE, 0)

        self.label_2 = wx.StaticText(self, wx.ID_ANY, "Path", style=wx.ALIGN_RIGHT)
        grid_sizer_2.Add(self.label_2, 1, wx.ALIGN_RIGHT | wx.EXPAND, 0)

        self.path_combo = wx.ComboBox(self, wx.ID_ANY, choices=[], style=0)
        self.path_combo.SetMinSize((100, -1))
        grid_sizer_2.Add(self.path_combo, 7, wx.EXPAND, 0)

        self.PathBrowseButton = wx.Button(self, wx.ID_ANY, "Browse")
        grid_sizer_2.Add(self.PathBrowseButton, 1, 0, 0)

        self.label_cat = wx.StaticText(self, wx.ID_ANY, "Info")
        grid_sizer_2.Add(self.label_cat, 1, 0, 0)

        grid_sizer_2.Add((5, 10), 3, 0, 0)

        grid_sizer_2.Add((5, 5), 2, 0, 0)

        self.date_label = wx.StaticText(self, wx.ID_ANY, "Date")
        grid_sizer_2.Add(self.date_label, 1, wx.ALIGN_RIGHT, 0)

        self.date_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.date_text, 0, 0, 0)

        grid_sizer_2.Add((0, 0), 0, 0, 0)

        self.ifb_label = wx.StaticText(self, wx.ID_ANY, "Is Full Backup")
        grid_sizer_2.Add(self.ifb_label, 0, wx.ALIGN_RIGHT, 0)

        self.ifb_text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        grid_sizer_2.Add(self.ifb_text, 0, 0, 0)

        grid_sizer_2.Add((5, 10), 0, 0, 0)

        self.ss_label = wx.StaticText(self, wx.ID_ANY, "Snapshot State")
        grid_sizer_2.Add(self.ss_label, 0, wx.ALIGN_RIGHT, 0)

        self.ss_text = wx.TextCtrl(self, wx.ID_ANY, "")
        grid_sizer_2.Add(self.ss_text, 0, 0, 0)

        grid_sizer_2.Add((5, 10), 0, 0, 0)

        uuid_label = wx.StaticText(self, wx.ID_ANY, "UUID")
        grid_sizer_2.Add(uuid_label, 0, wx.ALIGN_RIGHT, 0)

        self.uuid_text = wx.TextCtrl(self, wx.ID_ANY, "")
        grid_sizer_2.Add(self.uuid_text, 0, 0, 0)

        grid_sizer_2.Add((5, 10), 0, 0, 0)

        label_3 = wx.StaticText(self, wx.ID_ANY, "Version")
        grid_sizer_2.Add(label_3, 0, wx.ALIGN_RIGHT, 0)

        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "")
        grid_sizer_2.Add(self.text_ctrl_5, 0, 0, 0)

        grid_sizer_2.Add((0, 0), 0, 0, 0)

        grid_sizer_2.Add((2, 40), 0, 0, 0)

        self.button_1 = wx.Button(self, wx.ID_CANCEL, "")
        grid_sizer_2.Add(self.button_1, 0, wx.ALIGN_BOTTOM, 0)

        self.Open_OK = wx.Button(self, wx.ID_OK, "")
        grid_sizer_2.Add(self.Open_OK, 0, wx.ALIGN_BOTTOM, 0)

        grid_sizer_2.AddGrowableCol(1)
        self.SetSizer(grid_sizer_2)
        grid_sizer_2.Fit(self)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.DoBrowsePath, self.PathBrowseButton)
        self.Bind(wx.EVT_BUTTON, self.Cancel_Open, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.DoOpen, self.Open_OK)

    def DoBrowsePath(self, event):
        print("Event handler 'DoBrowsePath' not implemented!")
        event.Skip()

    def Cancel_Open(self, event):
        print("Event handler 'Cancel_Open' not implemented!")
        event.Skip()

    def DoOpen(self, event):
        print("Event handler 'DoOpen' not implemented!")
        event.Skip()


class DomainList(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("Domains")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.list_ctrl_1 = wx.ListCtrl(self.panel_1, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.LC_VRULES)
        self.list_ctrl_1.AppendColumn("Domain", format=wx.LIST_FORMAT_LEFT, width=-1)
        sizer_1.Add(self.list_ctrl_1, 6, wx.EXPAND, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()


class FileList(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("Files")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.list_ctrl_1 = wx.ListCtrl(self.panel_1, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.list_ctrl_1.AppendColumn("A", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_1.AppendColumn("B", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_1.AppendColumn("C", format=wx.LIST_FORMAT_LEFT, width=-1)
        sizer_1.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()


class IOSb_base(wx.App):
    def OnInit(self):
        self.Main_Frame = IOSb_View(None, wx.ID_ANY, "")
        self.SetTopWindow(self.Main_Frame)
        self.Main_Frame.Show()
        return True

if __name__ == "__main__":
    IOSb_app = IOSb_base(0)
    IOSb_app.MainLoop()
