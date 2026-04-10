# Borderless theme for Windows 11 Start Menu Styler

A theme for the Start menu that removes the drop shadow and borders (thus the name), the greyish tint in Dark Mode, and the search bar and suggestions (on the old Start Menu).
Updated to include Search Popout as well (Search Bar still perserved).

**Author**: [Ali Cool](https://github.com/AliCool412)

![Screenshot](screenshot.png)
<!--
## Theme selection

The theme is integrated into the mod and can be selected directly from the mod's
settings:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Settings" tab.
* Select the theme and save the settings.

## Manual installation

The theme styles can also be imported manually. To do that, follow these steps:
-->
## Manual installation

The theme styles can be imported manually. To do that, follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Advanced" tab.
* Copy the content below to the text box under "Mod settings" and click "Save".

<details>
<summary>Content to import (click to expand)</summary>

```yaml
controlStyles:
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Grid#NoTopLevelSuggestionsText
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsContainer
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions
    styles:
      - Visibility=Collapsed
  - target: Border#DropShadow
    styles:
      - Opacity=0
  - target: Border#AcrylicBorder
    styles:
      - BorderThickness=0
  - target: Windows.UI.Xaml.Shapes.Rectangle
    styles:
      - Visibility=Collapsed
  - target: StartDocked.SearchBoxToggleButton#StartMenuSearchBox
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.TextBlock#ShowAllAppsButtonText
    styles:
      - Text=All Apps
  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.StackPanel > Windows.UI.Xaml.Controls.TextBlock
    styles:
      - Text=Back
  - target: Windows.UI.Xaml.Controls.TextBlock#UserTileNameText
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Button#ShowAllAppsButton
    styles:
      - Height=30
      - Width=Auto
  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton
    styles:
      - Height=30
      - Width=Auto
  - target: Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText
    styles:
      - Text=Start
      - FontSize=20
  - target: Windows.UI.Xaml.Controls.TextBlock#AllAppsHeading
    styles:
      - Text=All Apps
      - FontSize=20
  - target: StartDocked.NavigationPaneButton#UserTileButton > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ContentPresenter
    styles:
      - Padding=3,0,3,0
  - target: Windows.UI.Xaml.Controls.Button#ShowAllAppsButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.StackPanel > Windows.UI.Xaml.Controls.FontIcon
    styles:
      - Glyph=
      - FontSize=16
  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.StackPanel > Windows.UI.Xaml.Controls.FontIcon
    styles:
      - Glyph=
      - FontSize=10
  - target: Windows.UI.Xaml.Controls.Border#AcrylicOverlay
    styles:
      - Opacity=0
  - target: Windows.UI.Xaml.Controls.Border#StartDropShadow
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Grid#MainContent > Windows.UI.Xaml.Controls.Grid > StartMenu.SearchBoxToggleButton#SearchBoxToggleButton
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.TextBlock#AllListHeadingText
    styles:
      - Text=All Apps
      - FontSize=20
  - target: Microsoft.UI.Xaml.Controls.DropDownButton#ViewSelectionButton > Windows.UI.Xaml.Controls.Grid#RootGrid > ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.TextBlock
    styles:
      - Text=
      - FontFamily=Segoe Fluent Icons
      - FontSize=16
  - target: Windows.UI.Xaml.Controls.TextBlock#ShowMorePinnedButtonText
    styles:
      - Text=
      - FontFamily=Segoe Fluent Icons
      - FontSize=16
  - target: Windows.UI.Xaml.Controls.Border#RightCompanionDropShadow
    styles:
      - Visibility=Collapsed
  - target: Border#RootGridDropShadow
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Windows.UI.Xaml.Controls.Border > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter
    styles:
      - CornerRadius=2
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Border > ContentPresenter#ContentPresenter > FontIcon > Grid > TextBlock
    styles:
      - FontSize=16
      - Text=
  - target: Frame#StartFrame
    styles:
      - Margin=0,-64,0,0
  - target: Grid#MainMenu > Grid#MainContent > Grid
    styles:
      - Grid.Row=3
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Border > ContentPresenter
    styles:
      - Height=40
      - Width=40
      - CornerRadius=4
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Border
    styles:
      - Height=40
      - Width=40
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion
    styles:
      - Height=40
      - Width=40
      - Margin=16,0,-16,0
  - target: Windows.UI.Xaml.Controls.Border#dropshadow
    styles:
      - Opacity=0
  - target: Windows.UI.Xaml.Controls.Border#LayerBorder
    styles:
      - Opacity=0
  - target: Windows.UI.Xaml.Controls.Border#AppBorder
    styles:
      - BorderThickness=0
```
</details>
