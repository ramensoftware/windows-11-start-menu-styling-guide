# LiquidGlass theme for Windows 11 Start Menu Styler

**Author**: [PhantomNimbi](https://github.com/PhantomNimbi)

![Screenshot](screenshot.png)

> [!IMPORTANT]
> This theme is designed for the [redesigned Windows 11 Start menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/) that is gradually rolling out with the 25H2 update.

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

<details>
<summary>Content to import (click to expand)</summary>

```yaml
disableNewStartMenuLayout: forceNewLayout
styleConstants:
  - BorderThickness=0.3,1,0.3,0.3
  - ElementBorderThickness=0.3,0.3,0.3,1
  - CornerRadius=12
  - ElementCornerRadius=8
  - Background=<WindhawkBlur BlurAmount="15" TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="0.2" />
  - ElementBackground=<WindhawkBlur BlurAmount="15" TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="0.4" />
  - ElementBackground2 = <WindhawkBlur BlurAmount="15" TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="0.2"  />
  - AccentBackground=<WindhawkBlur BlurAmount="15" TintColor="{ThemeResource SystemAccentColorLight1}" TintOpacity="0.2"  />
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#50808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#50808080" Offset="1" /></LinearGradientBrush>"
  - ElementBorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#50808080" Offset="1" /><GradientStop Color="#50606060" Offset="0.15" /></LinearGradientBrush>
controlStyles:
  - target: Border#AcrylicOverlay
    styles:
      - Visibility=1
  - target: Border#AcrylicBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Border#AppBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Border#ContentBorder@CommonStates > Grid > Border#BackgroundBorder
    styles:
      - BorderThickness=$ElementBorderThickness
      - BorderBrush@PointerOver:=$ElementBorderBrush
      - BorderBrush@Pressed:=$ElementBorderBrush
      - CornerRadius=$ElementCornerRadius
  - target: Button > Grid@CommonStates > Border#BackgroundBorder
    styles:
      - BorderThickness=$ElementBorderThickness
      - BorderBrush@PointerOver:=$ElementBorderBrush
      - BorderBrush@Pressed:=$ElementBorderBrush
      - BackgroundSizing=InnerBorderEdge
      - CornerRadius=$ElementCornerRadius
  - target: StartMenu.CategoryControl > Grid > Border
    styles:
      - BorderThickness=$ElementBorderThickness
      - BorderBrush:=$ElementBorderBrush
      - BackgroundSizing=InnerBorderEdge
      - Background:=$ElementBackground
      - Opacity=0.8
      - CornerRadius=$ElementCornerRadius
  - target: Grid#LayoutRoot
    styles:
      - BackgroundTransition:=<BrushTransition Duration="0:0:0.083" />
  - target: Border#BackgroundBorder
    styles:
      - BackgroundTransition:=<BrushTransition Duration="0:0:0.083" />
  - target: Button#Header > Border@CommonStates
    styles:
      - BorderThickness=$ElementBorderThickness
      - BorderBrush@PointerOver:=$ElementBorderBrush
      - BorderBrush@Pressed:=$ElementBorderBrush
      - BackgroundSizing=InnerBorderEdge
      - CornerRadius=$ElementCornerRadius
  - target: ListViewItem > Grid@CommonStates > Border#BorderBackground
    styles:
      - BorderThickness=$ElementBorderThickness
      - BorderBrush@PointerOver:=$ElementBorderBrush
      - BorderBrush@Pressed:=$ElementBorderBrush
      - BackgroundSizing=InnerBorderEdge
      - CornerRadius=$ElementCornerRadius
  - target: StartMenu.SearchBoxToggleButton > Grid@CommonStates > Border#BorderElement
    styles:
      - CornerRadius=$ElementCornerRadius
      - BorderThickness=$ElementBorderThickness
      - BorderBrush:=$ElementBorderBrush
      - Background@Checked:=$ElementBackground
      - Background@CheckedPointerOver:=$AccentBackground
      - Background@CheckedPressed:=$ElementBackground2
      - BackgroundTransition:=<BrushTransition Duration="0:0:0.083" />
  - target: Button#HideMoreSuggestionsButton > Grid@CommonStates > Border#BackgroundBorder
    styles:
      - Background@Normal:=$ElementBackground
      - BorderBrush@Normal:=$ElementBorderBrush
      - BorderBrush@PointerOver:=$ElementBorderBrush
      - BorderBrush@Pressed:=$ElementBorderBrush
      - Background@PointerOver:=$AccentBackground
      - Background@Pressed:=$ElementBackground2
      - BorderThickness=$ElementBorderThickness
      - Margin=2
      - CornerRadius=$ElementCornerRadius
  - target: Button#ShowMoreSuggestionsButton > Grid@CommonStates > Border#BackgroundBorder
    styles:
      - Background@Normal:=$ElementBackground
      - BorderBrush@Normal:=$ElementBorderBrush
      - BorderBrush@PointerOver:=$ElementBorderBrush
      - BorderBrush@Pressed:=$ElementBorderBrush
      - Background@PointerOver:=$AccentBackground
      - Background@Pressed:=$ElementBackground2
      - BorderThickness=$ElementBorderThickness
      - Margin=2
      - CornerRadius=$ElementCornerRadius
  - target: StartMenu.FolderModal > Grid#Root > Border
    styles:
      - BorderThickness=$BorderThickness
      - BorderBrush:=$BorderBrush
      - CornerRadius=$CornerRadius
  - target: MenuFlyoutPresenter > Border
    styles:
      - BorderThickness=$BorderThickness
      - BorderBrush:=$BorderBrush
      - CornerRadius=$CornerRadius
  - target: Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter#ContentPresenter > ContentControl > Grid#RootGrid > Border#LogoBackgroundPlate > Image#AllAppsItemLogo
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
      - CornerRadius=$ElementCornerRadius
  - target: StartDocked.NavigationPaneButton > Grid@CommonStates > Border#BackgroundBorder
    styles:
      - BorderThickness=$ElementBorderThickness
      - BorderBrush@PointerOver:=$ElementBorderBrush
      - BorderBrush@Pressed:=$ElementBorderBrush
      - BackgroundSizing=InnerBorderEdge
      - CornerRadius=$ElementCornerRadius
  - target: StartDocked.AppListViewItem > Grid@CommonStates > Border#BackgroundBorder
    styles:
      - BorderThickness=$BorderThickness
      - BorderBrush@PointerOver:=$BorderBrush
      - BorderBrush@Pressed:=$BorderBrush
      - BackgroundSizing=InnerBorderEdge
      - CornerRadius=$ElementCornerRadius
  - target: Microsoft.UI.Xaml.Controls.DropDownButton > Grid@CommonStates
    styles:
      - Background@PointerOver:=$AccentBackground
      - Background@Pressed:=$ElementBackground2
      - BorderBrush@PointerOver:=$ElementBorderBrush
      - BorderBrush@Pressed:=$ElementBorderBrush
      - BackgroundSizing=InnerBorderEdge
      - Background@Normal:=$ElementBackground
      - BorderBrush@Normal:=$ElementBorderBrush
      - Padding=9,3,7,4
      - CornerRadius=$ElementCornerRadius
      - BorderThickness@Normal=$ElementBorderThickness
      - BorderThickness@PointerOver=$ElementBorderThickness
      - BorderThickness@Pressed=$ElementBorderThickness
  - target: Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter#ContentPresenter > ContentControl > Grid#RootGrid > Grid#LogoContainer > Image#AllAppsTileLogo
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
      - CornerRadius=$ElementCornerRadius
  - target: Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Grid
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
      - CornerRadius=$ElementCornerRadius
  - target: Grid#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Grid
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
      - CornerRadius=$ElementCornerRadius
  - target: ScrollViewer#MenuFlyoutPresenterScrollViewer > Border > Grid > ScrollContentPresenter > ItemsPresenter > StackPanel
    styles:
      - ChildrenTransitions:=<TransitionCollection><EntranceThemeTransition IsStaggeringEnabled="False" FromHorizontalOffset="-25" FromVerticalOffset="0" /></TransitionCollection>
  - target: FlyoutPresenter > Border > ScrollViewer > Border > Grid > ScrollContentPresenter > ContentPresenter > Border
    styles:
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Button > ContentPresenter#ContentPresenter@CommonStates
    styles:
      - Background@PointerOver:=$AccentBackground
      - Background@Pressed:=$ElementBackground2
      - BorderBrush@PointerOver:=$ElementBorderBrush
      - BorderBrush@Pressed:=$ElementBorderBrush
      - BorderThickness=$ElementBorderThickness
      - Background@Normal=$ElementBackground
      - CornerRadius=$ElementCornerRadius
  - target: Grid@SearchBoxInputStates > Border#TaskbarSearchBackground
    styles:
      - CornerRadius=$ElementCornerRadius
      - Background@ActiveInput:=$ElementBackground2
      - BorderBrush:=$ElementBorderBrush
      - BorderThickness=$ElementBorderThickness
      - Background@SearchBoxHover:=$AccentBackground
      - Background@NoFocus:=$ElementBackground
      - BackgroundTransition:=<BrushTransition Duration="0:0:0.083" />
  - target: Border@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Image
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
  - target: Grid#ContentBorder@CommonStates > ContentPresenter > Grid > Grid#LogoContainer > Grid
    styles:
      - RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />
      - RenderTransformOrigin=0.5,0.5
webContentStyles:
  - target: '*'
    styles:
      - 'transition: background-color 0.083s ease-in-out !important'
```
</details>
