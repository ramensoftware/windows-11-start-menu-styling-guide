# Windows11_Metro10 theme for Windows 11 Start Menu Styler

A simple theme inspired by the Windows 10 Metro Start menu.

**Author**: [Ian Div](https://github.com/iandiv)

![Screenshot](screenshot.png)

## Theme selection

The theme is integrated into the mod and can be selected directly from the mod's
settings:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Settings" tab.
* Select the theme and save the settings.

## Manual installation

The theme styles can also be imported manually. To do that, follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Settings" tab and select "Textual mode".
* Copy the content below to the text box and click "Save settings".

### Redesigned Start menu

A variant for the [redesigned Windows 11 Start
menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/)
that is slowly rolling out in the 25H2 update.

<details>
<summary>Content to import (click to expand)</summary>

```yaml
disableNewStartMenuLayout: newLayoutSideBySide
controlStyles:
#Frame
  - target: Windows.UI.Xaml.Controls.Frame
    styles:
      - Margin=0,-64,0,0 
  - target: Grid#FrameRoot
    styles:
      - MaxHeight=692      
  - target: Grid#MainMenu
    styles:
      - MaxWidth=650
  - target: Grid#MainMenu > Grid#MainContent > Grid
    styles:
      - Canvas.ZIndex=1      
  - target: Border#AcrylicOverlay
    styles:
      - Margin=0,-70,0,0

#Collapsed Elements
  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton
    styles:
      - Visibility=Collapsed    
  - target: Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions
    styles:
      - Visibility=Collapsed
      #show more button
  - target: Grid#TopLevelHeader > Grid[2]
    styles:
      - Visibility=Collapsed      
  - target: TextBlock#AllListHeadingText
    styles:
      - Visibility=Collapsed 
  - target: StartMenu.SearchBoxToggleButton
    styles:
      - Visibility=Collapsed
  - target: //TextBlock#ZoomedOutHeading
    styles:
      - Visibility=Collapsed
  - target: Grid#ShowMorePinnedGrid > Button
    styles:
      - Visibility=Collapsed 

#User Tile
  - target: StartDocked.UserTileView
    styles:
    - Margin=-30,0,0,0
  - target: StartDocked.NavigationPaneButton#UserTileButton > Grid@CommonStates > Border
    styles:
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>      
      - BorderThickness=1
      - Background@Pressed:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.8"/>     

#NavPane
  - target: StartDocked.AppListView#NavigationPanePlacesListView
    styles:
      - FlowDirection=1
      - Margin=30,0,-30,0   
  - target: StartDocked.AppListViewItem 
    styles:
      - Margin=2,0,2,0       
  - target: StartDocked.AppListViewItem > Grid > Border#BackgroundBorder
    styles:
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
  - target: Grid#ContentBorder@CommonStates
    styles:
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0"/>
      - CornerRadius=5          
            
#Power Button
  - target: StartDocked.NavigationPaneButton#PowerButton
    styles:
      - Margin=30,0,-30,0
  - target: StartDocked.NavigationPaneButton#PowerButton > Grid@CommonStates
    styles:
      - BorderThickness=1
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.8"/>
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="#22FFFFFF" TargetTheme="1" Opacity="1"/>
      - CornerRadius=5
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.8"/>        

#Phone Flyout Toggle Button
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion
    styles:
      - Visibility=Visible
      - Margin=12,-8,-12,0
  - target: Button
    styles:
      - Style:=<ResourceKey="ButtonRevealStyle" />    

#Apps list/Pinned List
  - target: Grid#SideBySidePinnedWrapper > Windows.UI.Xaml.Controls.ScrollViewer
    styles:
      - RenderTransform:=<TranslateTransform X="-480" />
      - Margin=-92,0,-172,-15
  - target: Grid#SideBySidePinnedWrapper > Windows.UI.Xaml.Controls.ScrollViewer#SideBySidePinnedScrollViewer
    styles:
      - RenderTransform:=<TranslateTransform X="172"  />
      - Canvas.ZIndex=-1
  - target: Button#Header > Border#Border@CommonStates
    styles:
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.3"/>
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.3"/>
      - BorderThickness=1
  - target: Windows.UI.Xaml.Controls.Border#ContentBorder > Windows.UI.Xaml.Controls.Grid#DroppedFlickerWorkaroundWrapper > Border#HighContrastBorder
    styles:
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.3"/>
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.7"/>
      - BorderThickness=1

#Pinned List
  - target: GridView#PinnedList
    styles:
      - Width=300
      - RenderTransform:=<TranslateTransform Y="-272"  />       
  - target: GridView#PinnedList > Border > Windows.UI.Xaml.Controls.ScrollViewer
    styles:
      - Height=265   
  - target: Windows.UI.Xaml.Controls.GridView#PinnedList > Border > Windows.UI.Xaml.Controls.ScrollViewer > Border > Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem > Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper 
    styles:
      - Background:=<RevealBorderBrush Color="#646464" TargetTheme="1" Opacity=".1"/>
      - Margin=2
      - CornerRadius=5
  - target: TextBlock#PinnedListHeaderText
    styles:  
      - Margin=260,-4,-260,0    

#Recommended List
  - target: Grid#TopLevelSuggestionsRoot
    styles:
      - MinHeight=132
      - Margin=-65,31,-65,-31
      - Width=400
      - RenderTransform:=<TranslateTransform Y="-550"/>
         
  - target: Windows.UI.Xaml.Controls.GridView#RecommendedList > Windows.UI.Xaml.Controls.Border > Windows.UI.Xaml.Controls.ScrollViewer#ScrollViewer > Windows.UI.Xaml.Controls.Border#Root > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter#ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem
    styles:
      - MaxWidth=145
      - MinWidth=145
      - Margin=0    
  - target: Windows.UI.Xaml.Controls.TextBlock#NoSuggestionsWithoutSettingsLink
    styles:
      - Margin=11,0,48,0
  - target: Windows.UI.Xaml.Controls.GridView#RecommendedList > Border > Windows.UI.Xaml.Controls.ScrollViewer > Border > Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem > Border > Grid > Border
    styles:
      - Background:=<RevealBorderBrush Color="#646464" TargetTheme="1" Opacity=".1"/>
      - Margin=2
      

#Pinned/Recommended List Scroll Mode (allows scrolling, otherwise fixed height)  
  - target: ScrollViewer
    styles:
      - ScrollViewer.VerticalScrollMode=0 
  - target: GridView#AllAppsGrid > Border > Grid#SideBySidePinnedWrapper > ScrollViewer#ScrollViewer   
    styles:   
     -  ScrollViewer.VerticalScrollMode=2 
  - target: Windows.UI.Xaml.Controls.GridView > Border > ScrollViewer
    styles:
      - ScrollViewer.VerticalScrollMode=2

#Scrollbar    
  - target: Windows.UI.Xaml.Controls.Primitives.ScrollBar
    styles:
      - MaxHeight=575
      - Canvas.ZIndex=99
      - RenderTransform:=<TranslateTransform X="-20" Y="-5" />    

#View Mode Dropdown
  - target: Microsoft.UI.Xaml.Controls.DropDownButton
    styles:
      - Background:=<RevealBorderBrush Color="#646464" TargetTheme="1" Opacity=".1"/>
      - Style:=<StaticResource ResourceKey="ButtonRevealStyle"/>
      - Margin=-120,-7,120,7
      - Padding=4,2,4,2

#Zoomed Out View (Alphabet) 
  - target: ItemsWrapGrid > ListViewItem > Grid@CommonStates
    styles:
      - BorderThickness=1
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="#34FFFFFF" TargetTheme="1" Opacity="1"/>
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - CornerRadius=5
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0"/>

#Grouped Folder Modal
  - target: StartMenu.ExpandedFolderList > Grid > Grid
    styles:
      - Margin=0,0,80,0
  - target: StartMenu.ExpandedFolderList > Grid > Border
    styles:
      - Width=350
      - Margin=0,0,92,0
  - target: StartMenu.ExpandedFolderList > Grid > Grid > Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager
    styles:
      - Margin=-20,0,20,0

#Grid View
  - target: Grid#PageRoot@ViewStates > SemanticZoom#TopLevelRoot > Grid > ScrollViewer#ScrollViewer > ScrollContentPresenter#ScrollContentPresenter > Grid > ContentPresenter#ZoomedInPresenter > GridView#AllAppsGrid > Border > Grid#SideBySidePinnedWrapper > ScrollViewer#ScrollViewer > Border#Root > Grid > ScrollContentPresenter#ScrollContentPresenter > ItemsPresenter
    styles:      
      - Margin@Alpha_GridView=14,0,0,0

#Category View    
  - target: StartMenu.CategoryControl > Grid > Border
    styles:
      - Width=132
      - Height=132
      - CornerRadius=8
  - target: Button#LogoContainer > Grid@CommonStates > Border
    styles:
      - Width=58
      - Height=58
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0"/>
  - target: Button#FolderPlate > Grid@CommonStates > Border
    styles:
      - Width=58
      - Height=58
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0"/>
  - target: StartMenu.CategoryControl
    styles:
      - Margin=60,-8,-60,-16
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/> 
  - target: Button#SeeAllButton
    styles:
      - MaxWidth=132
      - Margin=0,-6,0,6      
  - target: Button#SeeAllButton > Grid@CommonStates
    styles:
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.4"/>
      - CornerRadius=5
      - BorderThickness=1    

#User Account Flyout
  - target: FlyoutPresenter
    styles:
      - RenderTransform:=<TranslateTransform X="20" Y="-24" />
```
</details>

### Classic Start menu

<details>
<summary>Content to import (click to expand)</summary>

```yaml
controlStyles:
  - target: Windows.UI.Xaml.Controls.Grid#UndockedRoot
    styles:
      - Visibility=Visible
      - MaxWidth=600
      - Margin=290,-10,0,0
  - target: Windows.UI.Xaml.Controls.Grid#AllAppsRoot
    styles:
      - Visibility=Visible
      - Width=360
      - RenderTransform:=<TranslateTransform X="-217"/>
  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton
    styles:
      - Visibility=Collapsed
  - target: StartDocked.StartSizingFrame
    styles:
      - MaxHeight=670
      - MaxWidth=1874
  - target: StartDocked.LauncherFrame > Grid#RootGrid > Grid#RootContent
    styles:
      - MinWidth=650
      - MaxWidth=650
  - target: StartDocked.LauncherFrame > Grid#RootPanel > Grid#RootGrid
    styles:
      - MinWidth=650
      - MaxWidth=650
  - target: StartDocked.LauncherFrame > Grid#RootPanel > Grid#RootGrid > Grid#RootContent
    styles:
      - MinWidth=650
      - MaxWidth=650
  - target: Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Button#ShowAllAppsButton
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.GridView#RecommendedList > Windows.UI.Xaml.Controls.Border > Windows.UI.Xaml.Controls.ScrollViewer#ScrollViewer > Windows.UI.Xaml.Controls.Border#Root > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter#ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem
    styles:
      - MaxWidth=145
      - MinWidth=145
      - Margin=0
  - target: StartDocked.AllAppsGridListView#AppsList
    styles:
      - Padding=90,3,6,16
  - target: Windows.UI.Xaml.Controls.Grid#AllAppsPaneHeader
    styles:
      - Margin=97,-10,0,0
  - target: Windows.UI.Xaml.Controls.Grid#SuggestionsParentContainer
    styles:
      - Height=168
  - target: StartDocked.NavigationPaneView#NavigationPane
    styles:
      - FlowDirection=0
      - Margin=30,0,30,0
  - target: StartDocked.PowerOptionsView#PowerButton
    styles:
      - FlowDirection=0
  - target: StartDocked.AppListView#NavigationPanePlacesListView
    styles:
      - FlowDirection=1
  - target: Windows.UI.Xaml.Controls.ListViewItem
    styles:
      - FlowDirection=0
  - target: Windows.UI.Xaml.Controls.ItemsStackPanel > Windows.UI.Xaml.Controls.ListViewItem
    styles:
      - FlowDirection=0
  - target: StartDocked.SearchBoxToggleButton#StartMenuSearchBox
    styles:
      - Margin=23,-101,23,14
  - target: Windows.UI.Xaml.Controls.TextBlock#NoSuggestionsWithoutSettingsLink
    styles:
      - Margin=11,0,48,0
  - target: StartDocked.LauncherFrame > Grid#RootGrid > Grid#RootContent > Grid#MainContent > Grid#InnerContent > Rectangle
    styles:
      - Margin=67,7,0,21
  - target: StartDocked.LauncherFrame > Grid#RootPanel > Grid#RootGrid > Grid#RootContent > Grid#MainContent > Grid#InnerContent > Rectangle
    styles:
      - Margin=67,7,0,21
  - target: Windows.UI.Xaml.Controls.SemanticZoom#ZoomControl
    styles:
      - IsZoomOutButtonEnabled=true
      - Margin=0
  - target: Windows.UI.Xaml.Controls.Button#ZoomOutButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.TextBlock
    styles:
      - Text=
  - target: Windows.UI.Xaml.Controls.Button#ZoomOutButton
    styles:
      - Width=28
      - Height=28
      - Margin=-1,-36,0,0
      - FontSize=14
      - CornerRadius=4
      - VerticalAlignment=0
      - Background=Transparent
      - BorderBrush=Transparent
  - target: Windows.UI.Xaml.Controls.ListView#ZoomAppsList
    styles:
      - Padding=86,0,27,0
  - target: StartDocked.SearchBoxToggleButton
    styles:
      - Height=0
      - Margin=0,-100,0,24
  - target: StartMenu.PinnedList
    styles:
      - MaxHeight=400
  - target: Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText
    styles:
      - Margin=-30,-2,0,0
  - target: Windows.UI.Xaml.Controls.Grid#SuggestionsParentContainer
    styles:
      - Margin=-20,0,0,0
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader
    styles:
      - Margin=35,0,0,0
  - target: Windows.UI.Xaml.Controls.Border#ContentBorder > Windows.UI.Xaml.Controls.Grid#DroppedFlickerWorkaroundWrapper > Border@CommonStates
    styles:
      - BorderBrush@Active:=<RevealBorderBrush Color="White" TargetTheme="1" Opacity="0.3"/>
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.3"/>
      - Margin=1
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.8"/>
  - target: Windows.UI.Xaml.Controls.Border#ContentBorder > Windows.UI.Xaml.Controls.Grid#DroppedFlickerWorkaroundWrapper > Border#BackgroundBorder
    styles:
      - Background:=<RevealBorderBrush Color="#646464" TargetTheme="1" Opacity=".1"/>
      - Margin=2
  - target: Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText
    styles:
      - Visibility=Visible
  - target: Rectangle[4]
    styles:
      - Margin=0,-20,0,0
  - target: GridView#RecommendedList
    styles:
      - Margin=-20,0,20,0
  - target: StartMenu.ExpandedFolderList > Grid > Grid
    styles:
      - Margin=0,0,80,0
  - target: StartMenu.ExpandedFolderList > Grid > Border
    styles:
      - Width=350
      - Margin=0,0,92,0
  - target: Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager
    styles:
      - Margin=-10,0,0,0
  - target: StartMenu.ExpandedFolderList > Grid > Grid > Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager
    styles:
      - Margin=-20,0,20,0
```
</details>
