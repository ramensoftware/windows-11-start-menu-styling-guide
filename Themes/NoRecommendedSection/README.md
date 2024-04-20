# NoRecommendedSection theme for Windows 11 Start Menu Styler

![Screenshot](screenshot.png)

## Installation

The easiest way to install this theme is to import its mod settings. To do that,
follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Advanced" tab.
* Copy the content below to the text box under "Mod settings" and click "Save".

<details>
<summary>Content to import (click to expand)</summary>

```json
{
  "controlStyles[0].target": "Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions",
  "controlStyles[0].styles[0]": "Visibility=Collapsed",
  "controlStyles[1].target": "Windows.UI.Xaml.Controls.Grid#SuggestionsParentContainer",
  "controlStyles[1].styles[0]": "Visibility=Collapsed",
  "controlStyles[2].target": "Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader",
  "controlStyles[2].styles[0]": "Visibility=Collapsed",
  "controlStyles[3].target": "StartMenu.PinnedList",
  "controlStyles[3].styles[0]": "Height=504"
}
```
</details>
