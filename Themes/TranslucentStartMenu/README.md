# TranslucentStartMenu theme for Windows 11 Start Menu Styler

A theme with a clear view of the Start menu acrylic background.

**Author**: [Undisputed00x](https://github.com/Undisputed00x)

![Screenshot](screenshot.png)

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

### Redesigned Start menu

A variant for the [redesigned Windows 11 Start menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/) that is slowly rolling out in the 25H2 update.

<details>
<summary>Content to import (click to expand)</summary>

```json
{
  "controlStyles[0].target": "Border#AcrylicBorder",
  "controlStyles[0].styles[0]": "Background:=$CommonBgBrush",
  "controlStyles[0].styles[1]": "BorderThickness=0",
  "controlStyles[0].styles[2]": "CornerRadius=15",
  "controlStyles[1].target": "Border#AcrylicOverlay",
  "controlStyles[1].styles[0]": "Visibility=Collapsed",
  "controlStyles[2].target": "Border#BorderElement",
  "controlStyles[2].styles[0]": "Background:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#15000000\"/>",
  "controlStyles[2].styles[1]": "BorderThickness=0",
  "controlStyles[2].styles[2]": "CornerRadius=10",
  "controlStyles[3].target": "MenuFlyoutPresenter > Border",
  "controlStyles[3].styles[0]": "Background:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#22000000\"/>",
  "controlStyles[3].styles[1]": "BorderThickness=1",
  "controlStyles[4].target": "Border#AppBorder",
  "controlStyles[4].styles[0]": "Background:=$CommonBgBrush",
  "controlStyles[4].styles[1]": "BorderThickness=0",
  "controlStyles[4].styles[2]": "CornerRadius=15",
  "controlStyles[5].target": "Border#AccentAppBorder",
  "controlStyles[5].styles[0]": "Background:=$CommonBgBrush",
  "controlStyles[5].styles[1]": "BorderThickness=0",
  "controlStyles[5].styles[2]": "CornerRadius=15",
  "controlStyles[6].target": "Border#LayerBorder",
  "controlStyles[6].styles[0]": "Visibility=Collapsed",
  "controlStyles[7].target": "Border#TaskbarSearchBackground",
  "controlStyles[7].styles[0]": "Background:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#15000000\"/>",
  "controlStyles[7].styles[1]": "BorderThickness=0",
  "controlStyles[7].styles[2]": "CornerRadius=10",
  "controlStyles[8].target": "Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > Border",
  "controlStyles[8].styles[0]": "Background@Normal:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.2\"/>",
  "controlStyles[8].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.3\"/>",
  "controlStyles[8].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[8].styles[3]": "Background@Pressed:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.3\"/>",
  "controlStyles[8].styles[4]": "BorderBrush@Pressed:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[9].target": "Button#ShowAllAppsButton > ContentPresenter@CommonStates",
  "controlStyles[9].styles[0]": "Background@Normal:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#15C0C0C0\"/>",
  "controlStyles[9].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.5\"/>",
  "controlStyles[9].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[9].styles[3]": "BorderThickness=1",
  "controlStyles[10].target": "StartMenu.SearchBoxToggleButton > Grid > Border#BorderElement",
  "controlStyles[10].styles[0]": "BorderBrush:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[10].styles[1]": "BorderThickness=1",
  "controlStyles[11].target": "StartDocked.NavigationPaneButton#UserTileButton > Grid@CommonStates > Border",
  "controlStyles[11].styles[0]": "Background@Normal:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.2\"/>",
  "controlStyles[11].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.5\"/>",
  "controlStyles[11].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.8\"/>",
  "controlStyles[11].styles[3]": "BorderThickness=1",
  "controlStyles[12].target": "StartDocked.AppListViewItem > Grid@CommonStates > Border",
  "controlStyles[12].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.45\"/>",
  "controlStyles[12].styles[1]": "BorderBrush:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.7\"/>",
  "controlStyles[12].styles[2]": "BorderThickness=1",
  "controlStyles[12].styles[3]": "Margin@Normal=4",
  "controlStyles[13].target": "StartDocked.NavigationPaneButton#PowerButton > Grid@CommonStates > Border",
  "controlStyles[13].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.45\"/>",
  "controlStyles[13].styles[1]": "BorderBrush:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.7\"/>",
  "controlStyles[13].styles[2]": "BorderThickness=1",
  "controlStyles[13].styles[3]": "Margin@Normal=4",
  "controlStyles[14].target": "ToolTip > ContentPresenter#LayoutRoot",
  "controlStyles[14].styles[0]": "Background:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#22000000\"/>",
  "controlStyles[15].target": "Border#dropshadow",
  "controlStyles[15].styles[0]": "CornerRadius=16",
  "controlStyles[15].styles[1]": "Margin=-1",
  "controlStyles[16].target": "Border#StartDropShadow",
  "controlStyles[16].styles[0]": "CornerRadius=15",
  "controlStyles[16].styles[1]": "Margin=-1",
  "controlStyles[17].target": "Grid#TopLevelSuggestionsRoot",
  "controlStyles[17].styles[0]": "Visibility=Collapsed",
  "controlStyles[18].target": "TextBlock#Text",
  "controlStyles[18].styles[0]": "Foreground=White",
  "controlStyles[19].target": "Microsoft.UI.Xaml.Controls.DropDownButton > Grid#RootGrid",
  "controlStyles[19].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.3\"/>",
  "controlStyles[19].styles[1]": "BorderBrush:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.6\"/>",
  "controlStyles[19].styles[2]": "BorderThickness=1",
  "controlStyles[20].target": "Button > Grid@CommonStates > Border",
  "controlStyles[20].styles[0]": "Background@Normal:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.2\"/>",
  "controlStyles[20].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.3\"/>",
  "controlStyles[20].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.6\"/>",
  "controlStyles[20].styles[3]": "BorderThickness=1",
  "controlStyles[21].target": "DropDownButton",
  "controlStyles[21].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.2\"/>",  
  "controlStyles[22].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0\"/>",
  "controlStyles[22].target": "Button#Header > Border#Border@CommonStates",
  "controlStyles[22].styles[1]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.6\"/>",
  "controlStyles[22].styles[2]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.8\"/>",
  "controlStyles[23].target": "StartMenu.FolderModal > Grid > Border",
  "controlStyles[23].styles[0]": "Background:=$CommonBgBrush",
  "controlStyles[23].styles[1]": "BorderBrush:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.8\"/>",
  "controlStyles[23].styles[2]": "BorderThickness=1",
  "controlStyles[24].target": "ListViewItem > Grid#ContentBorder@CommonStates",
  "controlStyles[24].styles[0]": "BorderBrush:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.8\"/>",
  "controlStyles[24].styles[1]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[24].styles[2]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0\"/>",
  "controlStyles[24].styles[3]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.9\"/>",
  "controlStyles[24].styles[4]": "BorderThickness=1",
  "controlStyles[24].styles[5]": "CornerRadius=5",
  "styleConstants[0]": "CommonBgBrush=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#25323232\"/>"
}
```
</details>

### Classic Start menu

<details>
<summary>Content to import (click to expand)</summary>

```json
{
  "controlStyles[0].target": "Border#AcrylicBorder",
  "controlStyles[0].styles[0]": "Background:=$CommonBgBrush",
  "controlStyles[0].styles[1]": "BorderThickness=0",
  "controlStyles[0].styles[2]": "CornerRadius=15",
  "controlStyles[1].target": "Border#AcrylicOverlay",
  "controlStyles[1].styles[0]": "Visibility=Collapsed",
  "controlStyles[2].target": "Border#BorderElement",
  "controlStyles[2].styles[0]": "Background:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#15000000\"/>",
  "controlStyles[2].styles[1]": "BorderThickness=0",
  "controlStyles[2].styles[2]": "CornerRadius=10",
  "controlStyles[3].target": "Grid#ShowMoreSuggestions",
  "controlStyles[3].styles[0]": "Visibility=Collapsed",
  "controlStyles[4].target": "Grid#SuggestionsParentContainer",
  "controlStyles[4].styles[0]": "Visibility=Collapsed",
  "controlStyles[5].target": "Grid#TopLevelSuggestionsListHeader",
  "controlStyles[5].styles[0]": "Visibility=Collapsed",
  "controlStyles[6].target": "StartMenu.PinnedList",
  "controlStyles[6].styles[0]": "Height=504",
  "controlStyles[7].target": "MenuFlyoutPresenter > Border",
  "controlStyles[7].styles[0]": "Background:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#00000000\"/>",
  "controlStyles[7].styles[1]": "BorderThickness=0",
  "controlStyles[8].target": "Border#AppBorder",
  "controlStyles[8].styles[0]": "Background:=$CommonBgBrush",
  "controlStyles[8].styles[1]": "BorderThickness=0",
  "controlStyles[8].styles[2]": "CornerRadius=15",
  "controlStyles[9].target": "Border#AccentAppBorder",
  "controlStyles[9].styles[0]": "Background:=$CommonBgBrush",
  "controlStyles[9].styles[1]": "BorderThickness=0",
  "controlStyles[9].styles[2]": "CornerRadius=15",
  "controlStyles[10].target": "Border#LayerBorder",
  "controlStyles[10].styles[0]": "Visibility=Collapsed",
  "controlStyles[11].target": "Border#TaskbarSearchBackground",
  "controlStyles[11].styles[0]": "Background:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#15000000\"/>",
  "controlStyles[11].styles[1]": "BorderThickness=0",
  "controlStyles[11].styles[2]": "CornerRadius=10",
  "controlStyles[12].target": "Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > Border",
  "controlStyles[12].styles[0]": "Background@Normal:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"0\" Opacity=\"0.2\"/>",
  "controlStyles[12].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.3\"/>",
  "controlStyles[12].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[12].styles[3]": "Margin=1",
  "controlStyles[12].styles[4]": "Background@Pressed:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.3\"/>",
  "controlStyles[12].styles[5]": "BorderBrush@Pressed:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[13].target": "Button#ShowAllAppsButton > ContentPresenter@CommonStates",
  "controlStyles[13].styles[0]": "Background@Normal:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#15C0C0C0\"/>",
  "controlStyles[13].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.5\"/>",
  "controlStyles[13].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[13].styles[3]": "BorderThickness=1",
  "controlStyles[14].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Grid > Border#BorderElement",
  "controlStyles[14].styles[0]": "BorderBrush:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[14].styles[1]": "BorderThickness=1",
  "controlStyles[15].target": "StartDocked.NavigationPaneButton#UserTileButton > Grid@CommonStates > Border",
  "controlStyles[15].styles[0]": "Background@Normal:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"0\" Opacity=\"0.2\"/>",
  "controlStyles[15].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.5\"/>",
  "controlStyles[15].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.8\"/>",
  "controlStyles[15].styles[3]": "BorderThickness=1",
  "controlStyles[16].target": "StartDocked.AppListViewItem > Grid@CommonStates > Border",
  "controlStyles[16].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.45\"/>",
  "controlStyles[16].styles[1]": "BorderBrush:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.7\"/>",
  "controlStyles[16].styles[2]": "BorderThickness=1",
  "controlStyles[16].styles[3]": "Margin@Normal=4",
  "controlStyles[17].target": "StartDocked.NavigationPaneButton#PowerButton > Grid@CommonStates > Border",
  "controlStyles[17].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.45\"/>",
  "controlStyles[17].styles[1]": "BorderBrush:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.7\"/>",
  "controlStyles[17].styles[2]": "BorderThickness=1",
  "controlStyles[17].styles[3]": "Margin@Normal=4",
  "controlStyles[18].target": "ToolTip > ContentPresenter#LayoutRoot",
  "controlStyles[18].styles[0]": "Background:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#00000000\"/>",
  "controlStyles[19].target": "StartDocked.AllAppsGridListViewItem > Grid@CommonStates > Border",
  "controlStyles[19].styles[0]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.8\"/>",
  "controlStyles[19].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.55\"/>",
  "controlStyles[19].styles[2]": "BorderThickness=1",
  "controlStyles[20].target": "Button#CloseAllAppsButton > ContentPresenter@CommonStates",
  "controlStyles[20].styles[0]": "Background@Normal:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#15C0C0C0\"/>",
  "controlStyles[20].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.5\"/>",
  "controlStyles[20].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[20].styles[3]": "BorderThickness=1",
  "controlStyles[21].target": "StartDocked.AllAppsZoomListViewItem > Grid@CommonStates > Border",
  "controlStyles[21].styles[0]": "Background@Normal:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"0\" Opacity=\"0.2\"/>",
  "controlStyles[21].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.3\"/>",
  "controlStyles[21].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.6\"/>",
  "controlStyles[22].target": "Border#dropshadow",
  "controlStyles[22].styles[0]": "CornerRadius=16",
  "controlStyles[22].styles[1]": "Margin=-1",
  "controlStyles[23].target": "Border#DropShadow",
  "controlStyles[23].styles[0]": "CornerRadius=15",
  "controlStyles[24].target": "StartDocked.AllAppsGridListViewItem > Grid#ContentBorder@CommonStates",
  "controlStyles[24].styles[0]": "Background@PointerOver:=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#15C0C0C0\"/>",
  "controlStyles[24].styles[1]": "CornerRadius=4",
  "styleConstants[0]": "CommonBgBrush=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#25323232\"/>"
}
```
</details>
