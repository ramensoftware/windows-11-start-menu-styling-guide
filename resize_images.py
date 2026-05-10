from PIL import Image
from pathlib import Path

def resize_screenshot(screenshot_path, output_path, target_height):
    """Resize an image to target height while maintaining aspect ratio."""
    try:
        with Image.open(screenshot_path) as img:
            # Calculate new width to maintain aspect ratio
            aspect_ratio = img.width / img.height
            new_width = int(target_height * aspect_ratio)
            
            # Resize image
            resized_img = img.resize((new_width, target_height), Image.Resampling.LANCZOS)
            
            # Save resized image
            resized_img.save(output_path)
            print(f"Resized {screenshot_path.name} -> {output_path.name} ({new_width}x{target_height})")
    except Exception as e:
        print(f"Error processing {screenshot_path}: {e}")

def main():
    # Get the Themes directory
    themes_dir = Path(__file__).parent / "Themes"
    
    if not themes_dir.exists():
        print(f"Themes directory not found: {themes_dir}")
        return
    
    # Iterate over all subdirectories in Themes
    for theme_dir in themes_dir.iterdir():
        if not theme_dir.is_dir():
            continue
        
        screenshot_path = theme_dir / "screenshot.png"
        
        if not screenshot_path.exists():
            print(f"No screenshot found for theme: {theme_dir.name}")
            continue
        
        # Determine target height based on theme name
        target_height = 100 if theme_dir.name == "OnlySearch" else 200
        
        # Output path
        output_path = theme_dir / "screenshot-small.png"
        
        # Resize the screenshot
        resize_screenshot(screenshot_path, output_path, target_height)

if __name__ == "__main__":
    main()
