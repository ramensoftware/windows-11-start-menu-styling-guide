# Sun Valley Start & Search theme for Windows 11 Start Menu Styler

This theme tries to recreate the design that the Windows 11 Start menu and search menu had on early Windows 11 builds,
which included:
* 22000.51's searchbox
* Changed 'All' to 'All apps' as it was on older Windows 11 builds
* Custom Acrylic + Accent color & light/dark mode support
* New Windows 11 Start Menu support
* Windows 10-like search menu (to adapt to the [SunValley Taskbar theme](https://github.com/ramensoftware/windows-11-taskbar-styling-guide/blob/main/Themes/SunValley/README.md))
* Support for the new Copilot Search Menu

**Author**: [Tails](https://github.com/milestprower92)

## Screenshots
### Old Windows 11 Start Menu:
![Screenshot](screenshot.png)
### New Windows 11 Start Menu
![Screenshot](screenshot2.png)
### Search Menu
![Screenshot](screenshot-search.png)
### Copilot Search Menu
![Screenshot](screenshot-cortana.png)

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
"controlStyles[0].target":"Cortana.UI.Views.TaskbarSearchPage", 
"controlStyles[0].styles[0]":"Margin=-2,0,0,0", 
"controlStyles[1].target":"Border#TaskbarMargin", 
"controlStyles[1].styles[0]":"Visibility=1", 
"controlStyles[2].target":"Border#TaskbarSearchBackground", 
"controlStyles[2].styles[0]":"Grid.Row=3", 
"controlStyles[2].styles[1]":"Margin=0,0,0,2", 
"controlStyles[2].styles[2]":"Background:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeAltHighColor}\" TintOpacity=\"0.6\" TintLuminosityOpacity=\"0.6\" FallbackColor=\"{ThemeResource SystemChromeMediumColor}\" />", 
"controlStyles[2].styles[3]":"Height=44", 
"controlStyles[2].styles[4]":"VerticalAlignment=2", 
"controlStyles[2].styles[5]":"CornerRadius=0,0,7,7", 
"controlStyles[2].styles[6]":"BorderThickness=0,0,1,1", 
"controlStyles[3].target":"Cortana.UI.Views.RichSearchBoxControl#SearchBoxControl", 
"controlStyles[3].styles[0]":"Margin=0,0,0,2", 
"controlStyles[3].styles[1]":"Grid.Row=3", 
"controlStyles[3].styles[2]":"Height=44", 
"controlStyles[3].styles[3]":"VerticalAlignment=2", 
"controlStyles[3].styles[4]":"HorizontalAlignment=0", 
"controlStyles[3].styles[5]":"Width=340", 
"controlStyles[4].target":"ScrollViewer > ScrollContentPresenter > Border", 
"controlStyles[4].styles[0]":"Margin=0,0,0,0", 
"controlStyles[5].target":"Cortana.UI.Views.RichSearchBoxControl#SearchBoxControl > Grid@SearchBoxStates", 
"controlStyles[5].styles[0]":"Background:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeMediumColor}\" TintOpacity=\"0\" TintLuminosityOpacity=\"0.7\" FallbackColor=\"{ThemeResource SystemChromeMediumColor}\" />", 
"controlStyles[5].styles[1]":"BorderThickness=1", 
"controlStyles[5].styles[2]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource SystemBaseHighColor}\" Opacity=\"0.2\" />", 
"controlStyles[5].styles[3]":"CornerRadius=4",
"controlStyles[6].target":"Microsoft.UI.Xaml.Controls.AnimatedIcon#SearchIconPlayer", 
"controlStyles[6].styles[0]":"Visibility=Collapsed",
"controlStyles[7].target":"Button#SearchGlyphContainer", 
"controlStyles[7].styles[0]":"Visibility=Visible", 
"controlStyles[7].styles[1]":"Width=35", 
"controlStyles[7].styles[2]":"Margin=2,0,-11,0", 
"controlStyles[8].target":"Button#SearchGlyphContainer > Grid > ContentPresenter > FontIcon", 
"controlStyles[8].styles[0]":"FontFamily=Segoe Fluent Icons", 
"controlStyles[8].styles[1]":"FontSize=17", 
"controlStyles[8].styles[2]":"Foreground:=<SolidColorBrush Color=\"{ThemeResource SystemBaseHighColor}\" Opacity=\"0.8\" />", 
"controlStyles[9].target":"Cortana.UI.Views.CortanaRichSearchBox#SearchTextBox > Grid > TextBlock#PlaceholderTextContentPresenter", 
"controlStyles[9].styles[0]":"Text=Type here to search", 
"controlStyles[9].styles[1]":"FontFamily=Segoe UI", 
"controlStyles[9].styles[2]":"FontSize=15", 
"controlStyles[9].styles[3]":"Padding=39,0,0,0", 
"controlStyles[9].styles[4]":"Foreground:=<SolidColorBrush Color=\"{ThemeResource SystemBaseHighColor}\" Opacity=\"0.8\" />", 
"controlStyles[10].target":"Cortana.UI.Views.CortanaRichSearchBox#SearchTextBox > Grid > ScrollViewer > Border > Grid > ScrollContentPresenter", 
"controlStyles[10].styles[0]":"Margin=38,0,0,0", 
"controlStyles[10].styles[1]":"FontSize=15", 
"controlStyles[11].target":"Grid#SearchBoxOnTaskbarGleamContainer > Grid", 
"controlStyles[11].styles[0]":"Margin=0,0,-3,0", 
"controlStyles[11].styles[1]":"CornerRadius=4", 
"controlStyles[12].target":"Cortana.UI.Views.TaskbarSearchPage > Grid#RootGrid > Grid#OuterBorderGrid > Grid#BorderGrid > Border", 
"controlStyles[12].styles[0]":"CornerRadius=7,7,0,0", 
"controlStyles[13].target":"Cortana.UI.Views.TaskbarSearchPage > Grid#RootGrid > Grid#OuterBorderGrid > Grid#BorderGrid > Border#AppBorder", 
"controlStyles[13].styles[0]":"Background:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeAltHighColor}\" TintOpacity=\"0.4\" TintLuminosityOpacity=\"0.4\" FallbackColor=\"{ThemeResource SystemChromeMediumColor}\" />", 
"controlStyles[13].styles[1]":"Visibility=Visible", 
"controlStyles[13].styles[2]":"BorderThickness=1,1,1,0", 
"controlStyles[14].target":"Cortana.UI.Views.TaskbarSearchPage > Grid#RootGrid > Grid#OuterBorderGrid > Grid#BorderGrid > Border#dropshadow", 
"controlStyles[14].styles[0]":"Opacity=0", 
"controlStyles[15].target":"Cortana.UI.Views.RichSearchBoxControl#SearchBoxControl > Grid > Grid#UnderlineContainer", 
"controlStyles[15].styles[0]":"Visibility=0", 
"controlStyles[15].styles[1]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource SystemAccentColor}\" />", 
"controlStyles[15].styles[2]":"BorderThickness=0,0,0,2", 
"controlStyles[15].styles[3]":"CornerRadius=5", 
"controlStyles[15].styles[4]":"Margin=-3,0,-3,0", 
"controlStyles[16].target":"StartDocked.SearchBoxToggleButton > Grid > ContentPresenter > TextBlock#PlaceholderText", 
"controlStyles[16].styles[0]":"Margin=28,0,0,0", 
"controlStyles[16].styles[1]":"Text=Type here to search", 
"controlStyles[17].target":"StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Grid > Border#BorderElement", 
"controlStyles[17].styles[0]":"BorderThickness=0,0,0,2", 
"controlStyles[17].styles[1]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource SystemAccentColorLight1}\" />", 
"controlStyles[18].target":"StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Grid > FontIcon#SearchGlyph", 
"controlStyles[18].styles[0]":"Foreground:=<SolidColorBrush Color=\"{ThemeResource SystemBaseHighColor}\" Opacity=\"0.5\" />", 
"controlStyles[18].styles[1]":"Margin=13,0,-13,1", 
"controlStyles[18].styles[2]":"Visibility=Visible", 
"controlStyles[19].target":"StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Grid", 
"controlStyles[19].styles[0]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource SystemBaseHighColor}\" Opacity=\"0.1\" />", 
"controlStyles[19].styles[1]":"CornerRadius=4", 
"controlStyles[19].styles[2]":"BorderThickness=1", 
"controlStyles[20].target":"StartDocked.SearchBoxToggleButton", 
"controlStyles[20].styles[0]":"CornerRadius=4", 
"controlStyles[20].styles[1]":"Height=40", 
"controlStyles[21].target":"Windows.UI.Xaml.Controls.Button#ShowAllAppsButton > Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter > Windows.UI.Xaml.Controls.StackPanel > Windows.UI.Xaml.Controls.TextBlock#ShowAllAppsButtonText", 
"controlStyles[21].styles[0]":"Text=All apps", 
"controlStyles[22].target":"Windows.UI.Xaml.Controls.TextBlock#AllAppsHeading", 
"controlStyles[22].styles[0]":"Text=All apps", 
"controlStyles[23].target":"Image#SearchIconOn", 
"controlStyles[24].target":"Image#SearchIconOff", 
"controlStyles[23].styles[0]":"Visibility=Collapsed", 
"controlStyles[24].styles[0]":"Visibility=Collapsed", 
"controlStyles[25].target":"StartMenu.SearchBoxToggleButton#SearchBoxToggleButton > Grid > Border", 
"controlStyles[25].styles[0]":"CornerRadius=0", 
"controlStyles[25].styles[1]":"BorderThickness=0,0,0,2", 
"controlStyles[25].styles[2]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource SystemAccentColor}\"/>", 
"controlStyles[25].styles[3]":"Background:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeMediumColor}\" TintOpacity=\"0\" TintLuminosityOpacity=\"0.7\" FallbackColor=\"{ThemeResource SystemChromeMediumColor}\" />", 
"controlStyles[26].target":"Windows.UI.Xaml.Controls.TextBlock#AllListHeadingText", 
"controlStyles[26].styles[0]":"Text=All apps", 
"controlStyles[27].target":"Microsoft.UI.Xaml.Controls.DropDownButton > Grid@CommonStates", 
"controlStyles[27].styles[0]":"Background@Normal:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorDefault}\" />", 
"controlStyles[27].styles[1]":"Background@PointerOver:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorSecondary}\" />", 
"controlStyles[27].styles[2]":"Background@Pressed:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorTertiary}\" />", 
"controlStyles[27].styles[3]":"BorderBrush:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeHighColor}\" FallbackColor=\"{ThemeResource SystemChromeMediumHighColor}\" TintOpacity=\"0\" />", 
"controlStyles[27].styles[4]":"BorderThickness=1", 
"controlStyles[28].target":"StartMenu.SearchBoxToggleButton > Grid > ContentPresenter > TextBlock#PlaceholderText", 
"controlStyles[28].styles[0]":"Text=Type here to search", 
"controlStyles[28].styles[1]":"Margin=24,0,0,0", 
"controlStyles[29].target":"StartMenu.SearchBoxToggleButton#SearchBoxToggleButton", 
"controlStyles[29].styles[0]":"Height=40", 
"controlStyles[30].target":"StartMenu.SearchBoxToggleButton > Grid > Rectangle#TextCaret", 
"controlStyles[30].styles[0]":"Margin=24,0,0,0", 
"controlStyles[31].target":"StartMenu.SearchBoxToggleButton > Grid", 
"controlStyles[31].styles[0]":"BorderThickness=1", 
"controlStyles[31].styles[1]":"BorderBrush:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeHighColor}\" FallbackColor=\"{ThemeResource SystemChromeMediumHighColor}\" TintOpacity=\"0\" />", 
"controlStyles[31].styles[2]":"CornerRadius=4", 
"controlStyles[32].target":"Grid#TopLevelHeader > Grid > Button > Grid@CommonStates", 
"controlStyles[32].styles[0]":"BorderBrush:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeHighColor}\" FallbackColor=\"{ThemeResource SystemChromeMediumHighColor}\" TintOpacity=\"0\" />", 
"controlStyles[32].styles[1]":"BorderThickness=1", 
"controlStyles[32].styles[2]":"CornerRadius=5", 
"controlStyles[33].target":"Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Border", 
"controlStyles[33].styles[0]":"BorderBrush:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeHighColor}\" FallbackColor=\"{ThemeResource SystemChromeMediumHighColor}\" TintOpacity=\"0\" />", 
"controlStyles[33].styles[1]":"BorderThickness=1", 
"controlStyles[33].styles[2]":"CornerRadius=5", 
"controlStyles[34].target":"Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Border > ContentPresenter", 
"controlStyles[34].styles[0]":"Height=40", 
"controlStyles[34].styles[1]":"Width=40", 
"controlStyles[35].target":"Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion", 
"controlStyles[35].styles[0]":"Height=40", 
"controlStyles[35].styles[1]":"Width=40", 
"controlStyles[36].target":"Windows.UI.Xaml.Controls.Primitives.ToggleButton#ShowHideCompanion > Border > ContentPresenter > FontIcon > Grid > TextBlock", 
"controlStyles[36].styles[0]":"FontSize=20", 
"controlStyles[37].target":"Grid#TopLevelHeader > Grid > Button > Grid@CommonStates > Border#BackgroundBorder", 
"controlStyles[37].styles[0]":"Background@Normal:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorDefault}\" />", 
"controlStyles[37].styles[1]":"Background@PointerOver:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorSecondary}\" />", 
"controlStyles[37].styles[2]":"Background@Pressed:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorTertiary}\" />", 
"controlStyles[38].target":"StartMenu.SearchBoxToggleButton > Grid > FontIcon#SearchGlyph", 
"controlStyles[38].styles[0]":"Visibility=Visible", 
"controlStyles[38].styles[1]":"Foreground:=<SolidColorBrush Color=\"{ThemeResource SystemBaseHighColor}\" Opacity=\"0.5\" />", 
"controlStyles[38].styles[2]":"Margin=13,0,-13,1", 
"controlStyles[39].target":"Grid#AnimationRoot > Grid#MainMenu > Windows.UI.Xaml.Controls.Border#AcrylicBorder", 
"controlStyles[39].styles[0]":"Opacity=0.5", 
"controlStyles[40].target":"Windows.UI.Xaml.Controls.Grid#MainContent", 
"controlStyles[40].styles[0]":"Background:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeAltHighColor}\" TintOpacity=\"0.4\" TintLuminosityOpacity=\"0.4\" FallbackColor=\"{ThemeResource SystemChromeMediumColor}\" />", 
"controlStyles[40].styles[1]":"CornerRadius=7", 
"controlStyles[41].target":"Button#ShowMoreSuggestionsButton > Grid@CommonStates", 
"controlStyles[41].styles[0]":"BorderBrush:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeHighColor}\" FallbackColor=\"{ThemeResource SystemChromeMediumHighColor}\" TintOpacity=\"0\" />", 
"controlStyles[41].styles[1]":"BorderThickness=1", 
"controlStyles[41].styles[2]":"CornerRadius=5", 
"controlStyles[42].target":"Button#ShowMoreSuggestionsButton > Grid@CommonStates > Border#BackgroundBorder", 
"controlStyles[42].styles[0]":"Background@Normal:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorDefault}\" />", 
"controlStyles[42].styles[1]":"Background@PointerOver:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorSecondary}\" />", 
"controlStyles[42].styles[2]":"Background@Pressed:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorTertiary}\" />", 
"controlStyles[43].target":"Button#HideMoreSuggestionsButton > Grid@CommonStates", 
"controlStyles[43].styles[0]":"BorderBrush:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeHighColor}\" FallbackColor=\"{ThemeResource SystemChromeMediumHighColor}\" TintOpacity=\"0\" />", 
"controlStyles[43].styles[1]":"BorderThickness=1", 
"controlStyles[43].styles[2]":"CornerRadius=5", 
"controlStyles[44].target":"Button#HideMoreSuggestionsButton > Grid@CommonStates > Border#BackgroundBorder", 
"controlStyles[44].styles[0]":"Background@Normal:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorDefault}\" />", 
"controlStyles[44].styles[1]":"Background@PointerOver:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorSecondary}\" />", 
"controlStyles[44].styles[2]":"Background@Pressed:=<SolidColorBrush Color=\"{ThemeResource ControlFillColorTertiary}\" />", 
"controlStyles[45].target":"Cortana.UI.Views.RichComposerBoxControl > Grid > Cortana.UI.Views.CortanaRichSearchBox", 
"controlStyles[45].styles[0]":"CornerRadius=4", 
"controlStyles[45].styles[1]":"Grid.Row=3", 
"controlStyles[45].styles[2]":"Margin=-1,0,-1,0", 
"controlStyles[46].target":"Cortana.UI.Views.RichComposerBoxControl > Grid", 
"controlStyles[46].styles[0]":"Transform3D:=<CompositeTransform3D TranslateY=\"60\" />", 
"controlStyles[46].styles[1]":"Background:=<AcrylicBrush TintColor=\"{ThemeResource SystemChromeMediumColor}\" TintOpacity=\"0\" TintLuminosityOpacity=\"0.7\" FallbackColor=\"{ThemeResource SystemChromeMediumColor}\" />", 
"controlStyles[46].styles[2]":"BorderThickness=1", 
"controlStyles[46].styles[3]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource SystemBaseHighColor}\" Opacity=\"0.2\" />", 
"controlStyles[46].styles[4]":"Height=44", 
"controlStyles[46].styles[5]":"CornerRadius=4", 
"controlStyles[47].target":"Grid#SearchBoxOnTaskbarGleamContainer > Grid > Image", 
"controlStyles[47].styles[0]":"Height=40", 
"controlStyles[48].target":"Cortana.UI.Views.RichComposerBoxControl ", 
"controlStyles[48].styles[0]":"Margin=-4,22,-4,0", 
"controlStyles[49].target":"Cortana.UI.Views.RichComposerBoxControl > Grid > Grid#ComposerBoxOnTaskbarGleamContainer", 
"controlStyles[49].styles[0]":"Padding=12,6,6,6", 
"controlStyles[50].target":"Cortana.UI.Views.RichComposerBoxControl > Grid > Cortana.UI.Views.CortanaRichSearchBox > Grid", 
"controlStyles[50].styles[0]":"BorderThickness=0,0,0,2", 
"controlStyles[50].styles[1]":"BorderBrush:=<SolidColorBrush Color=\"{ThemeResource SystemAccentColor}\" />", 
"controlStyles[50].styles[2]":"CornerRadius=4", 
"controlStyles[51].target":"Cortana.UI.Views.RichComposerBoxControl > Grid > Cortana.UI.Views.CortanaRichSearchBox > Grid > ScrollViewer", 
"controlStyles[51].styles[0]":"Margin=8,0,8,0", 
"controlStyles[52].target":"Cortana.UI.Views.RichComposerBoxControl > Grid > Cortana.UI.Views.CortanaRichSearchBox > Grid > TextBlock", 
"controlStyles[52].styles[0]":"Margin=8,0,0,1", 
"controlStyles[52].styles[1]":"Text=Ask me anything", 
"controlStyles[53].target":"Cortana.UI.Views.RichComposerBoxControl > Grid > StackPanel", 
"controlStyles[53].styles[0]":"Margin=0,0,5,0", 
"controlStyles[54].target":"Cortana.UI.Views.RichComposerBoxControl > Grid > StackPanel > Grid > Button > ContentPresenter", 
"controlStyles[54].styles[0]":"CornerRadius=6",
"controlStyles[55].target":"StartDocked.LauncherFrame > Grid#RootGrid > Grid#RootContent > Border#AcrylicBorder",
"controlStyles[55].styles[0]":"Opacity=0.5"
}
```
</details>
