# Command Center theme for Windows 11 Start Menu Styler

Command Center theme inspired by the command centers from various mobile operating systems. It features a completely transparent background to allow for a floating widget styled appearance.

**Author**: [PhantomNimbi](https://github.com/PhantomNimbi)

<img width="100%" src="preview.png" alt="Preview" />

> [!IMPORTANT]
> This theme is designed for the [redesigned Windows 11 Start menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/) that is gradually rolling out with the 25H2 update. It is meant to use the categories view and is not built for any other view mode.

## Notes
- This theme consists of the following backgrounds:
  - Translucent
  - Glass
  - Frosted
  - Acrylic

  In order to switch between these backgrounds, set the value `Background=$Translucent`, `Background=$Glass`, `Background=$Frosted` or `Background=$Acrylic` in the "Style constants" section of the mod's settings.

- This theme can style your lock screen as well. 

## Lock Screen

<img width="100%" src="lock-screen.jpg" alt="Lock Screen" />

To make it work, you'll need to:
- Add 'LockApp.exe' to the 'Custom process inclusion list' under 'Advanced settings' in the Windows 11 Start Menu Styler mod.
- Install the [Vivo Sans En VF](https://1drv.ms/u/c/67fedd4420ed716d/EXRoW1f5dABJrO2dPj0tbM0Bm1uYiGeoKyAYA7X7er2Zww?e=cLsiJJ) and [Morganite SemiBold](https://1drv.ms/u/c/67fedd4420ed716d/IQCHLlxP7GPITp4p-uPMw9O5AY3s2NJCHLKC-tYZZVWAGiY?e=yQrKQb) fonts.

Credits for this feature go to [Nathaniel4JC](https://github.com/Nathaniel4JC). It was something introduced in their [WindowsGlass](https://github.com/PhantomNimbi/windows-11-start-menu-styling-guide/tree/patch-1/Themes/WindowGlass) theme and I figured would go nice with this one as well.

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
  - Translucent=<WindhawkBlur BlurAmount="15" TintColor="#10808080"/>
  - Glass=<WindhawkBlur BlurAmount="5" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Acrylic=<WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8" />
  - Background=$Frosted
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - BorderBrush2=<WindhawkBlur BlurAmount="10" TintColor="#909090" TintOpacity="0.3"/>
  - ClockBG=<SolidColorBrush Color="{ThemeResource SystemAccentColor}" Opacity="1"/>
  - BorderThickness=0.3,1,0.3,1
  - CornerRadius=35
  - SearchBoxRadius=25
  - ElementCornerRadius=10
  - FlyoutCornerRadius=6
  - HoverCornerRadius=15
controlStyles:
  - target: StackPanel#TimeAndDatePanel
    styles:
      - VerticalAlignment=Top
      - HorizontalAlignment=Center
      - RenderTransform:=<TranslateTransform X="0" />
  - target: StackPanel#TimePanel > TextBlock#Time
    styles:
      - HorizontalAlignment:=Center
      - RenderTransform:=<TransformGroup><TranslateTransform X="-50" Y="20" /><ScaleTransform ScaleX="2.3" ScaleY="4" /></TransformGroup>
      - FontFamily=Morganite SemiBold
      - Foreground:=$ClockBG
  - target: StackPanel#TimeAndDatePanel > TextBlock#Date
    styles:
      - HorizontalAlignment=Center
      - RenderTransform:=<TranslateTransform X="0" Y="-110" />
      - FontFamily=vivo Sans EN VF
      - Foreground:=$ClockBG
  - target: Grid#WidgetFrameGrid
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Grid#WidgetCanvasPanel
    styles:
      - HorizontalAlignment=Center
      - RenderTransform:=<TranslateTransform X="0" Y="50" />
  - target: Grid#MediaTransportControls
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Grid#MediaControlsContainer
    styles:
      - Visibility=0
      - RenderTransform:=<TranslateTransform X="0" Y="-250" />
      - Margin=0,0,0,0
      - CornerRadius=$CornerRadius
  - target: FlyoutPresenter > Border#BackgroundElement
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness:=$BorderThickness
      - CornerRadius=$FlyoutCornerRadius
      - Padding=-1
  - target: MenuFlyoutPresenter > Border#BackgroundElement
    styles:
      - CornerRadius=$FlyoutCornerRadius
  - target: Grid#AllListHeading > Microsoft.UI.Xaml.Controls.DropDownButton#ViewSelectionButton > Grid#RootGrid
    styles:
      - CornerRadius=$ElementCornerRadius
      - Margin=-12,0,12,0
  - target: MenuFlyoutItem
    styles:
      - CornerRadius=$FlyoutCornerRadius
      - Margin=4,0,4,0
  - target: ToggleMenuFlyoutItem
    styles:
      - CornerRadius=$FlyoutCornerRadius
      - Margin=4,0,4,0
  - target: Border#OverflowFlyoutBackgroundBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$FlyoutCornerRadius
  - target: MenuFlyoutPresenter > Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$FlyoutCornerRadius
  - target: Grid#HoverFlyoutGrid > Border#HoverFlyoutBackground
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$FlyoutCornerRadius
  - target: StartMenu.FolderModal#StartFolderModal > Grid#Root
    styles:
      - MaxHeight:=420
      - MaxWidth:=420
      - Height=Auto
      - Width=Auto
  - target: StartMenu.FolderModal#StartFolderModal > Grid#Root > ContentControl#ContentControl > ContentPresenter > StartMenu.UniversalTileContainer#UniversalTileContainer > Grid#GridViewContainer
    styles:
      - Width=360
      - Height=400
  - target: Grid#Root > Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: StartMenu.ExpandedFolderList
    styles:
      - Margin=0,30,0,-120
  - target: ListViewItem > Grid@CommonStates > Border#BorderBackground
    styles:
      - BorderThickness=$BorderThickness
      - BorderBrush@PointerOver:=$BorderBrush
      - BorderBrush@Pressed:=$BorderBrush
      - CornerRadius=$ElementCornerRadius
      - BackgroundSizing=InnerBorderEdge
  - target: Border#ContentBorder@CommonStates > Grid > Border#BackgroundBorder
    styles:
      - BorderThickness=$BorderThickness
      - BorderBrush@PointerOver:=$BorderBrush
      - BorderBrush@Pressed:=$BorderBrush
      - CornerRadius=$ElementCornerRadius
      - BackgroundSizing=InnerBorderEdge
  - target: Button > Grid@CommonStates > Border#BackgroundBorder
    styles:
      - BorderThickness=$BorderThickness
      - BorderBrush@PointerOver:=$BorderBrush
      - BorderBrush@Pressed:=$BorderBrush
      - CornerRadius=$ElementCornerRadius
      - BackgroundSizing=InnerBorderEdge
  - target: Cortana.UI.Views.TaskbarSearchPage > Grid#RootGrid > Grid#OuterBorderGrid
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Border#LayerBorder
    styles:
      - Visibility=1
  - target: Border#AccentLayerBorder
    styles:
      - Visibility=1
  - target: Border#dropshadow
    styles:
      - Visibility=1
  - target: Border#AppBorder
    styles:
      - Visibility=1
  - target: ToolTip > ContentPresenter#LayoutRoot
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$ElementCornerRadius
  - target: Border#AccentAppBorder
    styles:
      - Visibility=1
  - target: Border#LayerBorder
    styles:
      - Visibility=1
  - target: Border#AppBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Grid#MainMenu > Border#AcrylicBorder
    styles:
      - Visibility=1
  - target: Border#AcrylicOverlay
    styles:
      - Visibility=1
  - target: StartDocked.StartSizingFrame
    styles:
      - Width=750
  - target: Border#RootGridDropShadow
    styles:
      - Visibility=1
  - target: Border#StartDropShadow
    styles:
      - Visibility=1
  - target: Border#DropShadowDismissTarget
    styles:
      - Visibility=1
  - target: Grid#UndockedRoot
    styles:
      - Visibility=0
      - Width=650
      - Canvas.ZIndex=1
      - MaxHeight:=340
  - target: StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Grid > ContentPresenter#ContentPresenter > TextBlock#PlaceholderText
    styles:
      - Text=Search This Precision
  - target: Grid#AllListHeading > TextBlock#AllListHeadingText
    styles:
      - Visibility=1
  - target: Grid#TopLevelRoot > Grid
    styles:
      - Visibility=1
  - target: StartDocked.NavigationPaneView#NavigationPane
    styles:
      - Width=550
      - RenderTransform:=<TranslateTransform X="0" Y="10" />
  - target: Button#ShowAllAppsButton
    styles:
      - Visibility=1
  - target: Grid#TopLevelSuggestionsRoot
    styles:
      - Visibility=1
  - target: StartMenu.PinnedList#StartMenuPinnedList > Grid#Root
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$ElementCornerRadius
  - target: StartMenu.SearchBoxToggleButton#SearchBoxToggleButton
    styles:
      - Height=50
      - Width=350
  - target: StartMenu.SearchBoxToggleButton#SearchBoxToggleButton > Grid > Border#BorderElement
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$SearchBoxRadius
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion
    styles:
      - Margin=-70,0,0,0
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Border
    styles:
      - Background:=Transparent
      - BorderBrush:=Transparent
      - BorderThickness=0
  - target: TextBlock#PinnedListHeaderText
    styles:
      - Visibility=1
  - target: Grid#AllListHeading
    styles:
      - Visibility=1
  - target: Grid#AllListHeading > TextBlock#AllListHeadingText
    styles:
      - Visibility=1
  - target: StartMenu.CategoryControl > Grid#RootGrid > Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$ElementCornerRadius
  - target: Windows.UI.Xaml.Controls.Primitives.ScrollBar
    styles:
      - Visibility=1
  - target: StartDocked.UserTileView > StartDocked.NavigationPaneButton > Grid@CommonStates > Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$ElementCornerRadius
      - Width=38
      - Height=38
  - target: Grid#UserTileIcon
    styles:
      - Width=26
      - Height=26
      - Margin=12,0,0,0
  - target: TextBlock#UserTileNameText
    styles:
      - Text=
  - target: StartDocked.PowerOptionsView > StartDocked.NavigationPaneButton > Grid@CommonStates > Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
      - Width=38
      - Height=38
  - target: Grid > LogosContainer > ItemsControl > ItemsPresenter > ItemsWrapGrid
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
      - Width=38
      - Height=38
  - target: StartDocked.AppListView#NavigationPanePlacesListView > Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$ElementCornerRadius
      - Height=38
  - target: StartDocked.NavigationPaneView#UserControl > Grid#RootPanel > StartDocked.AppListView#NavigationPanePlacesListView > Border > ScrollViewer#ScrollViewer > Border#Root > Grid > ScrollContentPresenter#ScrollContentPresenter > ItemsPresenter
    styles:
      - Padding=2,-1
  - target: GridView#AllAppsGrid > ItemsWrapGrid
    styles:
      - Visibility=0
  - target: Grid#TopLevelHeader > Grid > Button
    styles:
      - Visibility=1
  - target: Button#SeeAllButton > Grid > Border#BackgroundBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$ElementCornerRadius
      - Margin=18,4
  - target: Grid#MainMenu
    styles:
      - Width=470
      - Height=740
  - target: StartMenu.PinnedList#StartMenuPinnedList
    styles:
      - Width=360
      - MaxHeight=400
      - MinHeight=200
      - Height=Auto
  - target: GridView#PinnedList > Border > ScrollViewer
    styles:
      - ScrollViewer.VerticalScrollMode=2
      - MaxHeight:=336
      - MinHeight:=100
      - Width=300
      - Padding=0,15
      - Margin=-25,0,25,0
  - target: TextBlock#PinnedListHeaderText
    styles:
      - Visibility=1
  - target: StartMenu.StartMenuCompanion#RightCompanion
    styles:
      - Height=700
  - target: Grid#CompanionRoot > Border#AcrylicBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: StartDocked.StartMenuCompanion#RightCompanion > Grid#CompanionRoot > Border#AcrylicBorder
    styles:
      - Visibility=1
  - target: Border#RightCompanionDropShadow
    styles:
      - Visibility=1
  - target: StartDocked.StartMenuCompanion#RightCompanion > Grid#CompanionRoot
    styles:
      - Height=700
      - Padding=10,0,-2,0
  - target: Windows.UI.Xaml.Controls.Grid#ActionsBar > Windows.UI.Xaml.Controls.Button#ActionBarOverflowButton
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$ElementCornerRadius
      - Height=40
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
  - target: Button#ZoomOutButton
    styles:
      - Visibility=1
  - target: Button#ZoomInButton
    styles:
      - Visibility=1
  - target: Cortana.UI.Views.CortanaRichSearchBox#SearchTextBox > Grid > Border#BorderElement
    styles:
      - Background=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=6
  - target: Border#TaskbarSearchBackground
    styles:
      - CornerRadius=6
      - Background:=Transparent
      - BorderBrush:=Transparent
      - BorderThickness=0
  - target: Grid#SearchBoxOnTaskbarGleamContainer > Grid#SearchBoxOnTaskbarGleamImageContainer
    styles:
      - Visibility=1
webContentStyles:
  - target: '*'
    styles:
      - 'transition: background-color 0.083s ease-in-out !important'

```
</details>