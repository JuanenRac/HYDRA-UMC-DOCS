# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/brand.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The banner, the icon and the map of the families of this repository, in the look of HYDRA-UMC.

The look is the one of the HYDRA-UMC banners: a near-black gradient, thin cyan
circuit traces, a glowing line emblem and bold letter-spaced titles. The map
shows the families of the ecosystem and the few flows that the documents of
the repositories state; it carries no counts, so it cannot go stale.
"""
from __future__ import annotations

import html

CYAN = "#00E5FF"
GREEN = "#00FF66"
AMBER = "#FFB020"
BG_FROM, BG_TO = "#07090C", "#12161C"
TAGS = ("ARCHITECTURE", "INTERFACES", "SECURITY", "CATALOG", "MARKDOWN", "PYTHON")

# family -> (column, row); a family that is not here goes to an extra row below
POSITIONS: dict[str, tuple[int, int]] = {
    "Core Backend & Clients": (0, 0),
    "Complementary Tools": (0, 1),
    "Orchestration & Swarm": (1, 0),
    "Vision AI Node": (1, 1),
    "Cognitive AI Node": (1, 2),
    "Industrial Gateway": (2, 0),
    "Data & Analytics": (2, 1),
    "Digital Twin & Simulation": (2, 2),
    "Core Hardware": (3, 0),
    "External Automation Bridges": (3, 1),
    "Mobile & Autonomous Bridges": (3, 2),
    "Platform Foundation & Contracts": (0, 3),
    "Ecosystem Operations": (1, 3),
}
# (from, to): a flow that the documents of the repositories state
FLOWS: tuple[tuple[str, str], ...] = (
    ("Core Backend & Clients", "Core Hardware"),
    ("Core Backend & Clients", "Industrial Gateway"),
    ("Core Backend & Clients", "Vision AI Node"),
    ("Core Backend & Clients", "Cognitive AI Node"),
    ("External Automation Bridges", "Core Backend & Clients"),
    ("Mobile & Autonomous Bridges", "Core Backend & Clients"),
)
CONTRACT_USERS = ("Core Backend & Clients", "External Automation Bridges", "Mobile & Autonomous Bridges", "Core Hardware", "Ecosystem Operations")


def defs() -> str:
    return (
        f'<defs><linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%"><stop stop-color="{BG_FROM}"/><stop offset="1" stop-color="{BG_TO}"/></linearGradient>'
        '<filter id="g"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>'
    )


def book(stroke: str = CYAN, width: float = 4) -> str:
    """An open book, in a box of about 120 by 90 around the origin."""
    return (
        f'<path d="M-62,-34 Q-30,-46 0,-30 Q30,-46 62,-34 V34 Q30,22 0,38 Q-30,22 -62,34 Z" fill="none" stroke="{stroke}" stroke-width="{width}" stroke-linejoin="round"/>'
        f'<path d="M0,-30 V38" stroke="{stroke}" stroke-width="{width / 2}" opacity=".7"/>'
        f'<path d="M-46,-16 Q-30,-22 -14,-14 M-46,0 Q-30,-6 -14,2 M14,-14 Q30,-22 46,-16 M14,2 Q30,-6 46,0" fill="none" stroke="{stroke}" stroke-width="2.4" opacity=".6"/>'
    )


def banner(name: str = "HYDRA-UMC-DOCS", tagline: str = "ARCHITECTURE, INTERFACES & SECURITY BASELINE") -> str:
    name, tagline = html.escape(name), html.escape(tagline)
    tag_xs = [105 + index * 150 for index in range(len(TAGS))]
    tags = "".join(f'<text x="{x}" y="360">#{html.escape(tag)}</text>' for x, tag in zip(tag_xs, TAGS))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" role="img" aria-labelledby="title desc">
  <title id="title">{name}</title><desc id="desc">{name} | HYDRA-UMC ecosystem project banner</desc>
  {defs()}
  <rect width="1200" height="400" fill="url(#bg)"/><g fill="none" stroke="{CYAN}" stroke-width="1" opacity=".25"><path d="M0 100H200L250 150H600"/><path d="M1200 300H1000L950 250H600"/></g>
  <g transform="translate(205 185)" filter="url(#g)">{book()}</g>
  <text x="360" y="136" font-family="Arial,sans-serif" font-size="50" font-weight="bold" fill="#FFF" letter-spacing="8">HYDRA-UMC</text><text x="364" y="181" font-family="Arial,sans-serif" font-size="17" fill="{CYAN}" letter-spacing="4">UNIVERSAL MACHINES CONTROLLER ECOSYSTEM</text><text x="360" y="246" font-family="Arial,sans-serif" font-size="29" font-weight="bold" fill="#FFF">{name}</text><text x="362" y="282" font-family="Arial,sans-serif" font-size="15" fill="{CYAN}" opacity=".8" letter-spacing="3">{tagline}</text>
  <g font-family="monospace" font-size="12" fill="{CYAN}" opacity=".65">{tags}</g>
</svg>
"""


def icon() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32" role="img" aria-labelledby="title">
  <title id="title">HYDRA-UMC-DOCS</title>
  <defs><linearGradient id="bgIcon" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0A0D12"/><stop offset="50%" stop-color="#121720"/><stop offset="100%" stop-color="{BG_FROM}"/></linearGradient></defs>
  <rect width="32" height="32" rx="4" fill="url(#bgIcon)"/>
  <g transform="translate(16 16) scale(0.2)">{book(GREEN, 9)}</g>
</svg>
"""


def family_map(positions: dict[str, tuple[int, int]] | None = None) -> str:
    positions = positions or POSITIONS
    width, box_w, box_h, step_x, step_y, top = 1200, 230, 62, 285, 100, 118
    rows = max(row for _, row in positions.values()) + 1
    height = top + rows * step_y + 60

    def origin(name: str) -> tuple[float, float]:
        column, row = positions[name]
        return 40 + column * step_x, top + row * step_y

    def centre(name: str) -> tuple[float, float]:
        x, y = origin(name)
        return x + box_w / 2, y + box_h / 2

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '  <title id="title">HYDRA-UMC</title><desc id="desc">The families of repositories of HYDRA-UMC and the flows between them that their documents state</desc>',
        f"  {defs()}",
        f'  <rect width="{width}" height="{height}" fill="url(#bg)"/>',
        '  <text x="600" y="46" text-anchor="middle" font-family="Arial,sans-serif" font-size="26" font-weight="bold" fill="#FFF" letter-spacing="6">HYDRA-UMC FAMILIES</text>',
    ]
    platform = "Platform Foundation & Contracts"
    for name in CONTRACT_USERS:
        if name in positions and platform in positions:
            (x1, y1), (x2, y2) = centre(name), centre(platform)
            parts.append(f'  <path d="M{x1} {y1 + box_h / 2} L{x2} {y2 - box_h / 2}" fill="none" stroke="{GREEN}" stroke-width="1" stroke-dasharray="4 6" opacity=".35"/>')
    for source, target in FLOWS:
        if source not in positions or target not in positions:
            continue
        (x1, y1), (x2, y2) = centre(source), centre(target)
        if abs(x1 - x2) < 1:
            sx, tx, sy, ty = x1, x2, y1 + box_h / 2, y2 - box_h / 2
            if y2 < y1:
                sy, ty = y1 - box_h / 2, y2 + box_h / 2
            parts.append(f'  <path d="M{sx} {sy} L{tx} {ty}" fill="none" stroke="{CYAN}" stroke-width="1.6" opacity=".45"/><circle cx="{tx}" cy="{ty}" r="3.4" fill="{AMBER}"/>')
            continue
        sx = x1 + box_w / 2 if x2 > x1 else x1 - box_w / 2
        tx = x2 - box_w / 2 if x2 > x1 else x2 + box_w / 2
        mid = (sx + tx) / 2
        parts.append(f'  <path d="M{sx} {y1} C{mid} {y1}, {mid} {y2}, {tx} {y2}" fill="none" stroke="{CYAN}" stroke-width="1.6" opacity=".45"/><circle cx="{tx}" cy="{y2}" r="3.4" fill="{AMBER}"/>')
    for name in positions:
        x, y = origin(name)
        accent = AMBER if name == platform else CYAN
        label = html.escape(name)
        size = 13 if len(name) > 24 else 15
        parts.append(
            f'  <g transform="translate({x} {y})"><rect width="{box_w}" height="{box_h}" rx="12" fill="#0d1a22" stroke="{accent}" stroke-width="1.4" opacity=".95"/>'
            f'<text x="{box_w / 2}" y="{box_h / 2 + 5}" text-anchor="middle" font-family="Arial,sans-serif" font-size="{size}" font-weight="bold" fill="#FFF">{label}</text></g>'
        )
    parts.append(
        f'  <text x="600" y="{height - 22}" text-anchor="middle" font-family="monospace" font-size="12" fill="{GREEN}" opacity=".7">'
        "dashed: the contracts of HYDRA-UMC-SDK  ·  solid: a flow that the documents state</text>"
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def outputs() -> dict[str, str]:
    """Published path (relative to the repository) -> content."""
    return {
        "images/HYDRA_UMC_FAMILY.svg": family_map(),
        "brand/HYDRA_UMC_ICON.svg": icon(),
    }
