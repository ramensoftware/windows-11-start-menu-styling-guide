# SideBySideMinimal theme for Windows 11 Start Menu Styler

**Author**: [Olivia](https://github.com/OliviaIsTyping)

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
  "controlStyles[0].target": "Windows.UI.Xaml.Controls.Grid#UndockedRoot",
  "controlStyles[0].styles[0]": "Visibility=Visible",
  "controlStyles[0].styles[1]": "Width=348",
  "controlStyles[0].styles[2]": "Margin=132,-42,-132,0",
  "controlStyles[1].target": "Windows.UI.Xaml.Controls.Grid#AllAppsRoot",
  "controlStyles[1].styles[0]": "Visibility=Visible",
  "controlStyles[1].styles[1]": "Width=320",
  "controlStyles[1].styles[2]": "Margin=-830,-42,830,0",
  "controlStyles[2].target": "Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions",
  "controlStyles[2].styles[0]": "Visibility=Collapsed",
  "controlStyles[3].target": "Windows.UI.Xaml.Controls.Grid#SuggestionsParentContainer",
  "controlStyles[3].styles[0]": "Visibility=Collapsed",
  "controlStyles[4].target": "Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader",
  "controlStyles[4].styles[0]": "Visibility=Collapsed",
  "controlStyles[5].target": "StartDocked.SearchBoxToggleButton",
  "controlStyles[5].styles[0]": "Height=0",
  "controlStyles[5].styles[1]": "Width=0",
  "controlStyles[6].target": "Windows.UI.Xaml.Controls.Grid#TopLevelRoot > Windows.UI.Xaml.Controls.Border",
  "controlStyles[6].styles[0]": "Visibility=Collapsed",
  "controlStyles[7].target": "Windows.UI.Xaml.Controls.Button#CloseAllAppsButton",
  "controlStyles[7].styles[0]": "Visibility=Collapsed",
  "controlStyles[8].target": "StartDocked.PowerOptionsView",
  "controlStyles[8].styles[0]": "Margin=-575,0,0,0",
  "controlStyles[9].target": "StartDocked.UserTileView",
  "controlStyles[9].styles[0]": "Visibility=Collapsed",
  "controlStyles[10].target": "StartMenu.PinnedList",
  "controlStyles[10].styles[0]": "Height=504",
  "controlStyles[11].target": "StartMenu.ExpandedFolderList > Grid > Border",
  "controlStyles[11].styles[0]": "Margin=-40,0,40,0",
  "controlStyles[11].styles[1]": "Width=325",
  "controlStyles[12].target": "StartMenu.ExpandedFolderList > Grid > Grid",
  "controlStyles[12].styles[0]": "CornerRadius=8",
  "controlStyles[12].styles[1]": "Margin=-85,0,0,0",
  "controlStyles[12].styles[2]": "Width=350",
  "controlStyles[13].target": "StartMenu.ExpandedFolderList > Grid > Grid > Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager",
  "controlStyles[13].styles[0]": "Margin=-15,0,0,0",
  "controlStyles[14].target": "Rectangle[4]",
  "controlStyles[14].styles[0]": "Margin=0,-20,0,0",
  "controlStyles[15].target": "Grid#TopLevelSuggestionsContainer",
  "controlStyles[15].styles[0]": "Visibility=Collapsed",
  "controlStyles[16].target": "StartDocked.AppListView",
  "controlStyles[16].styles[0]": "Margin=38,0,-38,0"
}
```
</details>
