# Windows11_Metro10Minimal theme for Windows 11 Start Menu Styler

A minimalist version of Windows11_Metro10.

**Author**: [Y2K4](https://github.com/y2k04)

**Author of base theme**: [Ian Div](https://github.com/iandiv)

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

<details>
<summary>Content to import (click to expand)</summary>

```json
{
  "controlStyles[0].target": "Windows.UI.Xaml.Controls.Grid#UndockedRoot",
  "controlStyles[0].styles[0]": "MaxWidth=0",
  "controlStyles[0].styles[1]": "Margin=0",
  "controlStyles[1].target": "Windows.UI.Xaml.Controls.Grid#AllAppsRoot",
  "controlStyles[1].styles[0]": "Visibility=Visible",
  "controlStyles[1].styles[1]": "Width=540",
  "controlStyles[1].styles[2]": "Margin=-1000,0,0,0",
  "controlStyles[2].target": "StartDocked.StartSizingFrame",
  "controlStyles[2].styles[0]": "MinWidth=460",
  "controlStyles[2].styles[1]": "MaxWidth=460",
  "controlStyles[2].styles[2]": "MaxHeight=670",
  "controlStyles[3].target": "Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions",
  "controlStyles[3].styles[0]": "Visibility=Collapsed",
  "controlStyles[4].target": "Windows.UI.Xaml.Controls.Button#ShowAllAppsButton",
  "controlStyles[4].styles[0]": "Visibility=Collapsed",
  "controlStyles[5].target": "StartDocked.AllAppsGridListView#AppsList",
  "controlStyles[5].styles[0]": "Padding=90,3,6,16",
  "controlStyles[6].target": "Grid#AllAppsPaneHeader",
  "controlStyles[6].styles[0]": "Visibility=Collapsed",
  "controlStyles[7].target": "StartDocked.NavigationPaneView#NavigationPane",
  "controlStyles[7].styles[0]": "Margin=30,0,30,0",
  "controlStyles[8].target": "StartDocked.AppListView#NavigationPanePlacesListView",
  "controlStyles[8].styles[0]": "FlowDirection=1",
  "controlStyles[9].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox",
  "controlStyles[9].styles[0]": "Margin=23,-101,23,14",
  "controlStyles[10].target": "StartDocked.SearchBoxToggleButton",
  "controlStyles[10].styles[0]": "Height=0",
  "controlStyles[11].target": "Rectangle[4]",
  "controlStyles[11].styles[0]": "Margin=0,-20,0,0",
  "controlStyles[12].target": "StartMenu.ExpandedFolderList > Grid > Grid > Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager",
  "controlStyles[12].styles[0]": "Margin=-20,0,20,0",
  "controlStyles[13].target": "StartMenu.StartInnerFrame",
  "controlStyles[13].styles[0]": "Visibility=Collapsed",
  "controlStyles[14].target": "Grid#RootContent",
  "controlStyles[14].styles[0]": "MinWidth=460",
  "controlStyles[15].target": "Grid#InnerContent",
  "controlStyles[15].styles[0]": "Margin=0,12,0,0",
  "controlStyles[16].target": "Border#AcrylicBorder",
  "controlStyles[16].styles[0]": "Background:=<AcrylicBrush TintColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" FallbackColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" TintOpacity=\"0\" TintLuminosityOpacity=\".85\" Opacity=\"1\"/>",
  "controlStyles[16].styles[1]": "BorderBrush:=<AcrylicBrush TintColor=\"{ThemeResource SurfaceStrokeColorDefault}\" FallbackColor=\"{ThemeResource SurfaceStrokeColorDefault}\" TintOpacity=\"0\" TintLuminosityOpacity=\".25\" Opacity=\"1\"/>",
  "controlStyles[16].styles[2]": "BorderThickness=1",
  "controlStyles[17].target": "Border#AppBorder",
  "controlStyles[17].styles[0]": "Background:=<AcrylicBrush TintColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" FallbackColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" TintOpacity=\"0\" TintLuminosityOpacity=\".85\" Opacity=\"1\"/>",
  "controlStyles[17].styles[1]": "BorderBrush:=<AcrylicBrush TintColor=\"{ThemeResource SurfaceStrokeColorDefault}\" FallbackColor=\"{ThemeResource SurfaceStrokeColorDefault}\" TintOpacity=\"0\" TintLuminosityOpacity=\".25\" Opacity=\"1\"/>",
  "controlStyles[18].target": "Border#LayerBorder",
  "controlStyles[18].styles[0]": "Visibility=1"
}
```
</details>
