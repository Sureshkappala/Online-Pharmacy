import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

IMG_DIR = os.path.join(os.getcwd(), 'assets', 'images')
W, H = 1000, 620

# Create gradient background
img = Image.new("RGB", (W, H), (240, 253, 250))
draw = ImageDraw.Draw(img)

# Background gradient: teal light to cool cyan/white
for y in range(H):
    f = y / H
    r = int(240 * (1 - f) + 248 * f)
    g = int(253 * (1 - f) + 250 * f)
    b = int(250 * (1 - f) + 252 * f)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Subtle decorative medical background shapes
draw.ellipse([W - 250, -100, W + 150, 300], fill=(204, 251, 241))
draw.ellipse([-100, H - 250, 250, H + 100], fill=(224, 242, 254))

# Subtle grid dots
for gx in range(50, W, 40):
    for gy in range(50, H, 40):
        draw.ellipse([gx-1, gy-1, gx+1, gy+1], fill=(203, 213, 225))

# Center pharmacy pedestal / glass podium
cx, cy = W // 2, H // 2 + 30
# Soft shadow
draw.ellipse([cx - 360, cy + 140, cx + 360, cy + 220], fill=(203, 213, 225))
draw.ellipse([cx - 330, cy + 145, cx + 330, cy + 205], fill=(226, 232, 240))

# Glass counter podium
draw.rounded_rectangle([cx - 320, cy + 80, cx + 320, cy + 170], radius=24, fill=(255, 255, 255), outline=(204, 251, 241), width=3)
draw.line([cx - 300, cy + 125, cx + 300, cy + 125], fill=(241, 245, 249), width=2)

# --- 1. Main Prescription Medicine Box (Left Center) ---
bx, by = cx - 180, cy - 30
# Box shadow
draw.ellipse([bx - 100, by + 120, bx + 100, by + 150], fill=(148, 163, 184))
# Box body
draw.rounded_rectangle([bx - 90, by - 100, bx + 90, by + 120], radius=16, fill=(255, 255, 255), outline=(203, 213, 225), width=3)
# Teal top banner
draw.rounded_rectangle([bx - 90, by - 100, bx + 90, by - 40], radius=16, fill=(13, 148, 136))
draw.rectangle([bx - 90, by - 55, bx + 90, by - 40], fill=(13, 148, 136)) # flat bottom for header
# Rx Badge on box
draw.rounded_rectangle([bx - 70, by - 85, bx - 25, by - 55], radius=6, fill=(225, 29, 72))
draw.text((bx - 60, by - 80), "Rx", fill=(255, 255, 255))
# Medicine Title lines
draw.rectangle([bx - 15, by - 80, bx + 65, by - 70], fill=(255, 255, 255))
draw.rectangle([bx - 15, by - 65, bx + 45, by - 57], fill=(204, 251, 241))
# Blister preview lines
for ly in [by - 10, by + 30, by + 70]:
    draw.ellipse([bx - 70, ly - 12, bx - 46, ly + 12], fill=(240, 253, 250), outline=(13, 148, 136), width=2)
    draw.rectangle([bx - 30, ly - 8, bx + 65, ly], fill=(51, 65, 85))
    draw.rectangle([bx - 30, ly + 4, bx + 40, ly + 10], fill=(148, 163, 184))

# --- 2. High-Grade Amber / Clinical Bottle (Center) ---
botx, boty = cx, cy - 60
# Bottle shadow
draw.ellipse([botx - 70, boty + 150, botx + 70, boty + 180], fill=(148, 163, 184))
# Bottle body
draw.rounded_rectangle([botx - 65, boty - 30, botx + 65, boty + 150], radius=22, fill=(15, 118, 110), outline=(13, 148, 136), width=3)
# Label
draw.rounded_rectangle([botx - 55, boty + 5, botx + 55, boty + 115], radius=10, fill=(255, 255, 255))
# Label cross
draw.rectangle([botx - 6, boty + 25, botx + 6, boty + 55], fill=(13, 148, 136))
draw.rectangle([botx - 20, boty + 35, botx + 20, boty + 45], fill=(13, 148, 136))
draw.rectangle([botx - 35, boty + 70, botx + 35, boty + 78], fill=(30, 41, 59))
draw.rectangle([botx - 25, boty + 85, botx + 25, boty + 91], fill=(100, 116, 139))
# Bottle neck & cap
draw.rounded_rectangle([botx - 45, boty - 65, botx + 45, boty - 30], radius=8, fill=(248, 250, 252), outline=(203, 213, 225), width=2)
draw.rounded_rectangle([botx - 40, boty - 95, botx + 40, boty - 60], radius=8, fill=(255, 255, 255), outline=(13, 148, 136), width=3)
for rx_cap in range(botx - 30, botx + 31, 8):
    draw.line([rx_cap, boty - 90, rx_cap, boty - 65], fill=(13, 148, 136), width=2)

# --- 3. Digital Health Scanner / Tablet (Right Center) ---
tx, ty = cx + 185, cy - 20
# Tablet shadow
draw.ellipse([tx - 95, ty + 120, tx + 95, ty + 150], fill=(148, 163, 184))
# Tablet body
draw.rounded_rectangle([tx - 85, ty - 90, tx + 85, ty + 120], radius=20, fill=(15, 23, 42))
# Tablet screen
draw.rounded_rectangle([tx - 77, ty - 80, tx + 77, ty + 110], radius=14, fill=(240, 253, 250))
# Screen top bar
draw.rounded_rectangle([tx - 65, ty - 65, tx + 65, ty - 35], radius=6, fill=(13, 148, 136))
draw.text((tx - 45, ty - 58), "VERIFIED Rx", fill=(255, 255, 255))
# Big Verification Checkmark inside screen
draw.ellipse([tx - 40, ty - 15, tx + 40, ty + 65], fill=(255, 255, 255), outline=(16, 185, 129), width=3)
# Checkmark
draw.line([tx - 20, ty + 25, tx - 6, ty + 42], fill=(16, 185, 129), width=6)
draw.line([tx - 6, ty + 42, tx + 20, ty + 10], fill=(16, 185, 129), width=6)
# Screen status bar
draw.rectangle([tx - 55, ty + 80, tx + 55, ty + 88], fill=(203, 213, 225))
draw.rectangle([tx - 35, ty + 93, tx + 35, ty + 99], fill=(16, 185, 129))

# --- 4. Floating Capsule & Tablets (Decorative) ---
# Capsule top left
capx, capy = cx - 260, cy - 80
draw.rounded_rectangle([capx - 22, capy - 45, capx + 22, capy + 45], radius=22, fill=(13, 148, 136))
draw.rounded_rectangle([capx - 22, capy, capx + 22, capy + 45], radius=22, fill=(255, 255, 255))
draw.line([capx - 22, capy, capx + 22, capy], fill=(15, 118, 110), width=2)

# Round vitamin pill right
pillx, pilly = cx + 280, cy + 40
draw.ellipse([pillx - 28, pilly - 28, pillx + 28, pilly + 28], fill=(254, 240, 138), outline=(234, 179, 8), width=3)
draw.line([pillx - 18, pilly, pillx + 18, pilly], fill=(202, 138, 4), width=3)

# --- 5. Main Quality Stamp Badge (Bottom Center) ---
badgex, badgey = cx, cy + 185
draw.rounded_rectangle([badgex - 190, badgey - 20, badgex + 190, badgey + 20], radius=20, fill=(15, 23, 42), outline=(13, 148, 136), width=2)
# Green pulse dot
draw.ellipse([badgex - 170, badgey - 6, badgex - 158, badgey + 6], fill=(16, 185, 129))
draw.text((badgex - 145, badgey - 8), "STACKLY CERTIFIED DISPENSARY • 100% AUTHENTIC", fill=(255, 255, 255))

out = os.path.join(IMG_DIR, "hero-banner.webp")
img.save(out, format="WEBP", quality=90)
print(f"Hero Banner updated successfully: {os.path.getsize(out) / 1024:.1f} KB")
