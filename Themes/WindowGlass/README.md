# WindowGlass theme for Windows 11 Start Menu Styler

A theme that adds a modern, glassy aesthetic with a compact layout to the Windows 11 Start menu.

**Author**: [Nathaniel4JC](https://github.com/Nathaniel4JC)

![Screenshot](screenshot.png)

> [!IMPORTANT]
> This theme is made for the [redesigned Windows 11 Start menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/) that is slowly rolling out in the 25H2 update.

## Notes
- This theme works best on Windows 11 **25H2** and later.
- Works best on devices with a screen resolution of 1930x1200 and above.
- This theme currently works on displays with a resolution **above** 1366x768.
- This theme combines the start menu with the Phone Link panel and will only work on the 'New Windows 11 Start Menu'
- This theme consists of **three** backgrounds:
    - Glass
    - Frosted
    - Acrylic
  - In order to switch between these backgrounds, replace the value for "Background" with "$Glass", "$Frosted" or "$Acrylic".

## Bonus
- This theme can style your lock screen as well. 

## Lock Screen
![Lock Screen](Lock_Screen.jpg) 

To make it work, you'll need to:
- Add 'LockApp.exe' to the 'Custom process inclusion list' under 'Advanced settings' in the Windows 11 Start Menu Styler mod.
- Install the [Vivo Sans En VF](https://1drv.ms/u/c/67fedd4420ed716d/EXRoW1f5dABJrO2dPj0tbM0Bm1uYiGeoKyAYA7X7er2Zww?e=cLsiJJ) and [Morganite SemiBold](https://1drv.ms/u/c/67fedd4420ed716d/IQCHLlxP7GPITp4p-uPMw9O5AY3s2NJCHLKC-tYZZVWAGiY?e=yQrKQb) fonts.

## For a complete WindowGlass-themed UI, download the following mods and use the 'WindowGlass' theme:
- Windows 11 Taskbar Styler - for styling the taskbar.
- Windows 11 Notification Center Styler - for styling the Notification Center and Action Center.
- Windows 11 File Explorer Styler - for styling Windows Explorer windows.

---

## Theme selection

The theme is integrated into the mod and can simply be selected from the mod's
settings:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Settings" tab.
* Select the theme and save the settings.

## Manual installation

The theme styles can also be imported manually. To do that, follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Advanced" tab.
* Copy the content below to the text box under "Mod settings" and click "Save".

<details>
<summary>Content to import (click to expand)</summary>

```json
{
  "// Style Constants //": "",
  "styleConstants[0]": "Glass=<WindhawkBlur BlurAmount=\"5\" TintColor=\"{ThemeResource SystemChromeMediumColor}\" TintOpacity=\"0.7\" />",
  "styleConstants[1]": "Frosted=<WindhawkBlur BlurAmount=\"20\" TintColor=\"{ThemeResource SystemChromeMediumColor}\" TintOpacity=\"0.7\" />",
  "styleConstants[2]": "Acrylic=<WindhawkBlur BlurAmount=\"30\" TintColor=\"{ThemeResource SystemChromeMediumColor}\" TintOpacity=\"0.8\" />",
  "styleConstants[3]": "BorderBrush=<LinearGradientBrush StartPoint=\"0,0\" EndPoint=\"0,1\"><GradientStop Color=\"#60808080\" Offset=\"0.0\" /><GradientStop Color=\"#50404040\" Offset=\"0.25\" /><GradientStop Color=\"#40808080\" Offset=\"1\" /></LinearGradientBrush>",
  "styleConstants[4]": "BorderBrush2=<WindhawkBlur BlurAmount=\"10\" TintColor=\"#909090\" TintOpacity=\"0.3\"/>",
  "styleConstants[5]": "ClockBG=<AcrylicBrush TintColor=\"{ThemeResource SystemAccentColor}\" TintOpacity=\"0.4\" FallbackColor=\"{ThemeResource SystemAccentColor}\" />",
  "styleConstants[6]": "BorderThickness=0.3,1,0.3,1",
  "styleConstants[7]": "CornerRadius=25",
  "styleConstants[8]": "SearchBoxRadius=15",
  "styleConstants[9]": "ElementBG=<SolidColorBrush Color=\"{ThemeResource SystemChromeAltHighColor}\" Opacity=\"0.3\" />",
  "styleConstants[10]": "ElementBorderThickness=0.3,0.3,0.3,1",
  "styleConstants[11]": "ElementCornerRadius=18",
  "styleConstants[12]": "ElementBorderBrush=<LinearGradientBrush StartPoint=\"0,0\" EndPoint=\"0,1\"><GradientStop Color=\"#50808080\" Offset=\"1\" /><GradientStop Color=\"#50606060\" Offset=\"0.15\" /></LinearGradientBrush>",
  "styleConstants[13]": "ElementBorderBrush2=<WindhawkBlur BlurAmount=\"30\" TintColor=\"#909090\" TintOpacity=\"0.3\"/>",
  "disableNewStartMenuLayout": 0,
  "theme": "",
  "// Lock Screen //": "",
  "controlStyles[0].target": "StackPanel#TimeAndDatePanel",
  "controlStyles[0].styles[0]": "VerticalAlignment=Top",
  "controlStyles[0].styles[1]": "HorizontalAlignment=Center",
  "controlStyles[0].styles[2]": "RenderTransform:=<TranslateTransform X=\"0\" />",
  "controlStyles[1].target": "StackPanel#TimePanel > TextBlock#Time",
  "controlStyles[1].styles[0]": "HorizontalAlignment:=Center",
  "controlStyles[1].styles[1]": "RenderTransform:=<TransformGroup><TranslateTransform X=\"-30\" Y=\"-10\" /><ScaleTransform ScaleX=\"3.3\" ScaleY=\"6\" /></TransformGroup>",
  "controlStyles[1].styles[2]": "FontFamily=Morganite SemiBold",
  "controlStyles[1].styles[3]": "Foreground:=$ClockBG",
  "controlStyles[2].target": "StackPanel#TimeAndDatePanel > TextBlock#Date",
  "controlStyles[2].styles[0]": "HorizontalAlignment=Center",
  "controlStyles[2].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"-150\" />",
  "controlStyles[2].styles[2]": "FontFamily=vivo Sans EN VF",
  "controlStyles[2].styles[3]": "Foreground:=$ClockBG",
  "controlStyles[3].target": "Windows.UI.Xaml.Controls.Grid#WidgetFrameGrid",
  "controlStyles[3].styles[0]": "Background:=$Frosted",
  "controlStyles[3].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[3].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[3].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[4].target": "Windows.UI.Xaml.Controls.Grid#WidgetCanvasPanel",
  "controlStyles[4].styles[0]": "HorizontalAlignment=Center",
  "controlStyles[4].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"50\" />",
  "controlStyles[5].target": "Windows.UI.Xaml.Controls.Grid#MediaTransportControls",
  "controlStyles[5].styles[0]": "Background:=$Frosted",
  "controlStyles[5].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[5].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[5].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[6].target": "Windows.UI.Xaml.Controls.Grid#MediaControlsContainer",
  "controlStyles[6].styles[0]": "Visibility=Visible",
  "controlStyles[6].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"-250\" />",
  "controlStyles[6].styles[2]": "Margin=0,0,0,0",
  "controlStyles[6].styles[3]": "CornerRadius=$CornerRadius",
  "// Start Menu //": "",
  "controlStyles[7].target": "Windows.UI.Xaml.Controls.Grid#RootPanel > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Grid#RootContent",
  "controlStyles[7].styles[0]": "Margin=-20,-20,-20,0",
  "controlStyles[8].target": "StartDocked.StartSizingFrame",
  "controlStyles[8].styles[0]": "Width=860",
  "controlStyles[9].target": "Windows.UI.Xaml.Controls.Border#RootGridDropShadow",
  "controlStyles[9].styles[0]": "Visibility=1",
  "controlStyles[10].target": "Windows.UI.Xaml.Controls.Border#RightCompanionDropShadow",
  "controlStyles[10].styles[0]": "Visibility=1",
  "controlStyles[11].target": "Windows.UI.Xaml.Controls.Border#DropShadowDismissTarget",
  "controlStyles[11].styles[0]": "Background:=$Frosted",
  "controlStyles[11].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[11].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[11].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[11].styles[4]": "Margin=5",
  "controlStyles[12].target": "Windows.UI.Xaml.Controls.Grid#RootContent > Windows.UI.Xaml.Controls.Border#AcrylicBorder",
  "controlStyles[12].styles[0]": "Background:=$ElementBG",
  "controlStyles[12].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[12].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[12].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[12].styles[4]": "Margin=0,60,0,10",
  "controlStyles[12].styles[5]": "Visibility=1",
  "controlStyles[13].target": "Windows.UI.Xaml.Controls.Border#AcrylicOverlay",
  "controlStyles[13].styles[0]": "Visibility=1",
  "controlStyles[14].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox",
  "controlStyles[14].styles[0]": "Width=650",
  "controlStyles[14].styles[1]": "Height=50",
  "controlStyles[14].styles[2]": "Margin=0,-15,0,0",
  "controlStyles[15].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Border#BorderElement",
  "controlStyles[15].styles[0]": "Background:=$ElementBG",
  "controlStyles[15].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[15].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[15].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[16].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.TextBlock#PlaceholderText",
  "controlStyles[16].styles[0]": "Text=Search This Precision",
  "controlStyles[17].target": "Windows.UI.Xaml.Controls.Grid#TopLevelRoot > Windows.UI.Xaml.Controls.Grid",
  "controlStyles[17].styles[0]": "Visibility=1",
  "controlStyles[18].target": "StartDocked.NavigationPaneView#NavigationPane",
  "controlStyles[18].styles[0]": "Width=550",
  "controlStyles[18].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"10\" />",
  "controlStyles[19].target": "Windows.UI.Xaml.Controls.Button#ShowAllAppsButton",
  "controlStyles[19].styles[0]": "Visibility=1",
  "controlStyles[20].target": "StartMenu.PinnedList#StartMenuPinnedList",
  "controlStyles[20].styles[0]": "Margin=0",
  "controlStyles[20].styles[1]": "Height=280",
  "controlStyles[21].target": "StartMenu.PinnedList#StartMenuPinnedList > Windows.UI.Xaml.Controls.Grid#Root",
  "controlStyles[21].styles[0]": "Background:=$ElementBG",
  "controlStyles[21].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[21].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[21].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[22].target": "Windows.UI.Xaml.Controls.Grid#UndockedRoot",
  "controlStyles[22].styles[0]": "Visibility=0",
  "controlStyles[22].styles[1]": "Width=650",
  "controlStyles[22].styles[2]": "Margin=0,-130,0,230",
  "controlStyles[22].styles[3]": "Canvas.ZIndex=1",
  "controlStyles[22].styles[4]": "MaxHeight:=340",
  "controlStyles[23].target": "Windows.UI.Xaml.Controls.Grid#AllAppsRoot",
  "controlStyles[23].styles[0]": "Visibility=0",
  "controlStyles[23].styles[1]": "Margin=-1600,190,115,-100",
  "controlStyles[23].styles[2]": "MaxHeight=330",
  "controlStyles[23].styles[3]": "Background:=$ElementBG",
  "controlStyles[23].styles[4]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[23].styles[5]": "Width=650",
  "controlStyles[23].styles[6]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[23].styles[7]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[24].target": "Windows.UI.Xaml.Controls.Button#CloseAllAppsButton",
  "controlStyles[24].styles[0]": "Visibility=1",
  "controlStyles[25].target": "Windows.UI.Xaml.Controls.TextBlock#AllAppsHeading",
  "controlStyles[25].styles[0]": "Visibility=1",
  "controlStyles[26].target": "StartDocked.AllAppsPane#AllAppsPanel",
  "controlStyles[26].styles[0]": "Margin=-20,-20,20,20",
  "// Phone Link Panel //": "",
  "controlStyles[27].target": "StartDocked.StartMenuCompanion#RightCompanion > Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicBorder",
  "controlStyles[27].styles[0]": "Background:=$ElementBG",
  "controlStyles[27].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[27].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[27].styles[3]": "CornerRadius:=$ElementCornerRadius",
  "controlStyles[28].target": "Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Grid#MainContent > Windows.UI.Xaml.Controls.Grid#ActionsBar > Windows.UI.Xaml.Controls.Button#PrimaryActionBarButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter",
  "controlStyles[28].styles[0]": "Background:=$ElementBG",
  "controlStyles[28].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[28].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[28].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[28].styles[4]": "Height=40",
  "controlStyles[29].target": "Windows.UI.Xaml.Controls.Grid#ActionsBar > Windows.UI.Xaml.Controls.Button#ActionBarOverflowButton",
  "controlStyles[29].styles[0]": "Background:=$ElementBG",
  "controlStyles[29].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[29].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[29].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[29].styles[4]": "Height=40",
  "controlStyles[30].target": "StartDocked.StartMenuCompanion#RightCompanion > Windows.UI.Xaml.Controls.Grid#CompanionRoot",
  "controlStyles[30].styles[0]": "Height=730",
  "controlStyles[30].styles[1]": "Margin=0,-10,0,-10",
  "controlStyles[30].styles[2]": "Padding=10,0,-2,0",
  "// Flyouts and Menus //": "",
  "controlStyles[31].target": "Windows.UI.Xaml.Controls.Border#OverflowFlyoutBackgroundBorder",
  "controlStyles[31].styles[0]": "Background:=$Frosted",
  "controlStyles[31].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[31].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[31].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[32].target": "Windows.UI.Xaml.Controls.MenuFlyoutPresenter > Windows.UI.Xaml.Controls.Border",
  "controlStyles[32].styles[0]": "Background:=$Frosted",
  "controlStyles[32].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[32].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[32].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[33].target": "Windows.UI.Xaml.Controls.Grid#HoverFlyoutGrid > Windows.UI.Xaml.Controls.Border#HoverFlyoutBackground",
  "controlStyles[33].styles[0]": "Background:=$Frosted",
  "controlStyles[33].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[33].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[33].styles[3]": "CornerRadius=$ElementCornerRadius",
  "// Search Menu //": "",
  "controlStyles[34].target": "Cortana.UI.Views.TaskbarSearchPage > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Grid#OuterBorderGrid",
  "controlStyles[34].styles[0]": "Background:=$Frosted",
  "controlStyles[34].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[34].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[34].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[35].target": "Windows.UI.Xaml.Controls.Border#LayerBorder",
  "controlStyles[35].styles[0]": "Visibility=1",
  "controlStyles[36].target": "Windows.UI.Xaml.Controls.Borde#AccentLayerBorder",
  "controlStyles[36].styles[0]": "Visibility=1",
  "controlStyles[37].target": "Windows.UI.Xaml.Controls.Border#dropshadow",
  "controlStyles[37].styles[0]": "Visibility=1",
  "controlStyles[38].target": "Windows.UI.Xaml.Controls.Border#AppBorder",
  "controlStyles[38].styles[0]": "Visibility=1",
  "// ToolTip //": "",
  "controlStyles[39].target": "Windows.UI.Xaml.Controls.ToolTip > Windows.UI.Xaml.Controls.ContentPresenter#LayoutRoot",
  "controlStyles[39].styles[0]": "Background:=$Frosted",
  "controlStyles[39].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[39].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[39].styles[3]": "CornerRadius=15",
  "// Folder //": "",
  "controlStyles[40].target": "StartMenu.FolderModal#StartFolderModal > Windows.UI.Xaml.Controls.Grid#Root",
  "controlStyles[40].styles[0]": "MaxHeight:=420",
  "controlStyles[40].styles[1]": "MaxWidth:=420",
  "controlStyles[40].styles[2]": "Height=Auto",
  "controlStyles[40].styles[3]": "Width=Auto",
  "controlStyles[41].target": "StartMenu.FolderModal#StartFolderModal > Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.ContentControl#ContentControl > Windows.UI.Xaml.Controls.ContentPresenter > StartMenu.UniversalTileContainer#UniversalTileContainer > Windows.UI.Xaml.Controls.Grid#GridViewContainer",
  "controlStyles[41].styles[0]": "Width=400",
  "controlStyles[41].styles[1]": "Height=400",
  "controlStyles[42].target": "Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.Border",
  "controlStyles[42].styles[0]": "Background:=$Frosted",
  "controlStyles[42].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[42].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[42].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[43].target": "StartMenu.ExpandedFolderList",
  "controlStyles[43].styles[0]": "Margin=0,30,0,-120",
  "// New Start Menu//": "",
  "// Start Menu//": "",
  "controlStyles[44].target": "Windows.UI.Xaml.Controls.Grid#MainMenu > Windows.UI.Xaml.Controls.Border#AcrylicBorder",
  "controlStyles[44].styles[0]": "Visibility=1",
  "controlStyles[45].target": "StartMenu.SearchBoxToggleButton#SearchBoxToggleButton",
  "controlStyles[45].styles[0]": "Height=50",
  "controlStyles[45].styles[1]": "Margin=-12,20,-60,-20",
  "controlStyles[45].styles[2]": "Width=400",
  "controlStyles[46].target": "StartMenu.SearchBoxToggleButton#SearchBoxToggleButton > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Border#BorderElement",
  "controlStyles[46].styles[0]": "Background:=$ElementBG",
  "controlStyles[46].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[46].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[46].styles[3]": "CornerRadius:=$ElementCornerRadius",
  "controlStyles[47].target": "Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion",
  "controlStyles[47].styles[0]": "Margin=0,40,20,0",
  "controlStyles[48].target": "Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText",
  "controlStyles[48].styles[0]": "Visibility=1",
  "controlStyles[49].target": "Windows.UI.Xaml.Controls.Grid#AllListHeading",
  "controlStyles[49].styles[0]": "Margin=0,-10,0,0",
  "controlStyles[50].target": "Windows.UI.Xaml.Controls.Grid#AllListHeading > Windows.UI.Xaml.Controls.TextBlock#AllListHeadingText",
  "controlStyles[50].styles[0]": "Visibility=1",
  "controlStyles[51].target": "StartMenu.CategoryControl > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Border ",
  "controlStyles[51].styles[0]": "Background:=$ElementBG",
  "controlStyles[51].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[51].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[51].styles[3]": "CornerRadius=$ElementCornerRadius",
  "// Start menu Width//": "",
  "controlStyles[52].target": "Windows.UI.Xaml.Controls.Grid#MainMenu",
  "controlStyles[52].styles[0]": "Width=460",
  "// Pinned Apps//": "",
  "controlStyles[53].target": "StartMenu.PinnedList#StartMenuPinnedList",
  "controlStyles[53].styles[0]": "Width=400",
  "controlStyles[53].styles[1]": "Height=450",
  "controlStyles[53].styles[2]": "Margin=-0,0,0,80",
  "controlStyles[54].target": "Windows.UI.Xaml.Controls.GridView#PinnedList > Border > Windows.UI.Xaml.Controls.ScrollViewer",
  "controlStyles[54].styles[0]": "ScrollViewer.VerticalScrollMode=2",
  "controlStyles[54].styles[1]": "MaxHeight:=330",
  "controlStyles[54].styles[2]": "MinHeight:=100",
  "controlStyles[54].styles[3]": "Width=300",
  "controlStyles[54].styles[4]": "Margin=0,0,60,0",
  "// Phone Link Panel Dimensions//": "",
  "controlStyles[55].target": "StartMenu.StartMenuCompanion#RightCompanion",
  "controlStyles[55].styles[0]": "Height=810",
  "controlStyles[55].styles[1]": "Margin=0,0,30,0",
  "// Phone Link Panel//": "",
  "controlStyles[56].target": "Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicBorder",
  "controlStyles[56].styles[0]": "Background:=$ElementBG",
  "controlStyles[56].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[56].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[56].styles[3]": "CornerRadius=$ElementCornerRadius",
  "// All Apps Section//": ""
}
```
</details>
