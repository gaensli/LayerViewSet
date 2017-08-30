# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 28 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui

###########################################################################
## Class layerviewset_panel
###########################################################################

class layerviewset_panel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 312,300 ), style = wx.TAB_TRAVERSAL )
		
		self.Hide()
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_DEFAULT)
		
		self.interior_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_mgr.AddPane( self.interior_panel, wx.aui.AuiPaneInfo() .Center() .CaptionVisible( False ).CloseButton( False ).Dock().Resizable().FloatingSize( wx.DefaultSize ).DockFixed( True ).Row( 1 ) )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"Layers", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetToolTipString( u"Push visible Layers onto stack." )
		
		gbSizer1.Add( self.m_staticText4, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"Renders", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText41.Wrap( -1 )
		self.m_staticText41.SetToolTipString( u"Push visible Renders onto stack." )
		
		gbSizer1.Add( self.m_staticText41, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_LEFT|wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"-v-", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText42.Wrap( -1 )
		self.m_staticText42.SetToolTipString( u"Push visible Layers and Renders onto stack." )
		
		gbSizer1.Add( self.m_staticText42, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.interior_panel, wx.ID_ANY, u"--^--", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText5.Wrap( -1 )
		self.m_staticText5.SetToolTipString( u"Pop stack and assign visible layers and/or renders." )
		
		gbSizer1.Add( self.m_staticText5, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.LEFT|wx.TOP, 5 )
		
		self._message = wx.StaticText( self.interior_panel, wx.ID_ANY, u"Click below", wx.DefaultPosition, wx.DefaultSize, 0, u"message_label" )
		self._message.Wrap( -1 )
		gbSizer1.Add( self._message, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 2 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.EXPAND|wx.TOP, 5 )
		
		self.m_splitter1 = wx.SplitterWindow( self.interior_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )
		
		self.namepanel = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL, u"namewindow" )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText19 = wx.StaticText( self.namepanel, wx.ID_ANY, u"Named set", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText19.Wrap( -1 )
		bSizer7.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		
		self.namepanel.SetSizer( bSizer7 )
		self.namepanel.Layout()
		bSizer7.Fit( self.namepanel )
		self.linkpanel = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL, u"linkwindow" )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.linkpanel, wx.ID_ANY, u"My Set", wx.DefaultPosition, wx.DefaultSize, 0|wx.RAISED_BORDER )
		self.m_staticText3.Wrap( -1 )
		bSizer3.Add( self.m_staticText3, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button3 = wx.Button( self.linkpanel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_menu3 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Name", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem5 )
		
		self.m_menuItem6 = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.AppendItem( self.m_menuItem6 )
		
		self.m_button3.Bind( wx.EVT_RIGHT_DOWN, self.m_button3OnContextMenu ) 
		
		bSizer3.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		self.linkpanel.SetSizer( bSizer3 )
		self.linkpanel.Layout()
		bSizer3.Fit( self.linkpanel )
		self.m_splitter1.SplitVertically( self.namepanel, self.linkpanel, 0 )
		gbSizer1.Add( self.m_splitter1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 3 ), wx.EXPAND, 5 )
		
		
		gbSizer1.AddGrowableCol( 2 )
		gbSizer1.AddGrowableRow( 2 )
		
		self.interior_panel.SetSizer( gbSizer1 )
		self.interior_panel.Layout()
		gbSizer1.Fit( self.interior_panel )
		
		self.m_mgr.Update()
		
		# Connect Events
		self.m_staticText4.Bind( wx.EVT_LEFT_UP, self.pushlayers )
		self.m_staticText41.Bind( wx.EVT_LEFT_UP, self.pushrenders )
		self.m_staticText42.Bind( wx.EVT_LEFT_UP, self.push )
		self.m_staticText5.Bind( wx.EVT_LEFT_UP, self.pop )
		self.m_staticText3.Bind( wx.EVT_SIZE, self.sizelabel )
		self.Bind( wx.EVT_MENU, self.nameset, id = self.m_menuItem5.GetId() )
		self.Bind( wx.EVT_MENU, self.deleteset, id = self.m_menuItem6.GetId() )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	
	
	# Virtual event handlers, overide them in your derived class
	def pushlayers( self, event ):
		event.Skip()
	
	def pushrenders( self, event ):
		event.Skip()
	
	def push( self, event ):
		event.Skip()
	
	def pop( self, event ):
		event.Skip()
	
	def sizelabel( self, event ):
		event.Skip()
	
	def nameset( self, event ):
		event.Skip()
	
	def deleteset( self, event ):
		event.Skip()
	
	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 0 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )
	
	def m_button3OnContextMenu( self, event ):
		self.m_button3.PopupMenu( self.m_menu3, event.GetPosition() )
		

