/**
 * STACKLY PHARMACY - CORE ENGINE
 * Vanilla JavaScript E-Commerce & Pharmacy Management
 */

// ==========================================
// 1. DEFAULT DATASET & CATALOG
// ==========================================
const DEFAULT_PRODUCTS = [
  {
    id: "med-01",
    name: "Amoxicillin 500mg Antibacterial Capsules",
    brand: "Stackly Labs",
    category: "Medicines",
    subCategory: "Antibiotics",
    price: 18.50,
    originalPrice: 22.00,
    requiresRx: true,
    inStock: true,
    stockCount: 45,
    rating: 4.8,
    reviews: 124,
    packSize: "10 Capsules Strip",
    image: "assets/images/amoxicillin-500mg.webp",
    description: "Amoxicillin is a broad-spectrum penicillin-type antibiotic used to treat bacterial infections. Requires strict adherence to prescription guidelines.",
    usage: "Take exactly as directed by your prescribing physician. Complete full course.",
    storage: "Store below 25°C in a dry place away from direct sunlight."
  },
  {
    id: "med-02",
    name: "Paracetamol 650mg Extra Relief Tablets",
    brand: "HealthPlus",
    category: "Medicines",
    subCategory: "Over-the-Counter (OTC) Products",
    price: 6.99,
    originalPrice: 8.50,
    requiresRx: false,
    inStock: true,
    stockCount: 180,
    rating: 4.9,
    reviews: 412,
    packSize: "15 Tablets",
    image: "assets/images/paracetamol-650.webp",
    description: "Effective symptomatic relief from mild-to-moderate pain, headaches, muscle aches, and fever. Fast-acting formulation.",
    usage: "Adults: 1 tablet every 4 to 6 hours as required. Do not exceed 4 tablets in 24 hours.",
    storage: "Keep in a cool, moisture-free environment."
  },
  {
    id: "med-03",
    name: "Metformin HCl 500mg Prolonged Release",
    brand: "GlycoCare",
    category: "Medicines",
    subCategory: "Diabetes Care",
    price: 14.20,
    originalPrice: 17.00,
    requiresRx: true,
    inStock: true,
    stockCount: 65,
    rating: 4.7,
    reviews: 89,
    packSize: "20 Tablets",
    image: "assets/images/metformin-500mg.webp",
    description: "Oral anti-hyperglycemic prescription medicine used in the clinical management of type 2 diabetes mellitus.",
    usage: "Usually taken with or immediately after meals as prescribed by an endocrinologist.",
    storage: "Store between 20°C to 25°C."
  },
  {
    id: "med-04",
    name: "Atorvastatin 20mg Lipid Lowering Tablets",
    brand: "CardioSafe",
    category: "Medicines",
    subCategory: "Cardiovascular",
    price: 24.50,
    originalPrice: 29.00,
    requiresRx: true,
    inStock: true,
    stockCount: 38,
    rating: 4.9,
    reviews: 140,
    packSize: "10 Tablets",
    image: "assets/images/atorvastatin-20mg.webp",
    description: "Statin medication used to lower low-density lipoprotein (LDL) cholesterol and reduce cardiovascular risk.",
    usage: "Take once daily in the evening or as directed by a doctor.",
    storage: "Store in original moisture-resistant packaging."
  },
  {
    id: "med-05",
    name: "Vitamin C 1000mg + Zinc Effervescent",
    brand: "VitaLife",
    category: "Vitamins and Nutrition",
    subCategory: "Over-the-Counter (OTC) Products",
    price: 12.99,
    originalPrice: 15.99,
    requiresRx: false,
    inStock: true,
    stockCount: 92,
    rating: 4.8,
    reviews: 280,
    packSize: "20 Effervescent Tablets",
    image: "assets/images/vitamin-c-zinc.webp",
    description: "Daily immunity booster formulated with bioavailable Vitamin C and elemental Zinc to support defense systems.",
    usage: "Dissolve 1 tablet in 200ml cold water daily.",
    storage: "Keep tube tightly closed in a dry place."
  },
  {
    id: "med-06",
    name: "Triple Strength Omega-3 Fish Oil 1200mg",
    brand: "VitaLife",
    category: "Medicines",
    subCategory: "Cardiovascular",
    price: 28.50,
    originalPrice: 34.00,
    requiresRx: true,
    inStock: true,
    stockCount: 54,
    rating: 4.9,
    reviews: 195,
    packSize: "60 Softgels",
    image: "assets/images/omega3-fishoil.webp",
    description: "Molecularly distilled EPA & DHA rich fish oil softgels supporting healthy heart rhythm, cognitive focus, and joint mobility.",
    usage: "1 softgel twice daily with meals.",
    storage: "Store in a cool dry area away from heat."
  },
  {
    id: "med-07",
    name: "Daily Multivitamin Men Active Performance",
    brand: "VitaLife",
    category: "Vitamins and Nutrition",
    subCategory: "Wellness Products",
    price: 19.99,
    originalPrice: 24.99,
    requiresRx: false,
    inStock: true,
    stockCount: 75,
    rating: 4.7,
    reviews: 150,
    packSize: "60 Tablets",
    image: "assets/images/multivitamin-men.webp",
    description: "Balanced complex of 24 essential vitamins, minerals, and antioxidants tailored specifically for active men.",
    usage: "Take 1 tablet daily after breakfast.",
    storage: "Keep out of reach of children."
  },
  {
    id: "med-08",
    name: "Daily Multivitamin Women Vitality & Glow",
    brand: "VitaLife",
    category: "Vitamins and Nutrition",
    subCategory: "Wellness Products",
    price: 19.99,
    originalPrice: 24.99,
    requiresRx: false,
    inStock: true,
    stockCount: 80,
    rating: 4.8,
    reviews: 165,
    packSize: "60 Tablets",
    image: "assets/images/multivitamin-women.webp",
    description: "Complete women's nutritional formula enriched with Biotin, Iron, Calcium, and Vitamin D3 for vitality.",
    usage: "Take 1 tablet daily with water.",
    storage: "Store tightly sealed below 25°C."
  },
  {
    id: "med-09",
    name: "Rapid-Read Clinical Digital Thermometer",
    brand: "OmronCare",
    category: "Medical Devices",
    subCategory: "General Healthcare",
    price: 15.00,
    originalPrice: 18.50,
    requiresRx: false,
    inStock: true,
    stockCount: 120,
    rating: 4.9,
    reviews: 310,
    packSize: "1 Digital Unit + Case",
    image: "assets/images/digital-thermometer.webp",
    description: "High-precision oral, rectal, and axillary body temperature measurement with 10-second fast beep readout.",
    usage: "Disinfect probe before and after each use.",
    storage: "Keep in protective sleeve when not in use."
  },
  {
    id: "med-10",
    name: "Automatic Upper Arm Blood Pressure Monitor",
    brand: "OmronCare",
    category: "Medical Devices",
    subCategory: "General Healthcare",
    price: 54.00,
    originalPrice: 65.00,
    requiresRx: false,
    inStock: true,
    stockCount: 40,
    rating: 4.9,
    reviews: 520,
    packSize: "1 Monitor + Cuff + Batteries",
    image: "assets/images/bp-monitor.webp",
    description: "Clinically validated oscillometric digital blood pressure monitor with hypertension alert indicator and 90-reading memory.",
    usage: "Sit quietly for 5 minutes before taking reading on left upper arm.",
    storage: "Keep in storage pouch, protect cuff from sharp objects."
  },
  {
    id: "med-11",
    name: "Fingertip Pulse Oximeter LED Display",
    brand: "OmronCare",
    category: "Medical Devices",
    subCategory: "General Healthcare",
    price: 26.50,
    originalPrice: 32.00,
    requiresRx: false,
    inStock: true,
    stockCount: 60,
    rating: 4.7,
    reviews: 210,
    packSize: "1 Unit with Lanyard",
    image: "assets/images/pulse-oximeter.webp",
    description: "Accurate SpO2 blood oxygen saturation and pulse rate monitor with instant OLED waveform graph.",
    usage: "Clip onto index finger, stay still during reading.",
    storage: "Remove batteries if unused for long periods."
  },
  {
    id: "med-12",
    name: "120-Piece Emergency First Aid Travel Kit",
    brand: "Curactive",
    category: "First Aid",
    subCategory: "General Healthcare",
    price: 29.99,
    originalPrice: 36.00,
    requiresRx: false,
    inStock: true,
    stockCount: 85,
    rating: 4.9,
    reviews: 180,
    packSize: "Complete Waterproof Bag",
    image: "assets/images/first-aid-kit.webp",
    description: "Hospital-grade first aid supplies including sterile dressings, burn gel, bandages, scissors, and CPR shield.",
    usage: "Refer to included emergency first aid handbook.",
    storage: "Store in easily accessible dry location."
  },
  {
    id: "med-13",
    name: "MediClean Antiseptic Wound Cleanser 500ml",
    brand: "Curactive",
    category: "First Aid",
    subCategory: "Personal Care",
    price: 8.75,
    originalPrice: 10.50,
    requiresRx: false,
    inStock: true,
    stockCount: 110,
    rating: 4.8,
    reviews: 95,
    packSize: "500 ml Bottle",
    image: "assets/images/antiseptic-liquid.webp",
    description: "Broad-spectrum antiseptic solution for cleansing cuts, abrasions, bites, and minor surgical wounds without stinging.",
    usage: "Apply undiluted on sterile cotton gauze to clean area.",
    storage: "Store below 30°C."
  },
  {
    id: "med-14",
    name: "HydraRepair Ceramide Barrier Cream 100ml",
    brand: "Dermacare",
    category: "Skin Care",
    subCategory: "Personal Care",
    price: 22.00,
    originalPrice: 26.00,
    requiresRx: false,
    inStock: true,
    stockCount: 70,
    rating: 4.9,
    reviews: 330,
    packSize: "100 ml Tube",
    image: "assets/images/ceramide-moisturizer.webp",
    description: "Dermatologist-developed barrier repair cream enriched with 3 essential ceramides and hyaluronic acid for sensitive skin.",
    usage: "Apply liberally to face and body as needed.",
    storage: "Keep in a cool dry room."
  },
  {
    id: "med-15",
    name: "Gentle Foaming Hydrating Facial Cleanser",
    brand: "Dermacare",
    category: "Skin Care",
    subCategory: "Personal Care",
    price: 16.50,
    originalPrice: 19.50,
    requiresRx: false,
    inStock: true,
    stockCount: 95,
    rating: 4.8,
    reviews: 240,
    packSize: "200 ml Pump Bottle",
    image: "assets/images/gentle-cleanser.webp",
    description: "Non-comedogenic, fragrance-free foaming gel cleanser that removes impurities while respecting skin's natural moisture barrier.",
    usage: "Massage into wet skin with circular motions and rinse.",
    storage: "Store at ambient room temperature."
  },
  {
    id: "med-16",
    name: "Gentle Zinc Baby Diaper Rash Barrier Cream",
    brand: "BabySafe",
    category: "Baby Care",
    subCategory: "Personal Care",
    price: 9.99,
    originalPrice: 12.00,
    requiresRx: false,
    inStock: true,
    stockCount: 65,
    rating: 4.9,
    reviews: 145,
    packSize: "100 g Tube",
    image: "assets/images/baby-diaper-rash-cream.webp",
    description: "Pediatrician-tested zinc oxide cream providing instant protective barrier against moisture and chafing.",
    usage: "Change wet diaper promptly and apply liberally with every change.",
    storage: "Store below 25°C."
  },
  {
    id: "med-17",
    name: "Tear-Free Organic Calendula Baby Wash 300ml",
    brand: "BabySafe",
    category: "Baby Care",
    subCategory: "Personal Care",
    price: 13.50,
    originalPrice: 16.00,
    requiresRx: false,
    inStock: true,
    stockCount: 80,
    rating: 4.8,
    reviews: 110,
    packSize: "300 ml Pump Bottle",
    image: "assets/images/baby-body-wash.webp",
    description: "Ultra-mild hypoallergenic shampoo and body wash infused with organic calendula extract for delicate infant skin.",
    usage: "Pump onto hands or washcloth, gently lather and rinse.",
    storage: "Store at room temperature."
  },
  {
    id: "med-18",
    name: "Multi-Strain Daily Probiotics 50 Billion CFU",
    brand: "PureHerb",
    category: "Wellness Products",
    subCategory: "Vitamins and Nutrition",
    price: 32.00,
    originalPrice: 39.00,
    requiresRx: false,
    inStock: true,
    stockCount: 42,
    rating: 4.8,
    reviews: 190,
    packSize: "30 Delayed-Release Caps",
    image: "assets/images/probiotic-complex.webp",
    description: "High-potency 10-strain probiotic formula designed to support gut microflora balance, digestion, and systemic immunity.",
    usage: "1 capsule daily on an empty stomach.",
    storage: "Store in a cool dry place or refrigerate for maximum potency."
  },
  {
    id: "med-19",
    name: "Melatonin & Chamomile Restful Night Capsules",
    brand: "PureHerb",
    category: "Wellness Products",
    subCategory: "Over-the-Counter (OTC) Products",
    price: 17.50,
    originalPrice: 21.00,
    requiresRx: false,
    inStock: true,
    stockCount: 50,
    rating: 4.7,
    reviews: 135,
    packSize: "60 Capsules",
    image: "assets/images/herbal-sleep-aid.webp",
    description: "Non-habit forming herbal sleep support with 5mg Melatonin, L-Theanine, Chamomile, and Lemon Balm.",
    usage: "Take 1 capsule 30 minutes before bedtime.",
    storage: "Store away from heat and direct sunlight."
  },
  {
    id: "med-20",
    name: "Natural Honey & Ivy Leaf Cough Syrup 150ml",
    brand: "PureHerb",
    category: "Over-the-Counter (OTC) Products",
    subCategory: "General Healthcare",
    price: 11.25,
    originalPrice: 13.50,
    requiresRx: false,
    inStock: true,
    stockCount: 105,
    rating: 4.8,
    reviews: 175,
    packSize: "150 ml Glass Bottle",
    image: "assets/images/herbal-cough-syrup.webp",
    description: "Soothes irritated airways and loosens stubborn phlegm using clinically researched dried ivy leaf extract and wildflower honey.",
    usage: "Adults: 10ml three times daily using measuring cup.",
    storage: "Shake well before use. Store below 25°C."
  },
  {
    id: "med-21",
    name: "Clinical Enamel Protection Oral Rinse 500ml",
    brand: "OrthoGuard",
    category: "Oral Care",
    subCategory: "Personal Care",
    price: 9.50,
    originalPrice: 11.50,
    requiresRx: false,
    inStock: true,
    stockCount: 85,
    rating: 4.7,
    reviews: 90,
    packSize: "500 ml Bottle",
    image: "assets/images/oral-rinse-antibacterial.webp",
    description: "Alcohol-free antimicrobial mouthwash that combats plaque, strengthens tooth enamel, and maintains fresh breath.",
    usage: "Rinse vigorously with 15ml for 30 seconds twice daily.",
    storage: "Do not swallow. Keep away from small children."
  },
  {
    id: "med-22",
    name: "Sonic Pulse Rechargeable Dental Toothbrush",
    brand: "OrthoGuard",
    category: "Oral Care",
    subCategory: "Medical Devices",
    price: 45.00,
    originalPrice: 55.00,
    requiresRx: false,
    inStock: true,
    stockCount: 30,
    rating: 4.9,
    reviews: 215,
    packSize: "1 Handle + 2 Brush Heads + Charger",
    image: "assets/images/electric-toothbrush.webp",
    description: "40,000 vibrations per minute sonic toothbrush with 4 cleaning modes and smart 2-minute quadrant timer.",
    usage: "Brush teeth for full 2 minutes twice daily.",
    storage: "Rinse brush head thoroughly after each use."
  },
  {
    id: "med-23",
    name: "Hospital Grade 75% Alcohol Hand Sanitizer",
    brand: "Curactive",
    category: "Personal Care",
    subCategory: "First Aid",
    price: 7.99,
    originalPrice: 9.99,
    requiresRx: false,
    inStock: true,
    stockCount: 140,
    rating: 4.9,
    reviews: 320,
    packSize: "500 ml Pump Bottle",
    image: "assets/images/hand-sanitizer-gel.webp",
    description: "Kills 99.99% of harmful bacteria and germs instantly. Formulated with soothing aloe vera and glycerin.",
    usage: "Pump coin-sized amount and rub hands briskly until dry.",
    storage: "Flammable. Keep away from open flame and heat."
  },
  {
    id: "med-24",
    name: "Instant Electrolytes Hydration Powder 10-Pack",
    brand: "VitaLife",
    category: "Wellness Products",
    subCategory: "Vitamins and Nutrition",
    price: 14.50,
    originalPrice: 17.50,
    requiresRx: false,
    inStock: true,
    stockCount: 88,
    rating: 4.8,
    reviews: 160,
    packSize: "10 Individual Sachets",
    image: "assets/images/electrolyte-powder.webp",
    description: "Rapid rehydration electrolyte drink mix with optimal sodium-to-potassium ratio and essential trace minerals.",
    usage: "Mix 1 packet into 500ml water and stir thoroughly.",
    storage: "Store in a cool dry environment."
  }
];

// Initialize Catalog in LocalStorage if not exists
function getStoredProducts() {
  const stored = localStorage.getItem("stackly_products_v2");
  if (!stored) {
    localStorage.setItem("stackly_products_v2", JSON.stringify(DEFAULT_PRODUCTS));
    return DEFAULT_PRODUCTS;
  }
  return JSON.parse(stored);
}

function saveProducts(products) {
  localStorage.setItem("stackly_products_v2", JSON.stringify(products));
}

// ==========================================
// 2. GLOBAL STATE & STORE HELPERS
// ==========================================
const Store = {
  getCart() {
    return JSON.parse(localStorage.getItem("medicare_cart") || "[]");
  },
  saveCart(cart) {
    localStorage.setItem("medicare_cart", JSON.stringify(cart));
    updateCartBadges();
  },
  addToCart(productId, qty = 1) {
    const products = getStoredProducts();
    const product = products.find(p => p.id === productId);
    if (!product) return false;

    const cart = this.getCart();
    const existing = cart.find(item => item.id === productId);

    if (existing) {
      existing.quantity += qty;
    } else {
      cart.push({
        id: product.id,
        name: product.name,
        price: product.price,
        image: product.image,
        requiresRx: product.requiresRx,
        packSize: product.packSize,
        category: product.category,
        quantity: qty
      });
    }

    this.saveCart(cart);

    if (product.requiresRx) {
      showToast(`Added "${product.name}". Note: Prescription verification required at checkout!`, "warning");
    } else {
      showToast(`Added "${product.name}" to cart!`, "success");
    }
    return true;
  },
  updateCartQty(productId, qty) {
    let cart = this.getCart();
    const item = cart.find(i => i.id === productId);
    if (item) {
      if (qty <= 0) {
        cart = cart.filter(i => i.id !== productId);
      } else {
        item.quantity = qty;
      }
      this.saveCart(cart);
    }
  },
  removeFromCart(productId) {
    let cart = this.getCart();
    cart = cart.filter(i => i.id !== productId);
    this.saveCart(cart);
    showToast("Item removed from cart.", "info");
  },
  clearCart() {
    localStorage.removeItem("medicare_cart");
    updateCartBadges();
  },
  getWishlist() {
    return JSON.parse(localStorage.getItem("medicare_wishlist") || "[]");
  },
  toggleWishlist(productId) {
    let list = this.getWishlist();
    const idx = list.indexOf(productId);
    let added = false;
    if (idx > -1) {
      list.splice(idx, 1);
      showToast("Removed from wishlist.", "info");
    } else {
      list.push(productId);
      added = true;
      showToast("Added to wishlist!", "success");
    }
    localStorage.setItem("medicare_wishlist", JSON.stringify(list));
    updateWishlistBadges();
    return added;
  },
  isInWishlist(productId) {
    return this.getWishlist().includes(productId);
  },
  getPrescriptions() {
    const list = localStorage.getItem("medicare_prescriptions");
    if (!list) {
      // Demo initial prescriptions for realistic flow
      const demoRx = [
        {
          id: "RX-88421",
          patientName: "Sarah Jenkins",
          email: "sarah.j@example.com",
          phone: "9876543210",
          fileName: "sarah_rx_amoxicillin.pdf",
          fileSize: "1.2 MB",
          uploadDate: "2026-11-02",
          status: "Verified",
          pharmacistNotes: "Prescription verified by Pharmacist Dr. Marcus Reed (Reg #PH-99214). Approved for dispensing.",
          itemsReferenced: "Amoxicillin 500mg"
        },
        {
          id: "RX-91204",
          patientName: "Robert Chen",
          email: "robert.c@example.com",
          phone: "9123456780",
          fileName: "metformin_prescription.jpg",
          fileSize: "840 KB",
          uploadDate: "2026-11-03",
          status: "Pending Review",
          pharmacistNotes: "In review queue. Awaiting dosage verification with clinic.",
          itemsReferenced: "Metformin HCl 500mg"
        }
      ];
      localStorage.setItem("medicare_prescriptions", JSON.stringify(demoRx));
      return demoRx;
    }
    return JSON.parse(list);
  },
  savePrescriptions(list) {
    localStorage.setItem("medicare_prescriptions", JSON.stringify(list));
  },
  getOrders() {
    const list = localStorage.getItem("medicare_orders");
    if (!list) {
      const demoOrders = [
        {
          orderId: "ORD-94281",
          date: "2026-11-01",
          customerName: "Alex Morgan",
          email: "alex.m@example.com",
          phone: "9876543210",
          address: "742 Evergreen Terrace, Springfield, IL 62704",
          items: [
            { name: "Paracetamol 650mg Extra Relief Tablets", quantity: 2, price: 6.99, requiresRx: false },
            { name: "Vitamin C 1000mg + Zinc Effervescent", quantity: 1, price: 12.99, requiresRx: false }
          ],
          subtotal: 26.97,
          shipping: 0,
          discount: 0,
          total: 26.97,
          status: "Delivered",
          hasRx: false,
          rxStatus: "N/A"
        },
        {
          orderId: "ORD-96102",
          date: "2026-11-03",
          customerName: "Alex Morgan",
          email: "alex.m@example.com",
          phone: "9876543210",
          address: "742 Evergreen Terrace, Springfield, IL 62704",
          items: [
            { name: "Amoxicillin 500mg Antibacterial Capsules", quantity: 1, price: 18.50, requiresRx: true },
            { name: "120-Piece Emergency First Aid Travel Kit", quantity: 1, price: 29.99, requiresRx: false }
          ],
          subtotal: 48.49,
          shipping: 0,
          discount: 5.00,
          total: 43.49,
          status: "Processing",
          hasRx: true,
          rxStatus: "Verified"
        }
      ];
      localStorage.setItem("medicare_orders", JSON.stringify(demoOrders));
      return demoOrders;
    }
    return JSON.parse(list);
  },
  saveOrders(orders) {
    localStorage.setItem("medicare_orders", JSON.stringify(orders));
  },
  getCurrentUser() {
    return JSON.parse(localStorage.getItem("medicare_user") || "null");
  },
  setCurrentUser(user) {
    localStorage.setItem("medicare_user", JSON.stringify(user));
  },
  logout() {
    localStorage.removeItem("medicare_user");
    window.location.href = "login.html";
  }
};

window.Store = Store;
window.handleLogout = function(e) {
  if (e && e.preventDefault) e.preventDefault();
  Store.logout();
};


// ==========================================
// 3. UI HELPERS & BADGES
// ==========================================
function updateCartBadges() {
  const cart = Store.getCart();
  const totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
  document.querySelectorAll(".cart-count-badge").forEach(el => {
    el.textContent = totalCount;
    el.style.display = totalCount > 0 ? "flex" : "none";
  });
}

function updateWishlistBadges() {
  const count = Store.getWishlist().length;
  document.querySelectorAll(".wishlist-count-badge").forEach(el => {
    el.textContent = count;
    el.style.display = count > 0 ? "flex" : "none";
  });
}

function showToast(message, type = "info") {
  let container = document.getElementById("toast-container");
  if (!container) {
    container = document.createElement("div");
    container.id = "toast-container";
    container.className = "toast-container";
    document.body.appendChild(container);
  }

  const toast = document.createElement("div");
  toast.className = `toast ${type === 'error' ? 'toast-error' : type === 'success' ? 'toast-success' : ''}`;
  
  const icon = type === 'success' 
    ? `<svg width="20" height="20" fill="none" stroke="#10b981" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>`
    : type === 'warning'
    ? `<svg width="20" height="20" fill="none" stroke="#d97706" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg>`
    : type === 'error'
    ? `<svg width="20" height="20" fill="none" stroke="#e11d48" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>`
    : `<svg width="20" height="20" fill="none" stroke="#0d9488" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>`;

  toast.innerHTML = `
    ${icon}
    <div style="flex:1;">${message}</div>
    <button style="opacity:0.6;font-size:1.1rem;margin-left:8px;" onclick="this.parentElement.remove()">&times;</button>
  `;

  container.appendChild(toast);
  setTimeout(() => {
    if (toast.parentElement) toast.remove();
  }, 4000);
}

// ==========================================
// 4. NAVBAR & DRAWER INITIALIZATION
// ==========================================
function openMobileDrawer(e) {
  if (e) {
    if (e.preventDefault) e.preventDefault();
    if (e.stopPropagation) e.stopPropagation();
  }
  const drawer = document.getElementById("mobile-drawer");
  const backdrop = document.getElementById("mobile-backdrop");
  const hamburger = document.getElementById("hamburger-btn");
  if (!drawer) return;
  drawer.classList.add("open");
  if (backdrop) backdrop.classList.add("open");
  if (hamburger) {
    hamburger.classList.add("active");
    hamburger.setAttribute("aria-expanded", "true");
  }
  document.body.classList.add("scroll-locked");
}

function closeMobileDrawer(e) {
  if (e) {
    if (e.preventDefault) e.preventDefault();
    if (e.stopPropagation) e.stopPropagation();
  }
  const drawer = document.getElementById("mobile-drawer");
  const backdrop = document.getElementById("mobile-backdrop");
  const hamburger = document.getElementById("hamburger-btn");
  if (drawer) drawer.classList.remove("open");
  if (backdrop) backdrop.classList.remove("open");
  if (hamburger) {
    hamburger.classList.remove("active");
    hamburger.setAttribute("aria-expanded", "false");
  }
  document.body.classList.remove("scroll-locked");
}

function toggleMobileDrawer(e) {
  if (e) {
    if (e.preventDefault) e.preventDefault();
    if (e.stopPropagation) e.stopPropagation();
  }
  const drawer = document.getElementById("mobile-drawer");
  if (!drawer) return;
  if (drawer.classList.contains("open")) {
    closeMobileDrawer(e);
  } else {
    openMobileDrawer(e);
  }
}

window.openMobileDrawer = openMobileDrawer;
window.closeMobileDrawer = closeMobileDrawer;
window.toggleMobileDrawer = toggleMobileDrawer;
window.openDrawer = openMobileDrawer;
window.closeDrawer = closeMobileDrawer;

function initNavbar() {
  const hamburger = document.getElementById("hamburger-btn");
  const drawer = document.getElementById("mobile-drawer");
  const backdrop = document.getElementById("mobile-backdrop");
  const closeBtn = document.getElementById("mobile-drawer-close");

  if (hamburger) {
    hamburger.addEventListener("click", toggleMobileDrawer);
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", closeMobileDrawer);
  }

  if (backdrop) {
    backdrop.addEventListener("click", closeMobileDrawer);
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && drawer && drawer.classList.contains("open")) {
      closeMobileDrawer(e);
    }
  });

  // Close drawer when any nav link or action button inside it is clicked
  if (drawer) {
    drawer.querySelectorAll(".nav-link, .mobile-drawer-footer a, .mobile-drawer-footer button").forEach(link => {
      link.addEventListener("click", () => {
        // give brief delay if navigating so transition is smooth
        setTimeout(() => closeMobileDrawer(), 100);
      });
    });
  }

  // Active link detection
  const currentPath = window.location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-link").forEach(link => {
    const href = link.getAttribute("href");
    if (href === currentPath || (currentPath === "" && href === "index.html")) {
      link.classList.add("active");
    }
  });

  // User auth state in header
  const user = Store.getCurrentUser();
  const authBtnDesktop = document.getElementById("nav-auth-btn");
  if (authBtnDesktop && user) {
    authBtnDesktop.innerHTML = `
      <svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/></svg>
      <span>${user.name.split(" ")[0]} (${user.role})</span>
    `;
    authBtnDesktop.href = user.role === "admin" ? "admin-dashboard.html" : "user-dashboard.html";
  }

  updateCartBadges();
  updateWishlistBadges();
}

// ==========================================
// 5. PRODUCT CARD RENDERER
// ==========================================
function createProductCardHTML(p) {
  const isWish = Store.isInWishlist(p.id);
  const discountPercent = p.originalPrice ? Math.round(((p.originalPrice - p.price) / p.originalPrice) * 100) : 0;

  return `
    <div class="product-card" data-id="${p.id}" data-category="${p.category}" data-price="${p.price}" data-rx="${p.requiresRx}">
      <div class="product-image-wrap">
        <img src="${p.image}" alt="${p.name}" loading="lazy" width="300" height="300">
        <div class="product-card-badges">
          ${p.requiresRx ? '<span class="badge badge-rx">Rx Required</span>' : '<span class="badge badge-green">OTC Safe</span>'}
          ${discountPercent > 0 ? `<span class="badge badge-amber">${discountPercent}% OFF</span>` : ''}
        </div>
        <button class="product-wishlist-btn ${isWish ? 'active' : ''}" title="${isWish ? 'Remove from Wishlist' : 'Add to Wishlist'}" onclick="handleWishlistClick('${p.id}', this)" aria-label="Wishlist">
          <svg width="18" height="18" fill="${isWish ? 'currentColor' : 'none'}" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/></svg>
        </button>
      </div>

      <div class="product-card-body">
        <span class="product-category-text">${p.category}</span>
        <h3 class="product-title" title="${p.name}">
          <a href="product-details.html?id=${p.id}">${p.name}</a>
        </h3>
        <p class="product-brand">${p.brand} • ${p.packSize || 'Standard Pack'}</p>

        <div class="product-rating">
          <div class="rating-stars">
            ${'★'.repeat(Math.round(p.rating))}${'☆'.repeat(5 - Math.round(p.rating))}
          </div>
          <span>(${p.reviews || 0})</span>
        </div>

        ${p.requiresRx ? `
          <div class="rx-notice-strip">
            <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
            Valid Doctor's Prescription Required
          </div>
        ` : ''}

        <div class="product-availability">
          <span class="status-dot ${p.inStock ? '' : 'out-of-stock'}"></span>
          <span>${p.inStock ? 'In Stock (Ready to dispatch)' : 'Temporarily Out of Stock'}</span>
        </div>

        <div class="product-price-row">
          <span class="product-current-price">$${p.price.toFixed(2)}</span>
          ${p.originalPrice ? `<span class="product-original-price">$${p.originalPrice.toFixed(2)}</span>` : ''}
          ${discountPercent > 0 ? `<span class="product-discount-pill">Save ${discountPercent}%</span>` : ''}
        </div>

        <div class="product-card-actions">
          <button class="btn btn-primary btn-sm" onclick="Store.addToCart('${p.id}', 1)" ${!p.inStock ? 'disabled' : ''}>
            <svg width="16" height="16" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
            Add to Cart
          </button>
          <a href="product-details.html?id=${p.id}" class="btn btn-outline-dark btn-sm" title="View Specifications">
            Details
          </a>
        </div>
      </div>
    </div>
  `;
}

function handleWishlistClick(id, btnEl) {
  const added = Store.toggleWishlist(id);
  if (btnEl) {
    btnEl.classList.toggle("active", added);
    const svg = btnEl.querySelector("svg");
    if (svg) svg.setAttribute("fill", added ? "currentColor" : "none");
  }
}

// ==========================================
// 6. INITIALIZE ON DOM READY
// ==========================================
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initNavbar);
} else {
  initNavbar();
}
