# Start Menu

## Installation
Follow the instructions listed below to install and setup the Windows Glass Start Menu theme on your system.

### Requirements

* **Windhawk Mods**:  
  * [Windows 11 Start Menu Styler](https://windhawk.net/mods/windows-11-start-menu-styler)

---

<img src="Preview-1.png" width="100%" height="auto" />

> [!NOTE]
> This theme is built for the new start menu layout.

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
  "theme": "",
  "disableNewStartMenuLayout": 0,
  "controlStyles[0].target": "Border#AcrylicOverlay",
  "controlStyles[0].styles[0]": "Visibility=1",
  "controlStyles[1].target": "Border#AcrylicBorder",
  "controlStyles[1].styles[0]": "Background:=$background",
  "controlStyles[1].styles[1]": "BorderBrush:=$borderColor",
  "controlStyles[1].styles[2]": "BorderThickness=$borderThickness",
  "controlStyles[2].target": "Border#AccentAppBorder",
  "controlStyles[2].styles[0]": "Background:=$background",
  "controlStyles[2].styles[1]": "BorderBrush:=$borderColor",
  "controlStyles[2].styles[2]": "BorderThickness=$borderThickness",
  "controlStyles[3].target": "Border#ContentBorder@CommonStates > Grid > Border#BackgroundBorder",
  "controlStyles[3].styles[0]": "BorderThickness=$orderThickness2",
  "controlStyles[3].styles[1]": "BorderBrush@PointerOver:=$borderColor2",
  "controlStyles[3].styles[2]": "BorderBrush@Pressed:=$borderColor2",
  "controlStyles[4].target": "Button > Grid@CommonStates > Border#BackgroundBorder",
  "controlStyles[4].styles[0]": "BorderThickness=$orderThickness2",
  "controlStyles[4].styles[1]": "BorderBrush@PointerOver:=$borderColor2",
  "controlStyles[4].styles[2]": "BorderBrush@Pressed:=$borderColor2",
  "controlStyles[4].styles[3]": "BackgroundSizing=InnerBorderEdge",
  "controlStyles[5].target": "StartMenu.CategoryControl > Grid > Border",
  "controlStyles[5].styles[0]": "BorderThickness=$borderThickness2",
  "controlStyles[5].styles[1]": "BorderBrush:=$borderColor2",
  "controlStyles[5].styles[2]": "BackgroundSizing=InnerBorderEdge",
  "controlStyles[5].styles[3]": "Background:=$background",
  "controlStyles[5].styles[4]": "Opacity=0.8",
  "controlStyles[6].target": "Grid#LayoutRoot",
  "controlStyles[6].styles[0]": "BackgroundTransition:=<BrushTransition Duration=\"0:0:0.083\" />",
  "controlStyles[7].target": "Border#BackgroundBorder",
  "controlStyles[7].styles[0]": "BackgroundTransition:=<BrushTransition Duration=\"0:0:0.083\" />",
  "controlStyles[8].target": "Button#Header > Border@CommonStates",
  "controlStyles[8].styles[0]": "BorderThickness=$borderThickness2",
  "controlStyles[8].styles[1]": "BorderBrush@PointerOver:=$borderColor2",
  "controlStyles[8].styles[2]": "BorderBrush@Pressed:=$borderColor2",
  "controlStyles[8].styles[3]": "BackgroundSizing=InnerBorderEdge",
  "controlStyles[9].target": "ListViewItem > Grid@CommonStates > Border#BorderBackground",
  "controlStyles[9].styles[0]": "BorderThickness=$borderThickness2",
  "controlStyles[9].styles[1]": "BorderBrush@PointerOver:=$borderColor2",
  "controlStyles[9].styles[2]": "BorderBrush@Pressed:=$borderColor2",
  "controlStyles[9].styles[3]": "BackgroundSizing=InnerBorderEdge",
  "controlStyles[10].target": "StartMenu.SearchBoxToggleButton > Grid@CommonStates > Border#BorderElement",
  "controlStyles[10].styles[0]": "CornerRadius=4",
  "controlStyles[10].styles[1]": "BorderThickness=1",
  "controlStyles[10].styles[2]": "BorderBrush:=$borderColor2",
  "controlStyles[10].styles[3]": "Background@Checked:=$background",
  "controlStyles[10].styles[4]": "Background@CheckedPointerOver:=$background",
  "controlStyles[10].styles[5]": "Background@CheckedPressed:=$background",
  "controlStyles[10].styles[6]": "BackgroundTransition:=<BrushTransition Duration=\"0:0:0.083\" />",
  "controlStyles[11].target": "Button#HideMoreSuggestionsButton > Grid@CommonStates > Border#BackgroundBorder",
  "controlStyles[11].styles[0]": "Background@Normal:=$background",
  "controlStyles[11].styles[1]": "BorderBrush@Normal:=$borderColor2",
  "controlStyles[11].styles[2]": "BorderBrush@PointerOver:=$borderColor2",
  "controlStyles[11].styles[3]": "BorderBrush@Pressed:=$borderColor2",
  "controlStyles[11].styles[4]": "Background@PointerOver:=$background",
  "controlStyles[11].styles[5]": "Background@Pressed:=$background",
  "controlStyles[11].styles[6]": "BorderThickness=1",
  "controlStyles[11].styles[7]": "Margin=2",
  "controlStyles[12].target": "Button#ShowMoreSuggestionsButton > Grid@CommonStates > Border#BackgroundBorder",
  "controlStyles[12].styles[0]": "Background@Normal:=$background",
  "controlStyles[12].styles[1]": "BorderBrush@Normal:=$borderColor",
  "controlStyles[12].styles[2]": "BorderBrush@PointerOver:=$borderColor",
  "controlStyles[12].styles[3]": "BorderBrush@Pressed:=$borderColor",
  "controlStyles[12].styles[4]": "Background@PointerOver:=$background",
  "controlStyles[12].styles[5]": "Background@Pressed:=$background",
  "controlStyles[12].styles[6]": "BorderThickness=1",
  "controlStyles[12].styles[7]": "Margin=2",
  "controlStyles[13].target": "StartMenu.FolderModal > Grid#Root > Border",
  "controlStyles[13].styles[0]": "BorderThickness=1",
  "controlStyles[13].styles[1]": "BorderBrush:=$borderColor",
  "controlStyles[14].target": "MenuFlyoutPresenter > Border",
  "controlStyles[14].styles[0]": "BorderThickness=1",
  "controlStyles[14].styles[1]": "BorderBrush:=$borderColor",
  "controlStyles[15].target": "Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter#ContentPresenter > ContentControl > Grid#RootGrid > Border#LogoBackgroundPlate > Image#AllAppsItemLogo",
  "controlStyles[15].styles[0]": "RenderTransform@Pressed:=<ScaleTransform ScaleX=\"0.8\" ScaleY=\"0.8\" />",
  "controlStyles[15].styles[1]": "RenderTransformOrigin=0.5,0.5",
  "controlStyles[16].target": "StartDocked.NavigationPaneButton > Grid@CommonStates > Border#BackgroundBorder",
  "controlStyles[16].styles[0]": "BorderThickness=1",
  "controlStyles[16].styles[1]": "BorderBrush@PointerOver:=$borderColor",
  "controlStyles[16].styles[2]": "BorderBrush@Pressed:=$borderColor",
  "controlStyles[16].styles[3]": "BackgroundSizing=InnerBorderEdge",
  "controlStyles[17].target": "StartDocked.AppListViewItem > Grid@CommonStates > Border#BackgroundBorder",
  "controlStyles[17].styles[0]": "BorderThickness=1",
  "controlStyles[17].styles[1]": "BorderBrush@PointerOver:=$borderColor",
  "controlStyles[17].styles[2]": "BorderBrush@Pressed:=$borderColor",
  "controlStyles[17].styles[3]": "BackgroundSizing=InnerBorderEdge",
  "controlStyles[18].target": "Microsoft.UI.Xaml.Controls.DropDownButton > Grid@CommonStates",
  "controlStyles[18].styles[0]": "Background@PointerOver:=$background",
  "controlStyles[18].styles[1]": "Background@Pressed:=$background",
  "controlStyles[18].styles[2]": "BorderBrush@PointerOver:=$borderColor",
  "controlStyles[18].styles[3]": "BorderBrush@Pressed:=$borderColor",
  "controlStyles[18].styles[4]": "BackgroundSizing=InnerBorderEdge",
  "controlStyles[18].styles[5]": "Background@Normal:=$background",
  "controlStyles[18].styles[6]": "BorderBrush@Normal:=$borderColor",
  "controlStyles[18].styles[7]": "Padding=9,3,7,4",
  "controlStyles[19].target": "Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter#ContentPresenter > ContentControl > Grid#RootGrid > Grid#LogoContainer > Image#AllAppsTileLogo",
  "controlStyles[19].styles[0]": "RenderTransform@Pressed:=<ScaleTransform ScaleX=\"0.8\" ScaleY=\"0.8\" />",
  "controlStyles[19].styles[1]": "RenderTransformOrigin=0.5,0.5",
  "controlStyles[20].target": "Border#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Grid",
  "controlStyles[20].styles[0]": "RenderTransform@Pressed:=<ScaleTransform ScaleX=\"0.8\" ScaleY=\"0.8\" />",
  "controlStyles[20].styles[1]": "RenderTransformOrigin=0.5,0.5",
  "controlStyles[21].target": "Grid#ContentBorder@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Grid",
  "controlStyles[21].styles[0]": "RenderTransform@Pressed:=<ScaleTransform ScaleX=\"0.8\" ScaleY=\"0.8\" />",
  "controlStyles[21].styles[1]": "RenderTransformOrigin=0.5,0.5",
  "controlStyles[22].target": "ScrollViewer#MenuFlyoutPresenterScrollViewer > Border > Grid > ScrollContentPresenter > ItemsPresenter > StackPanel",
  "controlStyles[22].styles[0]": "ChildrenTransitions:=<TransitionCollection><EntranceThemeTransition IsStaggeringEnabled=\"False\" FromHorizontalOffset=\"-25\" FromVerticalOffset=\"0\" /></TransitionCollection>",
  "controlStyles[23].target": "FlyoutPresenter > Border > ScrollViewer > Border > Grid > ScrollContentPresenter > ContentPresenter > Border",
  "controlStyles[23].styles[0]": "BorderBrush:=$borderColor",
  "controlStyles[23].styles[1]": "BorderThickness=1",
  "controlStyles[24].target": "Button > ContentPresenter#ContentPresenter@CommonStates",
  "controlStyles[24].styles[0]": "Background@PointerOver:=$background",
  "controlStyles[24].styles[1]": "Background@Pressed:=$background",
  "controlStyles[24].styles[2]": "BorderBrush@PointerOver:=$borderColor",
  "controlStyles[24].styles[3]": "BorderBrush@Pressed:=$borderColor",
  "controlStyles[24].styles[4]": "BorderThickness=1",
  "controlStyles[24].styles[5]": "Background@Normal=Transparent",
  "controlStyles[25].target": "Grid@SearchBoxInputStates > Border#TaskbarSearchBackground",
  "controlStyles[25].styles[0]": "CornerRadius=4",
  "controlStyles[25].styles[1]": "Background@ActiveInput:=$background",
  "controlStyles[25].styles[2]": "BorderBrush:=$borderColor",
  "controlStyles[25].styles[3]": "BorderThickness=1",
  "controlStyles[25].styles[4]": "Background@SearchBoxHover:=$background",
  "controlStyles[25].styles[5]": "Background@NoFocus:=$background",
  "controlStyles[25].styles[6]": "BackgroundTransition:=<BrushTransition Duration=\"0:0:0.083\" />",
  "controlStyles[26].target": "Border@CommonStates > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter > Grid > Grid#LogoContainer > Image",
  "controlStyles[26].styles[0]": "RenderTransform@Pressed:=<ScaleTransform ScaleX=\"0.8\" ScaleY=\"0.8\" />",
  "controlStyles[26].styles[1]": "RenderTransformOrigin=0.5,0.5",
  "controlStyles[27].target": "Grid#ContentBorder@CommonStates > ContentPresenter > Grid > Grid#LogoContainer > Grid",
  "controlStyles[27].styles[0]": "RenderTransform@Pressed:=<ScaleTransform ScaleX=\"0.8\" ScaleY=\"0.8\" />",
  "controlStyles[27].styles[1]": "RenderTransformOrigin=0.5,0.5",
  "webContentStyles[0].target": "*",
  "webContentStyles[0].styles[0]": "transition: background-color 0.083s ease-in-out !important",
  "webContentCustomJs": "",
  "styleConstants[0]": "borderColor=<LinearGradientBrush StartPoint=\"0,0\" EndPoint=\"0,1\"><GradientStop Color=\"#50808080\" Offset=\"0.0\" /><GradientStop Color=\"#50404040\" Offset=\"0.25\" /><GradientStop Color=\"#50808080\" Offset=\"1\" /></LinearGradientBrush>\"",
  "styleConstants[1]": "borderColor2=<LinearGradientBrush StartPoint=\"0,0\" EndPoint=\"0,1\"><GradientStop Color=\"#50808080\" Offset=\"1\" /><GradientStop Color=\"#50606060\" Offset=\"0.15\" /></LinearGradientBrush>",
  "styleConstants[2]": "background=<WindhawkBlur BlurAmount=\"10\" TintColor=\"#25323232\" TintOpacity=\"0.2\" />",
  "styleConstants[3]": "borderThickness=0.3,1,0.3,0.3",
  "styleConstants[4]": "borderThickness2=0.3,0.3,0.3,1",
  "resourceVariables[0].variableKey": "",
  "resourceVariables[0].value": ""
}
```

</details>
