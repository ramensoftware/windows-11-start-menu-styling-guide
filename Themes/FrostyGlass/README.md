# ❄️ Windows 11 Start Menu Styler: Frosty Glass Edition
> A refined, translucent "Frosty" experience for the redisigned Windows 11 Start Menu via Windhawk.

[![Windhawk](https://img.shields.io/badge/Requires-Windhawk-blue?style=flat-square)](https://windhawk.net/)
[![Style](https://img.shields.io/badge/Style-Frosty_Glass-lightgrey?style=flat-square)](#)

This configuration provides a modern **Frosty Glass** aesthetic for your Windows 11 Start Menu and Lock Screen. It utilizes custom translucent `AcrylicBrush` effects to create a soft, blurred interface that feels perfectly integrated with the desktop environment.

---

## 📋 Prerequisites

1. Download and install [Windhawk](https://windhawk.net/).
2. Inside Windhawk, search for and install the **Windows 11 Start Menu Styler** mod by Ramen Software.

---

## 📦 Manual Installation

The theme styles can be imported manually by following these steps:

1. Open the **Windows 11 Start Menu Styler** in Windhawk.
2. Go to the **Settings** tab and select **Textual mode**.
3. Copy the content below and click **Save settings**.

<details>
<summary>Content to import (click to expand)</summary>

```yaml
theme: ''
disableNewStartMenuLayout: ''
styleConstants:
  - Background=<AcrylicBrush TintColor="#10000020"/>
  - BorderBrush2=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="{ThemeResource SystemChromeHighColor}" Offset="0.0" /><GradientStop Color="{ThemeResource SystemChromeLowColor}" Offset="0.25" /><GradientStop Color="{ThemeResource SystemChromeHighColor}" Offset="1" /></LinearGradientBrush>
  - BorderThickness=1
  - CornerRadius=10
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#50808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#50808080" Offset="1" /></LinearGradientBrush>
  - Background2=<AcrylicBrush TintColor="{ThemeResource SystemChromeAltHighColor}" TintOpacity="0.3" FallbackColor="{ThemeResource SystemChromeAltHighColor}" />
  - TrayPadding=2
  - ElementBG=<SolidColorBrush Color="{ThemeResource SystemChromeAltHighColor}" Opacity="0.3" />
  - ElementBorderThickness=1
  - ElementBorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#50808080" Offset="1" /><GradientStop Color="#50606060" Offset="0.15" /></LinearGradientBrush>
  - ElementCornerRadius=10
  - CommonBgBrush=<WindhawkBlur BlurAmount=\"25\" TintColor=\"#25323232\"/>
  - ClockBG=<WindhawkBlur BlurAmount="8" TintColor="#FFFFFFFF"/>
  - Translucent=<WindhawkBlur BlurAmount="8" TintColor="#90FFFFFF"/>
  - Glass=<WindhawkBlur BlurAmount="9" TintColor="{ThemeResource SystemChromeHighColor}" TintOpacity="0.7" />
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeHighColor}" TintOpacity="0.7" />
  - Acrylic=<WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeHighColor}" TintOpacity="0.8" />
controlStyles:
  - target: StartDocked.SearchBoxToggleButton
    styles:
      - Height=32
      - Margin=32,30,32,59
      - CornerRadius=16
      - BorderThickness:=$BorderThickness
      - Background:=$Background
      - Width=Auto
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelSuggestionsListHeader
    styles:
      - Visibility=1
  - target: Grid#InnerContent
    styles:
      - Margin=0,120,0,0
  - target: Windows.UI.Xaml.Controls.Grid#SuggestionsParentContainer
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.TextBlock#DisplayName
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Internal.RootScrollViewer > ScrollContentPresenter > Border > StartMenu.StartBlendedFlexFrame > Grid#FrameRoot > Grid#AnimationRoot > Grid#MainMenu > Grid#MainContent > Frame#StartFrame > ContentPresenter > StartMenu.StartHome > Grid#PageRoot > SemanticZoom#TopLevelRoot > Grid > ScrollViewer#ScrollViewer > ScrollContentPresenter#ScrollContentPresenter > Grid > ContentPresenter#ZoomedInPresenter > GridView#AllAppsGrid > Border > ScrollViewer#ScrollViewer > Border#Root > Grid > ScrollContentPresenter#ScrollContentPresenter > ItemsPresenter > ContentControl > ContentPresenter > Grid#TopLevelHeader > Grid#ShowMorePinnedGrid > Button
    styles:
      - CornerRadius=7
      - Height=32
      - RenderTransform:=<TranslateTransform X="5" Y="0" />
      - Visibility=1
  - target: Border#AcrylicBorder
    styles:
      - Background:=$Background
      - CornerRadius=$CornerRadius
      - BorderThickness=$BorderThickness
      - BorderBrush:=$BorderBrush
  - target: Border#AppBorder
    styles:
      - Background:=$Background
      - CornerRadius:=$CornerRadius
      - BorderThickness:=$BorderThickness
      - BorderBrush:=$BorderBrush
  - target: StartMenu.CategoryControl > Windows.UI.Xaml.Controls.Grid#RootGrid > Windows.UI.Xaml.Controls.Border
    styles:
      - BorderThickness:=$ElementBorderThickness
      - Background:=$ElementBG
      - CornerRadius:=$ElementCornerRadius
      - BorderBrush:=$ElementBorderBrush
  - target: Windows.UI.Xaml.Controls.Border#BorderElement
    styles:
      - BorderThickness:=$BorderThickness
      - CornerRadius=16
      - Background:=Transparent
  - target: Windows.UI.Xaml.Controls.Border#BorderUnderline
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.Grid#WidgetFrameGrid
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness:=$BorderThickness
      - CornerRadius=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Grid#MediaTransportControls
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness:=$BorderThickness
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Grid#MediaControlsContainer
    styles:
      - Visibility=1
      - RenderTransform:=<TranslateTransform X="0" Y="0" />
      - Margin=0,0,0,0
      - CornerRadius=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicOverlay
    styles:
      - BorderThickness=0
  - target: Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.Border
    styles:
      - BorderBrush:=$BorderBrush
      - Background:=$Background
      - BorderThickness:=$BorderThickness
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Border#RootGridDropShadow
    styles:
      - CornerRadius=$CornerRadius
      - Visibility=0
  - target: Windows.UI.Xaml.Controls.Border#RightCompanionDropShadow
    styles:
      - CornerRadius:=$CornerRadius
      - Visibility=0
  - target: Windows.UI.Xaml.Controls.Grid#DroppedFlickerWorkaroundWrapper > Windows.UI.Xaml.Controls.Border#BackgroundBorder
    styles:
      - Background@PointerOver:=$Background
      - Background@Pressed:=$Background
      - Background@Selected:=$Background
      - CornerRadius:=$CornerRadius
      - Height=Auto
      - Width=Auto
      - RenderTransform:=<TranslateTransform X="0" Y="-14" />
      - Margin=20,15,20,15
  - target: Windows.UI.Xaml.Controls.Grid#ContentBorder
    styles:
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Border#BackgroundBorder
    styles:
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Border#LayerBorder
    styles:
      - CornerRadius:=$CornerRadius
      - Background:=Transparent
      - BorderBrush:=$BorderBrush
      - BorderThickness:=$BorderThickness
  - target: Windows.UI.Xaml.Controls.Grid#OuterBorderGrid
    styles:
      - Visibility=0
      - BorderBrush:=Transparent
      - Background:=Transparent
      - BorderThickness:=0
  - target: Windows.UI.Xaml.PopupRoot
    styles:
      - Visibility=0
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.ContentPresenter#ZoomedInPresenter > Windows.UI.Xaml.Controls.GridView#AllAppsGrid > Windows.UI.Xaml.Controls.Border > Windows.UI.Xaml.Controls.ScrollViewer#ScrollViewer > Windows.UI.Xaml.Controls.Border#Root > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.ScrollContentPresenter#ScrollContentPresenter > Windows.UI.Xaml.Controls.ItemsPresenter > Windows.UI.Xaml.Controls.ItemsWrapGrid
    styles:
      - MaximumRowsOrColumns=3
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText
    styles:
      - Visibility=1
  - target: Microsoft.UI.Xaml.Controls.DropDownButton#ViewSelectionButton
    styles:
      - RenderTransform:=<TranslateTransform X="0" Y="0" />
      - Visibility=1
  - target: StartMenu.PinnedList#StartMenuPinnedList > Windows.UI.Xaml.Controls.Grid#Root > Windows.UI.Xaml.Controls.GridView#PinnedList > Windows.UI.Xaml.Controls.Border
    styles:
      - Background:=Transparent
      - BorderBrush:=Transparent
      - CornerRadius=$CornerRadius
      - BorderThickness:=0
      - Margin:=0,35,0,0
      - HorizontalAlignment=Center
      - VerticalAlignment=Center
  - target: StartMenu.StartMenuCompanion#RightCompanion > Windows.UI.Xaml.Controls.Grid#CompanionRoot > Windows.UI.Xaml.Controls.Border#AcrylicBorder
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness:=$BorderThickness
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Grid#TopLevelHeader > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Button
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.MenuFlyoutPresenter > Windows.UI.Xaml.Controls.Border
    styles:
      - BorderBrush:=$BorderBrush
      - Background:=$Background
      - CornerRadius:=$CornerRadius
      - BorderThickness:=$BorderThickness
  - target: Windows.UI.Xaml.Controls.ToolTip > Windows.UI.Xaml.Controls.ContentPresenter#LayoutRoot
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness:=$BorderThickness
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.Button#AddButton
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness:=$BorderThickness
      - CornerRadius:=$CornerRadius
      - Visibility=1
  - target: Windows.UI.Xaml.Internal.RootScrollViewer > ScrollContentPresenter > Border > StartMenu.StartBlendedFlexFrame > Grid#FrameRoot
    styles:
      - Width=Auto
      - HorizontalAlignment=Center
      - VerticalAlignment=Center
      - Margin=0
  - target: Windows.UI.Xaml.Controls.Grid#MainMenu
    styles:
      - MaxWidth:=Auto
  - target: StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.Border#BorderElement
    styles:
      - Background:=$Background
      - BorderThickness:=$BorderThickness
      - Visibility=0
  - target: Border#AcrylicOverlay
    styles:
      - Visibility=1
  - target: Border#LayerBorder
    styles:
      - Visibility=1
      - BorderThickness:=$BorderThickness
      - BorderBrush:=$BorderBrush
      - CornerRadius:=$CornerRadius
      - Background:=Transparent
  - target: Grid#TopLevelSuggestionsRoot
    styles:
      - Visibility=1
  - target: StartDocked.PowerOptionsView
    styles:
      - Margin=0,0,-480,0
      - HorizontalAlignment=Right
  - target: StartDocked.UserTileView
    styles:
      - Margin=340,-5,-340,0
      - Height=45
      - MaxWidth=Auto
  - target: StartMenu.PinnedList
    styles:
      - Height=350
      - Margin=0,-25,0,-400
      - Visibility=0
      - HorizontalAlignment=Left
      - VerticalAlignment=Center
  - target: Grid@SearchBoxInputStates > Border#TaskbarSearchBackground
    styles:
      - Background:=$Background
  - target: Windows.UI.Xaml.Controls.Grid#MediaTransportControls
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
      - Width=Auto
  - target: Windows.UI.Xaml.Controls.Grid#MediaControlsContainer
    styles:
      - Visibility=0
      - RenderTransform:=<TranslateTransform X="0" Y="-4" />
      - Margin=0,0,0,0
      - CornerRadius=$CornerRadius
      - HorizontalAlignment=Center
  - target: Windows.UI.Xaml.Controls.ListView#MediaButtonsListView
    styles:
      - Width=Auto
      - Visibility=0
      - VerticalAlignment=Center
      - Height=20
      - Margin=130,-60,0,0
      - HorizontalAlignment=Right
  - target: Windows.UI.Xaml.Controls.Button#PlayPauseButton
    styles:
      - Width=32
      - Height=35
      - Margin=0
      - HorizontalAlignment=Center
      - Padding=0,0,0,0
      - CornerRadius:=7
      - Visibility=0
  - target: Windows.UI.Xaml.Controls.Primitives.RepeatButton#PreviousButton
    styles:
      - Width=32
      - Height=35
      - Margin=10,0,0,0
      - HorizontalAlignment=Center
      - Padding=0,0,2,0
      - CornerRadius:=7
  - target: Windows.UI.Xaml.Controls.Primitives.RepeatButton#NextButton
    styles:
      - Width=32
      - Height=35
      - Margin=10,0,10,0
      - Padding=0,0,-1.5,0
      - CornerRadius:=7
  - target: StackPanel#TimePanel > TextBlock#Time
    styles:
      - HorizontalAlignment:=Center
      - RenderTransform:=<TransformGroup><TranslateTransform X="0" Y="0" /><ScaleTransform ScaleX="1" ScaleY="1" /></TransformGroup>
      - Foreground:=$Translucent
      - FontSize=150
      - FontFamily=Quicksand SemiBold
  - target: StackPanel#TimeAndDatePanel > TextBlock#Date
    styles:
      - HorizontalAlignment=Center
      - RenderTransform:=<TranslateTransform X="0" Y="-190" />
      - Foreground:=$ClockBG
      - FontFamily=Segoe UI VF
  - target: Windows.UI.Xaml.Controls.FlyoutPresenter
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness:=$BorderThickness
      - CornerRadius:=$CornerRadius
  - target: Windows.UI.Xaml.Controls.FlyoutPresenter > Windows.UI.Xaml.Controls.Border > Windows.UI.Xaml.Controls.ScrollViewer  > Windows.UI.Xaml.Controls.Border  > Windows.UI.Xaml.Controls.Grid  > Windows.UI.Xaml.Controls.ScrollContentPresenter  > Windows.UI.Xaml.Controls.ContentPresenter > Windows.UI.Xaml.Controls.Border
    styles:
      - Background:=Transparent
      - CornerRadius=$CornerRadius
      - BorderBrush:=Transparent
  - target: Windows.UI.Xaml.Controls.HyperlinkButton
    styles:
      - Height=22
      - Padding=4,0,4,2
      - Margin=0,2,0,0
      - CornerRadius=5
  - target: TextBlock#UserTileNameText
    styles:
      - Visibility=1
  - target: Windows.UI.Xaml.Controls.TextBlock#AllListHeadingText
    styles:
      - Visibility=1
  - target: StartDocked.UserTileView > StartDocked.NavigationPaneButton > Grid@CommonStates > Border
    styles:
      - CornerRadius=10
      - Width=45
  - target: StartMenu.SearchBoxToggleButton#SearchBoxToggleButton
    styles:
      - Width=520
      - Margin=-4,0,0,0
      - Visibility=0
  - target: StartMenu.SearchBoxToggleButton > Grid@CommonStates > Border#BorderElement
    styles:
      - Background:=$Background
  - target: Windows.UI.Xaml.Controls.Border#BackplateBorder
    styles:
      - Background:=Transparent
      - BorderBrush:=Transparent
      - BorderThickness:=Transparent
      - CornerRadius:=Transparent
      - Width=Auto
      - Height=40
      - Margin=0,0,2,3
      - Visibility=0
  - target: Windows.UI.Xaml.Controls.Grid#NetworkIconV2
    styles:
      - Margin=0,0,-10,0
  - target: Windows.UI.Xaml.Controls.Grid#NewBatteryIcon
    styles:
      - Margin=0,0,-2,0
  - target: Windows.UI.Xaml.Controls.Primitives.ScrollBar
    styles:
      - Visibility=1
  - target: StartDocked.NavigationPaneView > Windows.UI.Xaml.Controls.Grid#RootPanel
    styles:
      - Margin=-100,0,488,0
  - target: Grid#FrameRoot
    styles:
      - Height=597
      - MinWidth=666
  - target: Windows.UI.Xaml.Controls.ScrollContentPresenter > Windows.UI.Xaml.Controls.Border > Cortana.UI.Views.TaskbarSearchPage > Grid#RootGrid
    styles:
      - Width=666
      - Margin=0,153,0,0
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion
    styles:
      - Margin=-70,0,0,0
      - CornerRadius:=5
themeResourceVariables:
  - ''
webContentStyles:
  - target: '#qfPreviewPane'
    styles:
      - 'min-width: 325px !important'
webContentCustomJs: ''
resourceVariables:
  - variableKey: ''
    value: ''

```

</details>

---

## 🎨 Recommended Setup for Uniformity
To achieve the exact minimalist "Frosty Glass" look seen in the screenshots, I recommend the following setup:

* **Minimalist Start Menu Folders:** Use only one folder in the Start Menu (e.g., Settings). This keeps the UI balanced, placing the power button on the right and your folder on the left. Adding more than one folder can disrupt the visual symmetry.

---

## 🔒 Bonus: Apply Styling to the Lock Screen
This theme includes custom styling for the Windows 11 Lock Screen (Clock, Date and Media Controls styling). To enable it, you need to allow the mod to target the lock screen process:

1. Open the "Windows 11 Start Menu Styler" mod settings in Windhawk.
2. Go to the **Advanced** tab.
3. Scroll down to **Custom process inclusion list**.
4. Type exactly this in the box: `LockApp.exe`
5. Click **Save**. Press `Win + L` to lock your PC and enjoy your new Frosty Lock Screen!

> **🔤 Important Note on Fonts:** 
> This theme uses specific fonts to achieve the clean, modern look shown in image_e6d7c2.png. Please install them before applying the mod:
> * **Clock Font:** [Quicksand](https://fonts.google.com/specimen/Quicksand?preview.script=Latn) 
> * **Date Font:** Segoe UI VF (system font)
>
> **How to apply them:**
> Open the mod settings in Windhawk, scroll through the styles list to find the Lock Screen targets, and update the `FontFamily` property. You must use the **exact name of the font as it appears installed in your Windows system** (for example, in my setup I use `Quicksand SemiBold` for the clock and `Segoe UI VF` for the date).

---

## 📸 Showcase

### ❄️ Start Menu & Search Style

<img width="2880" height="1800" alt="Screenshot 2026-06-30 115600" src="https://github.com/user-attachments/assets/1328ebd3-3831-485b-a111-286450ac0914" />
<img width="2880" height="1800" alt="Screenshot 2026-06-30 115623" src="https://github.com/user-attachments/assets/10d74d02-de1f-4d1d-a570-540c516e2930" />
<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/4db7877c-2a00-43a8-a4df-0707af11240b" />

### 🔒 Lock Screen Style

<img width="2880" height="1800" alt="image" src="https://github.com/user-attachments/assets/5d85068d-f56e-43a2-9e93-f9c5aa5a02d6" />

---

## 🔗 Related Projects

Complete the look across your entire UI! Check out my other Frosty Glass styling repositories:
* [❄️ Frosty Glass Taskbar Styler](https://github.com/guidolamanna/windows-11-taskbar-styling-guide/blob/main/Themes/FrostyGlass/README.md) to apply this exact same aesthetic to your Taskbar, Alt+Tab menu, volume sliders, and more!
* [❄️ Frosty Glass Notification Center Styler](https://github.com/guidolamanna/windows-11-notification-center-styling-guide/blob/main/Themes/FrostyGlass/README.md) to theme your Notifications, Calendar, and Control Center flyouts!

---

## 🙌 Credits & Inspiration

A huge thank you to [Ramen Software](https://github.com/ramensoftware) for creating Windhawk. This configuration was heavily inspired by the official [Windows 11 Start Menu Styling Guide](https://github.com/ramensoftware/windows-11-start-menu-styling-guide) and the Windhawk modding community.

---

*Created by [Guido Lamanna](https://github.com/guidolamanna)*
