# TranslucentStartMenu theme for Windows 11 Start Menu Styler

![screenshot](https://github.com/Undisputed00x/windows-11-start-menu-styling-guide/assets/80290008/9fdeb348-2097-487b-adf4-588bc7d2cd75)

A theme with a clear view of start menu acrylic background.

## Manual installation

The theme styles can also be imported manually. To do that, follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Advanced" tab.
* Copy the content below to the text box under "Mod settings" and click "Save".

<details>
<summary>Content to import (click to expand)</summary>

```json
{
  "controlStyles[0].target": "StartDocked.LauncherFrame > Grid#RootGrid > Grid#RootContent > Border#AcrylicBorder",
  "controlStyles[0].styles[0]": "CornerRadius=15",
  "controlStyles[0].styles[1]": "Background:=<AcrylicBrush TintColor=\"Transparent\" TintLuminosityOpacity=\"0\" TintOpacity=\"0\" Opacity=\"1\"/>",
  "controlStyles[0].styles[2]": "BorderThickness=0,0,0,0",
  "controlStyles[1].target": "StartDocked.LauncherFrame > Grid#RootGrid > Grid#RootContent > Grid#MainContent > Border#AcrylicOverlay",
  "controlStyles[1].styles[0]": "Visibility=Collapsed",
  "controlStyles[2].target": "StartDocked.SearchBoxToggleButton > Grid > Border#BorderElement",
  "controlStyles[2].styles[0]": "CornerRadius=10",
  "controlStyles[2].styles[1]": "BorderThickness=0,0,0,0",
  "controlStyles[2].styles[2]": "Background:=<AcrylicBrush TintLuminosityOpacity=\"0.03\" TintOpacity=\"0\" Opacity=\"1\"/>",
  "controlStyles[3].target": "Grid#ShowMoreSuggestions",
  "controlStyles[3].styles[0]": "Visibility=Collapsed",
  "controlStyles[4].target": "Grid#SuggestionsParentContainer",
  "controlStyles[4].styles[0]": "Visibility=Collapsed",
  "controlStyles[5].target": "Grid#TopLevelSuggestionsListHeader",
  "controlStyles[5].styles[0]": "Visibility=Collapsed",
  "controlStyles[6].target": "StartMenu.PinnedList",
  "controlStyles[6].styles[0]": "Height=504",
  "controlStyles[7].target": "Windows.UI.Xaml.Controls.MenuFlyoutPresenter",
  "controlStyles[7].styles[0]": "Background:=<AcrylicBrush TintColor=\"Transparent\" TintLuminosityOpacity=\"0\" TintOpacity=\"0\" Opacity=\"1\"/>",
  "controlStyles[7].styles[1]": "BorderThickness=0,0,0,0"
}
```
</details>
