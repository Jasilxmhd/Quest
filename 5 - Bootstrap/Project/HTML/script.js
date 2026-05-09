// =========================
// THEME
// =========================
const body = document.body;
const themeBtn = document.getElementById("theme-toggle");

themeBtn?.addEventListener("click", () => {
  body.classList.toggle("dark-mode");
  body.classList.toggle("light-mode");

  const i = themeBtn.querySelector("i");
  i?.classList.toggle("fa-moon");
  i?.classList.toggle("fa-sun");
});

// =========================
// WISHLIST SYSTEM (TRACKiT)
// =========================
function getWishlist() {
  return JSON.parse(localStorage.getItem("wishlist")) || [];
}

function saveWishlist(list) {
  localStorage.setItem("wishlist", JSON.stringify(list));
}

function updateFavCount() {
  const list = getWishlist();
  const badge = document.getElementById("favCount");
  if (badge) badge.textContent = list.length;
}

function syncWishlistIcons() {
  const list = getWishlist();
  const names = new Set(list.map(i => i.name));

  document.querySelectorAll(".product-card").forEach(card => {
    const name = card.querySelector(".product-title")?.innerText.trim();
    const fav = card.querySelector(".fav-icon");
    if (!name || !fav) return;

    const inWish = names.has(name);
    fav.classList.toggle("fa-solid", inWish);
    fav.classList.toggle("fa-regular", !inWish);
    fav.classList.toggle("active", inWish);
  });
}

function toggleWishlist(product, favIcon) {
  let list = getWishlist();
  const index = list.findIndex(i => i.name === product.name);

  if (index > -1) list.splice(index, 1);
  else list.push(product);

  saveWishlist(list);
  updateFavCount();

  const inWish = index === -1;
  favIcon.classList.toggle("fa-solid", inWish);
  favIcon.classList.toggle("fa-regular", !inWish);
  favIcon.classList.toggle("active", inWish);
}

// =========================
// BANNER SLIDER
// =========================
const slides = [...document.querySelectorAll(".banner-slider .slide")];
let idx = 0, t;
const IMG_MS = 3000, VID_MAX = 12000;

const show = (n) => {
  slides.forEach((s, i) => {
    s.classList.toggle("active", i === n);
    const v = s.querySelector("video");
    if (v) { v.pause(); v.currentTime = 0; }
  });

  const v = slides[n]?.querySelector("video");
  if (v) v.play().catch(()=>{});

  const ms = v ? Math.min(((v.duration || 5) * 1000), VID_MAX) : IMG_MS;
  clearTimeout(t);
  t = setTimeout(() => show(idx = (idx + 1) % slides.length), ms);
};

if (slides.length) {
  show(0);
  const banner = document.querySelector(".banner-slider");
  banner?.addEventListener("mouseenter", () => clearTimeout(t));
  banner?.addEventListener("mouseleave", () => show(idx));
}

// =========================
// CART SYSTEM (TRACKiT)
// =========================
function getCart() {
  return JSON.parse(localStorage.getItem("cart")) || [];
}

function saveCart(cart) {
  localStorage.setItem("cart", JSON.stringify(cart));
}

function updateCartCount() {
  const cart = getCart();
  const totalQty = cart.reduce((sum, item) => sum + item.qty, 0);

  const badge = document.getElementById("cartCount");
  if (badge) badge.textContent = totalQty;
}

function parsePrice(priceText) {
  return Number((priceText || "").replace(/[^0-9.]/g, "")) || 0;
}

function addToCart(product) {
  const cart = getCart();
  const existing = cart.find(item => item.name === product.name);

  if (existing) existing.qty += 1;
  else cart.push({ ...product, qty: 1 });

  saveCart(cart);
  updateCartCount();
}

// =========================
// SMART SEARCH + PRIORITY
// =========================
const searchInput = document.querySelector(".search-bar input");
const searchBtn = document.getElementById("searchBtn");

let originalCards = [];

function normalize(str) {
  return (str || "").toLowerCase().trim();
}

function resetToOriginalOrder() {
  const main = document.querySelector("main");
  if (!main || !originalCards.length) return;

  originalCards.forEach(card => {
    card.classList.remove("priority");
    card.style.display = "block";
    main.appendChild(card);
  });
}

function runSearch() {
  const q = normalize(searchInput?.value);
  const main = document.querySelector("main");
  const cards = Array.from(document.querySelectorAll("main .product-card"));
  if (!main || !cards.length) return;

  // reset styles
  cards.forEach(card => {
    card.classList.remove("priority");
    card.style.display = "block";
  });

  // empty => restore original order
  if (!q) {
    resetToOriginalOrder();
    return;
  }

  // MATCH (title + alt + data-type)
  const isMatch = (card) => {
    const title = normalize(card.querySelector(".product-title")?.innerText);
    const alt = normalize(card.querySelector(".product-img")?.getAttribute("alt"));
    const type = normalize(card.dataset.type);
    return title.includes(q) || alt.includes(q) || type.includes(q);
  };

  const matches = cards.filter(isMatch);

  if (!matches.length) {
    resetToOriginalOrder();
    return;
  }

  let priority = [];
  let rest = [];

  if (q.includes("laptop")) {
    priority = matches.filter(card => normalize(card.dataset.type) === "laptop");
    if (!priority.length) priority = matches;
  } else {
    priority = matches;
  }

  rest = cards.filter(card => !priority.includes(card));

  [...priority].reverse().forEach(card => {
    card.classList.add("priority");
    main.prepend(card);
  });

  rest.forEach(card => main.appendChild(card));

  priority[0]?.scrollIntoView({ behavior: "smooth", block: "start" });
}

// =========================
// INIT (ONE DOMContentLoaded)
// =========================
document.addEventListener("DOMContentLoaded", () => {
  originalCards = Array.from(document.querySelectorAll("main .product-card"));

  updateCartCount();
  updateFavCount();
  syncWishlistIcons();

  // Product card expand + wishlist
  document.querySelectorAll(".product-card").forEach((card) => {
    const panel = card.querySelector(".action-panel");
    const fav = card.querySelector(".fav-icon");

    card.classList.add("collapsed");

    card.addEventListener("click", () => {
      const open = card.classList.toggle("expanded");
      card.classList.toggle("collapsed", !open);
      panel?.classList.toggle("show", open);
    });

    fav?.addEventListener("click", (e) => {
      e.stopPropagation();

      const img = card.querySelector(".product-img")?.getAttribute("src") || "";
      const name = card.querySelector(".product-title")?.innerText.trim() || "Product";
      const price = card.querySelector(".product-price")?.innerText.trim() || "$0";

      toggleWishlist({ name, price, img }, fav);
    });
  });

  // Add to cart buttons
  document.querySelectorAll(".add-cart").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();

      const card = btn.closest(".product-card");
      if (!card) return;

      const img = card.querySelector(".product-img")?.getAttribute("src") || "";
      const name = card.querySelector(".product-title")?.innerText.trim() || "Product";
      const priceText = card.querySelector(".product-price")?.innerText || "$0";
      const price = parsePrice(priceText);

      addToCart({ name, price, img });

      const oldText = btn.innerText;
      btn.innerText = "ADDED ✓";
      btn.disabled = true;

      setTimeout(() => {
        btn.innerText = oldText;
        btn.disabled = false;
      }, 700);
    });
  });

  // ✅ SEARCH ONLY WHEN CLICK ICON
  searchBtn?.addEventListener("click", (e) => {
    e.preventDefault();
    runSearch();
  });

  // ✅ Optional: Enter = click icon (not auto search while typing)
  searchInput?.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      searchBtn?.click();
    }
  });
});
