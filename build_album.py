from collections import defaultdict
from datetime import datetime
from pathlib import Path
import json
import re

img_dir = Path("assets/img/lab")
out_file = Path("_data/album.json")
pattern = re.compile(r"^lab(\d{8})[-_](\d+)\.(jpg|jpeg|png|webp)$", re.IGNORECASE)
groups = defaultdict(list)

for path in sorted(img_dir.iterdir()):
    if not path.is_file():
        continue
    match = pattern.match(path.name)
    if not match:
        continue
    date_key, order = match.group(1), int(match.group(2))
    groups[date_key].append((order, f"/assets/img/lab/{path.name}"))

album = []
year_map = defaultdict(list)

for date_key in sorted(groups, reverse = True):
    dt = datetime.strptime(date_key, "%Y%m%d")
    year_map[dt.year].append({
        "id": f"lab{date_key}",
        "date": dt.strftime("%B %-d, %Y"),
        "images": [img for _, img in sorted(groups[date_key], key = lambda x: x[0])]
    })

for year in sorted(year_map, reverse = True):
    album.append({"year": year, "items": year_map[year]})

out_file.parent.mkdir(parents = True, exist_ok = True)
out_file.write_text(json.dumps(album, indent = 2, ensure_ascii = False) + "\n")
print(f"Written {out_file}")
