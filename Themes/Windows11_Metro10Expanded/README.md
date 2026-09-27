# Windows11_Metro10Expanded theme for Windows 11 Start Menu Styler

An expanded-height variant of Windows11_Metro10 for the redesigned Windows 11 Start menu. It keeps the original Metro10 appearance and tile sizing while using substantially more of the available right-hand pane before scrolling is required.

**Author**: [YiftahCooper](https://github.com/YiftahCooper)

**Author of base theme**: [Ian Div](https://github.com/iandiv)

![Screenshot](screenshot.png)

## Differences from Windows11_Metro10

The redesigned-menu variant makes two deliberate layout changes:

* Expands the pinned/category scroll viewport from `265` to `610` logical pixels so additional rows can use the otherwise empty vertical space.
* Moves the right-hand pane down by `38` logical pixels to retain comfortable spacing at the top.

The category tiles remain the original `132 × 132` size, and overflow continues to scroll normally.

## Compatibility

This variant is intended for the **redesigned Windows 11 Start menu**. The classic Start menu is unchanged; use the original Windows11_Metro10 theme for the classic layout.

Because this variant intentionally uses a taller fixed viewport, users with unusually small displays or high display scaling may need to reduce the `Height=610` value.

## Manual installation

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the **Settings** tab and select **Textual mode**.
* Copy the content below into the text box and click **Save settings**.

### Redesigned Start menu

<details>
<summary>Content to import (click to expand)</summary>

```yaml
disableNewStartMenuLayout: newLayoutSideBySide
controlStyles:
  - target: Windows.UI.Xaml.Controls.Frame
    styles:
      - Margin=0,-64,0,0

  - target: Grid#FrameRoot
    styles:
      - MaxHeight=692

  - target: Grid#MainMenu
    styles:
      - MaxWidth=650

  - target: Grid#MainMenu > Grid#MainContent > Grid
    styles:
      - Canvas.ZIndex=1

  - target: Border#AcrylicOverlay
    styles:
      - Margin=0,-70,0,0
      - CornerRadius=20,20,0,0

  - target: Windows.UI.Xaml.Controls.Button#CloseAllAppsButton
    styles:
      - Visibility=Collapsed

  - target: Windows.UI.Xaml.Controls.Grid#ShowMoreSuggestions
    styles:
      - Visibility=Collapsed

  - target: Grid#TopLevelHeader > Grid[2]
    styles:
      - Visibility=Collapsed

  - target: TextBlock#AllListHeadingText
    styles:
      - Visibility=Collapsed

  - target: StartMenu.SearchBoxToggleButton
    styles:
      - Visibility=Collapsed

  - target: //TextBlock#ZoomedOutHeading
    styles:
      - Visibility=Collapsed

  - target: Grid#ShowMorePinnedGrid > Button
    styles:
      - Visibility=Collapsed

  - target: TextBlock#PinnedListHeaderText
    styles:
      - Visibility=Collapsed

  - target: StartDocked.UserTileView
    styles:
      - Margin=-30,0,0,0

  - target: StartDocked.NavigationPaneButton#UserTileButton > Grid@CommonStates > Border
    styles:
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - BorderThickness=1
      - Background@Pressed:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.8"/>

  - target: StartDocked.AppListView#NavigationPanePlacesListView
    styles:
      - FlowDirection=1
      - Margin=30,0,-30,0

  - target: StartDocked.AppListViewItem
    styles:
      - Margin=2,0,2,0

  - target: StartDocked.AppListViewItem > Grid > Border#BackgroundBorder
    styles:
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>

  - target: Grid#ContentBorder@CommonStates
    styles:
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0"/>
      - CornerRadius=5

  - target: StartDocked.NavigationPaneButton#PowerButton
    styles:
      - Margin=30,0,-30,0

  - target: StartDocked.NavigationPaneButton#PowerButton > Grid@CommonStates
    styles:
      - BorderThickness=1
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.8"/>
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="#22FFFFFF" TargetTheme="1" Opacity="1"/>
      - CornerRadius=5
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.8"/>

  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion
    styles:
      - Visibility=Visible
      - Margin=12,-8,-12,0

  - target: Button
    styles:
      - Style:=<ResourceKey="ButtonRevealStyle" />

  - target: Grid#TopLevelHeader
    styles:
      - Margin=0,0,-1,0

  - target: Grid#SideBySidePinnedWrapper > Windows.UI.Xaml.Controls.ScrollViewer
    styles:
      - RenderTransform:=<TranslateTransform X="-480" />
      - Margin=-92,-12,-172,-15

  - target: Grid#SideBySidePinnedWrapper > Windows.UI.Xaml.Controls.ScrollViewer#SideBySidePinnedScrollViewer
    styles:
      - RenderTransform:=<TranslateTransform X="172" Y="38" />
      - Canvas.ZIndex=-1

  - target: Button#Header > Border#Border@CommonStates
    styles:
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.3"/>
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.3"/>
      - BorderThickness=1

  - target: Windows.UI.Xaml.Controls.Border#ContentBorder > Windows.UI.Xaml.Controls.Grid#DroppedFlickerWorkaroundWrapper > Border#HighContrastBorder
    styles:
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.3"/>
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.7"/>
      - BorderThickness=1

  - target: GridView#PinnedList
    styles:
      - Width=300
      - RenderTransform:=<TranslateTransform Y="-24" />

  - target: GridView#PinnedList > Border > Windows.UI.Xaml.Controls.ScrollViewer
    styles:
      - Height=610

  - target: Windows.UI.Xaml.Controls.GridView#PinnedList > Border > Windows.UI.Xaml.Controls.ScrollViewer > Border > Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem > Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper
    styles:
      - Background:=<RevealBorderBrush Color="#646464" TargetTheme="1" Opacity=".1"/>
      - Margin=2
      - CornerRadius=5

  - target: Grid#TopLevelSuggestionsRoot
    styles:
      - MinHeight=132
      - Margin=-65,31,-65,-31
      - Width=400
      - RenderTransform:=<TranslateTransform Y="-80"/>

  - target: Windows.UI.Xaml.Controls.GridView#RecommendedList > Windows.UI.Xaml.Controls.Border > Windows.UI.Xaml.Controls.ScrollViewer#ScrollViewer > Windows.UI.Xaml.Controls.Border#Root > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter#ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem
    styles:
      - MaxWidth=145
      - MinWidth=145
      - Margin=0

  - target: Windows.UI.Xaml.Controls.TextBlock#NoSuggestionsWithoutSettingsLink
    styles:
      - Margin=11,0,48,0

  - target: Windows.UI.Xaml.Controls.GridView#RecommendedList > Border > Windows.UI.Xaml.Controls.ScrollViewer > Border > Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem > Border > Grid > Border
    styles:
      - Background:=<RevealBorderBrush Color="#646464" TargetTheme="1" Opacity=".1"/>
      - Margin=2

  - target: ScrollViewer
    styles:
      - ScrollViewer.VerticalScrollMode=0

  - target: GridView#AllAppsGrid > Border > Grid#SideBySidePinnedWrapper > ScrollViewer#ScrollViewer
    styles:
      - ScrollViewer.VerticalScrollMode=2

  - target: Windows.UI.Xaml.Controls.GridView > Border > ScrollViewer
    styles:
      - ScrollViewer.VerticalScrollMode=2

  - target: Windows.UI.Xaml.Controls.Primitives.ScrollBar
    styles:
      - MaxHeight=575
      - Canvas.ZIndex=99
      - RenderTransform:=<TranslateTransform X="-20" Y="-5" />

  - target: Microsoft.UI.Xaml.Controls.DropDownButton
    styles:
      - Background:=<RevealBorderBrush Color="#646464" TargetTheme="1" Opacity=".1"/>
      - Style:=<StaticResource ResourceKey="ButtonRevealStyle"/>
      - Margin=-120,-7,120,7
      - Padding=4,2,4,2

  - target: ItemsWrapGrid > ListViewItem > Grid@CommonStates
    styles:
      - BorderThickness=1
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="#34FFFFFF" TargetTheme="1" Opacity="1"/>
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - CornerRadius=5
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0"/>

  - target: StartMenu.ExpandedFolderList > Grid > Grid
    styles:
      - Margin=0,0,80,0

  - target: StartMenu.ExpandedFolderList > Grid > Border
    styles:
      - Width=350
      - Margin=0,0,92,0

  - target: StartMenu.ExpandedFolderList > Grid > Grid > Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager
    styles:
      - Margin=-20,0,20,0

  - target: Grid#PageRoot@ViewStates > SemanticZoom#TopLevelRoot > Grid > ScrollViewer#ScrollViewer > ScrollContentPresenter#ScrollContentPresenter > Grid > ContentPresenter#ZoomedInPresenter > GridView#AllAppsGrid > Border > Grid#SideBySidePinnedWrapper > ScrollViewer#ScrollViewer > Border#Root > Grid > ScrollContentPresenter#ScrollContentPresenter > ItemsPresenter
    styles:
      - Margin@Alpha_GridView=14,0,0,0

  - target: StartMenu.CategoryControl > Grid > Border
    styles:
      - Width=132
      - Height=132
      - CornerRadius=8

  - target: Button#LogoContainer > Grid@CommonStates > Border
    styles:
      - Width=58
      - Height=58
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0"/>

  - target: Button#FolderPlate > Grid@CommonStates > Border
    styles:
      - Width=58
      - Height=58
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0"/>

  - target: StartMenu.CategoryControl
    styles:
      - Margin=60,-8,-60,-16
      - BorderBrush:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>

  - target: Button#SeeAllButton
    styles:
      - MaxWidth=132
      - Margin=0,-6,0,6

  - target: Button#SeeAllButton > Grid@CommonStates
    styles:
      - BorderBrush@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="1"/>
      - Background@PointerOver:=<RevealBorderBrush Color="Transparent" TargetTheme="1" Opacity="0.4"/>
      - CornerRadius=5
      - BorderThickness=1

  - target: FlyoutPresenter
    styles:
      - RenderTransform:=<TranslateTransform X="20" Y="-24" />
```
</details>
