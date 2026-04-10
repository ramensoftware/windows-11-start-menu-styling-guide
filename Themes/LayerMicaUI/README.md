# LayerMicaUI theme for Windows 11 Start Menu Styler

**Author**: [Nimai-HK](https://github.com/Nimai-HK)

LayerMicaUI is a theme with adaptive layouts for the new Windows 11 25H2 Start menu.

![GIF](theme-preview.gif)

<table style="width:100%;">
  <tr>
    <td style="height:20%; text-align:center;"><img src="screenshot-expanded.png" style="width:auto; height:100%; display:block; margin:auto;"></td>
    <td style="height:20%; text-align:center;"><img src="screenshot-collapsed.png" style="width:auto; height:100%; display:block; margin:auto;"></td>
    <td style="height:20%; text-align:center;"><img src="screenshot-folderview.png" style="width:auto; height:100%; display:block; margin:auto;"></td>
  </tr>
</table>

> [!IMPORTANT]
> This theme is designed for the [redesigned Windows 11 Start menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/) that is gradually rolling out with the 25H2 update.

## Notes
- Optimized for Windows 11 **25H2** and later with the new Start menu.
- Integrates the Start menu with the Phone Link panel.
- Supports screen resolutions of **1280×720** and above.
- Start menu aligns with the taskbar position.
- Fully compatible with both light and dark modes.
- Suggestions and recommended sections are hidden.
- Recommended to disable Start menu folders.

---

## Additional customization
<details>
  <summary>Font Customization (Click to expand)</summary>

- Font to be installed: [Nunito](https://fonts.google.com/specimen/Nunito)
- Add these items to the "Style constants" section of the settings page of the Windows 11 Start Menu Styler Mod

  ```
  ThFntWt=Semibold
  ThHdnWt=Bold
  ```
</details>

<details>
  <summary>Taskbar Search Bar (Click to expand)</summary>

- The taskbar search bar in clicked/active state is styled by this theme.
- *If you use the [LayerMicaUI Taskbar Styler Theme](https://github.com/ramensoftware/windows-11-taskbar-styling-guide/tree/main/Themes/LayerMicaUI), this change is recommended.*

    ```yaml
    - target: Border#TaskbarSearchBackground
      styles:
        - CornerRadius=$InnerRadius
        - Background:=$ThemeOverlay
        - BorderThickness=0
        - Height=32
        - Transform3D:=<CompositeTransform3D TranslateY="-2" TranslateX="1"/>

    - target: Cortana.UI.Views.RichSearchBoxControl#SearchBoxControl > Grid#RootGrid
      styles:
        - CornerRadius=$InnerRadius
        - Transform3D:=<CompositeTransform3D TranslateY="-2" TranslateX="1"/>
    ```
</details>

<details>
  <summary>Hide Phone Link Companion Button (Click to expand)</summary>

- To hide the Phone Link Companion button:

  ```yaml
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion
    styles:
      - Visibility=1
  ```
</details>

---
## Some More Information
- Start menu and Phone Link panel use separate surfaces, and on certain backgrounds the seam between them may be visible.
- Start menu and Search window have fixed heights to prevent element displacement.

## Other LayerMicaUI Themes
- [LayerMicaUI Taskbar Theme](https://github.com/ramensoftware/windows-11-taskbar-styling-guide/tree/main/Themes/LayerMicaUI)

- [LayerMicaUI Notification And Control Center Theme](https://github.com/ramensoftware/windows-11-notification-center-styling-guide/tree/main/Themes/LayerMicaUI)

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
styleConstants:
  - ThemeBorder=<SolidColorBrush Color="{ThemeResource Border}" />
  - OuterRadius=10
  - InnerRadius=8
  - ThFnt=Nunito
  - ThemeOverlay=<SolidColorBrush Color="{ThemeResource Overlay}" />
  - ThFntWt=Normal
  - ThHdnWt=Semibold
  - ThemeBtn=<SolidColorBrush Color="{ThemeResource Btn}"/>
  - ThemeControlBorder=<SolidColorBrush Color="{ThemeResource ControlBorder}" />
  - ThemeOutBorder=<SolidColorBrush Color="#66757575"/>
  - ThemeFlyout=<AcrylicBrush BackgroundSource="Backdrop" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.1" TintLuminosityOpacity="0.8" FallbackColor="{ThemeResource SystemChromeMediumColor}" />
controlStyles:
  - target: Border#AcrylicBorder
    styles:
      - CornerRadius=$OuterRadius
      - BorderThickness=1
      - Width=445
      - // Main Background of the Start Menu
  - target: Grid#MainMenu > Grid#MainContent > Border#AcrylicOverlay
    styles:
      - Margin=9,-3,9,-55
      - CornerRadius=8,8,10,10
      - BorderThickness=1
      - Background:=$ThemeOverlay
      - // Acrylic Overlay of the Start Menu
  - target: StartDocked.PowerOptionsView > StartDocked.NavigationPaneButton > Grid@CommonStates > Border
    styles:
      - CornerRadius=0,8,8,0
      - Margin=-2,-1,-2,-1
      - BorderThickness=1
      - Background@Normal:=$ThemeOverlay
      - Background@Pressed:=$ThemeBtn
      - Background@PointerOver:=$ThemeBtn
      - Background@Disabled:=$ThemeOverlay
      - BorderBrush:=$ThemeControlBorder
      - // Power Button > Background
  - target: StartDocked.UserTileView > StartDocked.NavigationPaneButton > Grid@CommonStates > Border
    styles:
      - Margin=0,-1,0,-1
      - CornerRadius=0
      - Background@Pressed:=$ThemeBtn
      - BorderThickness=0,1,0,1
      - Width=48
      - Background@PointerOver:=$ThemeBtn
      - Background@Normal:=$ThemeOverlay
      - Background@Disabled:=$ThemeOverlay
      - Background:=$ThemeOverlay
      - BorderBrush:=$ThemeControlBorder
      - // User Profile > Background
  - target: StartMenu.SearchBoxToggleButton#SearchBoxToggleButton > Grid@CommonStates > Border
    styles:
      - Background@Normal:=$ThemeOverlay
      - CornerRadius=8,0,0,8
      - BorderBrush:=$ThemeControlBorder
      - BorderThickness=1
      - Background@PointerOver:=$ThemeBtn
      - Background@Pressed:=$ThemeBtn
      - Background:=$ThemeOverlay
      - // Start Menu Search Box Background
  - target: Border#ContentBorder > Grid#DroppedFlickerWorkaroundWrapper > Border@CommonStates
    styles:
      - Margin=1
      - // Fixes something
  - target: StartMenu.FolderModal#StartFolderModal > Grid#Root > Border
    styles:
      - BorderThickness=1
      - Width=340
      - Height=350
      - Margin=5,0,0,0
      - BorderBrush:=$ThemeOutBorder
      - Background:=$ThemeFlyout
      - // Start Menu Open Folder Background
  - target: Border#StartDropShadow
    styles:
      - Width=445
      - Visibility=1
      - // Start Menu Shadow
  - target: StartMenu.StartMenuCompanion#RightCompanion > Grid#CompanionRoot > Border#AcrylicBorder
    styles:
      - Width=225
      - CornerRadius=0,$OuterRadius,$OuterRadius,0
      - BorderBrush:=$ThemeOutBorder
      - BorderThickness=0,1,1,1
      - // Phone Link Companion > Main Background
  - target: StartMenu.StartMenuCompanion#RightCompanion > Grid#CompanionRoot > Grid#MainContent > Border#AcrylicOverlay
    styles:
      - Margin=20,170,20,-2
      - BorderThickness=0,1,0,1
      - CornerRadius=0
      - Background:=Transparent
      - BorderBrush:=$ThemeControlBorder
      - // Phone Link Companion > Acrylic Overlay
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Border
    styles:
      - Background:=$ThemeOverlay
      - BorderBrush:=$ThemeControlBorder
      - BorderThickness=1
      - Background:=$ThemeOverlay
      - // Phone Link Panel Show-Hide Button Background
  - target: Border > ScrollViewer#ScrollViewer > Border#Root > Grid > ScrollContentPresenter#ScrollContentPresenter > ItemsPresenter > ItemsWrapGrid > GridViewItem > Border#ContentBorder > Grid#DroppedFlickerWorkaroundWrapper > Border#BackgroundBorder
    styles:
      - CornerRadius=$InnerRadius
      - // Adds a rounded corner to list view items
  - target: StartMenu.PinnedList#StartMenuPinnedList > Grid#Root > GridView#PinnedList > Border
    styles:
      - Padding=0,5,0,10
      - BorderThickness=0,0,0,1
      - BorderBrush:=$ThemeControlBorder
      - Margin=0,0,0,-25
      - // Start Menu Pinned List Background
  - target: ScrollViewer#ScrollViewer > Border#Root > Grid > ScrollContentPresenter#ScrollContentPresenter > ItemsPresenter > ItemsStackPanel > ListViewItem > Grid#ContentBorder > Border#BorderBackground
    styles:
      - CornerRadius=$InnerRadius
      - // Adds a rounded corner to some other list view items
  - target: GridViewHeaderItem > Border > ContentPresenter#ContentPresenter > Button#Header > Border#Border
    styles:
      - CornerRadius=$InnerRadius
      - // Adds a rounded corner to some other list view items
  - target: ScrollContentPresenter > Border
    styles:
      - MaxHeight=665
      - VerticalAlignment=Bottom
      - MinWidth=700
      - // Start menu and Search Host Sizing, Main root of both.
  - target: Cortana.UI.Views.TaskbarSearchPage > Grid#RootGrid > Grid#OuterBorderGrid > Grid#BorderGrid > Border#LayerBorder
    styles:
      - Visibility=1
      - // Search page Tinted Overlay
  - target: Cortana.UI.Views.TaskbarSearchPage > Grid#RootGrid > Grid#OuterBorderGrid > Grid#BorderGrid > Border#AppBorder
    styles:
      - BorderBrush:=$ThemeOutBorder
      - CornerRadius=$OuterRadius
      - Margin=1
      - // Search Page Main Background
  - target: MenuFlyoutPresenter > Border
    styles:
      - Background:=$ThemeFlyout
      - BorderBrush:=$ThemeOutBorder
      - // Right Click Menu > Background
  - target: Button#ZoomInButton > Grid > Border#BackgroundBorder
    styles:
      - CornerRadius=$InnerRadius
      - // Zoom into list view button
  - target: ListView#ZoomedOutListView > Border > ScrollViewer#ScrollViewer > Border#Root > Grid > ScrollContentPresenter#ScrollContentPresenter > ItemsPresenter > ItemsWrapGrid > ListViewItem > Grid#ContentBorder > Border#BorderBackground
    styles:
      - CornerRadius=$InnerRadius
      - BorderBrush:=$ThemeControlBorder
      - // Adds a rounded corner to some other list view items
  - target: Border#RightCompanionDropShadowDismissTarget
    styles:
      - Visibility=1
      - // Phone Link Companion Shadow and something
  - target: Border#RightCompanionDropShadow
    styles:
      - Visibility=1
      - // Phone Link Companion Shadow
  - target: Border#LeftCompanionDropShadowDismissTarget
    styles:
      - Visibility=1
      - // Start Menu Shadow with Phone Link Companion Active
  - target: Border#DropShadowDismissTarget
    styles:
      - Visibility=1
      - // Start Menu Normal Shadow
  - target: Grid#TopLevelHeader > Grid
    styles:
      - RenderTransform:=<TranslateTransform X="3" Y="-8" />
      - Canvas.ZIndex=99
      - // Pinned List Heading grid
  - target: StartMenu.StartMenuCompanion#RightCompanion > Grid#CompanionRoot > Grid#MainContent > ContentPresenter#PrimaryCardContainer
    styles:
      - Margin=0,0,0,-8
      - // Phone Link Companion > Actions + Recents Card
  - target: Grid#CommandSpace > Button#PrimaryButton > ContentPresenter#ContentPresenter
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - // Not Sure Which Button's font I changed
  - target: Grid#CommandSpace > Button#SecondaryButton > Button#CloseButton > ContentPresenter#ContentPresenter
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - // Not Sure Which Button's font I changed
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Border > ContentPresenter#ContentPresenter
    styles:
      - Height=42
      - Width=45
      - CornerRadius=0
      - // Phone Link Panel Show-Hide Button Icon
  - target: Cortana.UI.Views.CortanaRichSearchBox#SearchTextBox
    styles:
      - FontFamily=$ThFnt
      - FontSize=14
      - FontWeight=$ThFntWt
      - // Taskbar Search Box Font
  - target: Frame#StartFrame
    styles:
      - Margin=0,-10,0,0
      - // Start Menu Frame
  - target: Grid#SuggestionsParentContainer
    styles:
      - Visibility=Collapsed
      - // Suggestions Container
  - target: Grid#TopLevelSuggestionsListHeader
    styles:
      - Visibility=Collapsed
      - // Suggestions Header
  - target: Grid#GridViewContainer
    styles:
      - Width=360
      - Margin=5,0,-5,0
      - // Might be Start Menu Folder Container
  - target: Grid#FrameRoot
    styles:
      - Height=665
      - // Base Frame Size
  - target: Grid#MainMenu
    styles:
      - Width=445
      - CornerRadius=$OuterRadius
      - // Start Menu Main List ( Pinned + All Apps )
  - target: ScrollViewer > ScrollContentPresenter > Border > StartMenu.StartBlendedFlexFrame > Grid#FrameRoot
    styles:
      - Margin=0
      - // Start Menu Frame Padding
  - target: Grid#RightCompanionContainerGrid
    styles:
      - Width=221
      - Padding=-10,0,0,0
      - RenderTransform:=<TranslateTransform X="-9" />
      - // Phone Link Panel Grid Container
  - target: Grid#CompanionRoot
    styles:
      - Width=225
      - // Phone Link Panel Base Sizing Grid
  - target: StartMenu.StartMenuCompanion#RightCompanion > Grid#CompanionRoot > Grid#MainContent > Grid#ActionsBar
    styles:
      - Transform3D:=<CompositeTransform3D TranslateX="-3"/>
      - // Phone Link Panel Send and Three dots Region Bar
  - target: Grid#AllListHeading > Microsoft.UI.Xaml.Controls.DropDownButton#ViewSelectionButton > Grid#RootGrid
    styles:
      - CornerRadius=$InnerRadius
      - Margin=2,0,0,0
      - // All Apps Heading Grid > View type button
  - target: Grid#NavPanePlaceholder
    styles:
      - Margin=310,-577,-17,576
      - Width=96
      - // Navigation Pane of Start Menu ( Userprofile, Powerbutton, Folder Lists )
  - target: Grid#AllListHeading
    styles:
      - Margin=0,80,-5,0
      - // All Apps Heading Grid
  - target: Grid#NoTopLevelSuggestionsText
    styles:
      - Height=0
      - Visibility=1
      - // Start Menu > Suggested Section Header
  - target: Grid#ShowMoreSuggestions
    styles:
      - Height=0
      - Visibility=1
      - // Start Menu > Suggested Section > Show More Button Region
  - target: Grid#TopLevelSuggestionsRoot > Grid[2]
    styles:
      - MinHeight=0
      - Visibility=1
      - // Start Menu > Suggestions Grid 2
  - target: GridView#PinnedList
    styles:
      - Margin=9,0,-9,-60
      - // Start Menu > Pinned List Position Grid
  - target: GridView#RecommendedList
    styles:
      - Visibility=1
      - // Start menu > Recommended section > List
  - target: StartMenu.PinnedList#StartMenuPinnedList
    styles:
      - Margin=0,-30,0,0
      - Padding=0
      - // Start Menu > Pinned List Root
  - target: Microsoft.UI.Xaml.Controls.PipsPager#PipsPager
    styles:
      - Margin=-30,-10,0,10
      - // Folder Open > Scrolling Dots
  - target: StartDocked.PowerOptionsView
    styles:
      - Margin=-3,0,3,0
      - // Power Button Root
  - target: Cortana.UI.Views.TaskbarSearchPage > Grid#RootGrid > Grid#QueryFormulationRoot
    styles:
      - Margin=0,-4,0,10
      - // Search Page > Main Results grid
  - target: StartMenu.SearchBoxToggleButton#SearchBoxToggleButton
    styles:
      - Height=42
      - Margin=-23,-2,72,0
      - // Start Menu > Search Box Button Root
  - target: StartMenu.StartHome
    styles:
      - Width=450
      - Margin=-15,8,5,-53
      - // Start Menu > Contents Base grid
  - target: TextBlock#ZoomedOutHeading
    styles:
      - Visibility=1
      - // Start Menu > Zoomed Out list > Heading Text
  - target: TextBlock#DisplayName
    styles:
      - Margin=8,3,8,0
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - // Pinned List Apps > Name Textblock
  - target: TextBlock#PinnedListHeaderText
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThHdnWt
      - Margin=62,6,0,-6
      - // Pinned List title Text
  - target: TextBlock#AllListHeadingText
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThHdnWt
      - // All Apps List title text
  - target: TextBlock#UserTileNameText
    styles:
      - Visibility=1
      - // User profile Name TextBlock
  - target: StartMenu.SearchBoxToggleButton > Grid > ContentPresenter > TextBlock#PlaceholderText
    styles:
      - FontFamily=$ThFnt
      - FontSize=14
      - FontWeight=$ThFntWt
      - RenderTransform:=<TranslateTransform Y="1" />
      - // Start Menu > Search Box Inactive Placeholder Text
  - target: TextBlock#AppDisplayName
    styles:
      - FontFamily=$ThFnt
      - FontSize=12.5
      - FontWeight=$ThFntWt
      - // Apps List > App Names Textblock
  - target: Button#Header > Border > TextBlock
    styles:
      - FontFamily=$ThFnt
      - FontSize=14
      - FontWeight=$ThHdnWt
      - '// App List Heading lettering: (#, A, B..) Text'
  - target: TextBlock#PlaceholderTextContentPresenter
    styles:
      - FontFamily=$ThFnt
      - // Idk which Placeholder text this is
  - target: Microsoft.UI.Xaml.Controls.DropDownButton > Grid > ContentPresenter > TextBlock
    styles:
      - FontFamily=$ThFnt
      - FontSize=14
      - FontWeight=$ThFntWt
      - // Right Click Menus > TextBlocks
  - target: TextBlock#ShowMorePinnedButtonText
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - // Pinned List > Show More Pinned Apps Text
  - target: ItemsWrapGrid > GridViewItem > Border#ContentBorder > Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter#ContentPresenter > ContentControl > Grid > TextBlock
    styles:
      - FontFamily=$ThFnt
      - FontSize=12.5
      - FontWeight=$ThFntWt
      - // Some List View Item's TextBlock
  - target: TextBlock[FontSize=12]
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - FontSize=12.5
      - // An attempt to Apply Font Styles to all TextBlocks with Font Size 12
  - target: TextBlock[FontSize=14]
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - // An attempt to Apply Font Styles to all TextBlocks with Font Size 14
  - target: TextBlock[FontSize=18]
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThHdnWt
      - // An attempt to Apply Font Styles to all TextBlocks with Font Size 18
  - target: ToolTip > ContentPresenter > TextBlock
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - FontSize=13
      - // Mouse Hover Tooltips > TextBlock
  - target: ContentPresenter#PrimaryCardContainer > Grid > Grid > TextBlock
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThHdnWt
      - FontSize=15
      - // An attempt to Apply Font Styles to TextBlocks in Phone Link Panel
  - target: ContentPresenter > TextBlock#FolderNameTextBlock
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThHdnWt
      - // All Apps List > Folders > Name Textblock
  - target: MenuFlyoutItem > Grid#LayoutRoot > TextBlock
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - FontSize=14.5
      - RenderTransform:=<TranslateTransform X="1" Y="0.5" />
      - // Right Click Menu items > TextBlock
  - target: Button#ZoomInButton > Grid > ContentPresenter#ContentPresenter > StackPanel > TextBlock
    styles:
      - FontFamily=$ThFnt
      - // Back button on the Zoomed Out View ( Alphabet Grid )
  - target: ListView#ZoomedOutListView > Border > ScrollViewer#ScrollViewer > Border#Root > Grid > ScrollContentPresenter#ScrollContentPresenter > ItemsPresenter > ItemsWrapGrid > ListViewItem > Grid#ContentBorder > ContentPresenter#ContentPresenter > Viewbox > Border > TextBlock
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - // Some List View Item's TextBlock
  - target: Grid#DroppedFlickerWorkaroundWrapper > ContentPresenter#ContentPresenter > Grid > TextBlock
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - // Some List View Item's TextBlock
  - target: TextBlock#SeeAllButtonLabelTextblock
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThFntWt
      - // Not sure which Button textblock
  - target: TextBlock#FolderNameTextBlock
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThHdnWt
      - // All Apps List > Category View > Folder Open > Heading TextBlock
  - target: TextBox#MutableFolderNameTextBox
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThHdnWt
      - // Pinned List > Folder Open > Heading TextBlock
  - target: TextBox#MutableFolderNameTextBox > Grid > ScrollViewer#ContentElement > Border#Root > Grid > ScrollContentPresenter#ScrollContentPresenter > Windows.UI.Xaml.Internal.TextBoxView
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThHdnWt
      - // Pinned List > Folder Open > Heading TextBlock (same-same, but different)
  - target: Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion
    styles:
      - Margin=-73,-1,73,1
      - Height=42
      - Width=45
      - // Show/Hide Phone Link Panel Button > Button Sizing
  - target: ToolTip
    styles:
      - CornerRadius=$OuterRadius
      - BorderBrush:=$ThemeOutBorder
      - Background:=$ThemeFlyout
      - // Mouse Hover Flyouts > Adjusting Background
  - target: StartDocked.UserTileView
    styles:
      - Margin=0,0,-23,0
      - // User Profile Root Alignment
  - target: TextBlock#SubFolderNameTextBlock
    styles:
      - FontFamily=$ThFnt
      - FontWeight=$ThHdnWt
      - // App List > Category View > Folder > Sub folder Heading TextBlock
  - target: Grid#TopLevelHeader > Grid > Button > Grid
    styles:
      - RenderTransform:=<TranslateTransform X="5" />
      - CornerRadius=$InnerRadius
      - // Pinned List Heading grid > Show All Pinned Apps button
themeResourceVariables:
  - Overlay@Light=#40FFFFFF
  - Overlay@Dark=#09FFFFFF
  - Border@Light=#0F000000
  - Border@Dark=#19000000
  - ControlBorder@Light=#0F000000
  - ControlBorder@Dark=#15FFFFFF
  - Btn@Light=#90FFFFFF
  - Btn@Dark=#20FFFFFF
webContentStyles:
  - target: '.curatedSettingsGroup, #scopesHeader'
    styles:
      - 'display: none !important'
  - target: '#qfPreviewPane'
    styles:
      - 'margin-right: -10px !important'
      - 'border-radius: 8px !important'
  - target: .suggsList, .suggContainer
    styles:
      - 'margin-right: 5px !important'
      - 'margin-left: 0px !important'
```
</details>
