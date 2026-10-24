<p align="center">
  <img src="images/HYDRA_UMC_BANNER.svg" alt="HYDRA-UMC-DOCS banner" width="100%">
</p>

# 📚 HYDRA-UMC-DOCS

<p align="center"><a href="README.md">🇺🇸 English</a> | <a href="README_spa.md">🇪🇸 Español</a> | <a href="README_fra.md">🇫🇷 Français</a> | <a href="README_ita.md">🇮🇹 Italiano</a> | <a href="README_deu.md">🇩🇪 Deutsch</a> | 🇨🇳 <b>简体中文</b> | <a href="README_jpn.md">🇯🇵 日本語</a> | <a href="README_por.md">🇵🇹 Português</a></p>

### 架构、接口、安全基线，以及关于哪些已被证实的实情

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Version-0.0.3-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-scaffolding-FFB020.svg" alt="Maturity">
</p>

---

**诚实性检查 - 今天真正能运行的部分：** 本仓库包含文档和小工具。这些工具（目录生成器、品牌素材生成器、README 生成器、发布检查和家族检查）是真实的，并有在 CI 中运行的单元测试；夜间工作流会针对家族中的其他仓库运行它们。文档依据这些仓库的 README、清单、变更日志和文档编写，以为本版本阅读时的内容为准，无法追溯到某个仓库的说法会被如实标明。这里的任何内容都不是硬件测试：能力矩阵会对每项能力说明它只是被模拟、在计算机上测试过，还是在真实硬件上运行过，固件仓库也说明目前尚不存在已焊装的电路板。

---

> **安全与安防现状:**本生态系统不是经认证的安全系统。目前尚无硬件 E-STOP 通路,没有由固件强制执行的限位或联锁,也没有经过验证的运动指令;固件映像使用 CRC32 和共享密钥的 HMAC-SHA256 校验,而非非对称签名;TLS 与双向 TLS 均为可选项,默认关闭;自制电路板尚未组装或测试。在依赖此处任何说法来保障人身安全之前,请先阅读[安全基线](docs/SECURITY_BASELINE.md)和[威胁模型](docs/THREAT_MODEL.md)。

## 📋 速览

| | |
|---|---|
| 版本 | `0.0.3` |
| 成熟度 | 雏形 |
| 技术栈 | Markdown / Mermaid / Python / SVG |
| 目标 | 使用者的电脑 |
| 真实硬件 | 不适用：这里的内容不在硬件上运行 |

## 🚦 项目状态

每一行是本仓库的一个部分，灯号表示它今天做到了哪一步。内容依据仓库能够展示的证据（测试、构建、运行），而不是计划。

🟢 已完成并验证 · 🟡 可用，有已知限制 · 🟠 部分完成或尚未验证 · 🔴 未完成或不可用

| 领域 | 状态 | 在这里的含义 |
|---|---|---|
| 软件 | 🟠 | 目前只有结构和最初的部分，大部分工作尚未完成 |
| 测试 | 🟠 | 此仓库尚未记录测试数量 |
| 真实硬件 | 🟢 | 不适用：这里的内容不在硬件上运行 |
| 文档 | 🟢 | 八种语言的 README，每次变更都会与清单核对 |

## 🎯 简介

<p align="center">
  <img src="images/HYDRA_UMC_FAMILY.svg" alt="HYDRA-UMC families" width="100%">
</p>

下图显示各仓库家族，以及它们的文档所陈述的数据流。

* [架构](docs/ARCHITECTURE.md): 分层、数据流、端口和信任边界。
* [接口](docs/INTERFACES.md): 每份契约归谁所有，以及记录在哪里。
* [能力矩阵](docs/CAPABILITY_MATRIX.md): 哪些在软件中已证实、哪些需要硬件，逐个项目说明。
* [安全基线](docs/SECURITY_BASELINE.md): 代码已强制执行的内容和仍然缺少的内容；以及[威胁模型](docs/THREAT_MODEL.md)。
* [第一个垂直切片](docs/FIRST_VERTICAL_SLICE.md): 今天已存在的最小端到端路径。
* [项目目录](docs/PROJECT_CATALOG.md): 家族中的每个仓库，依据其自身清单生成。
* **工具：** `make_catalog.py` 生成目录，`make_brand.py` 生成横幅、图标和家族图，`make_readmes.py` 生成本仓库的八份 README，`publication_check.py` 在发布前查找任何私有内容，`check_all.sh` 运行家族中每个仓库自己的检查，并为每个仓库输出一行 PASS、FAIL 或 SKIP。`make_glance.py` 根据每个仓库的清单和 `data/glance.json` 生成其“速览”表（`--check` 比较，`--apply` 写入）；提升版本后，运行 `python tools/make_glance.py --apply --repo NAME` 即可刷新该仓库的表。`check_claims.py` 读取该系列每个仓库的英文 README,当某个句子含有风险词(E-STOP、联锁、实时、已签名、mTLS、FDCAN、YOLO、AI 驱动、自主、已认证等)而旁边没有状态标记(计划中、未实现、可选、默认关闭、模拟、已测试等),且不在人工对照代码读过并登记于 `data/claims_reviewed.json` 的行中时,检查失败。

## 🧩 在 HYDRA-UMC 中的角色

HYDRA-UMC-DOCS 是整个生态的记忆：架构、接口、安全基线和能力矩阵都放在这里，同时也保存着把所有仓库并排比较的工具。每个仓库保留自己的 README、测试和契约；本仓库说明它们如何配合，以及真正证实了什么。

## 📂 仓库结构

```text
HYDRA-UMC-DOCS/
├── docs/     架构、接口、能力矩阵、安全基线、威胁模型、第一个切片、生成的目录
├── src/      以包形式提供的工具（目录、品牌素材、README、发布检查）
├── tools/    包之上的薄脚本、check_all.sh，以及生态共享的 CI 检查
├── tests/    工具的单元测试
├── images/   横幅和家族图
├── brand/    图标
├── build.sh / build.bat, build-test.sh / build-test.bat, run.sh / run.bat
└── hydra-umc.project.json, pyproject.toml, CHANGELOG.md, LICENSE, LICENSE.md
```

## 🛠️ 构建与运行

**要求：** Python 3.10 或更新版本；测试需要 pytest

```bash
python tools/make_catalog.py --check             # 目录是最新的（需要本仓库旁边有其他仓库）
python tools/make_brand.py --check               # 横幅、图标和家族图是最新的
python tools/make_readmes.py --check             # 八份 README 是最新的
python tools/make_glance.py --check              # 家族的“速览”表是最新的（需要本仓库旁边有其他仓库）
python tools/publication_check.py                # 发布时不会带出任何私有内容
python tools/check_claims.py --require-siblings  # 没有任何 README 在不说明状态的情况下声称具备高风险能力(需要与本仓库相邻的其他仓库)
bash tools/check_all.sh                          # 每个仓库的检查，每个一行
python -m pytest tests -q                        # 工具的单元测试
```

`build.sh` / `build.bat` 将版本提升一步（生态的里程表规则），安装包并运行测试；`build-test.sh` / `build-test.bat` 在不改变任何版本的情况下进行检查。

## 🔗 相关项目

HYDRA-UMC 由相互独立的仓库组成，每个仓库都有自己的版本、测试和 README。以下是按组划分的家族：

* **Cognitive AI Node:** [HYDRA-UMC-COGNITIVE-NODE](https://github.com/JuanenRac/HYDRA-UMC-COGNITIVE-NODE), [HYDRA-UMC-DOCS-QA](https://github.com/JuanenRac/HYDRA-UMC-DOCS-QA), [HYDRA-UMC-LOCAL-TECHNICIAN](https://github.com/JuanenRac/HYDRA-UMC-LOCAL-TECHNICIAN), [HYDRA-UMC-SEMANTIC-PLANNER](https://github.com/JuanenRac/HYDRA-UMC-SEMANTIC-PLANNER), [HYDRA-UMC-VLA-ENGINE](https://github.com/JuanenRac/HYDRA-UMC-VLA-ENGINE), [HYDRA-UMC-VOICE-UI](https://github.com/JuanenRac/HYDRA-UMC-VOICE-UI)
* **Complementary Tools:** [HYDRA-UMC-DASHBOARD-AI](https://github.com/JuanenRac/HYDRA-UMC-DASHBOARD-AI), [HYDRA-UMC-TOOL-CLI](https://github.com/JuanenRac/HYDRA-UMC-TOOL-CLI), [HYDRA-UMC-WATCH](https://github.com/JuanenRac/HYDRA-UMC-WATCH)
* **Core Backend & Clients:** [HYDRA-UMC-ANDROID-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-ANDROID-CONTROL), [HYDRA-UMC-DSI](https://github.com/JuanenRac/HYDRA-UMC-DSI), [HYDRA-UMC-EDITOR-STL](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-STL), [HYDRA-UMC-EDITOR-URDF](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-URDF), [HYDRA-UMC-IOS-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-IOS-CONTROL), [HYDRA-UMC-SERVER](https://github.com/JuanenRac/HYDRA-UMC-SERVER), [HYDRA-UMC-STUDIO](https://github.com/JuanenRac/HYDRA-UMC-STUDIO), [HYDRA-UMC-SUITE](https://github.com/JuanenRac/HYDRA-UMC-SUITE)
* **Core Hardware:** [HYDRA-UMC](https://github.com/JuanenRac/HYDRA-UMC)
* **Data & Analytics:** [HYDRA-UMC-ANOMALY-DETECTOR](https://github.com/JuanenRac/HYDRA-UMC-ANOMALY-DETECTOR), [HYDRA-UMC-DATALAKE](https://github.com/JuanenRac/HYDRA-UMC-DATALAKE), [HYDRA-UMC-PRODUCTION-REPORTS](https://github.com/JuanenRac/HYDRA-UMC-PRODUCTION-REPORTS), [HYDRA-UMC-TELEMETRY-COLLECTOR](https://github.com/JuanenRac/HYDRA-UMC-TELEMETRY-COLLECTOR)
* **Digital Twin & Simulation:** [HYDRA-UMC-HIL-BRIDGE](https://github.com/JuanenRac/HYDRA-UMC-HIL-BRIDGE), [HYDRA-UMC-PHYSICS-REPLICA](https://github.com/JuanenRac/HYDRA-UMC-PHYSICS-REPLICA), [HYDRA-UMC-SYNTHETIC-DATA-GEN](https://github.com/JuanenRac/HYDRA-UMC-SYNTHETIC-DATA-GEN), [HYDRA-UMC-TWIN](https://github.com/JuanenRac/HYDRA-UMC-TWIN)
* **Ecosystem Operations:** [HYDRA-UMC-DEV-SERVER](https://github.com/JuanenRac/HYDRA-UMC-DEV-SERVER), **HYDRA-UMC-DOCS** (本仓库), [HYDRA-UMC-OPS-AGENT](https://github.com/JuanenRac/HYDRA-UMC-OPS-AGENT), [HYDRA-UMC-OS-REBUILDER](https://github.com/JuanenRac/HYDRA-UMC-OS-REBUILDER), [HYDRA-UMC-UPDATER](https://github.com/JuanenRac/HYDRA-UMC-UPDATER)
* **External Automation Bridges:** [HYDRA-UMC-BRIDGE-CNC](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-CNC), [HYDRA-UMC-BRIDGE-LASER](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-LASER), [HYDRA-UMC-BRIDGE-OPENPNP](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-OPENPNP), [HYDRA-UMC-BRIDGE-PRINTER3D](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-PRINTER3D), [HYDRA-UMC-BRIDGE-ROS2](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-ROS2)
* **Industrial Gateway:** [HYDRA-UMC-GATEWAY-INDUSTRIAL](https://github.com/JuanenRac/HYDRA-UMC-GATEWAY-INDUSTRIAL), [HYDRA-UMC-MQTT-BROKER](https://github.com/JuanenRac/HYDRA-UMC-MQTT-BROKER), [HYDRA-UMC-MTCONNECT-ADAPTER](https://github.com/JuanenRac/HYDRA-UMC-MTCONNECT-ADAPTER), [HYDRA-UMC-OPCUA-SERVER](https://github.com/JuanenRac/HYDRA-UMC-OPCUA-SERVER)
* **Mobile & Autonomous Bridges:** [HYDRA-UMC-BRIDGE-AMR](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-AMR), [HYDRA-UMC-BRIDGE-DROIDS](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-DROIDS), [HYDRA-UMC-BRIDGE-UAV](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-UAV)
* **Orchestration & Swarm:** [HYDRA-UMC-JOB-DISPATCHER](https://github.com/JuanenRac/HYDRA-UMC-JOB-DISPATCHER), [HYDRA-UMC-NODE-HEALING](https://github.com/JuanenRac/HYDRA-UMC-NODE-HEALING), [HYDRA-UMC-ORCHESTRATOR](https://github.com/JuanenRac/HYDRA-UMC-ORCHESTRATOR), [HYDRA-UMC-PATH-PLANNER-3D](https://github.com/JuanenRac/HYDRA-UMC-PATH-PLANNER-3D), [HYDRA-UMC-SWARM-SYNC](https://github.com/JuanenRac/HYDRA-UMC-SWARM-SYNC)
* **Platform Foundation & Contracts:** [HYDRA-UMC-CONNECTOR-HUB](https://github.com/JuanenRac/HYDRA-UMC-CONNECTOR-HUB), [HYDRA-UMC-OS](https://github.com/JuanenRac/HYDRA-UMC-OS), [HYDRA-UMC-SDK](https://github.com/JuanenRac/HYDRA-UMC-SDK)
* **Vision AI Node:** [HYDRA-UMC-DETECTION-HEF](https://github.com/JuanenRac/HYDRA-UMC-DETECTION-HEF), [HYDRA-UMC-SAFETY-ZONES](https://github.com/JuanenRac/HYDRA-UMC-SAFETY-ZONES), [HYDRA-UMC-VISION-NODE](https://github.com/JuanenRac/HYDRA-UMC-VISION-NODE), [HYDRA-UMC-VISION-STREAMER](https://github.com/JuanenRac/HYDRA-UMC-VISION-STREAMER), [HYDRA-UMC-VISUAL-SERVOING-API](https://github.com/JuanenRac/HYDRA-UMC-VISUAL-SERVOING-API)

**HYDRA-UMC 之外：**

* **[ARMOR-DOCS](https://github.com/JuanenRac/ARMOR-DOCS)** - 同样的思路，用于 A.R.M.O.R. 安防生态
* **[URTC](https://github.com/JuanenRac/URTC)** - 通用机器人工具控制器，通过 SDK 连接的独立产品
* **[JuanenRac](https://github.com/JuanenRac/JuanenRac)** - 所有生态的个人主页和状态面板

## 📚 文档与社区

更多阅读：

* [能力矩阵：哪些已证实，哪些没有](docs/CAPABILITY_MATRIX.md)
* [项目目录：各仓库的版本和类型](docs/PROJECT_CATALOG.md)
* [本仓库的变更日志](CHANGELOG.md)
* [许可证 (GPL-3.0-or-later)](LICENSE)
* 问题、想法和报告：electrohobby3d@gmail.com

## 👤 作者

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 许可证

软件：GPL-3.0-or-later - 见 [LICENSE](LICENSE)。文档：CC BY-SA 4.0 - 见 [LICENSE.md](LICENSE.md)。
