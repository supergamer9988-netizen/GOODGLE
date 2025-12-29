# GOODGLE - The Immortal Search Engine 🧠
**Powered by HDC + GZIP + WEB3 + GitHub Actions**

GOODGLE is a censorship-resistant, serverless search engine that runs entirely on the edge. It uses a **Hybrid Loading Architecture** (Cloud First + P2P Backup) and features a decentralized "Community Submission" system.

## 🌟 Features
*   **Immortal Data:** Database stored on GitHub Pages (Versioned) & Archive.org (Backup).
*   **Hybrid Speed:** Loads instantly via HTTP, falls back to WebTorrent P2P if servers fail.
*   **Smart UX:** Google-style Autocomplete & "Press Enter" support.
*   **Decentralized:** Users submit links via GitHub Issues -> A Robot (GitHub Actions) automatically indexes them.

## 🆚 GOODGLE vs. Google
| Feature | 🔵 Google | 🟢 GOODGLE |
| :--- | :--- | :--- |
| **Control** | Centralized (They decide) | **Decentralized (You decide)** |
| **Privacy** | Tracks your every move | **Zero Tracking (Client-side)** |
| **Data Source** | Crawls everything (Noise) | **Curated by Community (Signal)** |
| **Uptime** | Can be blocked/shut down | **Immortal (P2P + Hybrid)** |
| **Speed** | Fast (Server-side) | **Instant (Local Memory)** |

## 🚀 How to Deploy (For New Owners)
1.  **Fork this Repository.**
2.  Enable **GitHub Pages** in Settings (Source: `main` branch).
3.  Go to **Actions** tab and enable workflows.
4.  That's it! Your search engine is live.

## 🤖 How the "Auto-Bot" Works
We use a **GitHub Action** (`.github/workflows/auto_indexer.yml`) that acts as a robot librarian:
1.  A user clicks **"➕ Add Link"** on the website.
2.  They submit a GitHub Issue with the URL.
3.  The Robot wakes up, extracts the URL, and adds it to `sites.txt`.
4.  The Robot runs `build_db.py` to scrape the new site.
5.  The Robot updates `database.json.gz` and pushes it to the repo.
6.  The website updates automatically in ~1 minute!

## 🛠️ Manual Usage (Local)
To run the scraper on your own machine:
```bash
# 1. Install requirements
pip install requests beautifulsoup4

# 2. Add URLs to sites.txt
echo "https://example.com" >> sites.txt

# 3. Run builder
python build_db.py
```

## 📂 Project Structure
*   `index.html`: The search engine frontend (Single File).
*   `build_db.py`: The Python brain that reads sites and builds the DB.
*   `sites.txt`: The list of indexed websites.
*   `.github/workflows/`: The automation logic.

---
*Built for the Free Web.*
