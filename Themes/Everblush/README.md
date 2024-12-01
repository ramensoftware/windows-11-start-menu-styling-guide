# Everbrush theme for Windows 11 Start Menu Styler

The starter is based on the [Everblush](https://github.com/everblush) color scheme. There are no new designs in this menu, you can get the Everblush color with the default menu.

**Tip**: You can apply other menu styles in Everbrush colors by manually importing the Everbrush styles in "Mod Settings" under the "Advanced tab" and then adding any preferred Start Menu styles through the Theme option in the "Settings tab."

**Author**: [VIN STAR](https://github.com/vinstartheme) 


![Screenshot](https://github.com/user-attachments/assets/32ca7838-56d5-4532-b124-5f624a3d1466)


<!--
## Theme selection

The theme is integrated into the mod, and can be simply selected from the mod's
settings:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Settings" tab.
* Select the theme and save the settings.
-->
## Manual installation

<!-- The theme styles can also be imported manually. To do that, follow these steps: -->
To import the theme manually, follow these steps:

* Open the Windows 11 Start Menu Styler mod in Windhawk.
* Go to the "Advanced" tab.
* Copy the content below to the text box under "Mod settings" and click "Save".

<details>
<summary>Content to import (click to expand)</summary>

```json
{
  "controlStyles[0].target": "Border#AcrylicBorder",
  "controlStyles[0].styles[0]": "Background:=#141b1e",
  "controlStyles[0].styles[1]": "BorderBrush:=#268ccf7e",
  "controlStyles[1].target": "Border#AcrylicOverlay",
  "controlStyles[1].styles[0]": "Background:=#141b1e",
  "controlStyles[2].target": "StartDocked.SearchBoxToggleButton > Grid > Border",
  "controlStyles[2].styles[0]": "Background=#232a2d",
  "controlStyles[2].styles[1]": "BorderBrush=transparent",
  "controlStyles[3].target": "StartMenu.ExpandedFolderList > Grid > Border",
  "controlStyles[3].styles[0]": "Background=#232a2d",
  "controlStyles[4].target": "TextBlock#PlaceholderText",
  "controlStyles[4].styles[0]": "Foreground:=#80b3b9b8",
  "controlStyles[5].target": "Windows.UI.Xaml.Controls.Button",
  "controlStyles[5].styles[0]": "Background:=#d28ccf7e",
  "controlStyles[6].target": "StackPanel > Windows.UI.Xaml.Controls.Button",
  "controlStyles[6].styles[0]": "Background:=transparent",
  "controlStyles[6].styles[1]": "BorderBrush:=transparent",
  "controlStyles[7].target": "Microsoft.UI.Xaml.Controls.ItemsRepeater > Windows.UI.Xaml.Controls.Button",
  "controlStyles[7].styles[0]": "Background:=transparent",
  "controlStyles[7].styles[1]": "BorderBrush:=transparent",
  "controlStyles[8].target": "TextBlock#DisplayName",
  "controlStyles[8].styles[0]": "Foreground:=#e5c76b",
  "controlStyles[9].target": "TextBlock#Title",
  "controlStyles[9].styles[0]": "Foreground:=#b3b9b8",
  "controlStyles[10].target": "TextBlock#Subtitle",
  "controlStyles[10].styles[0]": "Foreground:=#6cbfbf",
  "controlStyles[11].target": "TextBlock#PinnedListHeaderText",
  "controlStyles[11].styles[0]": "Foreground:=#8ccf7e",
  "controlStyles[12].target": "TextBlock#TopLevelSuggestionsListHeaderText",
  "controlStyles[12].styles[0]": "Foreground:=#8ccf7e",
  "controlStyles[13].target": "TextBlock#AllAppsHeading",
  "controlStyles[13].styles[0]": "Foreground:=#e5c76b",
  "controlStyles[14].target": "TextBlock#MoreSuggestionsListHeaderText",
  "controlStyles[14].styles[0]": "Foreground:=#e5c76b",
  "controlStyles[15].target": "TextBlock#AppDisplayName",
  "controlStyles[15].styles[0]": "Foreground:=#8ccf7e",
  "controlStyles[16].target": "TextBlock#Text ",
  "controlStyles[16].styles[0]": "Foreground:=#e5c76b",
  "controlStyles[17].target": "TextBlock#FolderGlyph",
  "controlStyles[17].styles[0]": "Foreground:=#e5c76b",
  "controlStyles[18].target": "TextBlock#StatusMessage",
  "controlStyles[18].styles[0]": "Foreground:=#a2b3b9b8",
  "controlStyles[19].target": "Windows.UI.Xaml.Controls.Border#ContentBorder > Windows.UI.Xaml.Controls.Grid#DroppedFlickerWorkaroundWrapper > Border@CommonStates",
  "controlStyles[19].styles[0]": "Background:=<LinearGradientBrush StartPoint=\"0.5,0\" EndPoint=\"0,0.5\"> <GradientStop Color=\"#268ccf7e\" Offset=\"0\" /><GradientStop Color=\"#26e5c76b\" Offset=\"1\" /></LinearGradientBrush>",
  "controlStyles[19].styles[1]": "BorderBrush:=<LinearGradientBrush StartPoint=\"0.5,0\" EndPoint=\"0,0.5\"> <GradientStop Color=\"#828ccf7e\" Offset=\"0\" /><GradientStop Color=\"#82e5c76b\" Offset=\"1\" /></LinearGradientBrush>",
  "controlStyles[19].styles[2]": "CornerRadius=6",
  "controlStyles[20].target": "Windows.UI.Xaml.Controls.Border#ContentBorder > Windows.UI.Xaml.Controls.Grid#DroppedFlickerWorkaroundWrapper > Border#BackgroundBorder",
  "controlStyles[20].styles[0]": "Background:=transparent",
  "controlStyles[21].target": " Border#AppBorder",
  "controlStyles[21].styles[0]": "Background:=#141b1e",
  "controlStyles[22].target": "Border#TaskbarSearchBackground",
  "controlStyles[22].styles[0]": "Background:=#232a2d",
  "controlStyles[22].styles[1]": "BorderBrush:=transparent",
  "controlStyles[23].target": "Grid",
  "controlStyles[23].styles[0]": "RequestedTheme=2",
  "controlStyles[24].target": "TextBlock#UserTileNameText",
  "controlStyles[24].styles[0]": "Foreground=#67b0e8",
  "controlStyles[25].target": "Windows.UI.Xaml.Controls.ContentPresenter > Windows.UI.Xaml.Controls.FontIcon > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.TextBlock",
  "controlStyles[25].styles[0]": "Foreground=#6cbfbf",
  "controlStyles[26].target": "Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.FontIcon > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.TextBlock",
  "controlStyles[26].styles[0]": "Foreground=#e5c76b",
  "controlStyles[27].target": "MenuFlyoutPresenter",
  "controlStyles[27].styles[0]": "Background=#232a2d",
  "controlStyles[28].target": "Windows.UI.Xaml.Controls.FontIcon#SearchGlyph > Windows.UI.Xaml.Controls.Grid > Windows.UI.Xaml.Controls.TextBlock",
  "controlStyles[28].styles[0]": "Foreground:=#232a2d"
}
```
</details>
