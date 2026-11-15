"""Apply bounded timeout settings for Render Free's 0.1 CPU, then rebuild and seal the changed dashboard."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parent
api=ROOT/'marswalk/fastapi_app.py'
s=api.read_text();old='planner=Planner(terrain) if terrain else None'
if old not in s:raise RuntimeError('Unexpected planner source; inspect before applying deployment tuning')
api.write_text(s.replace(old,'planner=Planner(terrain, timeout_s=120) if terrain else None',1))
p=ROOT/'frontend/dashboard/index.html';p.write_text(p.read_text().replace('AbortSignal.timeout(60000)','AbortSignal.timeout(150000)'))
from tools.build_dashboard import build
build()
p=ROOT/'config/release_checksums.json';checks=json.loads(p.read_text())
checks['frontend/dist/index.html']=hashlib.sha256((ROOT/'frontend/dist/index.html').read_bytes()).hexdigest()
p.write_text(json.dumps(checks,indent=2)+'\n')
print('Render Free compute timeout: 120 s; browser timeout: 150 s. Terrain data unchanged.')
