# SideBySide2 theme for Windows 11 Start Menu Styler

**Author**: [Pyxisynth](https://github.com/dreamsynth) (classic Start menu), [m417z](https://github.com/m417z) (redesigned Start menu)

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
      - ColumnDefinitions:=<ColumnDefinitionCollection><ColumnDefinition Width="292*"/><ColumnDefinition Width="540*"/></ColumnDefinitionCollection>
  - target: GridView#AllAppsGrid > Border > Grid#SideBySidePinnedWrapper > ScrollViewer#ScrollViewer
    styles:
      - Grid.Column=0
  - target: ScrollViewer#SideBySidePinnedScrollViewer
    styles:
      - Grid.Column=1
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
  - target: Grid#NavPanePlaceholder
    styles:
      - Margin=32,0,32,0
  - target: StartDocked.NavigationPaneView#UserControl > Grid#RootPanel
    styles:
      - FlowDirection=1
  - target: StartDocked.PowerOptionsView#PowerButton
    styles:
      - FlowDirection=0
  - target: ItemsStackPanel > ListViewItem
    styles:
      - FlowDirection=0
```
</details>

### Classic Start menu

<details>
<summary>Content to import (click to expand)</summary>

```yaml
controlStyles:
  - target: Windows.UI.Xaml.Controls.Grid#UndockedRoot
    styles:
      - Visibility=Visible
      - Width=510
      - MinHeight=585
      - Margin=264,0,0,0
  - target: Windows.UI.Xaml.Controls.Grid#AllAppsRoot
    styles:
      - Visibility=Visible
      - Width=320
      - RenderTransform:=<TranslateTransform X="-284"/>
  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton
    styles:
      - Visibility=1
  - target: StartDocked.StartSizingFrame
    styles:
      - MaxWidth=1874
  - target: StartDocked.LauncherFrame > Grid#RootGrid
    styles:
      - MinWidth=776
      - MaxWidth=776
  - target: StartDocked.LauncherFrame > Grid#RootPanel > Grid#RootGrid
    styles:
      - MinWidth=776
      - MaxWidth=776
  - target: Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions
    styles:
      - Visibility=0
  - target: Windows.UI.Xaml.Controls.Button#ShowAllAppsButton
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.GridView#RecommendedList > Windows.UI.Xaml.Controls.Border > Windows.UI.Xaml.Controls.ScrollViewer#ScrollViewer > Windows.UI.Xaml.Controls.Border#Root > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter#ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem
    styles:
      - MaxWidth=220
      - MinWidth=220
  - target: StartDocked.AllAppsGridListView#AppsList
    styles:
      - Padding=48,3,-36,16
  - target: Windows.UI.Xaml.Controls.Grid#AllAppsPaneHeader
    styles:
      - Margin=97,0,0,0
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsContainer
    styles:
      - Height=302
  - target: StartDocked.NavigationPaneView#NavigationPane
    styles:
      - FlowDirection=1
      - Margin=30,0,30,0
  - target: StartDocked.PowerOptionsView#PowerButton
    styles:
      - FlowDirection=0
  - target: Windows.UI.Xaml.Controls.ItemsStackPanel > Windows.UI.Xaml.Controls.ListViewItem
    styles:
      - FlowDirection=0
  - target: StartDocked.LauncherFrame > Grid#RootGrid > Grid#RootContent > Grid#MainContent > Grid#InnerContent > StartDocked.SearchBoxToggleButton#StartMenuSearchBox
    styles:
      - Margin=23,1,23,14
  - target: StartDocked.LauncherFrame > Grid#RootPanel > Grid#RootGrid > Grid#RootContent > Grid#MainContent > Grid#InnerContent > StartDocked.SearchBoxToggleButton#StartMenuSearchBox
    styles:
      - Margin=23,1,23,14
  - target: Windows.UI.Xaml.Controls.TextBlock#NoSuggestionsWithoutSettingsLink
    styles:
      - Margin=11,0,48,0
  - target: StartDocked.LauncherFrame > Grid#RootGrid > Grid#RootContent > Grid#MainContent > Grid#InnerContent > Rectangle
    styles:
      - Margin=67,7,0,21
  - target: StartDocked.LauncherFrame > Grid#RootPanel > Grid#RootGrid > Grid#RootContent > Grid#MainContent > Grid#InnerContent > Rectangle
    styles:
      - Margin=67,7,0,21
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
      - Margin=0,0,0,0
      - FontSize=14
      - CornerRadius=4
      - VerticalAlignment=0
      - Transform3D:=<CompositeTransform3D TranslateX="-1" TranslateY="-34"/>
  - target: Windows.UI.Xaml.Controls.ListView#ZoomAppsList
    styles:
      - Padding=86,0,25,0
  - target: StartMenu.PinnedList#StartMenuPinnedList > Windows.UI.Xaml.Controls.Grid#Root
    styles:
      - Padding=0,0,4,0
  - target: Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText
    styles:
      - Margin=-32,0,32,0
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader
    styles:
      - Margin=31,-3,12,0
  - target: Windows.UI.Xaml.Controls.Grid#NoTopLevelSuggestionsText
    styles:
      - Margin=31,0,63,0
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsContainer
    styles:
      - Margin=20,0,0,0
  - target: Windows.UI.Xaml.Controls.ListView#RecommendedList
    styles:
      - Width=490
  - target: Windows.UI.Xaml.Controls.Button#ShowMoreSuggestionsButton
    styles:
      - Margin=0,0,36,2
      - Height=24
  - target: Windows.UI.Xaml.Controls.Button#HideMoreSuggestionsButton
    styles:
      - Margin=0,0,36,2
      - Height=24
  - target: Windows.UI.Xaml.Controls.Grid#MoreSuggestionsRoot > Windows.UI.Xaml.Controls.Grid
    styles:
      - Margin=31,-3,0,0
  - target: Windows.UI.Xaml.Controls.Grid#MoreSuggestionsContainer
    styles:
      - Margin=20,0,0,0
  - target: Windows.UI.Xaml.Controls.ItemsStackPanel > Windows.UI.Xaml.Controls.ListViewItem[MaxHeight=5000]
    styles:
      - MaxWidth=460
      - MinWidth=460
      - Margin=0,0,16,0
      - Padding=10,0,14,0
  - target: Windows.UI.Xaml.Controls.Button#ShowMoreSuggestionsButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.StackPanel > Windows.UI.Xaml.Controls.TextBlock
    styles:
      - Margin=0,0,2,0
  - target: Windows.UI.Xaml.Controls.Button#ShowMoreSuggestionsButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.StackPanel > Windows.UI.Xaml.Controls.FontIcon
    styles:
      - FontSize=12
  - target: Windows.UI.Xaml.Controls.Button#HideMoreSuggestionsButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.StackPanel > Windows.UI.Xaml.Controls.TextBlock
    styles:
      - Margin=2,0,0,0
  - target: Windows.UI.Xaml.Controls.Button#HideMoreSuggestionsButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.StackPanel > Windows.UI.Xaml.Controls.FontIcon
    styles:
      - FontSize=12
  - target: Windows.UI.Xaml.Controls.FlyoutPresenter[1]
    styles:
      - Margin=-268,0,0,0
  - target: Windows.UI.Xaml.Controls.FlyoutPresenter[1] > Grid
    styles:
      - Margin=-543,0,543,0
  - target: Windows.UI.Xaml.Controls.FlyoutPresenter
    styles:
      - Margin=-245,-12,0,0
```
</details>

## Removing the "Recommended" section

For the classic Start menu, the "Recommended" section can be removed by
following these steps:

* Import [the NoRecommendedSection
  theme](https://github.com/ramensoftware/windows-11-start-menu-styling-guide/blob/main/Themes/NoRecommendedSection/README.md)
  using the **Manual installation** instructions.
* Select this theme using the **Theme selection** instructions on this page.
