# SideBySide theme for Windows 11 Start Menu Styler

**Author**: [kaoshipaws](https://k4oshi.top/)

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
  "theme": "",
  "controlStyles[0].target": "Grid#UndockedRoot",
  "resourceVariables[0].variableKey": "",
  "resourceVariables[0].value": "",
  "controlStyles[0].styles[0]": "MaxWidth=700",
  "controlStyles[0].styles[1]": "Margin=0,0,300,0",
  "controlStyles[1].target": "Grid#AllAppsRoot",
  "controlStyles[1].styles[0]": "Visibility=Visible",
  "controlStyles[1].styles[1]": "Width=390",
  "controlStyles[1].styles[2]": "Margin=-590,0,590,0",
  "controlStyles[1].styles[3]": "Padding=0,0,40,0",
  "controlStyles[2].target": "Windows.UI.Xaml.Controls.Button#CloseAllAppsButton",
  "controlStyles[2].styles[0]": "Visibility=Collapsed",
  "controlStyles[3].target": "StartDocked.StartSizingFrame",
  "controlStyles[3].styles[1]": "MaxWidth=860",
  "controlStyles[4].target": "Windows.UI.Xaml.Controls.Button#ShowAllAppsButton",
  "controlStyles[4].styles[0]": "Visibility=Collapsed",
  "controlStyles[5].target": "Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText",
  "controlStyles[5].styles[0]": "Margin=-22,0,0,0",
  "controlStyles[6].target": "Grid#TopLevelSuggestionsListHeader",
  "controlStyles[6].styles[0]": "Margin=45,25,0,0",
  "controlStyles[7].target": "Windows.UI.Xaml.Controls.Primitives.ScrollBar[1]",
  "controlStyles[7].styles[0]": "Margin=0,0,6,0",
  "controlStyles[8].target": "Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager",
  "controlStyles[8].styles[0]": "Margin=-8,0,8,0",
  "controlStyles[3].styles[0]": "MinWidth=860",
  "controlStyles[9].target": "Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem",
  "controlStyles[9].styles[0]": "MaxWidth=220",
  "controlStyles[9].styles[1]": "MinWidth=85",
  "controlStyles[9].styles[2]": "MaxHeight=120",
  "controlStyles[10].target": "StartMenu.PinnedList#StartMenuPinnedList",
  "controlStyles[10].styles[0]": "Margin=-15,0,5,0",
  "controlStyles[11].target": "Grid#ShowMoreSuggestions",
  "controlStyles[11].styles[0]": "Margin=0,20,0,-20",
  "controlStyles[12].target": "Grid#MoreSuggestionsRoot",
  "controlStyles[12].styles[0]": "Margin=-1,-26,-4,0",
  "controlStyles[13].target": "Windows.UI.Xaml.Controls.FlyoutPresenter[1]",
  "controlStyles[13].styles[0]": "Margin=-10,-10,0,0",
  "controlStyles[14].target": "Windows.UI.Xaml.Controls.FlyoutPresenter > Grid",
  "controlStyles[14].styles[0]": "Margin=-400,0,400,0",
  "controlStyles[15].target": "Windows.UI.Xaml.Controls.TextBlock#MoreSuggestionsListHeaderText",
  "controlStyles[15].styles[0]": "Margin=-40,0,0,0"
}
```
</details>
