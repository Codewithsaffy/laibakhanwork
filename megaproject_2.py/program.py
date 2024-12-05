# 800 743
#   439 130
  # 553 544
import pyautogui
import time
import pyperclip  # To handle clipboard

# Step 1: Click on the icon at (800, 743)
pyautogui.click(801, 747)

# Add a short delay to ensure the system processes the click
time.sleep(1)

# Step 2: Drag from (439, 130) to (553, 544) to select the text
pyautogui.moveTo(54, 161)  # Move to the starting position
pyautogui.dragTo(803, 749, duration=1, button='left')  # Drag to the ending position

# Step 3: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c')  # Use Ctrl+C to copy
pyautogui.click(473 ,701)
# Add a short delay to ensure the clipboard is updated
time.sleep(1)

# Step 4: Retrieve the copied text from the clipboard and store it in a variable
copied_text = pyperclip.paste()

# Print the copied text (optional)
print("Copied text:", copied_text)

pyperclip.copy(copied_text)
# Step 5: Click at (240, 198)
pyautogui.click(544,110)
time.sleep(0.5)  # Short delay to ensure focus on the input field

# Step 6: Paste the copied text
pyautogui.hotkey('ctrl', 'v')  # Use Ctrl+V to paste
time.sleep(0.5)  # Short delay to ensure pasting completes

# Step 7: Press Enter
pyautogui.press('enter')

print("Text pasted and Enter key pressed.")
