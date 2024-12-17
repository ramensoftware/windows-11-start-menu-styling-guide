# TranslucentStartMenu theme for Windows 11 Start Menu Styler

A theme with a clear view of start menu acrylic background.

**Author**: [Undisputed00x](https://github.com/Undisputed00x)

![Screenshot](screenshot.png)

## Theme selection

The theme is integrated into the mod, and can be simply selected from the mod's
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
  "controlStyles[0].target": "Border#AcrylicBorder",
  "controlStyles[0].styles[0]": "Background:=<AcrylicBrush TintColor=\"Black\" TintLuminosityOpacity=\"0.12\" TintOpacity=\"0\" Opacity=\"1\" FallbackColor=\"#70262626\"/>",
  "controlStyles[0].styles[1]": "BorderThickness=0",
  "controlStyles[0].styles[2]": "CornerRadius=15",
  "controlStyles[1].target": "Border#AcrylicOverlay",
  "controlStyles[1].styles[0]": "Visibility=Collapsed",
  "controlStyles[2].target": "Border#BorderElement",
  "controlStyles[2].styles[0]": "Background:=<AcrylicBrush TintLuminosityOpacity=\"0.03\" TintOpacity=\"0\" Opacity=\"1\" FallbackColor=\"#70262626\"/>",
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
  "controlStyles[7].target": "MenuFlyoutPresenter",
  "controlStyles[7].styles[0]": "Background:=<AcrylicBrush TintColor=\"Black\" TintLuminosityOpacity=\"0.12\" TintOpacity=\"0\" Opacity=\"1\" FallbackColor=\"#70262626\"/>",
  "controlStyles[7].styles[1]": "BorderThickness=0",
  "controlStyles[8].target": "Border#AppBorder",
  "controlStyles[8].styles[0]": "Background:=<AcrylicBrush TintColor=\"Black\" TintLuminosityOpacity=\"0.12\" TintOpacity=\"0\" Opacity=\"1\" FallbackColor=\"#70262626\"/>",
  "controlStyles[8].styles[1]": "BorderThickness=0",
  "controlStyles[8].styles[2]": "CornerRadius=15",
  "controlStyles[9].target": "Border#AccentAppBorder",
  "controlStyles[9].styles[0]": "Background:=<AcrylicBrush TintColor=\"Black\" TintLuminosityOpacity=\"0.12\" TintOpacity=\"0\" Opacity=\"1\" FallbackColor=\"#70262626\"/>",
  "controlStyles[9].styles[1]": "BorderThickness=0",
  "controlStyles[9].styles[2]": "CornerRadius=15",
  "controlStyles[10].target": "Border#LayerBorder",
  "controlStyles[10].styles[0]": "Visibility=Collapsed",
  "controlStyles[11].target": "Border#TaskbarSearchBackground",
  "controlStyles[11].styles[0]": "Background:=<AcrylicBrush TintColor=\"Transparent\" TintLuminosityOpacity=\"0.03\" TintOpacity=\"0\" Opacity=\"1\" FallbackColor=\"#70262626\"/>",
  "controlStyles[11].styles[1]": "BorderThickness=0",
  "controlStyles[11].styles[2]": "CornerRadius=10",
  "controlStyles[12].target": "Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > Border",
  "controlStyles[12].styles[0]": "Background@Normal:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"0\" Opacity=\"0.2\"/>",
  "controlStyles[12].styles[1]": "Background@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.3\"/>",
  "controlStyles[12].styles[2]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[12].styles[3]": "Margin=1",
  "controlStyles[13].target": "Button#ShowAllAppsButton > ContentPresenter@CommonStates",
  "controlStyles[13].styles[0]": "Background@Normal:=<AcrylicBrush TintColor=\"Transparent\" TintLuminosityOpacity=\"0.05\" TintOpacity=\"1\" Opacity=\"1\" FallbackColor=\"#70262626\"/>",
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
  "controlStyles[18].styles[0]": "Background:=<AcrylicBrush TintColor=\"Transparent\" TintOpacity=\"0\" TintLuminosityOpacity=\"0\" Opacity=\"1\" FallbackColor=\"#A0262626\"/>",
  "controlStyles[19].target": "StartDocked.AllAppsGridListViewItem > Grid@CommonStates > Border",
  "controlStyles[19].styles[0]": "BorderBrush@PointerOver:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\"/>",
  "controlStyles[19].styles[1]": "BorderThickness=1",
  "controlStyles[20].target": "Button#CloseAllAppsButton > ContentPresenter@CommonStates",
  "controlStyles[20].styles[0]": "Background@Normal:=<AcrylicBrush TintColor=\"Transparent\" TintLuminosityOpacity=\"0.05\" TintOpacity=\"1\" Opacity=\"1\" FallbackColor=\"#70262626\"/>",
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
  "controlStyles[23].styles[0]": "CornerRadius=15"
}
```
</details>

## TranslucentSearchMenu Support

This section is only relevant for older versions of Windows 11 Start Menu
Styler. Versions 1.2 and newer automatically apply the styles to the search
menu.

<details>
<summary>Expand</summary>

To add this feature go to Start Menu Styler > **Advanced** > **Custom process
inclusion list**, add `SearchHost.exe` to the process list and click save.

![TranslucentSearchMenu gif](TranslucentSearchMenu.gif)
</details>
