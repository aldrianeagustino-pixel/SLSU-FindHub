<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campus Lost & Found Portal</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome Icons CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-50 font-sans text-slate-800 min-h-screen flex flex-col">

    <!-- Header / Navbar -->
    <header class="bg-indigo-700 text-white shadow-md">
        <div class="max-w-7xl mx-auto px-4 py-4 flex flex-col sm:flex-row justify-between items-center gap-4">
            <div class="flex items-center space-x-3">
                <i class="fa-solid fa-[#ffffff] fa-boxes-stacked text-3xl"></i>
                <div>
                    <h1 class="text-xl font-bold tracking-wide">Campus Lost & Found</h1>
                    <p class="text-xs text-indigo-200">Official Student & Staff Portal</p>
                </div>
            </div>
            <nav class="flex space-x-2">
                <button id="navBrowseBtn" onclick="switchTab('browse')" class="px-4 py-2 rounded-lg bg-indigo-800 font-medium text-sm transition">
                    <i class="fa-solid fa-magnifying-glass mr-2"></i>Browse Items
                </button>
                <button id="navReportBtn" onclick="switchTab('report')" class="px-4 py-2 rounded-lg hover:bg-indigo-600 font-medium text-sm transition">
                    <i class="fa-solid fa-plus-circle mr-2"></i>Report Item
                </button>
            </nav>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="max-w-7xl mx-auto px-4 py-8 flex-grow w-full">

        <!-- ================= BROWSE TAB ================= -->
        <section id="browseTab">
            <!-- Search & Filters -->
            <div class="bg-white p-4 rounded-xl shadow-sm border border-slate-200 mb-8 flex flex-col md:flex-row gap-4 justify-between items-center">
                <div class="relative w-full md:w-1/2">
                    <i class="fa-solid fa-search absolute left-3 top-3.5 text-slate-400"></i>
                    <input type="text" id="searchInput" oninput="filterItems()" placeholder="Search by name, description, or location..." class="w-full pl-10 pr-4 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500">
                </div>
                <div class="flex flex-wrap gap-2 w-full md:w-auto">
                    <!-- Type Filter Buttons -->
                    <button onclick="setTypeFilter('ALL')" id="filterAll" class="filter-btn px-4 py-2 rounded-lg text-sm font-medium bg-indigo-600 text-white">All</button>
                    <button onclick="setTypeFilter('LOST')" id="filterLost" class="filter-btn px-4 py-2 rounded-lg text-sm font-medium bg-slate-100 text-slate-600 hover:bg-slate-200">Lost</button>
                    <button onclick="setTypeFilter('FOUND')" id="filterFound" class="filter-btn px-4 py-2 rounded-lg text-sm font-medium bg-slate-100 text-slate-600 hover:bg-slate-200">Found</button>
                    
                    <!-- Category Dropdown -->
                    <select id="categorySelect" onchange="filterItems()" class="px-3 py-2 border border-slate-300 rounded-lg text-sm text-slate-600 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        <option value="ALL">All Categories</option>
                        <option value="Electronics">Electronics</option>
                        <option value="ID/Documents">ID/Documents</option>
                        <option value="Keys">Keys</option>
                        <option value="Clothing">Clothing</option>
                        <option value="Bags">Bags</option>
                        <option value="Other">Other</option>
                    </select>
                </div>
            </div>

            <!-- Items Grid -->
            <div id="itemsGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                <!-- Dynamic cards populated by JavaScript -->
            </div>

            <!-- Empty State Message -->
            <div id="noResults" class="hidden text-center py-12">
                <i class="fa-solid fa-ghost text-5xl text-slate-300 mb-3"></i>
                <p class="text-slate-500 text-lg">No matching items found.</p>
            </div>
        </section>


        <!-- ================= REPORT ITEM TAB ================= -->
        <section id="reportTab" class="hidden max-w-2xl mx-auto">
            <div class="bg-white p-6 sm:p-8 rounded-xl shadow-sm border border-slate-200">
                <h2 class="text-2xl font-bold mb-2 text-slate-800">Report a Lost or Found Item</h2>
                <p class="text-slate-500 text-sm mb-6">Fill out the form below to post an item to the campus bulletin.</p>

                <form id="reportForm" onsubmit="handleFormSubmit(event)">
                    <div class="space-y-4">
                        <!-- Listing Type -->
                        <div>
                            <label class="block text-sm font-medium text-slate-700 mb-1">Status Type *</label>
                            <div class="flex space-x-4">
                                <label class="flex items-center cursor-pointer">
                                    <input type="radio" name="itemType" value="LOST" checked class="text-indigo-600 focus:ring-indigo-500">
                                    <span class="ml-2 text-sm font-semibold text-rose-600">I Lost Something</span>
                                </label>
                                <label class="flex items-center cursor-pointer">
                                    <input type="radio" name="itemType" value="FOUND" class="text-indigo-600 focus:ring-indigo-500">
                                    <span class="ml-2 text-sm font-semibold text-emerald-600">I Found Something</span>
                                </label>
                            </div>
                        </div>

                        <!-- Item Title -->
                        <div>
                            <label for="title" class="block text-sm font-medium text-slate-700 mb-1">Item Name / Title *</label>
                            <input type="text" id="title" required placeholder="e.g. Blue Hydro Flask, Student ID Card" class="w-full p-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none">
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                            <!-- Category -->
                            <div>
                                <label for="category" class="block text-sm font-medium text-slate-700 mb-1">Category *</label>
                                <select id="category" required class="w-full p-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none">
                                    <option value="">Select Category</option>
                                    <option value="Electronics">Electronics</option>
                                    <option value="ID/Documents">ID/Documents</option>
                                    <option value="Keys">Keys</option>
                                    <option value="Clothing">Clothing</option>
                                    <option value="Bags">Bags</option>
                                    <option value="Other">Other</option>
                                </select>
                            </div>
                            <!-- Location -->
                            <div>
                                <label for="location" class="block text-sm font-medium text-slate-700 mb-1">Location *</label>
                                <input type="text" id="location" required placeholder="e.g. Science Building, Library 2nd Floor" class="w-full p-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none">
                            </div>
                        </div>

                        <!-- Date -->
                        <div>
                            <label for="date" class="block text-sm font-medium text-slate-700 mb-1">Date (Lost or Found) *</label>
                            <input type="date" id="date" required class="w-full p-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none">
                        </div>

                        <!-- Description -->
                        <div>
                            <label for="description" class="block text-sm font-medium text-slate-700 mb-1">Detailed Description *</label>
                            <textarea id="description" rows="3" required placeholder="Describe distinct features, stickers, contents, brand, etc." class="w-full p-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none"></textarea>
                        </div>

                        <!-- Contact Info -->
                        <div>
                            <label for="contact" class="block text-sm font-medium text-slate-700 mb-1">Your Contact Email/Phone *</label>
                            <input type="text" id="contact" required placeholder="student@university.edu or (555) 000-0000" class="w-full p-2.5 border border-slate-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none">
                        </div>

                        <!-- Submit Button -->
                        <button type="submit" class="w-full py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-medium rounded-lg shadow-sm transition mt-4">
                            Submit Report
                        </button>
                    </div>
                </form>
            </div>
        </section>

    </main>

    <!-- Item Details Modal -->
    <div id="itemModal" class="fixed inset-0 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4 hidden z-50">
        <div class="bg-white rounded-xl shadow-xl max-w-md w-full p-6 relative">
            <button onclick="closeModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-600 text-xl">&times;</button>
            <div id="modalContent">
                <!-- Injected via JavaScript -->
            </div>
        </div>
    </div>

    <!-- JavaScript Application Logic -->
    <script>
        // Sample Initial Data
        let items = [
            {
                id: 1,
                title: "MacBook Air M2 (Space Gray)",
                type: "LOST",
                category: "Electronics",
                location: "Central Library, 3rd Floor",
                date: "2026-09-08",
                description: "Has a yellow anime sticker on the top shell. Left inside a black laptop sleeve.",
                contact: "alex.m@univ.edu"
            },
            {
                id: 2,
                title: "Campus ID - Sarah Jenkins",
                type: "FOUND",
                category: "ID/Documents",
                location: "Student Union Cafeteria",
                date: "2026-09-09",
                description: "Found near the cashier counter. Turned in to campus security desk.",
                contact: "security@univ.edu"
            },
            {
                id: 3,
                title: "Car Keys with Red Lanyard",
                type: "FOUND",
                category: "Keys",
                location: "North Parking Lot B",
                date: "2026-09-07",
                description: "Toyota key fob attached to a red Nike lanyard.",
                contact: "parking-office@univ.edu"
            },
            {
                id: 4,
                title: "Denim Jacket with Pins",
                type: "LOST",
                category: "Clothing",
                location: "Engineering Hall Room 102",
                date: "2026-09-05",
                description: "Vintage blue denim jacket with several enamel pins on the left lapel.",
                contact: "j.doe@univ.edu"
            }
        ];

        let currentTypeFilter = 'ALL';

        // Initialize Render
        document.addEventListener('DOMContentLoaded', () => {
            renderItems(items);
        });

        // Tab Switcher
        function switchTab(tab) {
            const browseTab = document.getElementById('browseTab');
            const reportTab = document.getElementById('reportTab');
            const navBrowseBtn = document.getElementById('navBrowseBtn');
            const navReportBtn = document.getElementById('navReportBtn');

            if (tab === 'browse') {
                browseTab.classList.remove('hidden');
                reportTab.classList.add('hidden');
                navBrowseBtn.className = "px-4 py-2 rounded-lg bg-indigo-800 font-medium text-sm transition";
                navReportBtn.className = "px-4 py-2 rounded-lg hover:bg-indigo-600 font-medium text-sm transition";
            } else {
                browseTab.classList.add('hidden');
                reportTab.classList.remove('hidden');
                navReportBtn.className = "px-4 py-2 rounded-lg bg-indigo-800 font-medium text-sm transition";
                navBrowseBtn.className = "px-4 py-2 rounded-lg hover:bg-indigo-600 font-medium text-sm transition";
            }
        }

        // Render Item Cards
        function renderItems(data) {
            const grid = document.getElementById('itemsGrid');
            const noResults = document.getElementById('noResults');
            grid.innerHTML = '';

            if (data.length === 0) {
                noResults.classList.remove('hidden');
                return;
            } else {
                noResults.classList.add('hidden');
            }

            data.forEach(item => {
                const isLost = item.type === 'LOST';
                const badgeColor = isLost ? 'bg-rose-100 text-rose-700 border-rose-200' : 'bg-emerald-100 text-emerald-700 border-emerald-200';
                
                const card = document.createElement('div');
                card.className = "bg-white rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between overflow-hidden";
                card.innerHTML = `
                    <div class="p-5">
                        <div class="flex justify-between items-start mb-3">
                            <span class="px-2.5 py-1 text-xs font-bold rounded-full border ${badgeColor}">
                                ${item.type}
                            </span>
                            <span class="text-xs text-slate-400 font-medium">${item.category}</span>
                        </div>
                        <h3 class="font-bold text-slate-800 text-lg mb-2 line-clamp-1">${escapeHtml(item.title)}</h3>
                        <p class="text-slate-600 text-sm mb-4 line-clamp-2">${escapeHtml(item.description)}</p>
                        
                        <div class="space-y-1.5 text-xs text-slate-500">
                            <div class="flex items-center"><i class="fa-solid fa-location-dot w-4 text-slate-400"></i><span class="truncate">${escapeHtml(item.location)}</span></div>
                            <div class="flex items-center"><i class="fa-solid fa-calendar w-4 text-slate-400"></i><span>${item.date}</span></div>
                        </div>
                    </div>
                    <div class="bg-slate-50 px-5 py-3 border-t border-slate-100">
                        <button onclick="openModal(${item.id})" class="w-full py-1.5 bg-white border border-slate-300 hover:bg-slate-100 text-slate-700 text-xs font-semibold rounded-lg transition">
                            View Details
                        </button>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        // Filtering Logic
        function setTypeFilter(type) {
            currentTypeFilter = type;
            
            // Update button styles
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.className = "filter-btn px-4 py-2 rounded-lg text-sm font-medium bg-slate-100 text-slate-600 hover:bg-slate-200";
            });
            if(type === 'ALL') document.getElementById('filterAll').className = "filter-btn px-4 py-2 rounded-lg text-sm font-medium bg-indigo-600 text-white";
            if(type === 'LOST') document.getElementById('filterLost').className = "filter-btn px-4 py-2 rounded-lg text-sm font-medium bg-indigo-600 text-white";
            if(type === 'FOUND') document.getElementById('filterFound').className = "filter-btn px-4 py-2 rounded-lg text-sm font-medium bg-indigo-600 text-white";

            filterItems();
        }

        function filterItems() {
            const searchQuery = document.getElementById('searchInput').value.toLowerCase();
            const categoryQuery = document.getElementById('categorySelect').value;

            const filtered = items.filter(item => {
                const matchesType = currentTypeFilter === 'ALL' || item.type === currentTypeFilter;
                const matchesCategory = categoryQuery === 'ALL' || item.category === categoryQuery;
                const matchesSearch = item.title.toLowerCase().includes(searchQuery) || 
                                      item.description.toLowerCase().includes(searchQuery) || 
                                      item.location.toLowerCase().includes(searchQuery);

                return matchesType && matchesCategory && matchesSearch;
            });

            renderItems(filtered);
        }

        // Handle Report Form Submit
        function handleFormSubmit(e) {
            e.preventDefault();
            
            const newItem = {
                id: Date.now(),
                title: document.getElementById('title').value,
                type: document.querySelector('input[name="itemType"]:checked').value,
                category: document.getElementById('category').value,
                location: document.getElementById('location').value,
                date: document.getElementById('date').value,
                description: document.getElementById('description').value,
                contact: document.getElementById('contact').value
            };

            items.unshift(newItem); // Add new item to front
            document.getElementById('reportForm').reset();
            
            // Switch back to browse view
            switchTab('browse');
            filterItems();
            
            alert('Item report published successfully!');
        }

        // Modal Functionality
        function openModal(id) {
            const item = items.find(i => i.id === id);
            if (!item) return;

            const modalContent = document.getElementById('modalContent');
            const badgeColor = item.type === 'LOST' ? 'bg-rose-100 text-rose-700' : 'bg-emerald-100 text-emerald-700';

            modalContent.innerHTML = `
                <div class="mb-4">
                    <span class="px-2.5 py-1 text-xs font-bold rounded-full ${badgeColor}">${item.type}</span>
                    <span class="text-xs text-slate-400 font-medium ml-2">${item.category}</span>
                </div>
                <h3 class="text-xl font-bold text-slate-800 mb-2">${escapeHtml(item.title)}</h3>
                <p class="text-slate-600 text-sm mb-6">${escapeHtml(item.description)}</p>
                
                <div class="bg-slate-50 p-4 rounded-lg space-y-2 text-sm border border-slate-100 mb-6">
                    <div class="flex items-center text-slate-600"><i class="fa-solid fa-location-dot w-6 text-indigo-500"></i><strong>Location:</strong>&nbsp;${escapeHtml(item.location)}</div>
                    <div class="flex items-center text-slate-600"><i class="fa-solid fa-calendar w-6 text-indigo-500"></i><strong>Date:</strong>&nbsp;${item.date}</div>
                </div>

                <div class="border-t pt-4">
                    <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1">Claim / Contact Information</p>
                    <p class="text-indigo-600 font-bold text-md select-all">${escapeHtml(item.contact)}</p>
                </div>
            `;

            document.getElementById('itemModal').classList.remove('hidden');
        }

        function closeModal() {
            document.getElementById('itemModal').classList.add('hidden');
        }

        // Helper function for XSS protection
        function escapeHtml(str) {
            return str.replace(/[&<>"']/g, function(m) {
                return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[m];
            });
        }
    </script>
</body>
</html>
