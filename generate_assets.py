import os
import math
from PIL import Image, ImageDraw, ImageFont

IMG_DIR = os.path.join(os.getcwd(), 'assets', 'images')
os.makedirs(IMG_DIR, exist_ok=True)

def create_gradient_canvas(width, height, c1=(240, 249, 255), c2=(248, 250, 252)):
    img = Image.new("RGB", (width, height), c1)
    draw = ImageDraw.Draw(img)
    for y in range(height):
        factor = y / height
        r = int(c1[0] + (c2[0] - c1[0]) * factor)
        g = int(c1[1] + (c2[1] - c1[1]) * factor)
        b = int(c1[2] + (c2[2] - c1[2]) * factor)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    return img

def add_medical_watermark(draw, width, height):
    # subtle healthcare circles / cross in background
    for x, y, r in [(60, 60, 40), (width - 70, 70, 50), (width - 60, height - 60, 45)]:
        draw.ellipse([x - r, y - r, x + r, y + r], outline=(224, 242, 254), width=3)
        draw.line([x - 12, y, x + 12, y], fill=(224, 242, 254), width=3)
        draw.line([x, y - 12, x, y + 12], fill=(224, 242, 254), width=3)

def generate_product_image(filename, draw_func, title="", badge_text=None, badge_color=(13, 148, 136)):
    W, H = 500, 500
    img = create_gradient_canvas(W, H, (241, 245, 249), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    add_medical_watermark(draw, W, H)
    
    # Backdrop pedestal
    draw.ellipse([100, 360, 400, 430], fill=(226, 232, 240))
    draw.ellipse([110, 365, 390, 420], fill=(241, 245, 249))

    # Execute custom drawing
    draw_func(draw, W // 2, H // 2 - 10)

    # Optional top badge
    if badge_text:
        badge_w = len(badge_text) * 9 + 20
        draw.rounded_rectangle([25, 25, 25 + badge_w, 55], radius=6, fill=badge_color)
        draw.text((35, 33), badge_text, fill=(255, 255, 255))

    out_path = os.path.join(IMG_DIR, filename)
    img.save(out_path, format="WEBP", quality=85)
    size_kb = os.path.getsize(out_path) / 1024
    print(f"Saved {filename} ({size_kb:.1f} KB)")

# Helper drawing functions
def draw_bottle(c_cap=(15, 118, 110), c_body=(255, 255, 255), rx=False, accent=(13, 148, 136)):
    def _draw(draw, cx, cy):
        # Shadow
        draw.ellipse([cx - 80, cy + 90, cx + 80, cy + 120], fill=(203, 213, 225))
        # Body
        draw.rounded_rectangle([cx - 70, cy - 60, cx + 70, cy + 100], radius=24, fill=c_body, outline=(203, 213, 225), width=3)
        # Cap
        draw.rounded_rectangle([cx - 50, cy - 110, cx + 50, cy - 60], radius=8, fill=c_cap)
        for rx_line in range(cx - 40, cx + 41, 8):
            draw.line([rx_line, cy - 105, rx_line, cy - 65], fill=(255, 255, 255, 160), width=2)
        # Label
        draw.rounded_rectangle([cx - 62, cy - 40, cx + 62, cy + 85], radius=10, fill=(255, 255, 255), outline=(226, 232, 240), width=2)
        # Brand top bar
        draw.rectangle([cx - 62, cy - 40, cx + 62, cy - 20], fill=accent)
        # Cross icon
        draw.rectangle([cx - 6, cy - 8, cx + 6, cy + 16], fill=(16, 185, 129))
        draw.rectangle([cx - 17, cy + 2, cx + 17, cy + 6], fill=(16, 185, 129))
        # Text simulation bars
        draw.rectangle([cx - 48, cy + 26, cx + 48, cy + 36], fill=(30, 41, 59))
        draw.rectangle([cx - 36, cy + 42, cx + 36, cy + 48], fill=(100, 116, 139))
        draw.rectangle([cx - 24, cy + 54, cx + 24, cy + 58], fill=(148, 163, 184))
        if rx:
            draw.rounded_rectangle([cx - 56, cy + 64, cx - 18, cy + 80], radius=4, fill=(225, 29, 72))
            draw.text((cx - 50, cy + 66), "Rx", fill=(255, 255, 255))
    return _draw

def draw_box(c_top=(13, 148, 136), c_accent=(16, 185, 129), rx=False):
    def _draw(draw, cx, cy):
        draw.ellipse([cx - 95, cy + 95, cx + 95, cy + 125], fill=(203, 213, 225))
        draw.rounded_rectangle([cx - 90, cy - 85, cx + 90, cy + 95], radius=16, fill=(255, 255, 255), outline=(203, 213, 225), width=3)
        # Header block
        draw.rounded_rectangle([cx - 90, cy - 85, cx + 90, cy - 20], radius=14, fill=c_top)
        draw.rectangle([cx - 90, cy - 40, cx + 90, cy - 20], fill=c_top)
        draw.rectangle([cx - 90, cy - 20, cx + 90, cy - 14], fill=c_accent)
        # Cross on header
        draw.rectangle([cx - 65, cy - 65, cx - 55, cy - 35], fill=(255, 255, 255))
        draw.rectangle([cx - 75, cy - 55, cx - 45, cy - 45], fill=(255, 255, 255))
        draw.rectangle([cx - 35, cy - 58, cx + 65, cy - 50], fill=(255, 255, 255))
        draw.rectangle([cx - 35, cy - 44, cx + 30, cy - 38], fill=(224, 242, 254))
        # Blister graphic
        draw.rounded_rectangle([cx - 60, cy + 5, cx + 60, cy + 50], radius=8, fill=(241, 245, 249), outline=(226, 232, 240), width=2)
        for offset_x in [-40, -13, 13, 40]:
            draw.ellipse([cx + offset_x - 8, cy + 28 - 8, cx + offset_x + 8, cy + 28 + 8], fill=c_top)
            draw.ellipse([cx + offset_x - 4, cy + 28 - 4, cx + offset_x + 4, cy + 28 + 4], fill=(255, 255, 255, 180))
        # Description bars
        draw.rectangle([cx - 70, cy + 62, cx + 20, cy + 70], fill=(30, 41, 59))
        draw.rectangle([cx - 70, cy + 76, cx - 10, cy + 82], fill=(148, 163, 184))
        if rx:
            draw.rounded_rectangle([cx + 35, cy + 62, cx + 75, cy + 84], radius=4, fill=(225, 29, 72))
            draw.text((cx + 45, cy + 66), "Rx", fill=(255, 255, 255))
    return _draw

def draw_thermometer():
    def _draw(draw, cx, cy):
        draw.ellipse([cx - 70, cy + 90, cx + 70, cy + 120], fill=(203, 213, 225))
        draw.rounded_rectangle([cx - 26, cy - 130, cx + 26, cy + 60], radius=16, fill=(255, 255, 255), outline=(203, 213, 225), width=3)
        draw.polygon([(cx - 18, cy + 60), (cx + 18, cy + 60), (cx + 6, cy + 130), (cx - 6, cy + 130)], fill=(203, 213, 225))
        draw.rounded_rectangle([cx - 6, cy + 124, cx + 6, cy + 138], radius=3, fill=(148, 163, 184))
        # Display
        draw.rounded_rectangle([cx - 18, cy - 65, cx + 18, cy - 15], radius=6, fill=(224, 242, 254), outline=(186, 230, 253), width=2)
        draw.rectangle([cx - 12, cy - 48, cx + 12, cy - 40], fill=(14, 116, 144))
        draw.rectangle([cx - 8, cy - 34, cx + 5, cy - 30], fill=(14, 116, 144))
        # Button & logo
        draw.ellipse([cx - 8, cy + 10, cx + 8, cy + 26], fill=(13, 148, 136))
        draw.rectangle([cx - 12, cy - 100, cx + 12, cy - 94], fill=(13, 148, 136))
    return _draw

def draw_bp():
    def _draw(draw, cx, cy):
        draw.ellipse([cx - 110, cy + 90, cx + 110, cy + 125], fill=(203, 213, 225))
        draw.rounded_rectangle([cx - 85, cy - 80, cx + 85, cy + 70], radius=20, fill=(255, 255, 255), outline=(203, 213, 225), width=3)
        # Screen
        draw.rounded_rectangle([cx - 65, cy - 60, cx + 65, cy + 18], radius=10, fill=(15, 23, 42))
        draw.rectangle([cx - 50, cy - 50, cx - 10, cy - 40], fill=(52, 211, 153))
        draw.rectangle([cx - 50, cy - 32, cx + 25, cy - 22], fill=(52, 211, 153))
        draw.rectangle([cx - 50, cy - 14, cx - 5, cy - 6], fill=(56, 189, 248))
        draw.rectangle([cx + 32, cy - 46, cx + 55, cy - 42], fill=(148, 163, 184))
        draw.rectangle([cx + 32, cy - 28, cx + 55, cy - 24], fill=(148, 163, 184))
        # Controls
        draw.ellipse([cx - 45, cy + 30, cx - 20, cy + 55], fill=(13, 148, 136))
        draw.ellipse([cx - 2, cy + 33, cx + 18, cy + 53], fill=(226, 232, 240))
        draw.ellipse([cx + 26, cy + 33, cx + 46, cy + 53], fill=(226, 232, 240))
        # Tube/Cuff
        draw.line([cx - 85, cy + 10, cx - 115, cy + 30], fill=(100, 116, 139), width=8)
        draw.rounded_rectangle([cx - 135, cy - 20, cx - 110, cy + 70], radius=10, fill=(51, 65, 85))
    return _draw

def draw_oximeter():
    def _draw(draw, cx, cy):
        draw.ellipse([cx - 70, cy + 75, cx + 70, cy + 105], fill=(203, 213, 225))
        draw.rounded_rectangle([cx - 65, cy - 80, cx + 65, cy + 60], radius=20, fill=(255, 255, 255), outline=(203, 213, 225), width=3)
        draw.rounded_rectangle([cx - 52, cy - 65, cx + 52, cy + 12], radius=12, fill=(15, 23, 42))
        draw.rectangle([cx - 38, cy - 52, cx - 5, cy - 40], fill=(244, 63, 94))
        draw.rectangle([cx + 10, cy - 50, cx + 42, cy - 42], fill=(56, 189, 248))
        draw.line([cx - 40, cy - 12, cx - 20, cy - 12, cx - 10, cy - 28, cx, cy + 4, cx + 15, cy - 18, cx + 40, cy - 12], fill=(234, 179, 8), width=3)
        draw.ellipse([cx - 14, cy + 24, cx + 14, cy + 52], fill=(13, 148, 136))
    return _draw

def draw_first_aid_box():
    def _draw(draw, cx, cy):
        draw.ellipse([cx - 100, cy + 85, cx + 100, cy + 115], fill=(203, 213, 225))
        draw.rounded_rectangle([cx - 95, cy - 70, cx + 95, cy + 70], radius=18, fill=(225, 29, 72), outline=(190, 18, 60), width=3)
        draw.rectangle([cx - 16, cy - 42, cx + 16, cy + 42], fill=(255, 255, 255))
        draw.rectangle([cx - 42, cy - 16, cx + 42, cy + 16], fill=(255, 255, 255))
        draw.rounded_rectangle([cx - 40, cy - 96, cx + 40, cy - 70], radius=10, fill=(241, 245, 249), outline=(203, 213, 225), width=3)
        draw.rounded_rectangle([cx - 28, cy - 85, cx + 28, cy - 70], radius=6, fill=(255, 255, 255))
    return _draw

def draw_pump_bottle(c_accent=(13, 148, 136)):
    def _draw(draw, cx, cy):
        draw.ellipse([cx - 65, cy + 95, cx + 65, cy + 120], fill=(203, 213, 225))
        draw.rounded_rectangle([cx - 50, cy - 50, cx + 50, cy + 95], radius=18, fill=(255, 255, 255), outline=(203, 213, 225), width=3)
        draw.rectangle([cx - 14, cy - 75, cx + 14, cy - 50], fill=(226, 232, 240))
        draw.polygon([(cx - 10, cy - 95), (cx + 32, cy - 105), (cx + 42, cy - 95), (cx + 30, cy - 82), (cx - 10, cy - 82)], fill=c_accent)
        draw.line([cx + 38, cy - 95, cx + 38, cy - 75], fill=c_accent, width=4)
        draw.rounded_rectangle([cx - 40, cy - 25, cx + 40, cy + 75], radius=8, fill=(240, 253, 250), outline=(204, 251, 241), width=2)
        draw.rectangle([cx - 30, cy - 10, cx + 30, cy - 2], fill=c_accent)
        draw.rectangle([cx - 25, cy + 10, cx + 25, cy + 16], fill=(71, 85, 105))
        draw.rectangle([cx - 20, cy + 24, cx + 20, cy + 28], fill=(148, 163, 184))
        draw.ellipse([cx - 12, cy + 42, cx + 12, cy + 66], fill=(16, 185, 129))
    return _draw

def draw_tube(c_accent=(13, 148, 136)):
    def _draw(draw, cx, cy):
        draw.ellipse([cx - 60, cy + 90, cx + 60, cy + 115], fill=(203, 213, 225))
        draw.polygon([(cx - 45, cy - 75), (cx + 45, cy - 75), (cx + 30, cy + 65), (cx - 30, cy + 65)], fill=(255, 255, 255))
        draw.line([(cx - 45, cy - 75), (cx + 45, cy - 75)], fill=c_accent, width=10)
        draw.rounded_rectangle([cx - 25, cy + 65, cx + 25, cy + 95], radius=6, fill=c_accent)
        draw.rectangle([cx - 24, cy - 35, cx + 24, cy - 22], fill=c_accent)
        draw.rectangle([cx - 20, cy - 10, cx + 20, cy - 2], fill=(30, 41, 59))
        draw.rectangle([cx - 16, cy + 8, cx + 16, cy + 14], fill=(148, 163, 184))
        draw.rectangle([cx - 12, cy + 22, cx + 12, cy + 26], fill=(203, 213, 225))
    return _draw

def draw_toothbrush():
    def _draw(draw, cx, cy):
        draw.ellipse([cx - 50, cy + 95, cx + 50, cy + 120], fill=(203, 213, 225))
        draw.rounded_rectangle([cx - 16, cy - 30, cx + 16, cy + 90], radius=12, fill=(255, 255, 255), outline=(203, 213, 225), width=2)
        draw.rounded_rectangle([cx - 10, cy + 85, cx + 10, cy + 105], radius=6, fill=(226, 232, 240))
        draw.ellipse([cx - 6, cy + 10, cx + 6, cy + 22], fill=(13, 148, 136))
        # Neck & Brush Head
        draw.polygon([(cx - 8, cy - 30), (cx + 8, cy - 30), (cx + 4, cy - 85), (cx - 4, cy - 85)], fill=(255, 255, 255))
        draw.rounded_rectangle([cx - 12, cy - 125, cx + 12, cy - 80], radius=10, fill=(13, 148, 136))
        # Bristles
        for br_y in range(cy - 120, cy - 85, 7):
            draw.line([cx + 12, br_y, cx + 28, br_y], fill=(56, 189, 248), width=3)
    return _draw

# Generate Banner Images
def generate_hero_banner():
    W, H = 1000, 650
    img = create_gradient_canvas(W, H, (240, 253, 250), (224, 242, 254))
    draw = ImageDraw.Draw(img)
    # Background decorative circles
    draw.ellipse([W - 350, -50, W + 150, 450], fill=(204, 251, 241, 150))
    draw.ellipse([W - 400, 150, W + 100, 650], fill=(224, 242, 254, 180))
    
    # Large Medical cross graphic
    cx, cy = W - 250, H // 2
    draw.ellipse([cx - 180, cy - 180, cx + 180, cy + 180], fill=(255, 255, 255), outline=(13, 148, 136), width=6)
    draw.rectangle([cx - 28, cy - 110, cx + 28, cy + 110], fill=(13, 148, 136))
    draw.rectangle([cx - 110, cy - 28, cx + 110, cy + 28], fill=(13, 148, 136))
    
    # Shield & Checkmark in center
    draw.polygon([(cx, cy - 25), (cx + 25, cy - 10), (cx + 20, cy + 25), (cx, cy + 38), (cx - 20, cy + 25), (cx - 25, cy - 10)], fill=(16, 185, 129))
    draw.line([cx - 10, cy + 5, cx - 2, cy + 15, cx + 12, cy - 8], fill=(255, 255, 255), width=5)

    # Floating medicine icons around
    draw.rounded_rectangle([cx - 170, cy + 110, cx - 70, cy + 190], radius=14, fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    draw.rounded_rectangle([cx - 150, cy + 125, cx - 90, cy + 175], radius=8, fill=(14, 165, 233))
    
    draw.rounded_rectangle([cx + 80, cy - 170, cx + 190, cy - 90], radius=14, fill=(255, 255, 255), outline=(203, 213, 225), width=2)
    draw.rounded_rectangle([cx + 100, cy - 155, cx + 170, cy - 105], radius=8, fill=(16, 185, 129))
    
    # Trust badge pill
    draw.rounded_rectangle([cx - 130, cy + 210, cx + 130, cy + 260], radius=25, fill=(15, 23, 42))
    draw.text((cx - 85, cy + 225), "VERIFIED PHARMACY", fill=(255, 255, 255))

    out = os.path.join(IMG_DIR, "hero-banner.webp")
    img.save(out, format="WEBP", quality=85)
    print(f"Hero Banner saved ({os.path.getsize(out) / 1024:.1f} KB)")

def generate_prescription_guide():
    W, H = 800, 500
    img = create_gradient_canvas(W, H, (248, 250, 252), (240, 253, 250))
    draw = ImageDraw.Draw(img)
    # Clipboard / prescription sheet
    cx, cy = W // 2, H // 2
    # Shadow
    draw.ellipse([cx - 160, cy + 160, cx + 160, cy + 200], fill=(203, 213, 225))
    # Clipboard board
    draw.rounded_rectangle([cx - 150, cy - 170, cx + 150, cy + 170], radius=20, fill=(203, 213, 225))
    # Clip on top
    draw.rounded_rectangle([cx - 50, cy - 195, cx + 50, cy - 155], radius=10, fill=(100, 116, 139))
    draw.rounded_rectangle([cx - 25, cy - 185, cx + 25, cy - 165], radius=6, fill=(241, 245, 249))
    # Paper sheet
    draw.rounded_rectangle([cx - 135, cy - 150, cx + 135, cy + 155], radius=10, fill=(255, 255, 255))
    # Rx Symbol
    draw.rounded_rectangle([cx - 110, cy - 130, cx - 60, cy - 90], radius=6, fill=(225, 29, 72))
    draw.text((cx - 95, cy - 120), "Rx", fill=(255, 255, 255))
    draw.rectangle([cx - 45, cy - 125, cx + 105, cy - 115], fill=(30, 41, 59))
    draw.rectangle([cx - 45, cy - 105, cx + 60, cy - 98], fill=(100, 116, 139))
    # Divider
    draw.line([cx - 110, cy - 80, cx + 110, cy - 80], fill=(226, 232, 240), width=2)
    # Medicine lines
    for ly in [cy - 50, cy - 10, cy + 30, cy + 70]:
        draw.ellipse([cx - 110, ly, cx - 98, ly + 12], fill=(13, 148, 136))
        draw.rectangle([cx - 88, ly, cx + 100, ly + 8], fill=(51, 65, 85))
        draw.rectangle([cx - 88, ly + 12, cx + 40, ly + 17], fill=(148, 163, 184))
    # Pharmacist verified stamp
    draw.ellipse([cx + 40, cy + 60, cx + 120, cy + 140], outline=(16, 185, 129), width=3)
    draw.ellipse([cx + 46, cy + 66, cx + 114, cy + 134], outline=(16, 185, 129), width=1)
    draw.text((cx + 52, cy + 93), "VERIFIED", fill=(16, 185, 129))

    out = os.path.join(IMG_DIR, "prescription-guide.webp")
    img.save(out, format="WEBP", quality=85)
    print(f"Prescription Guide saved ({os.path.getsize(out) / 1024:.1f} KB)")

def generate_about_banner():
    W, H = 800, 500
    img = create_gradient_canvas(W, H, (240, 253, 250), (224, 242, 254))
    draw = ImageDraw.Draw(img)
    # Modern pharmacy storefront & laboratory visual
    cx, cy = W // 2, H // 2
    # Building / Storefront
    draw.rounded_rectangle([cx - 240, cy - 130, cx + 240, cy + 140], radius=16, fill=(255, 255, 255), outline=(203, 213, 225), width=3)
    # Store canopy
    draw.polygon([(cx - 250, cy - 130), (cx + 250, cy - 130), (cx + 260, cy - 80), (cx - 260, cy - 80)], fill=(13, 148, 136))
    for st in range(cx - 240, cx + 250, 40):
        draw.line([st, cy - 130, st, cy - 80], fill=(20, 184, 166), width=6)
    # Signboard
    draw.rounded_rectangle([cx - 140, cy - 70, cx + 140, cy - 25], radius=8, fill=(15, 23, 42))
    draw.text((cx - 100, cy - 55), "MediCare Plus Pharmacy", fill=(255, 255, 255))
    # Glass showcase windows & doors
    draw.rounded_rectangle([cx - 210, cy - 10, cx - 60, cy + 120], radius=8, fill=(224, 242, 254), outline=(186, 230, 253), width=2)
    draw.rounded_rectangle([cx + 60, cy - 10, cx + 210, cy + 120], radius=8, fill=(224, 242, 254), outline=(186, 230, 253), width=2)
    # Center Door
    draw.rounded_rectangle([cx - 45, cy - 10, cx + 45, cy + 140], radius=6, fill=(241, 245, 249), outline=(148, 163, 184), width=2)
    draw.line([cx, cy - 10, cx, cy + 140], fill=(148, 163, 184), width=2)
    # Medical cross logo
    draw.ellipse([cx - 25, cy + 20, cx + 25, cy + 70], fill=(16, 185, 129))
    draw.rectangle([cx - 4, cy + 30, cx + 4, cy + 60], fill=(255, 255, 255))
    draw.rectangle([cx - 15, cy + 41, cx + 15, cy + 49], fill=(255, 255, 255))

    out = os.path.join(IMG_DIR, "about-pharmacy.webp")
    img.save(out, format="WEBP", quality=85)
    print(f"About Banner saved ({os.path.getsize(out) / 1024:.1f} KB)")

# Now generate all product images
products = [
    # 1. Amoxicillin
    ("amoxicillin-500mg.webp", draw_box(c_top=(225, 29, 72), c_accent=(251, 113, 133), rx=True), "Amoxicillin 500mg", "Rx ONLY", (225, 29, 72)),
    # 2. Paracetamol
    ("paracetamol-650.webp", draw_box(c_top=(13, 148, 136), c_accent=(45, 212, 191), rx=False), "Paracetamol 650mg", "OTC Bestseller", (13, 148, 136)),
    # 3. Metformin
    ("metformin-500mg.webp", draw_box(c_top=(14, 116, 144), c_accent=(56, 189, 248), rx=True), "Metformin 500mg", "Rx Required", (225, 29, 72)),
    # 4. Atorvastatin
    ("atorvastatin-20mg.webp", draw_box(c_top=(109, 40, 217), c_accent=(167, 139, 250), rx=True), "Atorvastatin 20mg", "Rx Required", (225, 29, 72)),
    # 5. Vitamin C
    ("vitamin-c-zinc.webp", draw_bottle(c_cap=(245, 158, 11), c_body=(255, 255, 255), rx=False, accent=(245, 158, 11)), "Vitamin C + Zinc", "Immunity Booster", (245, 158, 11)),
    # 6. Omega 3
    ("omega3-fishoil.webp", draw_bottle(c_cap=(14, 165, 233), c_body=(255, 255, 255), rx=False, accent=(2, 132, 199)), "Omega-3 Fish Oil", "Triple Strength", (2, 132, 199)),
    # 7. Multivitamin Men
    ("multivitamin-men.webp", draw_bottle(c_cap=(15, 23, 42), c_body=(255, 255, 255), rx=False, accent=(59, 130, 246)), "Multivitamin Men", "Daily Vitality", (59, 130, 246)),
    # 8. Multivitamin Women
    ("multivitamin-women.webp", draw_bottle(c_cap=(219, 39, 119), c_body=(255, 255, 255), rx=False, accent=(236, 72, 153)), "Multivitamin Women", "Active Balance", (219, 39, 119)),
    # 9. Thermometer
    ("digital-thermometer.webp", draw_thermometer(), "Digital Thermometer", "Clinical Grade", (16, 185, 129)),
    # 10. BP Monitor
    ("bp-monitor.webp", draw_bp(), "Blood Pressure Monitor", "Digital Accurate", (14, 116, 144)),
    # 11. Pulse Oximeter
    ("pulse-oximeter.webp", draw_oximeter(), "Pulse Oximeter", "Instant Read", (13, 148, 136)),
    # 12. First Aid Kit
    ("first-aid-kit.webp", draw_first_aid_box(), "First Aid Kit", "Emergency Kit", (225, 29, 72)),
    # 13. Antiseptic Liquid
    ("antiseptic-liquid.webp", draw_pump_bottle(c_accent=(180, 83, 9)), "Antiseptic Liquid", "Disinfectant", (180, 83, 9)),
    # 14. Ceramide Moisturizer
    ("ceramide-moisturizer.webp", draw_tube(c_accent=(13, 148, 136)), "Ceramide Cream", "Dermatologist Tested", (13, 148, 136)),
    # 15. Gentle Cleanser
    ("gentle-cleanser.webp", draw_pump_bottle(c_accent=(2, 132, 199)), "Gentle Face Cleanser", "Hydrating Formula", (2, 132, 199)),
    # 16. Baby Rash Cream
    ("baby-diaper-rash-cream.webp", draw_tube(c_accent=(244, 114, 182)), "Baby Rash Cream", "Hypoallergenic", (244, 114, 182)),
    # 17. Baby Body Wash
    ("baby-body-wash.webp", draw_pump_bottle(c_accent=(251, 191, 36)), "Baby Wash & Shampoo", "Tear-Free", (217, 119, 6)),
    # 18. Probiotics
    ("probiotic-complex.webp", draw_bottle(c_cap=(16, 185, 129), c_body=(255, 255, 255), rx=False, accent=(5, 150, 105)), "Daily Probiotics", "50 Billion CFU", (5, 150, 105)),
    # 19. Herbal Sleep Aid
    ("herbal-sleep-aid.webp", draw_bottle(c_cap=(67, 56, 202), c_body=(255, 255, 255), rx=False, accent=(99, 102, 241)), "Melatonin Herbal Sleep", "Natural Sleep", (99, 102, 241)),
    # 20. Cough Syrup
    ("herbal-cough-syrup.webp", draw_bottle(c_cap=(194, 65, 12), c_body=(255, 255, 255), rx=False, accent=(217, 119, 6)), "Herbal Cough Syrup", "Soothes Throat", (194, 65, 12)),
    # 21. Oral Rinse
    ("oral-rinse-antibacterial.webp", draw_bottle(c_cap=(6, 182, 212), c_body=(255, 255, 255), rx=False, accent=(14, 165, 233)), "Antibacterial Oral Rinse", "Zero Alcohol", (6, 182, 212)),
    # 22. Electric Toothbrush
    ("electric-toothbrush.webp", draw_toothbrush(), "Sonic Electric Toothbrush", "Smart Timer", (13, 148, 136)),
    # 23. Hand Sanitizer Gel
    ("hand-sanitizer-gel.webp", draw_pump_bottle(c_accent=(16, 185, 129)), "Hand Sanitizer 75%", "Kills 99.9% Germs", (16, 185, 129)),
    # 24. Electrolyte Powder
    ("electrolyte-powder.webp", draw_box(c_top=(234, 88, 12), c_accent=(251, 146, 60), rx=False), "Instant Electrolytes", "Rapid Hydration", (234, 88, 12)),
]

print("Starting generation...")
generate_hero_banner()
generate_prescription_guide()
generate_about_banner()

for fname, fn, tit, btxt, bcol in products:
    generate_product_image(fname, fn, tit, btxt, bcol)

print("All product assets generated successfully!")
