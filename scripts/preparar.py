"""Converte uma imagem para JPG otimizado para post do Google Meu Negócio.
Uso: python3 scripts/preparar.py <origem> <destino.jpg>"""
import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
if max(im.size) > 1600:
    im.thumbnail((1600, 1600), Image.LANCZOS)
im.save(dst, "JPEG", quality=88, optimize=True, progressive=True)
print(dst, im.size)
