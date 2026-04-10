# Command Center theme for Windows 11 Start Menu Styler

Command Center theme inspired by the command centers from various mobile operating systems. It features a completely transparent background to allow for a floating widget styled appearance.

**Author**: [PhantomNimbi](https://github.com/PhantomNimbi)

![Screenshot](preview.gif)

> [!IMPORTANT]
> This theme is designed for the [redesigned Windows 11 Start menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/) that is gradually rolling out with the 25H2 update. It is meant to use the categories view and is not built for any other view mode.

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

<details>
<summary>Content to import (click to expand)</summary>

```yaml
styleConstants:
  - CornerRadius=20
  - Background=<AcrylicBrush TintColor="{ThemeResource CardStrokeColorDefaultSolid}" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" TintOpacity="0" TintLuminosityOpacity=".5" Opacity="1"/>
  - BorderThickness=0.3,1,0.3,1
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
controlStyles:
  - target: Windows.UI.Xaml.Controls.Grid#RootPanel > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Grid#RootContent
    styles:
      - Margin=-20,-20,-20,0
  - target: StartDocked.StartSizingFrame
    styles:
      - Width=860
  - target: Windows.UI.Xaml.Controls.Border#RootGridDropShadow
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Border#RightCompanionDropShadow
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Border#StartDropShadow
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Border#DropShadowDismissTarget
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
      - Margin=2
      - Padding=0
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Grid#RootContent > Windows.UI.Xaml.Controls.Border#AcrylicBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
      - Margin=0,60,0,10
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Border#AcrylicOverlay
    styles:
      - Visibility=1
  - target: StartDocked.SearchBoxToggleButton#StartMenuSearchBox
    styles:
      - Width=650
      - Height=50
      - Margin=0,-15,0,0
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsRoot
    styles:
      - Visibility=1
  - target: StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Border#BorderElement
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.TextBlock#PlaceholderText
    styles:
      - Text=Search This PC
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelRoot > Windows.UI.Xaml.Controls.Grid
    styles:
      - Visibility=1
  - target: StartDocked.NavigationPaneView#NavigationPane
    styles:
      - Width=550
      - RenderTransform:=<TranslateTransform X="0" Y="10" />
  - target: Windows.UI.Xaml.Controls.Button#ShowAllAppsButton
    styles:
      - Visibility=1
  - target: StartMenu.PinnedList#StartMenuPinnedList
    styles:
      - Margin=0
      - Height=280
  - target: StartMenu.PinnedList#StartMenuPinnedList > Windows.UI.Xaml.Controls.Grid#Root
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Grid#UndockedRoot
    styles:
      - Visibility=0
      - Width=650
      - Margin=0,-130,0,230
      - Canvas.ZIndex=1
      - MaxHeight:=340
  - target: Windows.UI.Xaml.Controls.Grid#AllAppsRoot
    styles:
      - Visibility=0
      - Margin=-1600,190,115,-100
      - MaxHeight=330
      - Background:=$Background
      - CornerRadius=$CornerRadius
      - Width=650
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Grid > AllListHeading
    styles:
      - Visibility=1
  - target: StartDocked.AllAppsPane#AllAppsPanel
    styles:
      - Margin=-20,-20,20,20
  - target: StartDocked.StartMenuCompanion#RightCompanion > Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius:=$CornerRadius
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Grid#MainContent > Windows.UI.Xaml.Controls.Grid#ActionsBar > Windows.UI.Xaml.Controls.Button#PrimaryActionBarButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
      - Height=40
  - target: Windows.UI.Xaml.Controls.Grid#ActionsBar > Windows.UI.Xaml.Controls.Button#ActionBarOverflowButton
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
      - Height=40
  - target: StartDocked.StartMenuCompanion#RightCompanion > Windows.UI.Xaml.Controls.Grid#CompanionRoot
    styles:
      - Height=730
      - Margin=0,-10,0,-10
      - Padding=10,0,-2,0
  - target: Windows.UI.Xaml.Controls.Border#OverflowFlyoutBackgroundBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Windows.UI.Xaml.Controls.MenuFlyoutPresenter > Windows.UI.Xaml.Controls.Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Grid#HoverFlyoutGrid > Windows.UI.Xaml.Controls.Border#HoverFlyoutBackground
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Cortana.UI.Views.TaskbarSearchPage > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Grid#OuterBorderGrid
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Border#LayerBorder
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Border#AccentLayerBorder
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Border#DropShadow
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Border#AppBorder
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.ToolTip > Windows.UI.Xaml.Controls.ContentPresenter#LayoutRoot
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=15
  - target: Microsoft.UI.Xaml.Controls.PipsPager#PipsPager
    styles:
      - Margin=-30,-10,0,10
  - target: StartMenu.FolderModal#StartFolderModal > Windows.UI.Xaml.Controls.Grid#Root
    styles:
      - MaxHeight:=420
      - MaxWidth:=420
      - Height=Auto
      - Width=Auto
  - target: StartMenu.FolderModal#StartFolderModal > Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.ContentControl#ContentControl > Windows.UI.Xaml.Controls.ContentPresenter > StartMenu.UniversalTileContainer#UniversalTileContainer > Windows.UI.Xaml.Controls.Grid#GridViewContainer
    styles:
      - Width=360
      - Height=400
  - target: Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: StartMenu.ExpandedFolderList
    styles:
      - Margin=0,30,0,-120
  - target: Windows.UI.Xaml.Controls.Grid#MainMenu > Windows.UI.Xaml.Controls.Border#AcrylicBorder
    styles:
      - Visibility=1
  - target: StartMenu.SearchBoxToggleButton#SearchBoxToggleButton
    styles:
      - Height=50
      - Margin=-20,20,-20,-20
      - Width=340
  - target: StartMenu.SearchBoxToggleButton#SearchBoxToggleButton > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Border#BorderElement
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion
    styles:
      - Margin=-68,40,0,0
  - target: Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Grid#AllListHeading
    styles:
      - Visibility=1
  - target: StartMenu.CategoryControl > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Grid#MainMenu
    styles:
      - Width=460
  - target: StartMenu.PinnedList#StartMenuPinnedList
    styles:
      - Width=340
      - MaxHeight=450
      - Margin=0,0,0,30
  - target: Windows.UI.Xaml.Controls.GridView#PinnedList > Border > Windows.UI.Xaml.Controls.ScrollViewer
    styles:
      - ScrollViewer.VerticalScrollMode=2
      - MaxHeight:=336
      - MinHeight:=100
      - Width=300
      - Margin=0,0,60,0
  - target: StartMenu.StartMenuCompanion#RightCompanion
    styles:
      - Height=810
      - Margin=15,0,30,0
  - target: Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Windows.UI.Xaml.Controls.GridView#AllAppsGrid > Windows.UI.Xaml.Controls.ItemsWrapGrid
    styles:
      - Visibility=0
  - target: Windows.UI.Xaml.Controls.GridView#AllAppsGrid
    styles:
      - Margin=0,15,0,0
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelHeader > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Button
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.FlyoutPresenter
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness:=$BorderThickness
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.MenuFlyoutPresenter
    styles:
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Grid#AllListHeading > Microsoft.UI.Xaml.Controls.DropDownButton#ViewSelectionButton > Grid#RootGrid
    styles:
      - CornerRadius=$CornerRadius
      - Margin=-12,0,12,0
  - target: MenuFlyoutItem
    styles:
      - CornerRadius:=$CornerRadius
      - Margin=4,0,4,0
  - target: ToggleMenuFlyoutItem
    styles:
      - CornerRadius:=$CornerRadius
      - Margin=4,0,4,0
  - target: Windows.UI.Xaml.Controls.Primitives.ScrollBar
    styles:
      - Visibility=1
  - target: StartDocked.UserTileView > StartDocked.NavigationPaneButton > Grid@CommonStates > Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: StartDocked.PowerOptionsView > StartDocked.NavigationPaneButton > Grid@CommonStates > Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Border@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Image
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
  - target: Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Grid
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
  - target: Grid#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Grid
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
  - target: ScrollViewer#MenuFlyoutPresenterScrollViewer > Border > Grid > ScrollContentPresenter > ItemsPresenter > StackPanel
    styles:
      - ChildrenTransitions:=<TransitionCollection><EntranceThemeTransition IsStaggeringEnabled="False" FromHorizontalOffset="-25" FromVerticalOffset="0" /></TransitionCollection>
  - target: Border@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Image
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
  - target: Grid#ContentBorder@CommonStates > ContentPresenter > Grid > Grid#LogoContainer > Grid
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
  - target: Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter#ContentPresenter > ContentControl > Grid#RootGrid > Border#LogoBackgroundPlate > Image#AllAppsItemLogo
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
  - target: Border#BackgroundBorder
    styles:
      - BackgroundTransition:=<BrushTransition Duration="0:0:0.083" />
  - target: Grid#LayoutRoot
    styles:
      - BackgroundTransition:=<BrushTransition Duration="0:0:0.083" />
  - target: StartMenu.CategoryControl > Grid > Border
    styles:
      - BackgroundSizing=InnerBorderEdge
  - target: Windows.UI.Xaml.Controls.Grid > LogosContainer > Windows.UI.Xaml.Controls.ItemsControl > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: StartDocked.AppListView#NavigationPanePlacesListView > Windows.UI.Xaml.Controls.Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Button#ZoomOutButton
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Button#ZoomInButton
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Button#SeeAllButton > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Border#BackgroundBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=12
      - Margin=18,4
webContentStyles:
  - target: '*'
    styles:
      - 'transition: background-color 0.083s ease-in-out !important'
```
</details>
