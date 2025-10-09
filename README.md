# "Oversimplified & Accentuated" Theme for "Windows 11 Start Menu Styler"

A cleaner, more refined Windows Start Menu (& Search Menu) theme - removing unnecessary elements and offering better **Accent Color** integration.

> ⚠️ **Note:** This theme is optimized for Windows in **Dark Mode** and may not display correctly in **Light Mode**.

### ✨ Features
- Removed unnecessary text and lines
- Enlarged icons  
- Enhanced Accent Color Presence (Automatically Updates with Windows Accent Color)  
- Improved Transparency Effects
- Added Subtle, Neat Border Reveal Effects
- Took Fallback Colors (Colors in Battery Mode) into consideration

**Author:** [OsamaJT](https://github.com/OsamaHJT)

![Screenshot](Start.png)

---

## 🎨 Elements Modified
- Start Menu
- Search Menu
- Context Menu
  
---

## 🧩 Installation

1. Download **[Windhawk](https://windhawk.net/)**.  
2. Install the **“[Windows 11 Start Menu Styler](https://windhawk.net/mods/windows-11-start-menu-styler)”** plugin.  
3. Choose the **“Oversimplified & Accentuated”** theme from the integrated themes list.  
   **OR**  
   Copy the JSON code below and go to:  
   **Windows 11 Taskbar Styler → Details → Advanced → Mod Settings**  
   Paste the code into the "**Mod settings**" box and click **Save**.


---

## 🛠️ Modification Notes

I added an extra comment line at the end of each style group to indicate the target object with common language.  
The aim is to make it easier to modify or debug the theme in the future.


<details>
<summary>Content to import (click to expand)</summary>

```json
{
"controlStyles[0].target": "MenuFlyoutPresenter",
"controlStyles[0].styles[0]": "Background:=$DarkAccent",
"controlStyles[0].styles[1]": "BorderBrush=Transparent",
"controlStyles[0].styles[2]": "//Target= Context Menu",

"controlStyles[1].target": "Border#AcrylicBorder",
"controlStyles[1].styles[0]": "Background:=$Alt",
"controlStyles[1].styles[1]": "BorderBrush=Transparent",
"controlStyles[1].styles[2]": "CornerRadius=20",
"controlStyles[1].styles[3]": "//Target= Start Menu's Body",

"controlStyles[2].target": "Border#AcrylicOverlay",
"controlStyles[2].styles[0]": "Visibility=Collapsed",
"controlStyles[2].styles[1]": "//Target= Start Menu > Acrylic Overlay Layer",

"controlStyles[3].target": "Border#DropShadow",
"controlStyles[3].styles[0]": "Visibility=Collapsed",
"controlStyles[3].styles[1]": "//Target= Start Menu > Drop Shadow (Before 24H2)",

"controlStyles[4].target": "Border#RootGridDropShadow",
"controlStyles[4].styles[0]": "Visibility=Collapsed",
"controlStyles[4].styles[1]": "//Target= Start Menu > Drop Shadow",

"controlStyles[5].target": "Border#RightCompanionDropShadow",
"controlStyles[5].styles[0]": "Visibility=Collapsed",
"controlStyles[5].styles[1]": "//Target= Start Menu > Drop Shadow of \"Phone Link\" Menu",

"controlStyles[6].target": "Border#BorderElement",
"controlStyles[6].styles[0]": "Opacity=0",
"controlStyles[6].styles[1]": "//Target= Start Menu > Search Box Overlay",

"controlStyles[7].target": "StartDocked.SearchBoxToggleButton#StartMenuSearchBox > Grid",
"controlStyles[7].styles[0]": "BorderBrush:=$Reveal",
"controlStyles[7].styles[1]": "BorderThickness=2",
"controlStyles[7].styles[2]": "CornerRadius=20",
"controlStyles[7].styles[3]": "Margin=0,0,0,-8",
"controlStyles[7].styles[4]": "//Target= Start Menu > Seach Box",

"controlStyles[8].target": "Grid > Image#SearchIconOn",
"controlStyles[8].styles[0]": "Width=20",
"controlStyles[8].styles[1]": "//Target= Start Menu > Search icon",

"controlStyles[9].target": "TextBlock#PlaceholderText",
"controlStyles[9].styles[0]": "Text=Search",
"controlStyles[9].styles[1]": "//Target= Start Menu > Search Box Placerholder Text",

"controlStyles[10].target": "Grid#InnerContent > Rectangle",
"controlStyles[10].styles[0]": "Fill:=$SolidAccent",
"controlStyles[10].styles[1]": "MinHeight=22",
"controlStyles[10].styles[2]": "MinWidth=2",
"controlStyles[10].styles[3]": "Margin=80,8,0,31",
"controlStyles[10].styles[4]": "Opacity=1",
"controlStyles[10].styles[5]": "//Target= Start Menu > Search Box > Fake Carret",

"controlStyles[11].target": "StartMenu.PinnedList#StartMenuPinnedList",
"controlStyles[11].styles[0]": "Height=421",
"controlStyles[11].styles[1]": "//Target= Start Menu > Pinned Apps Section Container",

"controlStyles[12].target": "Microsoft.UI.Xaml.Controls.PipsPager#PinnedListPipsPager",
"controlStyles[12].styles[0]": "Visibility=Collapsed",
"controlStyles[12].styles[1]": "//Target= Start Menu > Page Count Indicator",

"controlStyles[13].target": "TextBlock#PinnedListHeaderText",
"controlStyles[13].styles[0]": "Visibility=Collapsed",
"controlStyles[13].styles[1]": "//Target= Start Menu > \"Pinned\" Text",

"controlStyles[14].target": "Border#ContentBorder > Grid#DroppedFlickerWorkaroundWrapper > Border#BackgroundBorder",
"controlStyles[14].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.3\" />",
"controlStyles[14].styles[1]": "BorderBrush:=$Reveal",
"controlStyles[14].styles[2]": "BorderThickness=2",
"controlStyles[14].styles[3]": "CornerRadius=12",
"controlStyles[14].styles[4]": "Height=70",
"controlStyles[14].styles[5]": "Width=70",
"controlStyles[14].styles[6]": "//Target= Start Menu > Hover-Over Box For Pinned items (Apps & Folders)",

"controlStyles[15].target": "Grid#LogoContainer",
"controlStyles[15].styles[0]": "Height=60",
"controlStyles[15].styles[1]": "Width=60",
"controlStyles[15].styles[2]": "//Target= Start Menu > Pinned App icon Container",

"controlStyles[16].target": "Image#Logo",
"controlStyles[16].styles[0]": "Height=40",
"controlStyles[16].styles[1]": "Width=40",
"controlStyles[16].styles[2]": "//Target= Start Menu > Pinned App Icon",

"controlStyles[17].target": "Border#FolderPlate",
"controlStyles[17].styles[0]": "Background=Transparent",
"controlStyles[17].styles[1]": "BorderBrush=Transparent",
"controlStyles[17].styles[2]": "Height=56",
"controlStyles[17].styles[3]": "Width=56",
"controlStyles[17].styles[4]": "//Target= Start Menu > Folder Container",

"controlStyles[18].target": "Grid#LogosContainer",
"controlStyles[18].styles[0]": "Height=68",
"controlStyles[18].styles[1]": "Width=68",
"controlStyles[18].styles[2]": "//Target= Start Menu > Folder's Content icons",

"controlStyles[19].target": "Grid#Root > Border",
"controlStyles[19].styles[0]": "Background:=$Alt",
"controlStyles[19].styles[1]": "BorderBrush:=Transparent",
"controlStyles[19].styles[2]": "CornerRadius=20",
"controlStyles[19].styles[3]": "//Target= Start Menu > Folder's Body",

"controlStyles[20].target": "TextBlock#DisplayName",
"controlStyles[20].styles[0]": "Visibility=Collapsed",
"controlStyles[20].styles[1]": "//Target= Start Menu > Name of Pinned Apps & Folders",

"controlStyles[21].target": "Grid#SuggestionsParentContainer",
"controlStyles[21].styles[0]": "Visibility=Collapsed",
"controlStyles[21].styles[1]": "//Target= Start Menu > Suggestions Section",

"controlStyles[22].target": "Grid#TopLevelSuggestionsListHeader",
"controlStyles[22].styles[0]": "Visibility=Collapsed",
"controlStyles[22].styles[1]": "//Target= Start Menu > Suggestions Text \"Recomended\"",

"controlStyles[23].target": "Grid#ShowMoreSuggestions",
"controlStyles[23].styles[0]": "Visibility=Collapsed",
"controlStyles[23].styles[1]": "//Target= Start Menu > Show More Suggestions Button",

"controlStyles[24].target": "Grid#TopLevelSuggestionsContainer",
"controlStyles[24].styles[0]": "Visibility=Collapsed",
"controlStyles[24].styles[1]": "//Target= Start Menu > Suggestions Entries",

"controlStyles[25].target": "StartDocked.NavigationPaneButton#PowerButton > Grid",
"controlStyles[25].styles[0]": "BorderBrush:=$Reveal",
"controlStyles[25].styles[1]": "BorderThickness=2",
"controlStyles[25].styles[2]": "CornerRadius=12",
"controlStyles[25].styles[3]": "//Target= Start Menu > Power Button",

"controlStyles[26].target": "StartDocked.NavigationPaneButton#PowerButton > Grid > ContentPresenter > Grid > FontIcon",
"controlStyles[26].styles[0]": "Foreground:=$SolidAccent",
"controlStyles[26].styles[1]": "//Target= Start Menu > Power Button icon",

"controlStyles[27].target": "FontIcon#WindowsUpdatePendingReminder",
"controlStyles[27].styles[0]": "Foreground:=$SolidAccent",
"controlStyles[27].styles[1]": "//Target= Start Menu > Power Button > Update Reminder (Default:#ff9900)",

"controlStyles[28].target": "FontIcon#IconOverlay",
"controlStyles[28].styles[0]": "Foreground:=$SolidAccent",
"controlStyles[28].styles[1]": "//Target= Start Menu > Power Button > Context Menu > Update Reminder (Default:#ff9900)",

"controlStyles[29].target": "Border#BackgroundBorder",
"controlStyles[29].styles[0]": "CornerRadius=12",
"controlStyles[29].styles[1]": "//Target= Start Menu > Hover-Over Box For Buttons (Power Button, Libraries & User Button)",

"controlStyles[30].target": "Button#ShowAllAppsButton > ContentPresenter",
"controlStyles[30].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.5\" />",
"controlStyles[30].styles[1]": "BorderBrush=Transparent",
"controlStyles[30].styles[2]": "Height=25",
"controlStyles[30].styles[3]": "//Target= Start Menu > \"All >\" Button",

"controlStyles[31].target": "Button#CloseAllAppsButton > ContentPresenter",
"controlStyles[31].styles[0]": "Background:=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"0.5\" />",
"controlStyles[31].styles[1]": "BorderBrush=Transparent",
"controlStyles[31].styles[2]": "Height=25",
"controlStyles[31].styles[3]": "//Target= Start Menu > All Apps Page > \"< Back\" Button",

"controlStyles[32].target": "Button > ContentPresenter > StackPanel > TextBlock",
"controlStyles[32].styles[0]": "Visibility=Collapsed",
"controlStyles[32].styles[1]": "//Target= Start Menu > \"All >\" & \"< Back\" Buttons Text",

"controlStyles[33].target": "StackPanel > FontIcon > Grid > TextBlock",
"controlStyles[33].styles[0]": "FontSize=14 //(Default=10)",
"controlStyles[33].styles[1]": "//Target= Start Menu > \"All >\" & \"< Back\" Buttons Arrows Text",

"controlStyles[34].target": "StartDocked.AllAppsZoomListViewItem > Grid#ContentBorder@DisabledStates > Border#BorderBackground",
"controlStyles[34].styles[0]": "BorderBrush@Enabled:=$Reveal",
"controlStyles[34].styles[1]": "//Target= Start Menu > All Apps Page > Alphabet Zoomed-Out Buttons",

"controlStyles[35].target": "Border#Border",
"controlStyles[35].styles[0]": "BorderBrush:=$Reveal",
"controlStyles[35].styles[1]": "BorderThickness=2",
"controlStyles[35].styles[2]": "CornerRadius=12",
"controlStyles[35].styles[3]": "//Target= Start Menu > All Apps Page > Hover-Over Box for Alphabet",

"controlStyles[36].target": "Border#BorderBackground",
"controlStyles[36].styles[0]": "CornerRadius=12",
"controlStyles[36].styles[1]": "//Target= Start Menu > All Apps Page > Hover-Over Box for Apps & Folders",

"controlStyles[37].target": "Border#AppBorder",
"controlStyles[37].styles[0]": "Background:=$Alt",
"controlStyles[37].styles[1]": "BorderBrush=Transparent",
"controlStyles[37].styles[2]": "CornerRadius=20",
"controlStyles[37].styles[3]": "//Target= Search Menu's Body",

"controlStyles[38].target": "Border#LayerBorder",
"controlStyles[38].styles[0]": "Visibility=Collapsed",
"controlStyles[38].styles[1]": "//Target= Search Menu > Acrylic Overlay Layer for Search Menu",

"controlStyles[39].target": "Border#dropshadow",
"controlStyles[39].styles[0]": "Visibility=Collapsed",
"controlStyles[39].styles[1]": "//Target= Search Menu > Drop Shadow",

"controlStyles[40].target": "Border#TaskbarSearchBackground",
"controlStyles[40].styles[0]": "Background=Transparent",
"controlStyles[40].styles[1]": "BorderBrush=Transparent",
"controlStyles[40].styles[2]": "//Target= Search Menu > Search Box Overlay",

"controlStyles[41].target": "Cortana.UI.Views.RichSearchBoxControl#SearchBoxControl > Grid#RootGrid",
"controlStyles[41].styles[0]": "BorderBrush:=$Reveal",
"controlStyles[41].styles[1]": "BorderThickness=2",
"controlStyles[41].styles[2]": "CornerRadius=20",
"controlStyles[41].styles[3]": "//Target= Search Menu > Seach Box",

"controlStyles[42].target": "Microsoft.UI.Xaml.Controls.AnimatedIcon#SearchIconPlayer",
"controlStyles[42].styles[0]": "Width=20",
"controlStyles[42].styles[1]": "//Target= Search Menu > Search icon",

"webContentStyles[0].target": "li.rightHeaderButtons.itemTooltip.MouseHoverTooltip",
"webContentStyles[0].styles[0]": "display: none",
"webContentStyles[0].styles[1]": "//Target= Account & Options Buttons",

"webContentStyles[1].target": ".scope-with-background__backButton",
"webContentStyles[1].styles[0]": "display: none !important",
"webContentStyles[1].styles[1]": "//Target= Back Button",

"webContentStyles[2].target": ".scope-with-background__rightCaret,.scope-with-background__leftCaret",
"webContentStyles[2].styles[0]": "display: none !important",
"webContentStyles[2].styles[1]": "//Target= left and right arrows",

"webContentStyles[3].target": ".previewContainer",
"webContentStyles[3].styles[0]": "border-radius: 20px !important",
"webContentStyles[3].styles[1]": "//Target= Preview Container",

"webContentStyles[4].target": ".scopes-list",
"webContentStyles[4].styles[0]": "justify-content: center",
"webContentStyles[4].styles[1]": "//Target= Filter Buttons Group",

"webContentStyles[5].target": ".scope-with-background.darkTheme .scope-tile--selected .scope-tile__title,.scope-with-background .scope-tile--selected .scope-tile__title",
"webContentStyles[5].styles[0]": "Background: var(--accent0) !important",
"webContentStyles[5].styles[1]": "color: white !important",
"webContentStyles[5].styles[2]": "//Target= Active Filter Button (Dark&Light)",

"webContentStyles[6].target": ".scope-tile > div",
"webContentStyles[6].styles[0]": "background-color: Transparent !important",
"webContentStyles[6].styles[1]": "//Target= Inactive Filter Buttons",

"webContentStyles[7].target": ".darkTheme #menuContainer",
"webContentStyles[7].styles[0]": "background: black",
"webContentStyles[7].styles[1]": "border: 1px solid #404040",
"webContentStyles[7].styles[2]": "border-radius: 20px",
"webContentStyles[7].styles[3]": "box-shadow: none",
"webContentStyles[7].styles[4]": "//Target= Dark Theme Context Menu Container",

"webContentStyles[8].target": "#root.darkTheme:not(.fileExplorer) .contextMenu",
"webContentStyles[8].styles[0]": "background: black !important",
"webContentStyles[8].styles[1]": "border-radius: 20px !important",
"webContentStyles[8].styles[2]": "//Target= Dark Theme Context Menu",

"webContentStyles[9].target": ".lightTheme #menuContainer",
"webContentStyles[9].styles[0]": "background: white !important",
"webContentStyles[9].styles[1]": "border: 1px solid #404040",
"webContentStyles[9].styles[2]": "border-radius: 20px !important",
"webContentStyles[9].styles[3]": "box-shadow: none",
"webContentStyles[9].styles[4]": "//Target= Light Theme Context Menu Container",

"webContentStyles[10].target": "#root:not(.fileExplorer) .contextMenu",
"webContentStyles[10].styles[0]": "background: white !important",
"webContentStyles[10].styles[1]": "border-radius: 20px !important",
"webContentStyles[10].styles[2]": "//Target= Light Theme Context Menu",

"webContentStyles[11].target": "ul.contextMenu::before",
"webContentStyles[11].styles[0]": "display: none !important",
"webContentStyles[11].styles[1]": "//Target= Extra Context Menu Elements (Dark&Light)",

"styleConstants[0]": "Alt=<AcrylicBrush TintColor=\"{ThemeResource SystemAltHighColor}\" TintOpacity=\"0.6\" TintLuminosityOpacity=\"0.6\" FallbackColor=\"{ThemeResource SystemAltHighColor}\" />",
"styleConstants[1]": "Accent=<AcrylicBrush TintColor=\"{ThemeResource SystemAccentColor}\" TintOpacity=\"0.6\" TintLuminosityOpacity=\"0.6\" FallbackColor=\"{ThemeResource SystemAccentColor}\" />",
"styleConstants[2]": "DarkAccent=<AcrylicBrush TintColor=\"{ThemeResource SystemAccentColorDark1}\" TintOpacity=\"0.6\" TintLuminosityOpacity=\"0.3\" FallbackColor=\"{ThemeResource SystemAccentColorDark1}\" />",
"styleConstants[3]": "SolidAccent=<SolidColorBrush Color=\"{ThemeResource SystemAccentColor}\" Opacity=\"1\"/>",
"styleConstants[4]": "Reveal=<RevealBorderBrush Color=\"Transparent\" TargetTheme=\"1\" Opacity=\"1\" />"
}
```
