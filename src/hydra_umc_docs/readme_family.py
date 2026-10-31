# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/readme_family.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The repositories of the family by group, as the Related Projects section of the READMEs lists them.

The list is written here, not read from the manifests, so that the READMEs can be
produced and checked in a CI run that has no sibling repository. The structure
check of the catalogue compares this list with the manifests found next to this
repository, so a repository that appears or disappears is reported.
"""
from __future__ import annotations

FAMILY_REPOS: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "Cognitive AI Node",
        (
            "HYDRA-UMC-COGNITIVE-NODE",
            "HYDRA-UMC-DOCS-QA",
            "HYDRA-UMC-SEMANTIC-PLANNER",
            "HYDRA-UMC-VLA-ENGINE",
            "HYDRA-UMC-VOICE-UI",
        ),
    ),
    (
        "Complementary Tools",
        (
            "HYDRA-UMC-DASHBOARD-AI",
            "HYDRA-UMC-MESHES",
            "HYDRA-UMC-TOOL-CLI",
            "HYDRA-UMC-WATCH",
        ),
    ),
    (
        "Core Backend & Clients",
        (
            "HYDRA-UMC-ANDROID-CONTROL",
            "HYDRA-UMC-DSI",
            "HYDRA-UMC-EDITOR-STL",
            "HYDRA-UMC-EDITOR-URDF",
            "HYDRA-UMC-IOS-CONTROL",
            "HYDRA-UMC-SERVER",
            "HYDRA-UMC-STUDIO",
            "HYDRA-UMC-SUITE",
        ),
    ),
    (
        "Core Hardware",
        (
            "HYDRA-UMC",
        ),
    ),
    (
        "Data & Analytics",
        (
            "HYDRA-UMC-ANOMALY-DETECTOR",
            "HYDRA-UMC-DATALAKE",
            "HYDRA-UMC-PRODUCTION-REPORTS",
            "HYDRA-UMC-TELEMETRY-COLLECTOR",
        ),
    ),
    (
        "Digital Twin & Simulation",
        (
            "HYDRA-UMC-HIL-BRIDGE",
            "HYDRA-UMC-PHYSICS-REPLICA",
            "HYDRA-UMC-SYNTHETIC-DATA-GEN",
            "HYDRA-UMC-TWIN",
        ),
    ),
    (
        "Ecosystem Operations",
        (
            "HYDRA-UMC-DEV-SERVER",
            "HYDRA-UMC-DOCS",
            "HYDRA-UMC-LOCAL-TECHNICIAN",
            "HYDRA-UMC-OPS-AGENT",
            "HYDRA-UMC-OS-REBUILDER",
            "HYDRA-UMC-UPDATER",
        ),
    ),
    (
        "External Automation Bridges",
        (
            "HYDRA-UMC-BRIDGE-CNC",
            "HYDRA-UMC-BRIDGE-LASER",
            "HYDRA-UMC-BRIDGE-OPENPNP",
            "HYDRA-UMC-BRIDGE-PRINTER3D",
            "HYDRA-UMC-BRIDGE-ROS2",
        ),
    ),
    (
        "Industrial Gateway",
        (
            "HYDRA-UMC-GATEWAY-INDUSTRIAL",
            "HYDRA-UMC-MQTT-BROKER",
            "HYDRA-UMC-MTCONNECT-ADAPTER",
            "HYDRA-UMC-OPCUA-SERVER",
        ),
    ),
    (
        "Mobile & Autonomous Bridges",
        (
            "HYDRA-UMC-BRIDGE-AMR",
            "HYDRA-UMC-BRIDGE-DROIDS",
            "HYDRA-UMC-BRIDGE-UAV",
        ),
    ),
    (
        "Orchestration & Swarm",
        (
            "HYDRA-UMC-JOB-DISPATCHER",
            "HYDRA-UMC-NODE-HEALING",
            "HYDRA-UMC-ORCHESTRATOR",
            "HYDRA-UMC-PATH-PLANNER-3D",
            "HYDRA-UMC-SWARM-SYNC",
        ),
    ),
    (
        "Platform Foundation & Contracts",
        (
            "HYDRA-UMC-CONNECTOR-HUB",
            "HYDRA-UMC-OS",
            "HYDRA-UMC-SDK",
        ),
    ),
    (
        "Vision AI Node",
        (
            "HYDRA-UMC-DETECTION-HEF",
            "HYDRA-UMC-SAFETY-ZONES",
            "HYDRA-UMC-VISION-NODE",
            "HYDRA-UMC-VISION-STREAMER",
            "HYDRA-UMC-VISUAL-SERVOING-API",
        ),
    ),
)


def all_names() -> set[str]:
    return {name for _, names in FAMILY_REPOS for name in names}
