# WindowGlass theme for Windows 11 Start Menu Styler

A theme that adds a modern, glassy aesthetic with a compact layout to the windows 11 Start Menu

**Author**: [Nathaniel4JC](https://github.com/Nathaniel4JC)

## Left/ Centered Aligned
![Left](Start_Menu.png)


## Notes
- This theme works best on Windows 11 **25H2** and later.
- This theme currently works on displays with a resolution **above** 1366x768.
- This theme places the start menu horizontally centered on the screen, reguardless of whether the taskbar icons are centered or left aligned.
- This theme combines the start menu with the Phone Link panel and will only work on the 'New Windows 11 Start Menu'


## Bonus
- This theme can style your lock screen as well. 

## Lock Screen
![Lock Screen](Lock_Screen.png) 

In order for it to work, you'll have to:
  - add 'LockApp.exe' to the 'Custom process inclusion list' in 'advanced settings' in the Start Menu Styler Mod.
  - Install [Vivo Sans En VF] and [Vivo Sans Clock Stencil] (https://github.com/Nathaniel4JC/Fonts/releases/download/Fonts/Vivo_Fonts.zip)


## More Details about this theme
- Theme is designed on Windows 11 - 24H2
- Compatible with both Light/ Dark mode

## For a complete WindowGlass themed UI, download the following mods and use the 'WindowGlass' theme:
- Windows 11 TaskBar Styler – for styling the Taskbar.
- Windows 11 Notification Center Styler - for styling the Notification Center and Action Center
- Windows 11 File Explorer Styler - for styling Windows Explorer windows

---

## Theme selection

The theme is integrated into the mod, and can be simply selected from the mod's
settings:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Settings" tab.
* Select the 'WindowGlass' theme and save the settings.

## Manual installation

The theme styles can also be imported manually. To do that, follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Advanced" tab.
* Copy the content below to the text box under "Mod settings" and click "Save".

<details>
<summary>Content to import (click to expand)</summary>

```json

{
  "controlStyles[0].target": "Border#AcrylicOverlay",
  "controlStyles[0].styles[0]": "Margin=0",
  "controlStyles[0].styles[1]": "BorderThickness=0",
  "controlStyles[0].styles[2]": "CornerRadius=10",
  "controlStyles[0].styles[3]": "Visibility=Collapsed",
  "controlStyles[1].target": "Border#AcrylicBorder",
  "controlStyles[1].styles[0]": "Background:=$Background",
  "controlStyles[1].styles[1]": "CornerRadius=$CornerRadius",
  "controlStyles[1].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[1].styles[3]": "BorderBrush:=$BorderBrush",
  "controlStyles[2].target": "StartMenu.SearchBoxToggleButton#SearchBoxToggleButton",
  "controlStyles[2].styles[0]": "Visibility=Visible",
  "controlStyles[2].styles[1]": "Width=340",
  "controlStyles[2].styles[2]": "Height=50",
  "controlStyles[2].styles[3]": "RenderTransform:=<TranslateTransform X=\"-185\" Y=\"35\"/>",
  "controlStyles[2].styles[4]": "Margin=0,-30,0,-50",
  "controlStyles[3].target": "Windows.UI.Xaml.Controls.Border#AppBorder",
  "controlStyles[3].styles[0]": "Background:=$Background",
  "controlStyles[3].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[3].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[4].target": "StartMenu.SearchBoxToggleButton#SearchBoxToggleButton > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Border#BorderElement",
  "controlStyles[4].styles[0]": "BorderThickness=$BorderThickness",
  "controlStyles[4].styles[1]": "CornerRadius=$CornerRadius",
  "controlStyles[5].target": "Border#TaskbarSearchBackground",
  "controlStyles[5].styles[0]": "Background:=$ElementBG",
  "controlStyles[5].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[5].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[5].styles[3]": "CornerRadius=$SearchBoxRadius",
  "controlStyles[5].styles[4]": "Width=500",
  "controlStyles[5].styles[5]": "RenderTransform:=<TranslateTransform X=\"-120\" />",
  "controlStyles[6].target": "Windows.UI.Xaml.Controls.Border#AppBorder",
  "controlStyles[6].styles[0]": "Background:=$Background",
  "controlStyles[6].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[6].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[6].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[7].target": "Cortana.UI.Views.RichSearchBoxControl#SearchBoxControl",
  "controlStyles[7].styles[0]": "Width=500",
  "controlStyles[7].styles[1]": "RenderTransform:=<TranslateTransform X=\"-120\" />",
  "controlStyles[8].target": "Windows.UI.Xaml.Controls.Border#BorderElement",
  "controlStyles[8].styles[0]": "Background=Transparent",
  "controlStyles[8].styles[1]": "BorderThickness=$BorderThickness",
  "controlStyles[9].target": "StartMenu.CategoryControl > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Border ",
  "controlStyles[9].styles[0]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[9].styles[3]": "Background:=$ElementBG",
  "controlStyles[9].styles[1]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[9].styles[2]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[10].target": "Windows.UI.Xaml.Controls.Border#BorderUnderline",
  "controlStyles[10].styles[0]": "Visibility=Visible",
  "controlStyles[11].target": "StackPanel#TimeAndDatePanel",
  "controlStyles[11].styles[0]": "VerticalAlignment=Top",
  "controlStyles[11].styles[1]": "HorizontalAlignment=Center",
  "controlStyles[11].styles[2]": "RenderTransform:=<TranslateTransform X=\"0\" />",
  "controlStyles[12].target": "StackPanel#TimePanel > TextBlock#Time",
  "controlStyles[12].styles[0]": "HorizontalAlignment=Center",
  "controlStyles[12].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"50\" />",
  "controlStyles[12].styles[2]": "FontFamily=vivo Sans Clock Stencil Regular",
  "controlStyles[12].styles[3]": "Foreground:=$ClockBG",
  "controlStyles[13].target": "StackPanel#TimeAndDatePanel > TextBlock#Date",
  "controlStyles[13].styles[0]": "HorizontalAlignment=Center",
  "controlStyles[13].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"-150\" />",
  "controlStyles[13].styles[2]": "FontFamily=vivo Sans EN VF",
  "controlStyles[13].styles[3]": "Foreground:=$ClockBG",
  "controlStyles[14].target": "Windows.UI.Xaml.Controls.Grid#WidgetFrameGrid",
  "controlStyles[14].styles[0]": "Background:=$Background",
  "controlStyles[14].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[14].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[14].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[15].target": "Windows.UI.Xaml.Controls.Grid#WidgetCanvasPanel",
  "controlStyles[15].styles[0]": "HorizontalAlignment=Center",
  "controlStyles[15].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"50\" />",
  "controlStyles[16].target": "Windows.UI.Xaml.Controls.Grid#MediaTransportControls",
  "controlStyles[16].styles[0]": "Background:=$Background",
  "controlStyles[16].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[16].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[16].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[17].target": "Windows.UI.Xaml.Controls.Grid#MediaControlsContainer",
  "controlStyles[17].styles[0]": "Visibility=Visible",
  "controlStyles[17].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"-785\" />",
  "controlStyles[17].styles[2]": "Margin=0,0,0,0",
  "controlStyles[17].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[18].target": "Windows.UI.Xaml.Controls.Border#BorderElement",
  "controlStyles[18].styles[0]": "CornerRadius=$CornerRadius",
  "controlStyles[19].target": "Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion",
  "controlStyles[19].styles[0]": "RenderTransform:=<TranslateTransform X=\"-120\" />",
  "controlStyles[19].styles[1]": "Visibility=1",
  "controlStyles[20].target": "Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicOverlay",
  "controlStyles[20].styles[0]": "BorderThickness=0",
  "controlStyles[21].target": "Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.Border",
  "controlStyles[21].styles[0]": "BorderBrush:=$BorderBrush",
  "controlStyles[21].styles[1]": "Background:=$Background",
  "controlStyles[21].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[21].styles[3]": "CornerRadius=$CornerRadius",
  "controlStyles[22].target": "Windows.UI.Xaml.Controls.Border#StartDropShadow",
  "controlStyles[22].styles[0]": "CornerRadius=$CornerRadius",
  "controlStyles[23].target": "Windows.UI.Xaml.Controls.Border#RightCompanionDropShadow",
  "controlStyles[23].styles[0]": "CornerRadius=$CornerRadius",
  "controlStyles[23].styles[1]": "Visibility=1",
  "controlStyles[24].target": "Windows.UI.Xaml.Controls.Grid#DroppedFlickerWorkaroundWrapper > Windows.UI.Xaml.Controls.Border#BackgroundBorder",
  "controlStyles[24].styles[0]": "Background@PointerOver:=$Background",
  "controlStyles[24].styles[1]": "Background@Pressed:=$Background",
  "controlStyles[24].styles[2]": "Background@Selected:=$Background",
  "controlStyles[25].target": "Windows.UI.Xaml.Controls.Border#BackgroundBorder",
  "controlStyles[25].styles[0]": "CornerRadius=10",
  "controlStyles[26].target": "Windows.UI.Xaml.Controls.Grid#ContentBorder",
  "controlStyles[26].styles[0]": "CornerRadius=10",
  "controlStyles[27].target": "Windows.UI.Xaml.Controls.Border#LayerBorder",
  "controlStyles[27].styles[0]": "CornerRadius=$CornerRadius",
  "controlStyles[28].target": "Windows.UI.Xaml.Controls.Grid#OuterBorderGrid",
  "controlStyles[28].styles[0]": "CornerRadius=$CornerRadius",
  "controlStyles[29].target": "Windows.UI.Xaml.Controls.Grid#MainMenu",
  "controlStyles[29].styles[0]": "",
  "controlStyles[30].target": "Windows.UI.Xaml.PopupRoot",
  "controlStyles[30].styles[0]": "CornerRadius=$CornerRadius",
  "controlStyles[31].target": "Windows.UI.Xaml.Controls.ContentPresenter#ZoomedInPresenter > Windows.UI.Xaml.Controls.GridView#AllAppsGrid > Windows.UI.Xaml.Controls.Border > Windows.UI.Xaml.Controls.ScrollViewer#ScrollViewer > Windows.UI.Xaml.Controls.Border#Root > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter#ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid",
  "controlStyles[31].styles[0]": "MaximumRowsOrColumns=2",
  "controlStyles[32].target": "Windows.UI.Xaml.Controls.Grid#RightCompanionContainerGrid",
  "controlStyles[32].styles[0]": "Margin=-420,142,0,50",
  "controlStyles[32].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"-90\" />",
  "controlStyles[32].styles[2]": "Width=300",
  "controlStyles[32].styles[3]": "Height=Auto",
  "controlStyles[32].styles[5]": "MaxHeight:=700",
  "controlStyles[32].styles[6]": "MinHeight:=300",
  "controlStyles[32].styles[4]": "CornerRadius=$CornerRadius",
  "controlStyles[33].target": "StartMenu.PinnedList#StartMenuPinnedList",
  "controlStyles[33].styles[0]": "Visibility=0",
  "controlStyles[33].styles[1]": "Margin=30,0,25,0",
  "controlStyles[33].styles[2]": "RenderTransform:=<TranslateTransform X=\"-0\" Y=\"0\" />",
  "controlStyles[33].styles[3]": "Height=Auto",
  "controlStyles[33].styles[4]": "MinHeight:=200",
  "controlStyles[33].styles[5]": "MaxHeight:=1000",
  "controlStyles[34].target": "Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText",
  "controlStyles[34].styles[0]": "Visibility=0",
  "controlStyles[34].styles[1]": "Margin=0",
  "controlStyles[34].styles[2]": "RenderTransform:=<TranslateTransform X=\"60\" Y=\"-10\" />",
  "controlStyles[35].target": "Microsoft.UI.Xaml.Controls.DropDownButton#ViewSelectionButton",
  "controlStyles[35].styles[0]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"0\" />",
  "controlStyles[36].target": "Windows.UI.Xaml.Controls.Grid#NavPanePlaceholder",
  "controlStyles[36].styles[0]": "Width=Auto",
  "controlStyles[36].styles[1]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"0\" />",
  "controlStyles[36].styles[2]": "Background:=$ElementBG",
  "controlStyles[36].styles[3]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[36].styles[4]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[36].styles[5]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[36].styles[6]": "Height=70",
  "controlStyles[36].styles[7]": "Padding=5",
  "controlStyles[36].styles[8]": "Margin=420,-100,0,0",
  "controlStyles[36].styles[9]": "MaxWidth:=300",
  "controlStyles[36].styles[10]": "MinWidth:=200",
  "controlStyles[37].target": "StartMenu.FolderModal#StartFolderModal",
  "controlStyles[37].styles[0]": "Margin=-100",
  "controlStyles[37].styles[1]": "Width=Auto",
  "controlStyles[37].styles[2]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"0\" />",
  "controlStyles[38].target": "Windows.UI.Xaml.Controls.Primitives.ScrollBar#VerticalScrollBar",
  "controlStyles[38].styles[0]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"0\" />",
  "controlStyles[39].target": "StartMenu.PinnedList#StartMenuPinnedList > Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.GridView#PinnedList > Windows.UI.Xaml.Controls.Border",
  "controlStyles[39].styles[0]": "Background:=$ElementBG",
  "controlStyles[39].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[39].styles[2]": "CornerRadius=$CornerRadius",
  "controlStyles[39].styles[3]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[39].styles[4]": "Padding:=20,10,0,10",
  "controlStyles[40].target": "Windows.UI.Xaml.Controls.Grid#TopLevelHeader > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Button",
  "controlStyles[40].styles[0]": "RenderTransform:=<TranslateTransform X=\"0\" Y=\"-5\" />",
  "controlStyles[41].target": "StartMenu.PinnedListTile > Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.Grid#DisplayNameAndDownloadIconContainer > Windows.UI.Xaml.Controls.TextBlock",
  "controlStyles[41].styles[0]": "Visibility=0",
  "controlStyles[42].target": "StartMenu.StartHome > Windows.UI.Xaml.Controls.Grid#FrameRoot",
  "controlStyles[42].styles[0]": "Margin=190,40,190,0",
  "controlStyles[42].styles[1]": "RenderTransform:=<TranslateTransform X=\"-190\" Y=\"0\" />",
  "controlStyles[42].styles[2]": "Padding=0,0,0-20",
  "controlStyles[43].target": "StartMenu.StartMenuCompanion#RightCompanion > Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicBorder",
  "controlStyles[43].styles[0]": "Background:=$ElementBG",
  "controlStyles[43].styles[1]": "BorderBrush:=$ElementBorderBrush",
  "controlStyles[43].styles[2]": "BorderThickness=$ElementBorderThickness",
  "controlStyles[43].styles[3]": "CornerRadius=$ElementCornerRadius",
  "controlStyles[44].target": "Windows.UI.Xaml.Controls.Grid#TopLevelHeader > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Button",
  "controlStyles[44].styles[0]": "Visibility=1",
  "controlStyles[45].target": "Windows.UI.Xaml.Controls.MenuFlyoutPresenter > Windows.UI.Xaml.Controls.Border",
  "controlStyles[45].styles[0]": "BorderBrush:=$BorderBrush",
  "controlStyles[45].styles[1]": "Background:=$Background",
  "controlStyles[45].styles[2]": "CornerRadius=15",
  "controlStyles[45].styles[3]": "BorderThickness=$BorderThickness",
  "controlStyles[46].target": "Windows.UI.Xaml.Controls.ToolTip > Windows.UI.Xaml.Controls.ContentPresenter#LayoutRoot",
  "controlStyles[46].styles[0]": "Background:=$Background",
  "controlStyles[46].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[46].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[46].styles[3]": "CornerRadius=15",
  "controlStyles[47].target": "Windows.UI.Xaml.Controls.Button#AddButton",
  "controlStyles[47].styles[0]": "Background:=$Background",
  "controlStyles[47].styles[1]": "BorderBrush:=$BorderBrush",
  "controlStyles[47].styles[2]": "BorderThickness=$BorderThickness",
  "controlStyles[47].styles[3]": "CornerRadius=15",
  "controlStyles[48].target": "StartMenu.StartBlendedFlexFrame > Windows.UI.Xaml.Controls.Grid#FrameRoot",
  "controlStyles[48].styles[0]": "Width=Auto",
  "controlStyles[48].styles[1]": "HorizontalAlignment=Center",
  "controlStyles[48].styles[2]": "MaxWidth:=1000",
  "controlStyles[48].styles[3]": "MinWidth:=500",
  "disableNewStartMenuLayout": 0,
  "webContentStyles[0].target": "",
  "webContentStyles[0].styles[0]": "",
  "resourceVariables[0].variableKey": "",
  "resourceVariables[0].value": "",
  "styleConstants[0]": "Background=<WindhawkBlur BlurAmount=\"15\" TintColor=\"#10808080\"/>",
  "styleConstants[1]": "BorderBrush2=<LinearGradientBrush StartPoint=\"0,0\" EndPoint=\"0,1\"><GradientStop Color=\"{ThemeResource SystemChromeHighColor}\" Offset=\"0.0\" /><GradientStop Color=\"{ThemeResource SystemChromeAltHighColor}\" Offset=\"0.25\" /><GradientStop Color=\"{ThemeResource SystemChromeHighColor}\" Offset=\"1\" /></LinearGradientBrush>",
  "webContentCustomJs": "",
  "styleConstants[2]": "BorderThickness=0.3,1,0.3,0.3",
  "styleConstants[3]": "CornerRadius=20",
  "styleConstants[4]": "ClockBG=<WindhawkBlur BlurAmount=\"20\" TintColor=\"{ThemeResource SystemAccentColorLight2}\" TintOpacity=\"0.3\" />",
  "styleConstants[5]": "SearchBoxRadius=15",
  "styleConstants[6]": "Background2=Transparent",
  "styleConstants[7]": "Background2=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeAltHighColor}\" TintOpacity=\"0.3\" FallbackColor=\"{ThemeResource SystemChromeAltHighColor}\" />",
  "styleConstants[8]": "ElementBG=<SolidColorBrush Color=\"{ThemeResource SystemChromeAltHighColor}\" Opacity=\"0.3\" />",
  "styleConstants[9]": "ElementBorderThickness=0.3,0.3,0.3,1",
  "styleConstants[10]": "ElementCornerRadius=20",
  "styleConstants[11]": "ElementBorderBrush=<LinearGradientBrush StartPoint=\"0,0\" EndPoint=\"0,1\"><GradientStop Color=\"#50808080\" Offset=\"1\" /><GradientStop Color=\"#50606060\" Offset=\"0.15\" /></LinearGradientBrush>",
  "styleConstants[12]": "BorderBrush=<LinearGradientBrush StartPoint=\"0,0\" EndPoint=\"0,1\"><GradientStop Color=\"#50808080\" Offset=\"0.0\" /><GradientStop Color=\"#50404040\" Offset=\"0.25\" /><GradientStop Color=\"#50808080\" Offset=\"1\" /></LinearGradientBrush>"
}
```
</details>
