"""Reconstruct the reviewable source archive transferred through the text-only GitHub connector."""
from pathlib import Path
import base64,hashlib,zipfile,io
ROOT=Path(__file__).resolve().parent
parts=sorted((ROOT/'deployment').glob('payload-*.b64'))
if len(parts)!=32:raise RuntimeError('Incomplete deployment source')
raw=base64.b64decode(''.join(p.read_text() for p in parts),validate=True)
if hashlib.sha256(raw).hexdigest()!='8f2ff87d150099730ac7fd83e6fb9832d919e83da355805767ee8ef68bf8dd22':raise RuntimeError('Source checksum mismatch')
target=ROOT/'application';target.mkdir(exist_ok=True)
with zipfile.ZipFile(io.BytesIO(raw)) as archive:
 for item in archive.infolist():
  if not (target/item.filename).resolve().is_relative_to(target.resolve()):raise RuntimeError('Invalid archive path')
 archive.extractall(target)
print('Verified and extracted complete application source')
