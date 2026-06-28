# -*- coding: utf-8 -*-
"""Gera 6 avatares ilustrados (flat) para os depoimentos."""
import os
OUT = os.path.dirname(os.path.abspath(__file__)) + "/avatars"
os.makedirs(OUT, exist_ok=True)

# (bg, skin, hair, cloth, feminino?)
people = [
    ("#FFE0C2", "#F1B589", "#3A2A20", "#E11D2A", True),   # 1 Juliana
    ("#FFD9B0", "#C98B5E", "#1C140F", "#1FA85A", False),  # 2 Rafael
    ("#FFE7CE", "#8A5A3B", "#241813", "#7B2D8E", True),   # 3 Aline
    ("#FFDCC0", "#E0A678", "#4A3326", "#F2480C", False),  # 4 Thiago
    ("#FFE2C6", "#B07848", "#2A1C14", "#FFB400", True),  # 5 Patricia
    ("#FFD7AE", "#9C6740", "#15100C", "#2563EB", False),  # 6 Marcos
]

def avatar(bg, skin, hair, cloth, fem):
    hair_shape = (
        f'<path d="M30 60 Q30 18 64 18 Q98 18 98 60 L98 50 Q92 30 64 30 Q36 30 30 50 Z" fill="{hair}"/>'
        if fem else
        f'<path d="M34 52 Q34 22 64 22 Q94 22 94 52 Q94 40 64 40 Q34 40 34 52 Z" fill="{hair}"/>'
    )
    longhair = (f'<path d="M30 58 Q26 92 40 100 L40 70 Q34 64 34 56 Z" fill="{hair}"/>'
                f'<path d="M98 58 Q102 92 88 100 L88 70 Q94 64 94 56 Z" fill="{hair}"/>') if fem else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128">
<circle cx="64" cy="64" r="64" fill="{bg}"/>
<g>
<path d="M22 128 Q22 92 64 92 Q106 92 106 128 Z" fill="{cloth}"/>
{longhair}
<circle cx="64" cy="60" r="30" fill="{skin}"/>
{hair_shape}
<circle cx="54" cy="60" r="3.4" fill="#2A1C14"/>
<circle cx="74" cy="60" r="3.4" fill="#2A1C14"/>
<path d="M55 72 Q64 80 73 72" stroke="#7a3b2a" stroke-width="3" fill="none" stroke-linecap="round"/>
</g>
</svg>'''

names = ["av1","av2","av3","av4","av5","av6"]
for n,(bg,skin,hair,cloth,fem) in zip(names, people):
    with open(f"{OUT}/{n}.svg","w",encoding="utf-8") as f:
        f.write(avatar(bg,skin,hair,cloth,fem))
    print("ok", n)
