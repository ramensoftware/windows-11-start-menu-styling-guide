# ModernStartMenu theme for Windows 11 Start Menu Styler (Windows 10 Start menu)

ModernStartMenu is a Fluent start menu theme designed for Windows 10 Start menu on Windows 11.

**Author**: [ndrew6075](https://github.com/ndrew6075)

![Screenshot](screenshot.png)
![Screenshot](screenshot-tiles.png)

## Enabling Windows 10 Start menu on Windows 11

If you're already using the Windows 10 Start menu, you can skip this step.

* Install [ExplorerPatcher](https://github.com/valinet/ExplorerPatcher).
* Once installed, open **Properties (ExplorerPatcher)** via the Start menu or right-click the taskbar > **Properties**.
* Go to **Start menu** > **Start menu style** > **Windows 10** > **Restart File Explorer**.

![Screenshot](open_ep.png)
![Screenshot](ep_configure.png)

> [!IMPORTANT]
> Set **Corner preference** to **Not rounded**, as ModernStartMenu rounds the Start menu instead of ExplorerPatcher.

## Bugs
* Legacy Windows 10 effects (Reveal, and 3D push) are still present.
* Items may not align/center correctly on higher DPIs.
* Tiles have a broken background when dragged from applist.
* Right-click menus in textbox are not styled correctly.

## Unsupported configurations/settings
* Windows 10 version **1607** and lower ([Segoe Fluent Icons](https://aka.ms/SegoeFluentIcons) required).
* *"Show accent color on Start and taskbar"* enabled.
* Fullscreen Start menu (ExplorerPatcher).

## Manual installation

The theme styles have to be imported manually. To do that, follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Settings" tab and select "Textual mode".
* Copy the content below to the text box and click "Save settings".

<details>
<summary>Content to import (click to expand)</summary>

```yaml
theme: ''
disableNewStartMenuLayout: '1'
styleConstants:
  - background=<AcrylicBrush TintColor="{ThemeResource AcrylicBG}" TintOpacity="0.25" TintLuminosityOpacity="1" FallbackColor="{ThemeResource AcrylicBG}" />
  - borderBrush=<SolidColorBrush Color="{ThemeResource Border}" />
  - accentButtonNormal=<SolidColorBrush Color="{ThemeResource AccentColor}" />
  - accentButtonPointerOver=<SolidColorBrush Color="{ThemeResource AccentColor}" Opacity="0.9" />
  - accentButtonPressed=<SolidColorBrush Color="{ThemeResource AccentColor}" Opacity="0.8" />
  - accentbuttonBorderBrush=<SolidColorBrush Color="{ThemeResource AccentButtonBorder}" />
  - buttonNormal=<SolidColorBrush Color="{ThemeResource ButtonFillNormal}" />
  - buttonPointerOver=<SolidColorBrush Color="{ThemeResource ButtonFillPointerOver}" />
  - buttonPressed=<SolidColorBrush Color="{ThemeResource ButtonFillPressed}" />
  - buttonBorderBrush=<LinearGradientBrush StartPoint="0.5,0.9" EndPoint="0.5,1"><GradientStop Color="{ThemeResource ButtonBorderBrushTopGradient}" Offset="0.0" /><GradientStop Color="{ThemeResource ButtonBorderBrushBottomGradient}" Offset="1" /></LinearGradientBrush>
  - menuPointerOver=<SolidColorBrush Color="{ThemeResource MenuFillPointerOver}" />
  - menuPressed=<SolidColorBrush Color="{ThemeResource MenuFillPressed}" />
  - listPointerOver=<SolidColorBrush Color="{ThemeResource ListFillPointerOver}" />
  - listPressed=<SolidColorBrush Color="{ThemeResource ListFillPressed}" />
  - tilesNormal=<SolidColorBrush Color="{ThemeResource TilesFillNormal}" />
  - tilesPointerOver=<SolidColorBrush Color="{ThemeResource TilesFillPointerOver}" />
  - tilesPressed=<SolidColorBrush Color="{ThemeResource TilesFillPressed}" />
  - tilesBorderBrushNormal=<LinearGradientBrush StartPoint="0.5,0" EndPoint="0.5,1"><GradientStop Color="{ThemeResource TilesBorderBrushTopGradientNormal}" Offset="0.0" /><GradientStop Color="{ThemeResource TilesBorderBrushBottomGradientNormal}" Offset="1" /></LinearGradientBrush>
  - tilesBorderBrushPointerOver=<LinearGradientBrush StartPoint="0.5,0" EndPoint="0.5,1"><GradientStop Color="{ThemeResource TilesBorderBrushTopGradientPointerOver}" Offset="0.0" /><GradientStop Color="{ThemeResource TilesBorderBrushBottomGradientPointerOver}" Offset="1" /></LinearGradientBrush>
  - tilesBorderBrushPressed=<LinearGradientBrush StartPoint="0.5,0" EndPoint="0.5,1"><GradientStop Color="{ThemeResource TilesBorderBrushTopGradientPressed}" Offset="0.0" /><GradientStop Color="{ThemeResource TilesBorderBrushBottomGradientPressed}" Offset="1" /></LinearGradientBrush>
  - textboxBorder=<SolidColorBrush Color="{ThemeResource TextBoxBorderBrush}" />
  - fontFamily=Segoe UI Variable
controlStyles:
  - target: Border#AcrylicBorder
    styles:
      - Background:=$background
      - BorderBrush:=$borderBrush
      - BorderThickness=1
      - CornerRadius=8
  - target: Border#NameTextBlockHost > TextBlock
    styles:
      - FontWeight=SemiBold
      - FontSize=14
      - FontFamily=$fontFamily
      - Margin=3,0,0,-6
  - target: Grid#RootGrid@ContentPaneStates > SplitView > Grid > Grid > Border > Grid > StartUI.AllAppsPane
    styles:
      - Margin@Apps=12,24,27,0
      - Margin@Classic=12,24,0,0
      - FontWeight=Semibold
  - target: Button#Header > Border > TextBlock
    styles:
      - FontSize=14
      - FontWeight=SemiBold
      - Margin=0,0,-16,2
      - FontFamily=$fontFamily
  - target: Border#GridPane
    styles:
      - Margin=8,24,0,0
  - target: TextBlock#AppDisplayName
    styles:
      - FontSize=12
      - Margin=20,0,0,0
      - FontFamily=$fontFamily
  - target: TextBlock#DisplayName
    styles:
      - FontSize=12
      - Margin=0,0,0,5
      - FontFamily=$fontFamily
  - target: Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter#Root@CommonStates
    styles:
      - RevealBackground@PointerOver:=$listPointerOver
      - RevealBackground@Pressed:=$listPressed
      - CornerRadius=9
      - PointerOverBackground:=
      - PressedBackground:=
      - SelectedBackground:=
      - RevealBorderBrush:=
      - RevealBackground@Normal:=
  - target: StartUI.NavigationPaneGrid
    styles:
      - CornerRadius=8,0,0,8
      - Background:=<SolidColorBrush Color="{ThemeResource NavPane}" />
      - BorderThickness=1,1,0,1
  - target: Grid#VerticalRoot
    styles:
      - CornerRadius=6
  - target: Windows.UI.Xaml.Controls.Primitives.RepeatButton#VerticalSmallDecrease > Grid@CommonStates > FontIcon > Grid > TextBlock
    styles:
      - Text=
      - Foreground@Normal:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" Opacity="0.5" />
      - Foreground@PointerOver:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" Opacity="0.75" />
      - Foreground@Pressed:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" Opacity="0.75" />
      - FontSize@Pressed=6
  - target: Windows.UI.Xaml.Controls.Primitives.RepeatButton#VerticalSmallIncrease > Grid@CommonStates > FontIcon > Grid > TextBlock
    styles:
      - Text=
      - Foreground@Normal:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" Opacity="0.5" />
      - Foreground@PointerOver:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" Opacity="0.75" />
      - Foreground@Pressed:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" Opacity="0.75" />
      - FontSize@Pressed=6
  - target: StartUI.GroupHeaderControl
    styles:
      - CornerRadius=6
  - target: Rectangle#ThumbVisual
    styles:
      - Width=6
      - Fill:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" Opacity="0.5" />
      - RadiusX=4
      - RadiusY=4
  - target: MenuFlyoutItem > Grid > TextBlock
    styles:
      - FontSize=14
      - FontFamily=$fontFamily
  - target: Grid#GridForContextMenuInvoke_MustHave_No_Columns_Or_Rows > Grid > TextBlock
    styles:
      - FontSize=14
      - FontFamily=$fontFamily
  - target: StartUI.TileFolderNameTextBox
    styles:
      - FontSize=14
      - FontWeight=SemiBold
      - FontFamily=$fontFamily
  - target: ToggleMenuFlyoutItem > Grid > Grid > FontIcon
    styles:
      - Glyph:=&#xE73E;
  - target: Border#UninstallFlyoutPresenterBorder
    styles:
      - MinWidth=376
      - MinHeight=149
      - Background:=$background
      - BorderBrush:=$borderBrush
      - CornerRadius=8
  - target: StartUI.UninstallFlyoutControl > StackPanel > TextBlock
    styles:
      - FontSize=14
      - FontFamily=$fontFamily
      - Text=This app and its related information will be removed.
      - Margin=9,8,0,0
  - target: Button#UninstallButton > Grid@CommonStates > ContentPresenter
    styles:
      - Background@Normal:=$accentButtonNormal
      - Background@PointerOver:=$accentButtonPointerOver
      - Background@Pressed:=$accentButtonPressed
      - BorderThickness=0,0,0,1
      - BorderBrush:=$accentbuttonBorderBrush
  - target: Button#UninstallButton > Grid@CommonStates > ContentPresenter > TextBlock
    styles:
      - FontFamily=$fontFamily
      - FontWeight=Normal
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemAltHighColor}" />
      - Opacity@Pressed=0.8
  - target: TextBlock#StatusMessage
    styles:
      - Margin=20,0,0,0
      - FontFamily=$fontFamily
  - target: Rectangle#SelectionRectangle
    styles:
      - RadiusX=2
      - RadiusY=2
      - Height=32
  - target: Border#Border@CommonStates
    styles:
      - Background@PointerOver:=$listPointerOver
      - Background@Pressed:=$listPressed
      - CornerRadius=6
      - BorderBrush=Transparent
  - target: StartUI.NavigationPaneButton#PowerButton > ContentPresenter@CommonStates
    styles:
      - Background@PointerOver:=$listPointerOver
      - Background@Pressed:=$listPressed
      - BorderBrush=Transparent
      - CornerRadius=6
      - Margin=-1,0,-1,0
  - target: StartUI.NavigationPaneButton#UserTileButton > ContentPresenter@CommonStates
    styles:
      - Background@PointerOver:=$listPointerOver
      - Background@Pressed:=$listPressed
      - BorderBrush=Transparent
      - CornerRadius=6
      - Margin=-1,0,-1,0
  - target: Grid#RootPanel@CommonStates > ContentPresenter
    styles:
      - BorderBrush=Transparent
      - Background@PointerOver:=$listPointerOver
      - Background@Pressed:=$listPressed
      - Background@PressedSelected:=$listPressed
      - Background@PointerOverSelected:=$listPointerOver
      - CornerRadius=6
      - BorderThickness=0
  - target: StartUI.AllAppsGridListViewItem
    styles:
      - CornerRadius=6
  - target: Button#Header
    styles:
      - CornerRadius=6
  - target: Grid#RootPanel
    styles:
      - CornerRadius=6
  - target: Button#PinButton > Grid@CommonStates
    styles:
      - Background@PointerOver:=$menuPointerOver
      - Background@Pressed:=$menuPressed
      - CornerRadius=0,4,4,0
  - target: MenuFlyoutPresenter
    styles:
      - MinWidth=165
      - CornerRadius=8
      - Background:=$background
  - target: JumpViewUI.ItemNotFoundFlyoutControl > StackPanel > TextBlock
    styles:
      - FontFamily=$fontFamily
      - FontSize=15
  - target: StackPanel > Button#DeleteButton > Grid@CommonStates
    styles:
      - Background@Normal:=$buttonNormal
      - Background@PointerOver:=$buttonPointerOver
      - Background@Pressed:=$buttonPressed
      - BorderThickness=1
      - BorderBrush:=$buttonBorderBrush
  - target: StackPanel > Button#DeleteButton > Grid@CommonStates > ContentPresenter > TextBlock
    styles:
      - FontFamily=$fontFamily
      - FontSize=14
      - Opacity@Pressed=0.8
      - Margin=0,-1,0,0
  - target: Button#CancelButton > Grid@CommonStates > ContentPresenter
    styles:
      - Background@Normal:=$accentButtonNormal
      - Background@PointerOver:=$accentButtonPointerOver
      - Background@Pressed:=$accentButtonPressed
      - BorderThickness=0,0,0,1
      - BorderBrush:=$accentbuttonBorderBrush
  - target: Button#CancelButton > Grid@CommonStates > ContentPresenter > TextBlock
    styles:
      - FontFamily=$fontFamily
      - FontSize=14
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemAltHighColor}" />
      - Opacity@Pressed=0.8
  - target: MenuFlyoutItem > Grid#LayoutRoot > Grid#InnerRoot > Ellipse
    styles:
      - Width=32
      - Height=32
      - Margin=1,0,0,2
  - target: MenuFlyoutItem > Grid#LayoutRoot > Grid#InnerRoot > StackPanel > TextBlock#TextBlock
    styles:
      - FontSize=14
      - Margin=8,0,0,1
      - FontFamily=$fontFamily
  - target: MenuFlyoutItem
    styles:
      - CornerRadius=4
      - Margin=3,-1,3,0
  - target: MenuFlyoutSubItem
    styles:
      - CornerRadius=4
      - FontSize=14
      - Margin=3,0,3,0
      - FontFamily=$fontFamily
      - MinHeight=30
  - target: ToggleMenuFlyoutItem
    styles:
      - CornerRadius=4
      - FontSize=14
      - Margin=3,0,3,0
      - FontFamily=$fontFamily
      - MinHeight=30
  - target: StackPanel > Button#DeleteButton
    styles:
      - CornerRadius=4
      - MinWidth=150
      - Height=32
  - target: Button#CancelButton
    styles:
      - CornerRadius=4
      - MinWidth=150
      - Height=32
  - target: StartUI.NavigationPaneBadgeView > Grid
    styles:
      - Margin=-16,-23,0,7
  - target: StartUI.NavigationPaneBadgeView > Grid > Windows.UI.Xaml.Shapes.Rectangle
    styles:
      - Fill:=$accentButtonNormal
      - Stroke:=$accentButtonNormal
  - target: StartUI.NavigationPaneBadgeView#Badge > Grid > TextBlock
    styles:
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemAltHighColor}" />
      - FontFamily=$fontFamily
  - target: ItemsStackPanel > StartUI.ViewSelectionListViewItem > Grid@CommonStates
    styles:
      - Background@Selected:=$buttonNormal
      - CornerRadius=6
  - target: Button#PinButton > Grid > Border
    styles:
      - Background=Transparent
      - Height=16
      - BorderBrush:=$buttonBorderBrush
      - BorderThickness=1,0,0,0
      - CornerRadius=0
      - ChildTransitions:=<TransitionCollection><EntranceThemeTransition IsStaggeringEnabled="True" FromHorizontalOffset="0" FromVerticalOffset="37.5" /></TransitionCollection>
  - target: JumpViewUI.JumpListListViewItem
    styles:
      - CornerRadius=4
      - Height=30
  - target: Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter@CommonStates > StartUI.TileViewControl > Grid > Border#Background
    styles:
      - Background@Normal:=$tilesNormal
      - Background@PointerOver:=$tilesPointerOver
      - Background@Pressed:=$tilesPressed
      - BorderBrush@Normal:=$tilesBorderBrushNormal
      - BorderBrush@PointerOver:=$tilesBorderBrushPointerOver
      - BorderBrush@Pressed:=$tilesBorderBrushPressed
      - BorderThickness=0,2,0,2
      - CornerRadius=8
  - target: TileGridNestedPanel > StartUI.TileListViewItem > Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter
    styles:
      - RevealBackground:=
      - PointerOverBackground:=
      - PressedBackground:=
      - CornerRadius=8
  - target: ToolTip > ContentPresenter
    styles:
      - CornerRadius=4
      - Background:=$background
      - BorderThickness=0
  - target: Button#UninstallButton
    styles:
      - Margin=0,15,9,0
      - MinWidth=159
      - Height=32
      - CornerRadius=4
  - target: StartUI.StartSizingFramePanel
    styles:
      - Margin=13
      - CornerRadius=8
  - target: Border#LogoBackgroundPlate
    styles:
      - Margin=12,6,0,6
  - target: MenuFlyoutItem > Grid@CommonStates
    styles:
      - Padding=12,0,0,0
      - MinHeight=30
      - Background@PointerOver:=$menuPointerOver
      - Background@Pressed:=$menuPressed
      - BorderBrush=Transparent
      - MinWidth=208
  - target: ToggleMenuFlyoutItem > Grid@CommonStates
    styles:
      - Padding=12,0,0,0
      - Height=28
      - Background@PointerOver:=$menuPointerOver
      - Background@Pressed:=$menuPressed
      - BorderBrush=Transparent
  - target: TextBlock#ShutdownConfirmationTextBlock
    styles:
      - FontFamily=$fontFamily
  - target: Button#ShutdownConfirmationButton
    styles:
      - Margin=0,17,0,0
      - MinWidth=150
      - Height=32
      - CornerRadius=4
  - target: Button#ShutdownConfirmationButton > ContentPresenter@CommonStates
    styles:
      - Background@Normal:=$buttonNormal
      - Background@PointerOver:=$buttonPointerOver
      - Background@Pressed:=$buttonPressed
      - BorderThickness=1
      - BorderBrush@Normal:=$buttonBorderBrush
  - target: TextBox > Grid > Button#DeleteButton > Grid@CommonStates
    styles:
      - Background@PointerOver:=$listPointerOver
      - CornerRadius=4
      - Height=20
      - Width=28
      - Margin=-12,0,0,0
      - Background@Pressed:=$listPressed
  - target: TextBox
    styles:
      - FontWeight=Semibold
      - FontSize=14
      - FontFamily=$fontFamily
  - target: Grid#InnerRoot
    styles:
      - Height=46
  - target: TextBlock#SignedInStatus
    styles:
      - FontSize=12
      - Margin=8,0,0,2
      - FontFamily=$fontFamily
  - target: MenuFlyoutSeparator
    styles:
      - Background:=$buttonBorderBrush
      - Padding=1,4,1,4
  - target: Grid#RootPanel@CommonStates > Rectangle
    styles:
      - Fill@Selected:=$accentButtonNormal
      - Height=16
      - Width=3
      - RadiusX=2
      - RadiusY=2
      - Canvas.ZIndex=5
      - Fill@PointerOverSelected:=$accentButtonNormal
  - target: 'StartUI.NavigationPaneGrid > StartUI.UserTileView > StartUI.NavigationPaneButton#UserTileButton '
    styles:
      - Margin=6
      - Height=36
      - CornerRadius=6
  - target: 'StartUI.NavigationPaneGrid > StartUI.PowerOptionsView > StartUI.NavigationPaneButton#PowerButton '
    styles:
      - Margin=6
      - Height=36
      - CornerRadius=6
  - target: StartUI.ViewSelectionListViewItem
    styles:
      - Margin=6
      - Height=36
      - CornerRadius=6
  - target: StartUI.AppListViewItem
    styles:
      - Margin=6
      - Height=36
      - CornerRadius=6
  - target: StartUI.AppListViewItem > Grid#RootPanel@CommonStates > ContentPresenter > StartUI.NavigationPaneItemPanel > FontIcon
    styles:
      - Margin=-12,0,0,0
      - Opacity@Pressed=0.8
  - target: StartUI.NavigationPaneButton#PowerButton > ContentPresenter@CommonStates > StartUI.NavigationPaneItemPanel > Grid > FontIcon
    styles:
      - Margin=-12,0,0,0
      - Opacity@Pressed=0.8
  - target: StartUI.NavigationPaneButton#UserTileButton > ContentPresenter@CommonStates > StartUI.NavigationPaneItemPanel > Grid
    styles:
      - Margin=-12,0,0,0
      - Opacity@Pressed=0.8
      - Width=24
      - Height=24
  - target: JumpViewUI.ItemNotFoundFlyoutControl > StackPanel > StackPanel > TextBlock
    styles:
      - FontFamily=$fontFamily
  - target: JumpViewUI.JumpListCategoryHeaderControl > Grid > TextBlock#HeadingTextBlock
    styles:
      - Margin=15,9,0,5
      - FontFamily=$fontFamily
  - target: MenuFlyoutSubItem > Grid@CommonStates
    styles:
      - Background@SubMenuOpened:=$menuPointerOver
      - Background@PointerOver:=$menuPointerOver
      - Padding=12,0,0,0
      - BorderBrush=Transparent
  - target: Viewbox > Border > TextBlock
    styles:
      - FontWeight=SemiBold
      - Margin=0,0,0,4
      - FontFamily=$fontFamily
  - target: StartUI.AllAppsZoomListViewItem
    styles:
      - CornerRadius=6
  - target: TextBlock#FolderDisplayName
    styles:
      - Margin=9,0,0,5
      - FontFamily=$fontFamily
  - target: JumpViewUI.JumpListListViewItem > Grid@CommonStates
    styles:
      - Background@PointerOver:=$menuPointerOver
      - Background@Pressed:=$menuPressed
      - BorderBrush=Transparent
  - target: Button#PinButton
    styles:
      - MinWidth=44
  - target: Button#PinButton > Grid@CommonStates > Border > ContentPresenter > TextBlock
    styles:
      - Margin=3,0,0,0
      - Opacity@Pressed=0.8
  - target: FontIcon#SubItemChevron
    styles:
      - Margin=-30,0,0,0
      - Glyph:=&#xE76C;
  - target: Border#SmallLogo
    styles:
      - Margin=0,0,0,4
  - target: MenuFlyoutPresenter > Grid > ScrollViewer > Border
    styles:
      - ChildTransitions:=<TransitionCollection><EntranceThemeTransition IsStaggeringEnabled="True" FromHorizontalOffset="-37.5" FromVerticalOffset="0" /></TransitionCollection>
  - target: ToolTip > ContentPresenter#LayoutRoot > TextBlock
    styles:
      - FontFamily=$fontFamily
  - target: StartUI.AllAppsGridListViewItem[AutomationProperties.AutomationId=RecentList] > StackPanel > Button > Border > TextBlock
    styles:
      - Margin=7,0,0,2
  - target: Button#ShutdownReasonButton
    styles:
      - MinWidth=150
      - Height=32
      - CornerRadius=4
  - target: Button#ShutdownReasonButton > ContentPresenter@CommonStates
    styles:
      - Background@Normal:=$buttonNormal
      - Background@PointerOver:=$buttonPointerOver
      - Background@Pressed:=$buttonPressed
      - BorderThickness=1
      - BorderBrush:=$buttonBorderBrush
  - target: ComboBox#ShutdownReasonComboBox
    styles:
      - CornerRadius=4
      - MinWidth=166
      - FontFamily=$fontFamily
  - target: ComboBox > Grid@CommonStates > Border#Background
    styles:
      - Background@Normal:=$buttonNormal
      - Background@PointerOver:=$buttonPointerOver
      - Background@Pressed:=$buttonPressed
      - CornerRadius=4
      - BorderThickness=1
      - BorderBrush:=$buttonBorderBrush
  - target: ComboBoxItem
    styles:
      - CornerRadius=4
      - Margin=3,0,3,0
  - target: ComboBoxItem > Grid@CommonStates
    styles:
      - Background@PointerOver:=$menuPointerOver
      - Background@Pressed:=$menuPressed
      - Background@Selected:=$menuPointerOver
      - Background@SelectedPressed:=$menuPressed
      - Background@SelectedPointerOver:=$menuPointerOver
      - BorderBrush=Transparent
  - target: Border#PopupBorder
    styles:
      - Background:=$background
      - CornerRadius=8
  - target: FlyoutPresenter
    styles:
      - CornerRadius=8
      - Background:=$background
      - BorderBrush:=$borderBrush
      - Padding=16
  - target: StackPanel#ShutdownConfirmationFlyoutPanel
    styles:
      - Margin=0,-1.5,0,0
  - target: StackPanel#ShutdownReasonFlyoutPanel
    styles:
      - Margin=0,-3,0,0
  - target: Button#ShutdownConfirmationButton > ContentPresenter@CommonStates > TextBlock
    styles:
      - FontFamily=$fontFamily
      - FontSize=14
      - Opacity@Pressed=0.8
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
  - target: Button#ShutdownReasonButton > ContentPresenter@CommonStates > TextBlock
    styles:
      - FontFamily=$fontFamily
      - FontSize=14
      - Opacity@Pressed=0.8
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
  - target: ComboBox > Grid@CommonStates > ContentPresenter > TextBlock
    styles:
      - FontFamily=$fontFamily
      - FontSize=14
      - Opacity@Pressed=0.8
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
  - target: ComboBoxItem > Grid@CommonStates > ContentPresenter > TextBlock
    styles:
      - FontFamily=$fontFamily
      - FontSize=14
      - Opacity@Pressed=0.8
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
      - Margin=0,1,0,-1
  - target: StartUI.AllAppsGridListViewItem[AutomationProperties.AutomationId=FrequentList] > StackPanel > Button > Border > TextBlock
    styles:
      - Margin=7,0,0,2
  - target: TextBlock#FolderGlyph
    styles:
      - FontSize=11
      - FontWeight=Light
      - FontFamily=Segoe Fluent Icons
  - target: ItemsWrapGrid > StartUI.AllAppsZoomListViewItem > Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter > Border > TextBlock
    styles:
      - FontWeight=Light
      - FontFamily=Segoe Fluent Icons
  - target: Grid#MainGrid@InteractionStates > Rectangle#BackgroundElement
    styles:
      - Fill@InteractionState_Edit:=
      - Fill@InteractionState_Rest:=
      - Fill@InteractionState_Pressed:=
      - Fill@InteractionState_Drag:=
      - StrokeThickness=0
      - RadiusX=4
      - RadiusY=4
  - target: TextBox > Grid > Border#BackgroundElement
    styles:
      - Background:=<SolidColorBrush Color="{ThemeResource TextBoxBG}" />
      - CornerRadius=4
      - BorderThickness=0,0,0,2
      - BorderBrush:=$accentButtonNormal
  - target: TextBox > Grid > Border#BorderElement
    styles:
      - BorderThickness=1,1,1,0
      - CornerRadius=4
      - BorderBrush:=<SolidColorBrush Color="{ThemeResource SystemChromeHighColor}" Opacity="0.5" />
      - Margin=2
  - target: Grid#MainGrid@FocusStates > Rectangle#BackgroundElement
    styles:
      - Fill@FocusState_Hover:=$tilesNormal
      - Fill@FocusState_None=Transparent
      - Fill@FocusState_HoverPlaceholder:=$tilesNormal
      - StrokeThickness=0
      - Fill@FocusState_Keyboard:=$tilesNormal
      - RadiusX=4
      - RadiusY=4
      - Height=28
      - Margin=0,3,0,0
  - target: Grid#MainGrid@FocusStates > Grid > Border#NameTextBlockHost
    styles:
      - BorderThickness=0,0,0,2
      - BorderBrush@FocusState_Hover:=$textboxBorder
      - CornerRadius=4
      - BorderBrush@FocusState_HoverPlaceholder:=$textboxBorder
      - Margin=0,0,-48,0
      - BorderBrush@FocusState_Keyboard:=$textboxBorder
  - target: StackPanel > Button#DeleteButton > Grid > ContentPresenter
    styles:
      - BorderBrush=Transparent
  - target: FontIcon
    styles:
      - FontFamily=Segoe Fluent Icons
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
  - target: Grid#ContentRoot
    styles:
      - BorderThickness=1,0,0,0
      - BorderBrush:=<SolidColorBrush Color="{ThemeResource NavPaneBorder}" />
      - Margin=0,1,0,1
  - target: Border#NameTextBoxHost > TextBox
    styles:
      - Margin=-2,2,-50,0
  - target: SplitView#RootContent
    styles:
      - IsPaneOpen=False
      - OpenPaneLength=48
  - target: StartUI.NavigationPaneGrid > Border
    styles:
      - Background:=<SolidColorBrush Color="{ThemeResource NavPane}" />
      - Width=48
  - target: StartUI.ExpandCollapseButton
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter > Grid > ProgressBar
    styles:
      - CornerRadius=2
      - Margin=20,0,4,4
  - target: Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter > Grid > ProgressBar > Grid > Border > Rectangle
    styles:
      - Fill:=$accentButtonNormal
      - Margin=-1,-2,0,-2
      - RadiusX=4
      - RadiusY=4
  - target: TextBox > Grid > Button#DeleteButton > Grid@CommonStates > Border > TextBlock#GlyphElement
    styles:
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
      - Opacity@Pressed=0.8
  - target: ScrollViewer#ContentElement
    styles:
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
      - Margin=5,0,0,1
      - FontFamily=Segoe UI Variable Small
  - target: Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter > Grid > ProgressBar > Grid > Border
    styles:
      - BorderThickness=1
      - Background:=<SolidColorBrush Color="{ThemeResource SystemChromeHighColor}" Opacity="0.5" />
  - target: TextBlock#Badge
    styles:
      - FontFamily=$fontFamily
  - target: StartUI.UserTileView
    styles:
      - Grid.Row=1
  - target: StartUI.ViewSelectionListView
    styles:
      - Grid.Row=0
  - target: Border#HighlightBackground
    styles:
      - Background:=$menuPointerOver
      - Margin=-2
      - CornerRadius=6
      - BorderBrush:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
  - target: Button#DeleteButton > Grid > Border
    styles:
      - Background=Transparent
  - target: StartUI.TileFolderNameTextBox > Grid@CommonStates > Border#BorderElement
    styles:
      - Background@PointerOver:=$tilesNormal
      - Background@Focused:=<SolidColorBrush Color="{ThemeResource TextBoxBG}" />
      - CornerRadius=4
      - BorderThickness=1,1,1,0
      - BorderBrush@Focused:=<SolidColorBrush Color="{ThemeResource SystemChromeHighColor}" Opacity="0.5" />
      - Height=28
      - Margin@PointerOver=-1
      - Margin@Focused=0
  - target: StartUI.TileFolderNameTextBox > Grid@CommonStates
    styles:
      - BorderThickness=0,0,0,2
      - BorderBrush@PointerOver:=$textboxBorder
      - BorderBrush@Focused:=$accentButtonNormal
      - CornerRadius=4
      - Height=28
  - target: StartUI.TileFolderNameTextBox > Grid@CommonStates > Border > ScrollViewer
    styles:
      - Margin=3,-4,0,0
  - target: Border#DeleteButtonWrapper > Button#DeleteButton > Grid@CommonStates
    styles:
      - Background@PointerOver:=$listPointerOver
      - Background@Pressed:=$listPressed
      - CornerRadius=4
      - Width=28
      - Height=20
      - Margin=-10,1,0,0
  - target: Border#DeleteButtonWrapper > Button#DeleteButton > Grid@CommonStates > Border > TextBlock#GlyphElement
    styles:
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
      - Opacity@Pressed=0.8
  - target: Windows.UI.Xaml.Controls.Primitives.RepeatButton#VerticalSmallIncrease > Grid
    styles:
      - Background=Transparent
  - target: Windows.UI.Xaml.Controls.Primitives.RepeatButton#VerticalSmallDecrease > Grid
    styles:
      - Background=Transparent
  - target: StartUI.TileFolderNameTextBox > Grid@CommonStates > Border > TextBlock#PlaceholderTextContentPresenter
    styles:
      - Margin=2,-4,0,0
      - Opacity@Normal=0
      - Opacity@PointerOver=1
      - Opacity@Focused=0
  - target: Windows.UI.Xaml.Controls.Primitives.ScrollBar > Grid > Grid > Rectangle
    styles:
      - Fill:=<SolidColorBrush Color="{ThemeResource SystemChromeHighColor}" Opacity="0.2" />
      - RadiusX=4
      - RadiusY=4
  - target: Rectangle#Overlay
    styles:
      - Opacity=0.5
  - target: Border#OverlayBorder
    styles:
      - Opacity=0.5
  - target: StartUI.TileViewControl > Grid#MainGrid > Grid > ProgressBar
    styles:
      - CornerRadius=2
      - Margin=4
  - target: StartUI.TileViewControl > Grid#MainGrid > Grid > ProgressBar > Grid > Border > Rectangle
    styles:
      - Margin=-1,-2,0,-2
      - Fill:=$accentButtonNormal
      - RadiusX=4
      - RadiusY=4
  - target: StartUI.TileViewControl > Grid#MainGrid > Grid > ProgressBar > Grid > Border
    styles:
      - BorderThickness=1
      - Background:=<SolidColorBrush Color="{ThemeResource SystemChromeHighColor}" Opacity="0.5" />
  - target: StartUI.ViewSelectionListViewItem > Grid#RootPanel@CommonStates > ContentPresenter > StartUI.NavigationPaneItemPanel > FontIcon
    styles:
      - Margin=-12,0,0,0
      - Opacity@Pressed=0.8
      - Opacity@PressedSelected=0.8
  - target: StartUI.TileViewControl > Grid
    styles:
      - CornerRadius=8
  - target: StartUI.GroupHeaderControl > Grid > Rectangle
    styles:
      - RadiusX=6
      - RadiusY=6
  - target: Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter > Grid > TextBlock#StatusMessage[Text=System]
    styles:
      - Visibility=1
  - target: StartUI.AllAppsGridListViewItem[AutomationProperties.AutomationId=ExpandCollapseButton] > Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter > StackPanel
    styles:
      - Margin=9,0,0,0
  - target: Windows.UI.Xaml.Controls.Primitives.ListViewItemPresenter > StackPanel > TextBlock#FolderGlyph
    styles:
      - Margin=9,0,0,0
  - target: FontIcon#Gripper
    styles:
      - Visibility=1
  - target: ComboBox > Grid@CommonStates > FontIcon#DropDownGlyph
    styles:
      - FontFamily=Segoe Fluent Icons
      - Opacity@Pressed=0.8
      - Foreground:=<SolidColorBrush Color="{ThemeResource SystemBaseHighColor}" />
  - target: JumpViewUI.ControlHostMenuFlyoutPresenter
    styles:
      - Background:=$background
themeResourceVariables:
  - AccentColor@Dark={ThemeResource SystemAccentColorLight2}
  - AccentColor@Light={ThemeResource SystemAccentColorDark1}
  - AccentButtonBorder@Dark={ThemeResource SystemAccentColorLight1}
  - AccentButtonBorder@Light={ThemeResource SystemAccentColorDark2}
  - ButtonFillNormal@Dark=#0FFFFFFF
  - ButtonFillNormal@Light=#B3FFFFFF
  - ButtonFillPointerOver@Dark=#15FFFFFF
  - ButtonFillPointerOver@Light=#80F9F9F9
  - ButtonFillPressed@Dark=#0BFFFFFF
  - ButtonFillPressed@Light=#4DF9F9F9
  - ButtonBorderBrushTopGradient@Dark=#12FFFFFF
  - ButtonBorderBrushTopGradient@Light=#0F000000
  - ButtonBorderBrushBottomGradient@Dark=#18FFFFFF
  - ButtonBorderBrushBottomGradient@Light=#26000000
  - NavPane@Dark=#40000000
  - NavPane@Light=#80FFFFFF
  - NavPaneBorder@Dark=#4D000000
  - NavPaneBorder@Light=#05000000
  - Border@Dark=#CC424242
  - Border@Light=#FFCCCCCC
  - AcrylicBG@Dark=#1F1F1F
  - AcrylicBG@Light=#F2F2F2
  - ListFillPointerOver@Dark=#15FFFFFF
  - ListFillPointerOver@Light=#FAFFFFFF
  - ListFillPressed@Dark=#0BFFFFFF
  - ListFillPressed@Light=#80FFFFFF
  - MenuFillPointerOver@Dark=#15FFFFFF
  - MenuFillPointerOver@Light=#09000000
  - MenuFillPressed@Dark=#0BFFFFFF
  - MenuFillPressed@Light=#06000000
  - TilesFillNormal@Dark=#0FFFFFFF
  - TilesFillNormal@Light=#80FFFFFF
  - TilesFillPointerOver@Dark=#26FFFFFF
  - TilesFillPointerOver@Light=#FAFFFFFF
  - TilesFillPressed@Dark=#0BFFFFFF
  - TilesFillPressed@Light=#80FFFFFF
  - TilesBorderBrushBottomGradientNormal@Dark=Transparent
  - TilesBorderBrushBottomGradientNormal@Light=#1A000000
  - TilesBorderBrushBottomGradientPointerOver@Dark=Transparent
  - TilesBorderBrushBottomGradientPointerOver@Light=#26000000
  - TilesBorderBrushBottomGradientPressed@Dark=Transparent
  - TilesBorderBrushBottomGradientPressed@Light=#1A000000
  - TilesBorderBrushTopGradientNormal@Dark=#33FFFFFF
  - TilesBorderBrushTopGradientNormal@Light=Transparent
  - TilesBorderBrushTopGradientPointerOver@Dark=#4DFFFFFF
  - TilesBorderBrushTopGradientPointerOver@Light=Transparent
  - TilesBorderBrushTopGradientPressed@Dark=#26FFFFFF
  - TilesBorderBrushTopGradientPressed@Light=Transparent
  - TextBoxBorderBrush@Dark=#33FFFFFF
  - TextBoxBorderBrush@Light=#1A000000
  - TextBoxBG@Dark={ThemeResource SystemChromeLowColor}
  - TextBoxBG@Light=White
webContentStyles:
  - target: ''
    styles:
      - ''
webContentCustomJs: ''
```
</details>
