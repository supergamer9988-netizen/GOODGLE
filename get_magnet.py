import bencodepy as bencode
import hashlib
import urllib.parse

# Config
torrent_file = "db_compressed.torrent"
web_seed_url = "https://archive.org/download/database.json_202512/database.json.gz"

# Read Torrent File
with open(torrent_file, 'rb') as f:
    torrent_data = bencode.decode(f.read())

# Calculate Info Hash
info = torrent_data[b'info']
info_encoded = bencode.encode(info)
info_hash = hashlib.sha1(info_encoded).hexdigest()

# Generate Magnet Link
encoded_name = urllib.parse.quote(info[b'name'])
encoded_ws = urllib.parse.quote(web_seed_url)

magnet_link = f"magnet:?xt=urn:btih:{info_hash}&dn={encoded_name}&ws={encoded_ws}"

print("MAGNET_LINK:", magnet_link)
