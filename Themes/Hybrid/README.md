# Hybrid theme for Windows 11 Start Menu Styler (Windows 10 Start menu)

**Author**: [SandTechStuff](https://github.com/SandTechStuff)

![Screenshot](screenshot.png)

> [!WARNING]
> Right clicking empty space of the navigation pane (eg. between the Settings and All Apps buttons in the above screenshot) will cause the Start menu to crash. So don't do that.

## Windows 10 Start menu on Windows 11 installation

If you're already using the Windows 10 Start menu, you can skip this step.

Installation:
* Install [ExplorerPatcher](https://github.com/valinet/ExplorerPatcher).
* Open *"Properties (ExplorerPatcher)"* via the Start menu or right-click the taskbar > *"Properties"*.
* Go to *"Start menu"* > *"Start menu style"* > *"Windows 10"* > *"Restart File Explorer"*.

## Required additional configuration

### Disable incompatible settings

Disable these Windows Start menu settings if they are not already:
* "Show app list in the Start menu"
* "Show more tiles on Start"
* "Use Start full screen"

### Configure user picture

This theme requires you to supply your own user picture image, separate from the one set in Windows settings.

Once you have imported the theme into the Start Menu Styler, go to the mod's settings and scroll all the way down. You should see a style constant with the content `userPicture=REPLACE ME`, after the "=" put the link to whatever image you want to use as your user picture.

For example: `userPicture=https://raw.githubusercontent.com/SandTechStuff/Stuff/refs/heads/main/Nintendo-3DS-AquaOpen-White.png`

## Manual installation

The theme styles have to be imported manually. To do that, follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Advanced" tab.
* Copy the content below to the text box under "Mod settings" and click "Save".

<details>
<summary>Content to import (click to expand)</summary>

```yaml
styleConstants:
  - userPicture=REPLACE ME
controlStyles:
  - target: Grid#PaneRoot
    styles:
      - Clip:=
      - FlowDirection=0
      - RenderTransform:=<TranslateTransform X="105" />
  - target: Grid#ContentRoot
    styles:
      - FlowDirection=0
  - target: SplitView#RootContent
    styles:
      - IsPaneOpen=False
  - target: SplitView#RootContent > Grid
    styles:
      - FlowDirection=1
  - target: StartUI.NavigationPaneGrid
    styles:
      - Width=165
      - Background:=<SolidColorBrush Color="{ThemeResource SystemListLowColor}" />
  - target: Windows.UI.Xaml.Shapes.Rectangle#BackgroundElement
    styles:
      - Visibility=Collapsed
  - target: StartUI.StartSizingFrame
    styles:
      - MinWidth=501
      - MaxWidth=501
  - target: StartUI.ExpandCollapseButton
    styles:
      - Visibility=Collapsed
  - target: StartUI.UserTileView
    styles:
      - Grid.Row=1
      - Margin=0,50,0,0
  - target: StartUI.AppListView
    styles:
      - Grid.Row=2
  - target: StartUI.NavigationPaneButton#UserTileButton
    styles:
      - Height=50
  - target: TextBlock#UserTileNameText
    styles:
      - HorizontalAlignment=Center
      - RenderTransform:=<TranslateTransform X="-25" />
  - target: StartUI.NavigationPaneButton#UserTileButton > ContentPresenter > StartUI.NavigationPaneItemPanel > Grid
    styles:
      - Width=48
      - Height=48
      - IsHitTestVisible=False
      - RenderTransform:=<TransformGroup><ScaleTransform ScaleX="1.5" ScaleY="1.5" /><TranslateTransform X="45" Y="-87" /></TransformGroup>
  - target: StartUI.ResizeThumb#HorizontalThumb
    styles:
      - Visibility=Collapsed
  - target: StartUI.NavigationPaneButton#UserTileButton > ContentPresenter > StartUI.NavigationPaneItemPanel > Grid > Windows.UI.Xaml.Shapes.Ellipse
    styles:
      - Fill:=<ImageBrush ImageSource="$userPicture" />
  - target: StartUI.StartSizingFramePanel
    styles:
      - Margin=0,50,0,0
  - target: Image#DropShadow
    styles:
      - Canvas.ZIndex=-1
  - target: StartUI.ViewSelectionListView
    styles:
      - Grid.Row=4
  - target: StartUI.NavigationPaneGrid > Image#DropShadow
    styles:
      - Visibility=Collapsed
  - target: StartUI.AllAppsGridListView
    styles:
      - HorizontalAlignment=Left
  - target: StartUI.AllAppsPane
    styles:
      - Width=324
      - Margin=5,0,0,0
      - HorizontalAlignment=Left
  - target: Border#GridPane
    styles:
      - Width=334
      - RenderTransform:=<TranslateTransform X="-84" />
  - target: Grid#ContentPaneGrid
    styles:
      - Width=500
  - target: StartUI.ViewSelectionListView
    styles:
      - Height=48
  - target: StartUI.ViewSelectionListViewItem > Grid@CommonStates
    styles:
      - Visibility@Selected=Collapsed
      - Visibility@PointerOverSelected=Collapsed
      - Visibility@PressedOverSelected=Collapsed
  - target: StartUI.ViewSelectionListViewItem[2]
    styles:
      - Margin=0,-48,0,0
  - target: TextBlock#StatusMessage[Text=System]
    styles:
      - Visibility=Collapsed
  - target: StartUI.TileViewControl > Grid#MainGrid > Rectangle#Background
    styles:
      - Fill:=<SolidColorBrush Color="{ThemeResource SystemListLowColor}" />
```
</details>

