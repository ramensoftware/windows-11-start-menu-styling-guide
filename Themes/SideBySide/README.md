# SideBySide theme for Windows 11 Start Menu Styler

**Author**: [kaoshipaws](https://k4oshi.top/) (classic Start menu), [m417z](https://github.com/m417z) (redesigned Start menu)

![Screenshot](screenshot.png)

## Theme selection

The theme is integrated into the mod and can be selected directly from the mod's
settings:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Settings" tab.
* Select the theme and save the settings.

## Manual installation

The theme styles can also be imported manually. To do that, follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Settings" tab and select "Textual mode".
* Copy the content below to the text box and click "Save settings".

### Redesigned Start menu

A variant for the [redesigned Windows 11 Start
menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/)
that is slowly rolling out in the 25H2 update.

<details>
<summary>Content to import (click to expand)</summary>

```yaml
disableNewStartMenuLayout: newLayoutSideBySide
controlStyles:
  - target: Grid#SideBySidePinnedWrapper
    styles:
      - ColumnDefinitions:=<ColumnDefinitionCollection><ColumnDefinition Width="540*"/><ColumnDefinition Width="292*"/></ColumnDefinitionCollection>
  - target: Grid#SideBySidePinnedWrapper > ScrollViewer > Border#Root > Grid > ScrollContentPresenter > ItemsPresenter > ItemsWrapGrid
    styles:
      - Margin=32,0,32,14
  - target: Grid#AllListHeading > TextBlock#AllListHeadingText
    styles:
      - Margin=43,6,12,7
  - target: Grid#AllListHeading > Microsoft.UI.Xaml.Controls.DropDownButton#ViewSelectionButton
    styles:
      - Margin=0,0,32,0
  - target: Grid#TopLevelSuggestionsContainer
    styles:
      - Margin=28,0,0,0
```
</details>

### Classic Start menu

<details>
<summary>Content to import (click to expand)</summary>

```yaml
controlStyles:
  - target: Grid#UndockedRoot
    styles:
      - MaxWidth=700
      - Margin=0,0,300,0
  - target: Grid#AllAppsRoot
    styles:
      - Visibility=Visible
      - Width=320
      - Background:=<AcrylicBrush TintColor="{ThemeResource CardStrokeColorDefaultSolid}" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" TintOpacity="0" TintLuminosityOpacity="1" Opacity="1"/>
      - RenderTransform:=<TranslateTransform X="269"/>
  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton
    styles:
      - Visibility=Collapsed
  - target: StartDocked.StartSizingFrame
    styles:
      - MaxWidth=1874
  - target: StartDocked.LauncherFrame > Grid#RootGrid
    styles:
      - MinWidth=860
      - MaxWidth=860
  - target: StartDocked.LauncherFrame > Grid#RootPanel > Grid#RootGrid
    styles:
      - MinWidth=860
      - MaxWidth=860
  - target: Windows.UI.Xaml.Controls.Button#ShowAllAppsButton
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText
    styles:
      - Margin=-22,-5,0,0
  - target: Grid#TopLevelSuggestionsListHeader
    styles:
      - Margin=45,-15,0,0
  - target: StartDocked.AllAppsGridListView > Windows.UI.Xaml.Controls.ScrollViewer > Border > Grid > Windows.UI.Xaml.Controls.Primitives.ScrollBar
    styles:
      - Margin=-8,0,8,2
  - target: Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager
    styles:
      - Margin=-8,0,8,0
  - target: Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem
    styles:
      - MaxWidth=185
      - MinWidth=85
  - target: StartMenu.PinnedList#StartMenuPinnedList
    styles:
      - Margin=-15,0,5,0
  - target: Grid#ShowMoreSuggestions
    styles:
      - Margin=0,20,0,-20
  - target: Grid#MoreSuggestionsRoot
    styles:
      - Margin=-1,0,-4,-30
  - target: Windows.UI.Xaml.Controls.TextBlock#MoreSuggestionsListHeaderText
    styles:
      - Margin=-40,0,0,0
  - target: Button#ShowMoreSuggestionsButton
    styles:
      - Margin=0,-58,25,0
  - target: Grid#TopLevelSuggestionsContainer
    styles:
      - Margin=30,-10,30,-60
  - target: Windows.UI.Xaml.Controls.GridViewItem
    styles:
      - Margin=0
  - target: Border#AcrylicOverlay
    styles:
      - Background:=<AcrylicBrush TintColor="{ThemeResource CardStrokeColorDefaultSolid}" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" TintOpacity="0.1" TintLuminosityOpacity="1" Opacity="1"/>
  - target: Windows.UI.Xaml.Controls.SemanticZoom#ZoomControl
    styles:
      - IsZoomOutButtonEnabled=true
  - target: Windows.UI.Xaml.Controls.Button#ZoomOutButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.TextBlock
    styles:
      - Text=
  - target: Windows.UI.Xaml.Controls.Button#ZoomOutButton
    styles:
      - Width=24
      - Height=24
      - FontSize=14
      - CornerRadius=4
      - VerticalAlignment=0
      - Margin=-8,-35,8,0
  - target: Border#LayerBorder
    styles:
      - Background:=<AcrylicBrush TintColor="{ThemeResource CardStrokeColorDefaultSolid}" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" TintOpacity="0.1" TintLuminosityOpacity="1" Opacity="1"/>
```
</details>

## Removing the "Recommended" section

The "Recommended" section can be removed by following these steps:

* Import [the NoRecommendedSection
  theme](https://github.com/ramensoftware/windows-11-start-menu-styling-guide/blob/main/Themes/NoRecommendedSection/README.md)
  using the **Manual installation** instructions.
* Select this theme using the **Theme selection** instructions on this page.
