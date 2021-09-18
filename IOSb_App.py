#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.1.0pre on Wed Sep 15 21:37:57 2021 from "D:\CJWork\Python\iosb\IOSb.wxg"
#
from biplist import *
import sys
import glob
import os
import sqlite3 
import datetime
import pprint
import wx
from IOSb_Base import IOSb_View as Base_View 
from IOSb_Base import IOSb_Open as Base_Open 
from biplist import *




class IOSb_View(Base_View):
    def __init__(self, *args, **kwds):
    
        Base_View.__init__(self, *args, **kwds)
        self.SetTitle("IOS Backup viewer")
        #self.window_1 = DomainList(self, wx.ID_ANY)
        #self.window_2 = FileList(self, wx.ID_ANY)
        #self.window_3 = IOSb_File_Properties(self, wx.ID_ANY)

    def OnFileRClick(self, event):
    
        self.currentItemF = self.file_list.GetFirstSelected()
        
        self.current_fileID       = self.file_list.GetItemText( self.currentItemF , 0 )
        self.current_relativePath = self.file_list.GetItemText( self.currentItemF , 1 )
        # 
        # for old versions the directory is just the backup path
        # for new versions it is split according to the first two characters of the id 
        
        self.current_file_dir     = os.path.join(  self.backup , self.current_fileID[:2] )
        self.current_file_path    = os.path.join( self.current_file_dir , self.current_fileID ) 
        self.current_file_exists  = os.path.exists( self.current_file_path )
        print( f'chosen file is {self.current_file_path} ' ) 
        self.current_file_orig = os.path.join(self.currentDomain, self.current_relativePath )
        print( f'        target {self.current_file_orig} ' ) 
        
        self.item_popup = wx.Menu()
        for entry in ["Clip", "Move", "Copy", "Delete", "Edit", "View", "Text"]:
            menu_item = self.item_popup.Append(-1, entry)
            self.Bind(wx.EVT_MENU, self.OnMenuAction, menu_item)
        # Show menu
        self.PopupMenu(self.item_popup)
        #self.contextmenu.Destroy()

    def OnMenuAction(self, event):
        ''' Determine menu event and act upon it
        '''
        menu_item = self.item_popup.FindItemById(event.GetId())
        menu_item_text = menu_item.GetItemLabelText()
        self.menu_item_text = menu_item.GetItemLabelText()

        Actions = dict((("Clip", self.DoClip), ("Copy", self.DoCMD),
                        ("Move", self.DoCMD), ("Delete", self.DoCMD),
                        ("Edit", self.DoNothing), ("View", self.DoNothing) ,
                        ("Text", self.DoNothing)))

        Action = Actions[menu_item_text]
        Action(event)
        
    def DoNothing(self, evt):
        print("Nothing doing ")

    def DoCMD(self, event):  # wxGlade: Cat_Frame.<event_handler>
        event.Skip()

        # display / entry fields
        # self.Source_File      (readonly) name of source file within source directory
        # self.Source_Location  (readonly) directory in which source file exists
        # self.DB_location      (readonly) the location information held in the catalog for a file with this name (if exists)

        MoveDialog = Catalog_Move(None, 150, ActionType=self.menu_item_text)
        MoveDialog.SetSource(self.fpath)
        MoveDialog.Show(True)

    def DoClip(self, event):
        """ put full path to backed up file onto clipboard """
        print( 'Clipping file path...' ) 

        list_separator = "\n"
        data = wx.TextDataObject()
        if isinstance( self.current_file_path , list ) :
            data.SetText(list_separator.join( self.fpath ))
        else:
            data.SetText(self.current_file_path)
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(data)
            wx.TheClipboard.Close()
        else:
            wx.MessageBox("Unable to open the clipboard", "Error")

        event.Skip()

    def DoOpen(self, event):
    
        print("Overridden Event handler 'DoOpen' is a work in progress")
    
        OpenDialog = IOSb_Open(None, 150)
        OpenDialog.Show(True)
        event.Skip()
    def On_Select_Domain( self, event )  :
    
        # determine selected domain
        # query db to find corresponding files
        # populate file list widget 
        
        
        def get_file_props(  props ) :
            
            from io import BytesIO
            with BytesIO(props) as props_f:
                props_plist = readPlist( props_f ) 
                
                zu = props_plist['$objects'][1]['LastModified']
                zs = props_plist['$objects'][1]['LastStatusChange']
                zc = props_plist['$objects'][1]['Birth']
                
                zu =  datetime.datetime.utcfromtimestamp(zu).isoformat()
                zs =  datetime.datetime.utcfromtimestamp(zs).isoformat()
                zc =  datetime.datetime.utcfromtimestamp(zc).isoformat()
                
                props_plist['$objects'][1]['LastModified']  = zu
                props_plist['$objects'][1]['LastStatusChange'] = zs
                props_plist['$objects'][1]['Birth'] = zc
                
            return props_plist 
           
        #############################################################################################
        self.currentItem = self.domain_list.GetFirstSelected()
        self.currentDomain  = self.domain_list.GetItemText( self.currentItem , 0 )
        
        # obtain files under this domain 
        qry = "select fileID, relativePath, file  from files where domain = ? and flags = 1 order by relativePath"
        cur = self.db.cursor()
        cur.execute(qry, ( self.currentDomain, )) 
        
        self.file_list.DeleteAllItems()
        
        for row in cur.fetchall() :
            props_plist = get_file_props( row[2] ) 
            last_modified      =  props_plist['$objects'][1]['LastModified'] 
            last_status_change =  props_plist['$objects'][1]['LastStatusChange'] 
            birth              =  props_plist['$objects'][1]['Birth'] 

            display_row = [  row[0] , row[1] , birth  , last_status_change , last_modified ]
            self.file_list.Append(display_row) 

        
    def DoRead( self , bkup ) :
        self.Directory_text.SetLabelText( bkup) 

        print ( 'Now...' )      

        self.backup = bkup 
        self.manifest = os.path.join( bkup , 'Manifest.db' ) 
        self.old_manifest = os.path.join( bkup , 'Manifest.mbdb' ) 
    
        if os.path.exists( self.old_manifest ) :
            print( 'old manifest' ) 
            return False
            
        elif os.path.exists( self.manifest) :
            self.db = sqlite3.connect(self.manifest)
            #db.create_function("part1", 1, part1)
            qry = 'select distinct domain from files order by 1 ; '
            cur = self.db.cursor()
            cur.execute(qry) 
            
        rc = 0    
        for row in cur.fetchall() :
            self.domain_list.Append(row)  
            rc += 1      

        print( f'{rc} domains ' )             
                 
            
        #import pdb
        #pdb.set_trace()        
            
        # pull sample file 

        

    def DoExport(self, event):
        print("Overridden Event handler 'DoExport' not implemented!")
        event.Skip()

    def DoQuit(self, event):
        print("Overridden Event handler 'DoQuit' not implemented!")
        event.Skip()


    def DoHelp(self, event):
        print("Overridden Event handler 'DoHelp' not implemented!")
        event.Skip()


class IOSb_Open(Base_Open):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLOSE_BOX | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.STAY_ON_TOP
        Base_Open.__init__(self, *args, **kwds)
        self.SetSize((620, 480))
        self.SetTitle("Backup Directory List /  Open")
        #self.DoPopen(1) 

    def DoBrowsePath(self, event):
        print("Event handler 'DoBrowsePath' not implemented!")
        event.Skip()

    def Cancel_Open(self, event):
        print("Event handler 'Cancel_Open' not implemented!")
        self.Close()
        event.Skip()

    def DoOpen(self, event):
    
        chosen_backup = self.path_combo.GetValue()
        
        zapp = wx.GetApp() 
        zview = zapp.GetTopWindow() 
        zview.DoRead( chosen_backup ) 
        
        event.Skip()

    def DoPopen(self, event):
    
        path = "C:\\Users\\*\\AppData\\Roaming\\Apple Computer\\MobileSync\\Backup\\*"
        all_paths = glob.glob(path)
        backup_list = list() 
        for f in all_paths :

            spl = os.path.join( f , 'Status.plist' )
            if os.path.exists( spl) : 
                backup_list.append( f ) 
                
        self.path_combo.Clear()
        self.path_combo.AppendItems(backup_list)


    def OnPathChosen(self, event):
        chosen_backup = self.path_combo.GetValue()
        print(f"Event handler 'OnPathChosen'  {chosen_backup} ")



        def rpl( xml_file ) :
            import plistlib 
            try:
                iplist = plistlib.load(open(xml_file,'rb'))
                return iplist
                
                wanted = ['Build Version', 'Device Name', 'Display Name', 'GUID', 'ICCID', 'IMEI',
                'Last Backup Date', 'MEID', 'Phone Number', 'Product Name', 'Product Type',
                'Product Version', 'Serial Number', 'zzzSync Settings', 'Target Identifier',
                'Target Type', 'Unique Identifier', 'zziTunes Files', 'zzziTunes Settings', 
                'iTunes Version']
                
                return dict( [( k , plist[k] ) for k  in plist if k in wanted ] )
                
            except (plistlib.InvalidFileException)as e:
                print ( "info.plist Not an xml  plist :", e )
                return dict()

        
        def rbp(binary_file)    : 
            """ dict of status values in printable form """
            try:
                plist = readPlist(binary_file)
                return dict([(k , f'{plist[k]}' ) for k in sorted(plist)])  
            except (InvalidPlistException, NotBinaryPlistException)as e:
                print ( "Not a plist :", e )
                return { 'Device Name'  : '????' }  
    
        status_file  = os.path.join( chosen_backup , 'Status.plist' )
        status = rbp( status_file ) 
        
        self.date_text.Value    = status[ 'Date' ] 
        self.ifb_text.Value     = status[ 'IsFullBackup' ] 
        self.ss_text.Value      = status[ 'SnapshotState' ] 
        self.uuid_text.Value    = status[ 'UUID' ]
        self.version_text.Value = status[ 'Version']
        
        
        info_file = os.path.join( chosen_backup , 'Info.plist' )
        info = rpl( info_file) 
       
        
        self.device_name_text.Value     = info.get( 'Device Name'     )
        self.serial_number_text.Value   = info.get( 'Serial Number'   )
        self.product_version_text.Value = info.get( 'Product Version' )
        self.product_name_text.Value    = info.get( 'Product Name'    )
        self.imei_text.Value            = info.get(  'IMEI' ) 
        
        
        print("Event handler 'DoPopen' not is a work in progress!")
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
        self.SetTitle("frame")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        self.list_ctrl_1 = wx.ListCtrl(self.panel_1, wx.ID_ANY, style=wx.LC_HRULES | wx.LC_REPORT | wx.LC_VRULES)
        self.list_ctrl_1.AppendColumn("A", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_1.AppendColumn("B", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.list_ctrl_1.AppendColumn("C", format=wx.LIST_FORMAT_LEFT, width=-1)
        sizer_1.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()


class FileList(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        self.SetTitle("frame")

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
