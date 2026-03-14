# SideBySide theme for Windows 11 Start Menu Styler

**Author**: [kaoshipaws](https://k4oshi.top/)

![Screenshot](screenshot.png)

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

### Redesigned Start menu

A variant for the [redesigned Windows 11 Start
menu](https://microsoft.design/articles/start-fresh-redesigning-windows-start-menu/)
that is slowly rolling out in the 25H2 update.

<details>
<summary>Content to import (click to expand)</summary>

```json
{
  "controlStyles[0].target": "StartMenu.PinnedList",
  "controlStyles[0].styles[0]": "MinHeight=420",
  "controlStyles[0].styles[1]": "MaxHeight=420",
  "controlStyles[1].target": "StartMenu.ExpandedFolderList > Grid > Border",
  "controlStyles[1].styles[0]": "Margin=-40,0,40,0",
  "controlStyles[1].styles[1]": "Width=325",
  "controlStyles[2].target": "StartMenu.ExpandedFolderList > Grid > Grid",
  "controlStyles[2].styles[0]": "CornerRadius=8",
  "controlStyles[2].styles[1]": "Margin=-85,0,0,0",
  "controlStyles[2].styles[2]": "Width=350",
  "controlStyles[3].target": "StartMenu.ExpandedFolderList > Grid > Grid > Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager",
  "controlStyles[3].styles[0]": "Margin=-15,0,0,0",
  "controlStyles[4].target": "Grid#MainMenu",
  "controlStyles[4].styles[0]": "Width=825",
  "controlStyles[5].target": "Grid#FrameRoot",
  "controlStyles[5].styles[0]": "Height=825",
  "controlStyles[6].target": "Border#AcrylicOverlay",
  "controlStyles[6].styles[0]": "Margin=0,-70,0,0",
  "controlStyles[7].target": "GridView#PinnedList",
  "controlStyles[7].styles[0]": "MaxWidth=480",
  "controlStyles[7].styles[1]": "RenderTransform:=<TranslateTransform X=\"-145\" Y=\"710\"/>",
  "controlStyles[7].styles[2]": "MinHeight=420",
  "controlStyles[7].styles[3]": "MaxHeight=420",
  "controlStyles[8].target": "GridView#AllAppsGrid > Border > ScrollViewer > Border > Grid > ScrollContentPresenter > ItemsPresenter > ItemsWrapGrid",
  "controlStyles[8].styles[0]": "Width=280",
  "controlStyles[8].styles[1]": "Margin=55,12,-55,0",
  "controlStyles[9].target": "GridView#AllAppsGrid > Border > ScrollViewer > Border > Grid > ScrollContentPresenter > ItemsPresenter",
  "controlStyles[9].styles[0]": "RenderTransform:=<TranslateTransform Y=\"-795\"/>",
  "controlStyles[10].target": "Microsoft.UI.Xaml.Controls.DropDownButton",
  "controlStyles[10].styles[0]": "Margin=-60,170,60,-170",
  "controlStyles[10].styles[1]": "FontWeight=SemiBold",
  "controlStyles[10].styles[2]": "Height=32",
  "controlStyles[10].styles[3]": "Width=200",
  "controlStyles[10].styles[4]": "Style:=",
  "controlStyles[11].target": "Windows.UI.Xaml.Controls.ListView#ZoomedOutListView",
  "controlStyles[11].styles[0]": "Margin=0,-35,0,35",
  "controlStyles[12].target": "TextBlock#PinnedListHeaderText",
  "controlStyles[12].styles[0]": "Visibility=Visible",
  "controlStyles[12].styles[1]": "RenderTransform:=<TranslateTransform X=\"-4\" Y=\"788.5\"/>",
  "controlStyles[12].styles[2]": "FontWeight=SemiBold",
  "controlStyles[13].target": "StartMenu.StartHome",
  "controlStyles[13].styles[0]": "RenderTransform:=<TranslateTransform Y=\"-1\"/>",
  "controlStyles[14].target": "Windows.UI.Xaml.Controls.Frame > Windows.UI.Xaml.Controls.ContentPresenter",
  "controlStyles[14].styles[0]": "Margin=0,-15,0,0",
  "controlStyles[15].target": "DropDownButton > Grid > ContentPresenter > TextBlock",
  "controlStyles[15].styles[0]": "MaxLines=2",
  "controlStyles[15].styles[1]": "TextLineBounds=0",
  "controlStyles[15].styles[2]": "HorizontalAlignment=1",
  "controlStyles[16].target": "Grid#TopLevelSuggestionsRoot",
  "controlStyles[16].styles[0]": "RenderTransform:=<TranslateTransform X=\"-160\" Y=\"800\"/>",
  "controlStyles[16].styles[1]": "Width=450",
  "controlStyles[16].styles[2]": "MinHeight=129",
  "controlStyles[16].styles[3]": "BorderThickness=0,1,0,0",
  "controlStyles[16].styles[4]": "BorderBrush=#22BBBBBB",
  "controlStyles[17].target": "TextBlock#TopLevelSuggestionsListHeaderText",
  "controlStyles[17].styles[0]": "RenderTransform:=<TranslateTransform X=\"-50\" />",
  "controlStyles[18].target": "Button#ShowMoreSuggestionsButton",
  "controlStyles[18].styles[0]": "RenderTransform:=<TranslateTransform X=\"50\" />",
  "controlStyles[19].target": "GridView#AllAppsGrid > Border > ScrollViewer > Border > Grid > ScrollContentPresenter > ItemsPresenter > ItemsWrapGrid",
  "controlStyles[19].styles[0]": "Margin=485,175,0,0",
  "controlStyles[20].target": "GridView#RecommendedList > Border > ScrollViewer > Border > Grid > ScrollContentPresenter > ItemsPresenter > ItemsWrapGrid > GridViewItem > Border",
  "controlStyles[20].styles[0]": "MaxWidth=185",
  "controlStyles[20].styles[1]": "HorizontalAlignment=2",
  "controlStyles[21].target": "Grid#TopLevelSuggestionsContainer",
  "controlStyles[21].styles[0]": "Width=630",
  "controlStyles[21].styles[1]": "Margin=-50,0,0,0",
  "controlStyles[22].target": "GridView#RecommendedList > Border > ScrollViewer > Border > Grid > ScrollContentPresenter > ItemsPresenter > ItemsWrapGrid > GridViewItem",
  "controlStyles[22].styles[0]": "Margin=-25,0,-25,0",
  "controlStyles[23].target": "StartDocked.AppListView",
  "controlStyles[23].styles[0]": "Margin=15,0,-15,0",
  "controlStyles[24].target": "Windows.UI.Xaml.Controls.Primitives.ScrollBar",
  "controlStyles[24].styles[0]": "Height=650",
  "controlStyles[24].styles[1]": "RenderTransform:=<TranslateTransform Y=\"-50\" />",
  "controlStyles[25].target": "Grid#MainMenu > Grid#MainContent > Grid",
  "controlStyles[25].styles[0]": "Canvas.ZIndex=1",
  "controlStyles[26].target": "Windows.UI.Xaml.Controls.GridView#PinnedList > Border > Windows.UI.Xaml.Controls.ScrollViewer",
  "controlStyles[26].styles[0]": "MaxHeight=260",
  "controlStyles[26].styles[1]": "ScrollViewer.VerticalScrollMode=2"
}
```
</details>

### Classic Start menu

<details>
<summary>Content to import (click to expand)</summary>

```json
{
  "controlStyles[0].target": "Grid#UndockedRoot",
  "controlStyles[0].styles[0]": "MaxWidth=700",
  "controlStyles[0].styles[1]": "Margin=0,0,300,0",
  "controlStyles[1].target": "Grid#AllAppsRoot",
  "controlStyles[1].styles[0]": "Visibility=Visible",
  "controlStyles[1].styles[1]": "MinWidth=390",
  "controlStyles[1].styles[2]": "Padding=-40,0,110,0",
  "controlStyles[1].styles[3]": "Background:=<AcrylicBrush TintColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" FallbackColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" TintOpacity=\"0\" TintLuminosityOpacity=\"1\" Opacity=\"1\"/>",
  "controlStyles[1].styles[4]": "Margin=-300,0,745,1",
  "controlStyles[2].target": "StartDocked.LauncherFrame > Grid#RootPanel > Grid#RootGrid > Grid#RootContent > Grid#MainContent > Grid#InnerContent > Grid#AllAppsRoot",
  "controlStyles[2].styles[0]": "Margin=-516,0,745,1",
  "controlStyles[3].target": "Windows.UI.Xaml.Controls.Button#CloseAllAppsButton",
  "controlStyles[3].styles[0]": "Visibility=Collapsed",
  "controlStyles[4].target": "StartDocked.StartSizingFrame",
  "controlStyles[4].styles[0]": "MaxWidth=860",
  "controlStyles[4].styles[1]": "Width=860",
  "controlStyles[5].target": "StartDocked.LauncherFrame > Grid#RootPanel > Grid#RootGrid",
  "controlStyles[5].styles[0]": "Width=644",
  "controlStyles[6].target": "Windows.UI.Xaml.Controls.Button#ShowAllAppsButton",
  "controlStyles[6].styles[0]": "Visibility=Collapsed",
  "controlStyles[7].target": "Windows.UI.Xaml.Controls.TextBlock#PinnedListHeaderText",
  "controlStyles[7].styles[0]": "Margin=-22,-5,0,0",
  "controlStyles[8].target": "Grid#TopLevelSuggestionsListHeader",
  "controlStyles[8].styles[0]": "Margin=45,-15,0,0",
  "controlStyles[9].target": "StartDocked.AllAppsGridListView > Windows.UI.Xaml.Controls.ScrollViewer > Border > Grid > Windows.UI.Xaml.Controls.Primitives.ScrollBar",
  "controlStyles[9].styles[0]": "Margin=-8,0,8,2",
  "controlStyles[10].target": "Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager",
  "controlStyles[10].styles[0]": "Margin=-8,0,8,0",
  "controlStyles[11].target": "Windows.UI.Xaml.Controls.ItemsWrapGrid > Windows.UI.Xaml.Controls.GridViewItem",
  "controlStyles[11].styles[0]": "MaxWidth=185",
  "controlStyles[11].styles[1]": "MinWidth=85",
  "controlStyles[12].target": "StartMenu.PinnedList#StartMenuPinnedList",
  "controlStyles[12].styles[0]": "Margin=-15,0,5,0",
  "controlStyles[13].target": "Grid#ShowMoreSuggestions",
  "controlStyles[13].styles[0]": "Margin=0,20,0,-20",
  "controlStyles[14].target": "Grid#MoreSuggestionsRoot",
  "controlStyles[14].styles[0]": "Margin=-1,0,-4,-30",
  "controlStyles[15].target": "Windows.UI.Xaml.Controls.TextBlock#MoreSuggestionsListHeaderText",
  "controlStyles[15].styles[0]": "Margin=-40,0,0,0",
  "controlStyles[16].target": "Button#ShowMoreSuggestionsButton",
  "controlStyles[16].styles[0]": "Margin=0,-58,25,0",
  "controlStyles[17].target": "Grid#TopLevelSuggestionsContainer",
  "controlStyles[17].styles[0]": "Margin=30,-10,30,-60",
  "controlStyles[18].target": "Windows.UI.Xaml.Controls.GridViewItem",
  "controlStyles[18].styles[0]": "Margin=0",
  "controlStyles[19].target": "Border#AcrylicOverlay",
  "controlStyles[19].styles[0]": "Background:=<AcrylicBrush TintColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" FallbackColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" TintOpacity=\"0.1\" TintLuminosityOpacity=\"1\" Opacity=\"1\"/>",
  "controlStyles[20].target": "Windows.UI.Xaml.Controls.SemanticZoom#ZoomControl",
  "controlStyles[20].styles[0]": "IsZoomOutButtonEnabled=true",
  "controlStyles[21].target": "Windows.UI.Xaml.Controls.Button#ZoomOutButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.TextBlock",
  "controlStyles[21].styles[0]": "Text=",
  "controlStyles[22].target": "Windows.UI.Xaml.Controls.Button#ZoomOutButton",
  "controlStyles[22].styles[0]": "Width=24",
  "controlStyles[22].styles[1]": "Height=24",
  "controlStyles[22].styles[2]": "FontSize=14",
  "controlStyles[22].styles[3]": "CornerRadius=4",
  "controlStyles[22].styles[4]": "VerticalAlignment=0",
  "controlStyles[22].styles[5]": "Margin=-8,-35,8,0",
  "controlStyles[23].target": "Border#LayerBorder",
  "controlStyles[23].styles[0]": "Background:=<AcrylicBrush TintColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" FallbackColor=\"{ThemeResource CardStrokeColorDefaultSolid}\" TintOpacity=\"0.1\" TintLuminosityOpacity=\"1\" Opacity=\"1\"/>"
}
```
</details>

## Removing the "Recommended" section

The "Recommended" section can be removed by following these steps:

* Import [the NoRecommendedSection
  theme](https://github.com/ramensoftware/windows-11-start-menu-styling-guide/blob/main/Themes/NoRecommendedSection/README.md)
  using the **Manual installation** instructions.
* Select this theme using the **Theme selection** instructions on this page.
