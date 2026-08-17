# [Down Aero](http://github.com/ramensoftware/windows-11-start-menu-styling-guide/tree/main/Themes/Down%20Aero) Theme (Windows 11 Start Menu Fix)

This is a modified version of the Down Aero theme for **Windows 11 Start Menu Styler** (Windhawk). It fixes the layout breaking issues caused by recent Windows 11 updates.

<img width="1115" height="644" alt="updated" src="https://github.com/user-attachments/assets/26ce2433-ae73-4696-92a9-c9aa9383fc71" />


## Bug Fixes & Improvements

### Fixed the "Category View" Overflow Bug
Recent Windows 11 updates introduced a new categorized Start Menu layout containing a "View" dropdown button and a new "CategoryControl" grid. These elements were breaking the clean, pinned-only layout of the Down Aero theme. Fixed this by explicitly collapsing the visibility of the new layout targets.

### Fixed the Oversized Folder View Bug
When opening a pinned app folder (app group), the folder background container was scaling incorrectly, resulting in a giant empty space and floating edit (pen) icons. Adjusted the margins and boundaries of the Folder View targets to restore the compact appearance.

## How to Apply

1. Open the **Windhawk** app.
2. Open the theme plugin (**Windows 11 Start Menu Styler**), find the **Settings** tab, and switch to **Textual mode**.
3. Clear the text box completely, paste the code below, and click **Save settings**.
4. If changes don't appear immediately, restart `explorer.exe` via Task Manager.

## Updated Code
<details>
<summary>Content to import (click to expand)</summary>

```yaml
theme: Down Aero
disableNewStartMenuLayout: ''
styleConstants:
  - ''
controlStyles:
  - target: Grid#FrameRoot
    styles:
      - MaxHeight=520
  - target: TextBlock#ZoomedOutHeading
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader
    styles:
      - Height=0
      - Visibility=>showMoreSuggestionsVisible
  - target: Grid#ShowMoreSuggestions
    styles:
      - Visibility={{showMoreSuggestionsVisible}}
  - target: Button#ShowMoreSuggestionsButton
    styles:
      - Margin=0,-77,147,0
  - target: Windows.UI.Xaml.Controls.Grid#NoTopLevelSuggestionsText
    styles:
      - Height=0
  - target: Button#ShowMoreSuggestionsButton > Grid > ContentPresenter > StackPanel > TextBlock
    styles:
      - Text=Recommended
      - Visibility=Visible
  - target: Border#StartDropShadow
    styles:
      - CornerRadius=30
  - target: StartMenu.SearchBoxToggleButton
    styles:
      - Visibility=Collapsed
  - target: Border#AcrylicBorder
    styles:
      - CornerRadius=30
      - Background:=<AcrylicBrush TintColor="{ThemeResource CardStrokeColorDefaultSolid}" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" TintOpacity="0" TintLuminosityOpacity=".5" Opacity="1"/>
  - target: Border#AcrylicOverlay
    styles:
      - CornerRadius=30
      - Background:=<AcrylicBrush TintColor="{ThemeResource CardStrokeColorDefaultSolid}" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" TintOpacity="0" TintLuminosityOpacity="1" Opacity="1"/>
      - Height=430
      - Margin=0,-65,0,0
  - target: Windows.UI.Xaml.Controls.Grid#AllAppsRoot
    styles:
      - Margin=0,-90,0,90
  - target: Grid#MainContent
    styles:
      - Grid.Row=0
      - VerticalAlignment=0
      - MinHeight=Auto
  - target: StartDocked.AppListView#NavigationPanePlacesListView > Windows.UI.Xaml.Controls.Border
    styles:
      - Background:=<AcrylicBrush TintColor="{ThemeResource CardStrokeColorDefaultSolid}" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" TintOpacity="0" TintLuminosityOpacity=".5" Opacity="1"/>
      - CornerRadius=18
      - Margin=0,0,15,0
  - target: StartDocked.NavigationPaneButton#PowerButton > Windows.UI.Xaml.Controls.Grid@CommonStates > Windows.UI.Xaml.Controls.Border#BackgroundBorder
    styles:
      - Background:=<AcrylicBrush TintColor="{ThemeResource CardStrokeColorDefaultSolid}" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" TintOpacity="0" TintLuminosityOpacity="1" Opacity="1"/>
      - BorderBrush@Normal:=<AcrylicBrush TintColor="{ThemeResource SurfaceStrokeColorDefault}" FallbackColor="{ThemeResource SurfaceStrokeColorDefault}" TintOpacity="0" TintLuminosityOpacity=".1" Opacity="1"/>
      - CornerRadius=30
      - BorderThickness=5
      - Margin=-7
      - BorderBrush@PointerOver:=<AcrylicBrush TintColor="{ThemeResource SystemAccentColor}" FallbackColor="{ThemeResource SystemAccentColor}" TintOpacity=".8" TintLuminosityOpacity=".5" Opacity="1"/>
  - target: StartDocked.NavigationPaneButton#UserTileButton > Grid > Border#BackgroundBorder
    styles:
      - Background:=<AcrylicBrush TintColor="{ThemeResource CardStrokeColorDefaultSolid}" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" TintOpacity="0" TintLuminosityOpacity=".5" Opacity="1"/>
      - CornerRadius=18
  - target: Button#ShowMoreSuggestionsButton > Grid@CommonStates > Border
    styles:
      - Background@Normal:=<SolidColorBrush Color="{ThemeResource SystemAltMediumLowColor}" Opacity="0" />
      - BorderBrush@Normal:=<SolidColorBrush Color="{ThemeResource SystemChromeAltHighColor}" Opacity=".8"/>
      - Padding=10,5
      - Margin=0,0,-2,0
      - CornerRadius=15,0,0,15
      - BorderThickness=2,2,0,2
      - Background@PointerOver:=<SolidColorBrush Color="{ThemeResource SystemBaseLowColor}" Opacity=".7" />
      - BorderBrush@PointerOver:=<SolidColorBrush Color="{ThemeResource SystemBaseLowColor}" Opacity="1"/>
  - target: Windows.UI.Xaml.Controls.Button#HideMoreSuggestionsButton
    styles:
      - Background:=<SolidColorBrush Color="{ThemeResource SystemChromeMediumLowColor}" Opacity="1"/>
      - CornerRadius=15
  - target: StartDocked.NavigationPaneView > Windows.UI.Xaml.Controls.Grid#RootPanel
    styles:
      - Grid.Row=2
  - target: Windows.UI.Xaml.Controls.Frame
    styles:
      - Margin=0,-65,0,0
  - target: Grid#MainMenu
    styles:
      - MaxWidth=650
  - target: TextBlock#AllListHeadingText
    styles:
      - Margin=63,-184,12,0
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.GridView#RecommendedList
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.GridView#AllAppsGrid > Border > Windows.UI.Xaml.Controls.ScrollViewer > Border > Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid
    styles:
      - Margin=45,-180,45,0
  - target: Microsoft.UI.Xaml.Controls.DropDownButton > Grid@CommonStates
    styles:
      - Visibility=Collapsed
  - target: StartMenu.PinnedList
    styles:
      - Margin=0,20,-40,180
      - ActualHeight=>pinnedListHeight
  - target: Grid#TopLevelSuggestionsRoot
    styles:
      - Grid.Row=1
  - target: Microsoft.UI.Xaml.Controls.DropDownButton
    styles:
      - Visibility=Collapsed
  - target: StartMenu.CategoryControl
    styles:
      - Visibility=Collapsed
  - target: Grid#TopLevelHeader > Grid > Button
    styles:
      - Visibility=Collapsed
  - target: GridView#PinnedList > Border > Windows.UI.Xaml.Controls.ScrollViewer
    styles:
      - ScrollViewer.VerticalScrollMode=2
      - Height=280
  - target: Border#RightCompanionDropShadow
    styles:
      - CornerRadius=30
  - target: Grid#CompanionRoot > Grid#MainContent > Border#AcrylicOverlay
    styles:
      - Margin=0
  - target: Windows.UI.Xaml.Controls.Primitives.ScrollBar
    styles:
      - Visibility=Collapsed
  - target: Grid#TopLevelHeader > Grid > Button > Grid@CommonStates > Border
    styles:
      - Visibility=Collapsed
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton
    styles:
      - Margin=12,7,-12,-7
  - target: Grid#MainMenu > Grid#MainContent > Grid
    styles:
      - Canvas.ZIndex=1
  - target: StartMenu.FolderView
    styles:
      - Margin=0,-45,0,0
      - MinHeight=0
      - MaxHeight=400
  - target: StartMenu.FolderView > Grid > GridView
    styles:
      - Margin=0,15,0,0
themeResourceVariables:
  - ''
webContentStyles:
  - target: ''
    styles:
      - ''
webContentCustomJs: ''
```
</details>


