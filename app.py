// Gumawa ng base URL helper para siguradong sa Flask backend pumupunta ang request
const API_BASE = window.location.origin; // O kaya: 'http://192.168.1.15:5000'

async function loadSystemData() {
    try {
        const [itemsRes, claimsRes] = await Promise.all([
            fetch(`${API_BASE}/api/items`),
            fetch(`${API_BASE}/api/claims`)
        ]);
        
        items = await itemsRes.json();
        claims = await claimsRes.json();

        filterItems();
        renderClaims();
        updateClaimsBadge();
    } catch (e) {
        console.error("API Fetch Error:", e);
    }
}

async function handleFormSubmit(e) {
    e.preventDefault();
    const userRole = document.querySelector('input[name="userRole"]:checked').value;
    const itemType = document.querySelector('input[name="itemType"]:checked').value;

    const newItem = {
        id: 'item_' + Date.now(),
        userRole: userRole,
        title: document.getElementById('title').value,
        type: itemType,
        category: document.getElementById('category').value,
        location: document.getElementById('location').value,
        date: document.getElementById('date').value,
        description: document.getElementById('description').value,
        contact: document.getElementById('contact').value,
        turnoverLocation: itemType === 'FOUND' ? document.getElementById('turnoverLocation').value : null,
        secretQuestion: itemType === 'FOUND' ? document.getElementById('secretQuestion').value : null
    };

    try {
        const res = await fetch(`${API_BASE}/api/items`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newItem)
        });

        if (res.ok) {
            alert("Report successfully posted!");
            document.getElementById('reportForm').reset();
            document.getElementById('date').valueAsDate = new Date();
            toggleFoundFields();
            await loadSystemData();
            switchTab('browse');
        } else {
            alert("Nagkaroon ng error sa pag-save ng report.");
        }
    } catch (err) {
        alert("Hindi maabot ang server. Siguraduhing nakakonekta sa parehong network.");
        console.error(err);
    }
}
