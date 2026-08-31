# SideBySide2_Tweaks theme for Windows 11 Start Menu Styler

A modified version of the existing theme [SideBySide2](https://github.com/ramensoftware/windows-11-start-menu-styling-guide/tree/main/Themes/SideBySide2) by [Pyxisynth](https://github.com/dreamsynth) with the following changes:
- Removed Recommended section
- Removed buggy Semantic zoom button
- Removed headers
- Layout/spacing adjustments

**Author**: [Nuzza](https://github.com/Nuzza)

**Author of base theme**: [Pyxisynth](https://github.com/dreamsynth)

![screenshot](https://github.com/user-attachments/assets/e9fe86d1-721c-4ca4-9186-a838a1a96374)

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
  "resourceVariables[0].variableKey": "",
  "resourceVariables[0].value": "",

  "controlStyles[0].target": "StartDocked.StartSizingFrame",
  "controlStyles[0].styles[0]": "MinWidth=776",
  "controlStyles[0].styles[1]": "MaxWidth=776",

  "controlStyles[1].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox",
  "controlStyles[1].styles[0]": "Margin=23,1,23,14",

  "controlStyles[2].target": "Windows.UI.Xaml.Controls.Grid#AllAppsRoot",
  "controlStyles[2].styles[0]": "Visibility=Visible",
  "controlStyles[2].styles[1]": "Width=340",
  "controlStyles[2].styles[2]": "Transform3D:=<CompositeTransform3D TranslateX=\"-1070\" />",

  "controlStyles[3].target": "Windows.UI.Xaml.Controls.Grid#AllAppsPaneHeader",
  "controlStyles[3].styles[0]": "Margin=97,0,0,0",
  "controlStyles[3].styles[1]": "Visibility=Collapsed",

  "controlStyles[4].target": "Windows.UI.Xaml.Controls.Button#CloseAllAppsButton",
  "controlStyles[4].styles[0]": "Visibility=1",

  "controlStyles[5].target": "Windows.UI.Xaml.Controls.Button#ShowAllAppsButton",
  "controlStyles[5].styles[0]": "Visibility=1",

  "controlStyles[6].target": "StartDocked.AllAppsGridListView#AppsList",
  "controlStyles[6].styles[0]": "Padding=48,3,-36,16",

  "controlStyles[7].target": "Windows.UI.Xaml.Controls.Grid#UndockedRoot",
  "controlStyles[7].styles[0]": "Visibility=Visible",
  "controlStyles[7].styles[1]": "Width=510",
  "controlStyles[7].styles[2]": "MinHeight=585",
  "controlStyles[7].styles[3]": "Margin=264,0,0,0",

  "controlStyles[8].target": "StartMenu.PinnedList#StartMenuPinnedList > Windows.UI.Xaml.Controls.Grid#Root",
  "controlStyles[8].styles[0]": "Padding=0,0,0,0",

  "controlStyles[9].target": "Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText",
  "controlStyles[9].styles[0]": "Margin=-32,0,32,0",
  "controlStyles[9].styles[1]": "Visibility=Collapsed",

  "controlStyles[10].target": "Windows.UI.Xaml.Controls.GridView#PinnedList",
  "controlStyles[10].styles[0]": "MinHeight=567",
  "controlStyles[10].styles[1]": "Margin=0,0,0,0",

  "controlStyles[11].target": "StartMenu.PinnedList#StartMenuPinnedList",
  "controlStyles[11].styles[0]": "MinHeight=567",
  "controlStyles[11].styles[1]": "Margin=0,-40,0,0",

  "controlStyles[12].target": "Windows.UI.Xaml.Controls.GridViewItem",
  "controlStyles[12].styles[0]": "MaxHeight=81",

  "controlStyles[13].target": "Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions",
  "controlStyles[13].styles[0]": "Visibility=Collapsed",

  "controlStyles[14].target": "Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsContainer",
  "controlStyles[14].styles[0]": "Visibility=Collapsed",

  "controlStyles[15].target": "Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader",
  "controlStyles[15].styles[0]": "Margin=31,-3,12,0",
  "controlStyles[15].styles[1]": "Visibility=Collapsed",

  "controlStyles[16].target": "Windows.UI.Xaml.Controls.Grid#NoTopLevelSuggestionsText",
  "controlStyles[16].styles[0]": "Margin=31,0,63,0",
  "controlStyles[16].styles[1]": "Visibility=Collapsed",

  "controlStyles[17].target": "StartDocked.NavigationPaneView#NavigationPane",
  "controlStyles[17].styles[0]": "FlowDirection=1",
  "controlStyles[17].styles[1]": "Margin=10,0,10,0",

  "controlStyles[18].target": "StartDocked.PowerOptionsView#PowerButton",
  "controlStyles[18].styles[0]": "FlowDirection=0",

  "controlStyles[19].target": "Windows.UI.Xaml.Controls.ItemsStackPanel > Windows.UI.Xaml.Controls.ListViewItem",
  "controlStyles[19].styles[0]": "FlowDirection=0",

  "controlStyles[20].target": "StartDocked.LauncherFrame > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Grid#RootContent > Windows.UI.Xaml.Controls.Grid#MainContent > Windows.UI.Xaml.Controls.Grid#InnerContent > Windows.UI.Xaml.Shapes.Rectangle",
  "controlStyles[20].styles[0]": "Margin=67,7,0,21",

  "controlStyles[21].target": "Windows.UI.Xaml.Controls.FlyoutPresenter",
  "controlStyles[21].styles[0]": "Margin=-265,-12,0,0"
}
```
</details>
