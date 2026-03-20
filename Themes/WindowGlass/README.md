# WindowGlass theme for Windows 11 Start Menu Styler

A theme that adds a modern, glassy aesthetic with a compact layout to the Windows 11 Start menu.

**Author**: [Nathaniel4JC](https://github.com/Nathaniel4JC)

![Screenshot](screenshot.png)

> [!IMPORTANT]
> This theme is designed for the [redesigned Windows 11 Start menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/) that is gradually rolling out with the 25H2 update.

## Notes
- This theme works best on Windows 11 **25H2** and later.
- Works best on devices with a screen resolution of 1930x1200 and above.
- This theme currently works on displays with a resolution **above** 1366x768.
- This theme combines the start menu with the Phone Link panel and will only work on the 'New Windows 11 Start Menu'
- This theme consists of the following backgrounds:
  - Translucent
  - Glass
  - Frosted
  - Acrylic

  In order to switch between these backgrounds, set the value `Background=$Translucent`, `Background=$Glass`, `Background=$Frosted` or `Background=$Acrylic` in the "Style constants" section of the mod's settings.

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

The theme is integrated into the mod and can be selected directly from the mod's
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
  "styleConstants[0]": "Translucent=<WindhawkBlur BlurAmount=\"15\" TintColor=\"#10808080\"/>",
  "styleConstants[1]": "Glass=<WindhawkBlur BlurAmount=\"5\" TintColor=\"{ThemeResource SystemChromeMediumColor}\" TintOpacity=\"0.7\" />",
  "styleConstants[2]": "Frosted=<WindhawkBlur BlurAmount=\"20\" TintColor=\"{ThemeResource SystemChromeMediumColor}\" TintOpacity=\"0.7\" />",
  "styleConstants[3]": "Acrylic=<WindhawkBlur BlurAmount=\"30\" TintColor=\"{ThemeResource SystemChromeMediumColor}\" TintOpacity=\"0.8\" />",
  "styleConstants[4]": "Background=$Glass",
  "styleConstants[5]": "BorderBrush=<LinearGradientBrush StartPoint=\"0,0\" EndPoint=\"0,1\"><GradientStop Color=\"#60808080\" Offset=\"0.0\" /><GradientStop Color=\"#50404040\" Offset=\"0.25\" /><GradientStop Color=\"#40808080\" Offset=\"1\" /></LinearGradientBrush>",
  "styleConstants[6]": "BorderBrush2=<WindhawkBlur BlurAmount=\"10\" TintColor=\"#909090\" TintOpacity=\"0.3\"/>",
  "styleConstants[7]": "ClockBG=<SolidColorBrush Color=\"{ThemeResource SystemAccentColor}\" Opacity=\"1\"/>",
  "styleConstants[8]": "BorderThickness=0.3,1,0.3,1",
  "styleConstants[9]": "CornerRadius=35",
  "styleConstants[10]": "SearchBoxRadius=20",
  "styleConstants[11]": "ElementBG=<SolidColorBrush Color=\"{ThemeResource SystemChromeAltHighColor}\" Opacity=\"0.3\" />",
  "styleConstants[12]": "ElementBorderThickness=0.3,0.3,0.3,1",
  "styleConstants[13]": "ElementCornerRadius=25",
  "styleConstants[14]": "ElementBorderBrush=<LinearGradientBrush StartPoint=\"0,0\" EndPoint=\"0,1\"><GradientStop Color=\"#50808080\" Offset=\"1\" /><GradientStop Color=\"#50606060\" Offset=\"0.15\" /></LinearGradientBrush>",
  "styleConstants[15]": "ElementBorderBrush2=<WindhawkBlur BlurAmount=\"30\" TintColor=\"#909090\" TintOpacity=\"0.3\"/>",
  "styleConstants[16]": "HoverCornerRadius=15",
  "controlStyles[0].target": "// Lock Screen",
  "controlStyles[1].target": "StackPanel#TimeAndDatePanel",
  "controlStyles[1].styles[0]": "VerticalAlignment=Top",
  "controlStyles[1].styles[1]": "HorizontalAlignment=Center",
  "controlStyles[1].styles[2]": "RenderTransform:=<TranslateTransform X=\"0\" />",
  "controlStyles[2].target": "StackPanel#TimePanel > TextBlock#Time",
  "controlStyles[2].styles[0]": "HorizontalAlignment:=Center",
  "controlStyles[2].styles[1]": "RenderTransform:=<TransformGroup><TranslateTransform X=\"-30\" Y=\"-10\" /><ScaleTransform ScaleX=\"3.3\" ScaleY=\"6\" /></TransformGroup>",
  "controlStyles[2].styles[2]": "FontFamily=Morganite SemiBold",
  "controlStyles[2].styles[3]": "Foreground:=$ClockBG",
  "controlStyles[3].target": "StackPanel#TimeAndDatePanel > TextBlock#Date",
  "controlStyles[3].styles[0]": "HorizontalAlignment=Center",
  "controlStyles[3].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"-110\" />",
  "controlStyles[3].styles[2]": "FontFamily=vivo Sans EN VF",
  "controlStyles[3].styles[3]": "Foreground:=$ClockBG",
  "controlStyles[4].target": "Windows.UI.Xaml.Controls.Grid#WidgetFrameGrid",
  "controlStyles[4].styles[0]": "Background:=$Background",
  "controlStyles[4].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[4].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[4].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[5].target": "Windows.UI.Xaml.Controls.Grid#WidgetCanvasPanel",
  "controlStyles[5].styles[0]": "HorizontalAlignment=Center",
  "controlStyles[5].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"50\" />",
  "controlStyles[6].target": "Windows.UI.Xaml.Controls.Grid#MediaTransportControls",
  "controlStyles[6].styles[0]": "Background:=$Background",
  "controlStyles[6].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[6].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[6].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[7].target": "Windows.UI.Xaml.Controls.Grid#MediaControlsContainer",
  "controlStyles[7].styles[0]": "Visibility=Visible",
  "controlStyles[7].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"-250\" />",
  "controlStyles[7].styles[2]": "Margin=0,0,0,0",
  "controlStyles[7].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[8].target": "// Start Menu",
  "controlStyles[9].target": "Windows.UI.Xaml.Controls.Grid#RootPanel > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Grid#RootContent",
  "controlStyles[9].styles[0]": "Margin=-20,-20,-20,0",
  "controlStyles[10].target": "StartDocked.StartSizingFrame",
  "controlStyles[10].styles[0]": "Width=860",
  "controlStyles[11].target": "Windows.UI.Xaml.Controls.Border#RootGridDropShadow",
  "controlStyles[11].styles[0]": "Visibility=1",
  "controlStyles[12].target": "Windows.UI.Xaml.Controls.Border#RightCompanionDropShadow",
  "controlStyles[12].styles[0]": "Visibility=1",
  "controlStyles[13].target": "Windows.UI.Xaml.Controls.Border#StartDropShadow",
  "controlStyles[13].styles[0]": "Visibility=1",
  "controlStyles[14].target": "Windows.UI.Xaml.Controls.Border#DropShadowDismissTarget",
  "controlStyles[14].styles[0]": "Background:=$Background",
  "controlStyles[14].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[14].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[14].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[14].styles[4]": "Margin=2",
  "controlStyles[14].styles[5]": "Padding=0",
  "controlStyles[15].target": "Windows.UI.Xaml.Controls.Grid#RootContent > Windows.UI.Xaml.Controls.Border#AcrylicBorder",
  "controlStyles[15].styles[0]": "Background:=$ElementBG",
  "controlStyles[15].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[15].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[15].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[15].styles[4]": "Margin=0,60,0,10",
  "controlStyles[15].styles[5]": "Visibility=1",
  "controlStyles[16].target": "Windows.UI.Xaml.Controls.Border#AcrylicOverlay",
  "controlStyles[16].styles[0]": "Visibility=1",
  "controlStyles[17].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox",
  "controlStyles[17].styles[0]": "Width=650",
  "controlStyles[17].styles[1]": "Height=50",
  "controlStyles[17].styles[2]": "Margin=0,-15,0,0",
  "controlStyles[18].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Border#BorderElement",
  "controlStyles[18].styles[0]": "Background:=$ElementBG",
  "controlStyles[18].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[18].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[18].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[19].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.TextBlock#PlaceholderText",
  "controlStyles[19].styles[0]": "Text=Search This Precision",
  "controlStyles[20].target": "Windows.UI.Xaml.Controls.Grid#TopLevelRoot > Windows.UI.Xaml.Controls.Grid",
  "controlStyles[20].styles[0]": "Visibility=1",
  "controlStyles[21].target": "StartDocked.NavigationPaneView#NavigationPane",
  "controlStyles[21].styles[0]": "Width=550",
  "controlStyles[21].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"10\" />",
  "controlStyles[22].target": "Windows.UI.Xaml.Controls.Button#ShowAllAppsButton",
  "controlStyles[22].styles[0]": "Visibility=1",
  "controlStyles[23].target": "StartMenu.PinnedList#StartMenuPinnedList",
  "controlStyles[23].styles[0]": "Margin=0",
  "controlStyles[23].styles[1]": "Height=280",
  "controlStyles[24].target": "StartMenu.PinnedList#StartMenuPinnedList > Windows.UI.Xaml.Controls.Grid#Root",
  "controlStyles[24].styles[0]": "Background:=$ElementBG",
  "controlStyles[24].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[24].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[24].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[25].target": "Windows.UI.Xaml.Controls.Grid#UndockedRoot",
  "controlStyles[25].styles[0]": "Visibility=0",
  "controlStyles[25].styles[1]": "Width=650",
  "controlStyles[25].styles[2]": "Margin=0,-130,0,230",
  "controlStyles[25].styles[3]": "Canvas.ZIndex=1",
  "controlStyles[25].styles[4]": "MaxHeight:=340",
  "controlStyles[26].target": "Windows.UI.Xaml.Controls.Grid#AllAppsRoot",
  "controlStyles[26].styles[0]": "Visibility=0",
  "controlStyles[26].styles[1]": "Margin=-1600,190,115,-100",
  "controlStyles[26].styles[2]": "MaxHeight=330",
  "controlStyles[26].styles[3]": "Background:=$ElementBG",
  "controlStyles[26].styles[4]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[26].styles[5]": "Width=650",
  "controlStyles[26].styles[6]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[26].styles[7]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[27].target": "Windows.UI.Xaml.Controls.Button#CloseAllAppsButton",
  "controlStyles[27].styles[0]": "Visibility=1",
  "controlStyles[28].target": "Windows.UI.Xaml.Controls.TextBlock#AllAppsHeading",
  "controlStyles[28].styles[0]": "Visibility=1",
  "controlStyles[29].target": "StartDocked.AllAppsPane#AllAppsPanel",
  "controlStyles[29].styles[0]": "Margin=-20,-20,20,20",
  "controlStyles[30].target": "// Phone Link Panel",
  "controlStyles[31].target": "StartDocked.StartMenuCompanion#RightCompanion > Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicBorder",
  "controlStyles[31].styles[0]": "Background:=$ElementBG",
  "controlStyles[31].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[31].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[31].styles[3]": "CornerRadius:=$ElementCornerRadius",
  "controlStyles[32].target": "Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Grid#MainContent > Windows.UI.Xaml.Controls.Grid#ActionsBar > Windows.UI.Xaml.Controls.Button#PrimaryActionBarButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter",
  "controlStyles[32].styles[0]": "Background:=$ElementBG",
  "controlStyles[32].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[32].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[32].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[32].styles[4]": "Height=40",
  "controlStyles[33].target": "Windows.UI.Xaml.Controls.Grid#ActionsBar > Windows.UI.Xaml.Controls.Button#ActionBarOverflowButton",
  "controlStyles[33].styles[0]": "Background:=$ElementBG",
  "controlStyles[33].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[33].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[33].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[33].styles[4]": "Height=40",
  "controlStyles[34].target": "StartDocked.StartMenuCompanion#RightCompanion > Windows.UI.Xaml.Controls.Grid#CompanionRoot",
  "controlStyles[34].styles[0]": "Height=730",
  "controlStyles[34].styles[1]": "Margin=0,-10,0,-10",
  "controlStyles[34].styles[2]": "Padding=10,0,-2,0",
  "controlStyles[35].target": "// Flyouts and Menus",
  "controlStyles[36].target": "Windows.UI.Xaml.Controls.Border#OverflowFlyoutBackgroundBorder",
  "controlStyles[36].styles[0]": "Background:=$Background",
  "controlStyles[36].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[36].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[36].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[37].target": "Windows.UI.Xaml.Controls.MenuFlyoutPresenter > Windows.UI.Xaml.Controls.Border",
  "controlStyles[37].styles[0]": "Background:=$Background",
  "controlStyles[37].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[37].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[37].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[38].target": "Windows.UI.Xaml.Controls.Grid#HoverFlyoutGrid > Windows.UI.Xaml.Controls.Border#HoverFlyoutBackground",
  "controlStyles[38].styles[0]": "Background:=$Background",
  "controlStyles[38].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[38].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[38].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[39].target": "// Search Menu",
  "controlStyles[40].target": "Cortana.UI.Views.TaskbarSearchPage > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Grid#OuterBorderGrid",
  "controlStyles[40].styles[0]": "Background:=$Background",
  "controlStyles[40].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[40].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[40].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[41].target": "Windows.UI.Xaml.Controls.Border#LayerBorder",
  "controlStyles[41].styles[0]": "Visibility=1",
  "controlStyles[42].target": "Windows.UI.Xaml.Controls.Border#AccentLayerBorder",
  "controlStyles[42].styles[0]": "Visibility=1",
  "controlStyles[43].target": "Windows.UI.Xaml.Controls.Border#dropshadow",
  "controlStyles[43].styles[0]": "Visibility=1",
  "controlStyles[44].target": "Windows.UI.Xaml.Controls.Border#AppBorder",
  "controlStyles[44].styles[0]": "Visibility=1",
  "controlStyles[45].target": "// ToolTip",
  "controlStyles[46].target": "Windows.UI.Xaml.Controls.ToolTip > Windows.UI.Xaml.Controls.ContentPresenter#LayoutRoot",
  "controlStyles[46].styles[0]": "Background:=$Background",
  "controlStyles[46].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[46].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[46].styles[3]": "CornerRadius=15",
  "controlStyles[47].target": "// Folder",
  "controlStyles[48].target": "StartMenu.FolderModal#StartFolderModal > Windows.UI.Xaml.Controls.Grid#Root",
  "controlStyles[48].styles[0]": "MaxHeight:=420",
  "controlStyles[48].styles[1]": "MaxWidth:=420",
  "controlStyles[48].styles[2]": "Height=Auto",
  "controlStyles[48].styles[3]": "Width=Auto",
  "controlStyles[49].target": "StartMenu.FolderModal#StartFolderModal > Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.ContentControl#ContentControl > Windows.UI.Xaml.Controls.ContentPresenter > StartMenu.UniversalTileContainer#UniversalTileContainer > Windows.UI.Xaml.Controls.Grid#GridViewContainer",
  "controlStyles[49].styles[0]": "Width=400",
  "controlStyles[49].styles[1]": "Height=400",
  "controlStyles[50].target": "Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.Border",
  "controlStyles[50].styles[0]": "Background:=$Background",
  "controlStyles[50].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[50].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[50].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[51].target": "StartMenu.ExpandedFolderList",
  "controlStyles[51].styles[0]": "Margin=0,30,0,-120",
  "controlStyles[52].target": "// Start Menu",
  "controlStyles[53].target": "Windows.UI.Xaml.Controls.Grid#MainMenu > Windows.UI.Xaml.Controls.Border#AcrylicBorder",
  "controlStyles[53].styles[0]": "Visibility=1",
  "controlStyles[54].target": "StartMenu.SearchBoxToggleButton#SearchBoxToggleButton",
  "controlStyles[54].styles[0]": "Height=50",
  "controlStyles[54].styles[1]": "Margin=-20,20,-20,-20",
  "controlStyles[54].styles[2]": "Width=400",
  "controlStyles[55].target": "StartMenu.SearchBoxToggleButton#SearchBoxToggleButton > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Border#BorderElement",
  "controlStyles[55].styles[0]": "Background:=$ElementBG",
  "controlStyles[55].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[55].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[55].styles[3]": "CornerRadius:=$ElementCornerRadius",
  "controlStyles[56].target": "Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion",
  "controlStyles[56].styles[0]": "Margin=-50,40,0,0",
  "controlStyles[57].target": "Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText",
  "controlStyles[57].styles[0]": "Visibility=1",
  "controlStyles[58].target": "Windows.UI.Xaml.Controls.Grid#AllListHeading",
  "controlStyles[58].styles[0]": "Margin=0,-10,0,0",
  "controlStyles[59].target": "Windows.UI.Xaml.Controls.Grid#AllListHeading > Windows.UI.Xaml.Controls.TextBlock#AllListHeadingText",
  "controlStyles[59].styles[0]": "Visibility=1",
  "controlStyles[60].target": "StartMenu.CategoryControl > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Border",
  "controlStyles[60].styles[0]": "Background:=$ElementBG",
  "controlStyles[60].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[60].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[60].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[61].target": "// Start menu Width",
  "controlStyles[62].target": "Windows.UI.Xaml.Controls.Grid#MainMenu",
  "controlStyles[62].styles[0]": "Width=460",
  "controlStyles[63].target": "// inned Apps",
  "controlStyles[64].target": "StartMenu.PinnedList#StartMenuPinnedList",
  "controlStyles[64].styles[0]": "Width=400",
  "controlStyles[64].styles[1]": "Height=450",
  "controlStyles[64].styles[2]": "Margin=0,0,0,30",
  "controlStyles[65].target": "Windows.UI.Xaml.Controls.GridView#PinnedList > Border > Windows.UI.Xaml.Controls.ScrollViewer",
  "controlStyles[65].styles[0]": "ScrollViewer.VerticalScrollMode=2",
  "controlStyles[65].styles[1]": "MaxHeight:=336",
  "controlStyles[65].styles[2]": "MinHeight:=100",
  "controlStyles[65].styles[3]": "Width=300",
  "controlStyles[65].styles[4]": "Margin=0,0,60,0",
  "controlStyles[66].target": "// Phone Link Panel Dimensions",
  "controlStyles[67].target": "StartMenu.StartMenuCompanion#RightCompanion",
  "controlStyles[67].styles[0]": "Height=810",
  "controlStyles[67].styles[1]": "Margin=15,0,30,0",
  "controlStyles[68].target": "// Phone Link Panel",
  "controlStyles[69].target": "Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicBorder",
  "controlStyles[69].styles[0]": "Background:=$ElementBG",
  "controlStyles[69].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[69].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[69].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[70].target": "// All Apps Section",
  "controlStyles[71].target": "Windows.UI.Xaml.Controls.GridView#AllAppsGrid > Windows.UI.Xaml.Controls.ItemsWrapGrid",
  "controlStyles[71].styles[0]": "Visibility=0",
  "controlStyles[72].target": "Windows.UI.Xaml.Controls.GridView#AllAppsGrid",
  "controlStyles[72].styles[0]": "Margin=0,15,0,0",
  "controlStyles[73].target": "Windows.UI.Xaml.Controls.Grid#TopLevelHeader > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Button",
  "controlStyles[73].styles[0]": "Visibility=1",
  "controlStyles[74].target": "// Flyouts",
  "controlStyles[75].target": "Windows.UI.Xaml.Controls.FlyoutPresenter",
  "controlStyles[75].styles[0]": "Background:=$Background",
  "controlStyles[75].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[75].styles[2]": "BorderThickness:=$BorderThickness",
  "controlStyles[75].styles[3]": "CornerRadius:=$ElementCornerRadius",
  "controlStyles[76].target": "Windows.UI.Xaml.Controls.MenuFlyoutPresenter",
  "controlStyles[76].styles[0]": "CornerRadius:=$ElementCornerRadius",
  "controlStyles[77].target": "Windows.UI.Xaml.Controls.Grid#AllListHeading > Microsoft.UI.Xaml.Controls.DropDownButton#ViewSelectionButton > Grid#RootGrid",
  "controlStyles[77].styles[0]": "CornerRadius=$HoverCornerRadius",
  "controlStyles[77].styles[1]": "Margin=-12,0,12,0",
  "controlStyles[78].target": "MenuFlyoutItem",
  "controlStyles[78].styles[0]": "CornerRadius:=$HoverCornerRadius",
  "controlStyles[78].styles[1]": "Margin=4,0,4,0",
  "controlStyles[79].target": "ToggleMenuFlyoutItem",
  "controlStyles[79].styles[0]": "CornerRadius:=$HoverCornerRadius",
  "controlStyles[79].styles[1]": "Margin=4,0,4,0"
}
```
</details>
