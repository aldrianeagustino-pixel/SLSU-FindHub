let items = [];
let claims = [];
let isAdmin = false;
let currentTypeFilter = 'ALL';
let currentRoleFilter = 'ALL';

document.getElementById('date').valueAsDate = new Date();

// Load data directly from Python REST API
async function loadSystemData() {
    try {
        const [itemsRes, claimsRes] = await Promise.all([
            fetch('/api/items'),
            fetch('/api/claims')
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

    const res = await fetch('/api/items', {
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
    }
}

async function submitClaim(e) {
    e.preventDefault();
    const itemId = document.getElementById('claimItemId').value;
    const item = items.find(i => i.id === itemId);

    const newClaim = {
        claimId: 'claim_' + Date.now(),
        itemId: itemId,
        itemTitle: item ? item.title : 'Item',
        claimantName: document.getElementById('claimantName').value,
        claimantContact: document.getElementById('claimantContact').value,
        claimAnswer: document.getElementById('claimAnswer').value,
        submittedAt: new Date().toLocaleDateString()
    };

    const res = await fetch('/api/claims', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newClaim)
    });

    if (res.ok) {
        closeClaimModal();
        alert("Claim submitted successfully!");
        await loadSystemData();
    }
}

async function approveClaim(claimId, itemId) {
    if (confirm("Approve claim and remove this item from listing?")) {
        const res = await fetch(`/api/claims/${claimId}/approve`, { method: 'POST' });
        if (res.ok) await loadSystemData();
    }
}

async function rejectClaim(claimId) {
    if (confirm("Reject this claim?")) {
        const res = await fetch(`/api/claims/${claimId}/reject`, { method: 'DELETE' });
        if (res.ok) await loadSystemData();
    }
}

// XSS Sanitization Helper
function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/[&<>"']/g, function(m) {
        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[m];
    });
}

window.onload = loadSystemData;
