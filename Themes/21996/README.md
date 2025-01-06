# 21996 Start & Search theme for Windows 11 Start Menu Styler

**Author**: [Tails](https://github.com/milesprower2293)

![Screenshot](Start.png)
![Screenshot](Search.png)

## Theme selection

The theme is integrated into the mod, and can be simply selected from the mod's
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
{"controlStyles[0].target":"StartDocked.SearchBoxToggleButton","controlStyles[0].styles[0]":"CornerRadius=4","controlStyles[0].styles[1]":"Height=40","controlStyles[1].target":"Border#TaskbarSearchBackground","controlStyles[1].styles[0]":"CornerRadius=4","controlStyles[1].styles[1]":"BorderThickness=0,0,0,0","controlStyles[1].styles[2]":"Height=33","controlStyles[1].styles[3]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource ControlStrokeColorDefault}\"/>","controlStyles[2].target":"StartDocked.SearchBoxToggleButton > Grid > ContentPresenter > TextBlock#PlaceholderText","controlStyles[2].styles[0]":"Margin=0,0,0,2","controlStyles[3].target":"StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Grid > Border#BorderElement","controlStyles[3].styles[0]":"BorderThickness=0,0,0,2","controlStyles[3].styles[1]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource SystemAccentColorLight1}\"/>","controlStyles[4].target":"StartDocked.SearchBoxToggleButton > Grid > FontIcon > Grid > TextBlock","controlStyles[4].styles[0]":"Foreground:=<SolidColorBrush Color=\"gray\" />","controlStyles[4].styles[1]":"Margin=0,0,0,1","controlStyles[5].target":"Microsoft.UI.Xaml.Controls.AnimatedIcon#SearchIconPlayer","controlStyles[5].styles[0]":"Visibility=1","controlStyles[6].target":"FontIcon#SearchBoxOnTaskbarSearchGlyph","controlStyles[6].styles[0]":"Visibility=0","controlStyles[6].styles[1]":"Foreground:=<SolidColorBrush Color=\"gray\" />","controlStyles[7].target":"StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Grid","controlStyles[7].styles[0]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource ControlStrokeColorDefault}\"/>","controlStyles[7].styles[1]":"BorderThickness=1,1,1,0","controlStyles[7].styles[2]":"CornerRadius=4","controlStyles[8].target":"Cortana.UI.Views.RichSearchBoxControl#SearchBoxControl > Grid#RootGrid","controlStyles[8].styles[0]":"CornerRadius=4","controlStyles[8].styles[1]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource SystemAccentColorLight1}\" />","controlStyles[8].styles[2]":"BorderThickness=2,2,2,2","controlStyles[8].styles[3]":"Margin=-2,-0,0,-2","controlStyles[5].styles[1]":"FlowDirection=1","controlStyles[6].styles[2]":"FlowDirection=1","controlStyles[6].styles[3]":"FontFamily=Segoe Fluent Icons","controlStyles[9].target":"Windows.UI.Xaml.Controls.Grid#SearchBoxOnTaskbarGleamContainer","controlStyles[9].styles[0]":"CornerRadius=4","controlStyles[5].styles[2]":"Transform3D:=<CompositeTransform3D RotationY=\"180\" TranslateX=\"16\" />","controlStyles[4].styles[2]":"Transform3D:=<CompositeTransform3D RotationY=\"180\" TranslateX=\"16\" />","controlStyles[10].target":"Windows.UI.Xaml.Controls.Grid#SearchBoxOnTaskbarGleamImageContainer","controlStyles[10].styles[0]":"CornerRadius=4","controlStyles[11].target":"Windows.UI.Xaml.Controls.Image#SearchIconOff","controlStyles[12].target":"Windows.UI.Xaml.Controls.Image#SearchIconOn","controlStyles[11].styles[0]":"Transform3D:=<CompositeTransform3D RotationY=\"180\" TranslateX=\"16\" TranslateY=\"-1\" />","controlStyles[12].styles[0]":"Transform3D:=<CompositeTransform3D RotationY=\"180\" TranslateX=\"16\" TranslateY=\"-1\" />","controlStyles[13].target":"Windows.UI.Xaml.Controls.Button#ShowAllAppsButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.StackPanel > Windows.UI.Xaml.Controls.TextBlock#ShowAllAppsButtonText","controlStyles[13].styles[0]":"Text=All apps","controlStyles[14].target":"Windows.UI.Xaml.Controls.TextBlock#AllAppsHeading","controlStyles[14].styles[0]":"Text=All apps","controlStyles[15].target":"StartDocked.SearchBoxToggleButton","controlStyles[15].styles[0]":"Height=0","controlStyles[15].styles[1]":"Margin=0,0,0,24","controlStyles[16].target":"StartDocked.LauncherFrame","controlStyles[16].styles[0]":"Height=670","controlStyles[17].target":"Windows.UI.Xaml.Controls.Grid#InnerContent","controlStyles[17].styles[0]":"Margin=0,0,0,0","controlStyles[10].styles[1]":"Transform3D:=<CompositeTransform3D TranslateX=\"1.8\" />","controlStyles[6].styles[4]":"RequestedTheme=1","controlStyles[6].styles[5]":"Transform3D:=<CompositeTransform3D RotationY=\"180\" TranslateX=\"23\" TranslateY=\"0.5\" />","controlStyles[6].styles[6]":"FontSize=17","controlStyles[18].target":"Cortana.UI.Views.HostedWebViewControl#QueryFormulationHostedWebView","controlStyles[18].styles[0]":"Background:=<SolidColorBrush Color=\"{ThemeResource ControlStrokeColorDefault}\" Opacity=\"100\"  />","controlStyles[19].target":"Windows.UI.Xaml.Controls.Grid#QueryFormulationRoot","controlStyles[19].styles[0]":"CornerRadius=10"}
```
</details>
