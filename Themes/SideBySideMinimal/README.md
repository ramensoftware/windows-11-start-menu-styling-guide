# SideBySideMinimal theme for Windows 11 Start Menu Styler

**Author**: [Olivia](https://github.com/OliviaIsTyping)

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
  - target: Grid#MainMenu
    styles:
      - Width=600
  - target: Grid#FrameRoot
    styles:
      - MaxHeight=710
  - target: StartMenu.SearchBoxToggleButton
    styles:
      - Height=0
  - target: Border#AcrylicOverlay
    styles:
      - Margin=0,-64,0,0
  - target: Frame#StartFrame
    styles:
      - Margin=0,-64,0,0
  - target: Grid#SideBySidePinnedWrapper
    styles:
      - ColumnDefinitions:=<ColumnDefinitionCollection><ColumnDefinition Width="250*"/><ColumnDefinition Width="348*"/></ColumnDefinitionCollection>
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
  - target: StartDocked.UserTileView
    styles:
      - Visibility=Collapsed
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
      - Width=348
      - Margin=132,-42,-132,0
  - target: Windows.UI.Xaml.Controls.Grid#AllAppsRoot
    styles:
      - Visibility=Visible
      - Width=320
      - Margin=0,-42,0,0
      - RenderTransform:=<TranslateTransform X="-188"/>
  - target: Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Grid#SuggestionsParentContainer
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader
    styles:
      - Visibility=Collapsed
  - target: StartDocked.SearchBoxToggleButton
    styles:
      - Height=0
      - Width=0
  - target: Windows.UI.Xaml.Controls.Button#ShowAllAppsButton
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton
    styles:
      - Visibility=Collapsed
  - target: StartDocked.PowerOptionsView
    styles:
      - Margin=-575,0,0,0
  - target: StartDocked.UserTileView
    styles:
      - Visibility=Collapsed
  - target: StartMenu.PinnedList
    styles:
      - Height=504
  - target: StartMenu.ExpandedFolderList > Grid > Border
    styles:
      - Margin=-40,0,40,0
      - Width=325
  - target: StartMenu.ExpandedFolderList > Grid > Grid
    styles:
      - CornerRadius=8
      - Margin=-85,0,0,0
      - Width=350
  - target: StartMenu.ExpandedFolderList > Grid > Grid > Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager
    styles:
      - Margin=-15,0,0,0
  - target: Rectangle[4]
    styles:
      - Margin=0,-20,0,0
  - target: Grid#TopLevelSuggestionsContainer
    styles:
      - Visibility=Collapsed
  - target: StartDocked.AppListView
    styles:
      - Margin=38,0,-38,0
```
</details>
