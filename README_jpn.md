<!-- =============================================================================
HYDRA-UMC-DOCS - Architecture, interfaces, security baseline and what is proven
Copyright (C) JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
GPL-3.0-or-later - see LICENSE
============================================================================= -->

<p align="center">
  <img src="images/HYDRA_UMC_BANNER.svg" alt="HYDRA-UMC-DOCS banner" width="100%">
</p>

# 📚 HYDRA-UMC-DOCS

<p align="center"><a href="README.md">🇺🇸 English</a> | <a href="README_spa.md">🇪🇸 Español</a> | <a href="README_fra.md">🇫🇷 Français</a> | <a href="README_ita.md">🇮🇹 Italiano</a> | <a href="README_deu.md">🇩🇪 Deutsch</a> | <a href="README_zho.md">🇨🇳 简体中文</a> | 🇯🇵 <b>日本語</b> | <a href="README_por.md">🇵🇹 Português</a></p>

### アーキテクチャ、インターフェース、セキュリティ基準、そして何が実証済みかという事実

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Tests-153%20passing-2ea44f.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Version-0.0.5-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-scaffolding-FFB020.svg" alt="Maturity">
</p>

---

**正直さの確認 - 今日実際に動くもの：** このリポジトリにはドキュメントと小さなツールがあります。ツール（カタログ生成、ブランド素材生成、README 生成、公開前チェック、ファミリーチェック）は実在し、CI で実行される単体テストがあります。夜間ワークフローは、ファミリーの他のリポジトリに対してそれらを実行します。ドキュメントは、このバージョンのために読んだ時点の各リポジトリの README、マニフェスト、変更履歴、ドキュメントから書かれており、リポジトリまでたどれなかった記述はその旨を明記しています。ここにあるものはハードウェアテストではありません。能力マトリクスは各能力について、シミュレーションのみか、コンピュータ上でテスト済みか、実機で動作したかを示します。ファームウェアのリポジトリは、実装済みの基板がまだ存在しないと述べています。

---

> **安全性とセキュリティの現状:** このエコシステムは認証された安全システムではありません。ハードウェアの E-STOP 経路、ファームウェアが強制する制限やインターロック、検証済みの動作コマンドはまだありません。ファームウェアイメージは CRC-32 と Ed25519 署名で検査し、リリースビルドは公開済みの開発用鍵を拒否します(リレーの先のツールヘッドと拡張ボードは引き続き URTC のブートローダーを使い、署名ではなく共有鍵の HMAC-SHA256 を使います)。TLS と相互 TLS は任意で、既定では無効です。独自基板はまだ実装も試験もされていません。ここに書かれた内容を人の安全のために頼る前に、[セキュリティベースライン](docs/SECURITY_BASELINE.md)と[脅威モデル](docs/THREAT_MODEL.md)をお読みください。

---

## 📋 ひと目で

| | |
|---|---|
| バージョン | `0.0.5` |
| 成熟度 | 足場段階 |
| テスト | 153 (`python -m pytest tests -q`) |
| 技術 | Markdown / Mermaid / Python / SVG |
| 対象 | 利用者の PC |
| 実機での確認 | 対象外：ここにあるものはハードウェア上では動きません |

**移動：** [概要](#-概要) · [アーキテクチャ](#-アーキテクチャ) · [セキュリティと安全](#-セキュリティと安全) · [クイックスタート](#-クイックスタート) · [テスト](#-テスト) · [リポジトリの構成](#-リポジトリの構成) · [関連プロジェクト](#-関連プロジェクト)

## 🚦 プロジェクトの状況

各行はこのリポジトリの一部分で、信号は今日どこまで進んでいるかを示します。計画ではなく、リポジトリが示せるもの（テスト、ビルド、実行）に基づいて書かれています。

🟢 完了・検証済み · 🟡 動作する（既知の制限あり） · 🟠 一部のみ、または未検証 · 🔴 未実装または動作しない

| 領域 | 状態 | ここでの意味 |
|---|---|---|
| ソフトウェア | 🟠 | 構造と最初の部品のみで、作業の大部分はこれからです |
| テスト | 🟡 | 自動テスト 153 件。変更のたびに実行されます |
| 実機 | 🟡 | 対象外：ここにあるものはハードウェア上では動きません |
| ドキュメント | 🟡 | 8 言語の README。変更のたびにマニフェストと照合されます |

## 🎯 概要

<p align="center">
  <img src="images/HYDRA_UMC_FAMILY.svg" alt="HYDRA-UMC families" width="100%">
</p>

下の図は、リポジトリのファミリーと、各ドキュメントが述べるデータの流れを示します。

* [アーキテクチャ](docs/ARCHITECTURE.md): レイヤー、データの流れ、ポート、信頼境界。
* [インターフェース](docs/INTERFACES.md): 各契約の所有者と、その文書の場所。
* [能力マトリクス](docs/CAPABILITY_MATRIX.md): ソフトウェアで実証済みのものとハードウェアが必要なものを、プロジェクトごとに。
* [セキュリティ基準](docs/SECURITY_BASELINE.md): コードが強制していることとまだ足りないこと。および[脅威モデル](docs/THREAT_MODEL.md)。
* [最初の垂直スライス](docs/FIRST_VERTICAL_SLICE.md): 今日存在する最小のエンドツーエンド経路。
* [プロジェクトカタログ](docs/PROJECT_CATALOG.md): ファミリーの全リポジトリを、それぞれのマニフェストから生成。
* **ツール：** `make_catalog.py` はカタログを、`make_brand.py` はバナー・アイコン・ファミリーマップを、`make_readmes.py` はこのリポジトリの 8 つの README を書きます。`publication_check.py` は公開前に非公開のものを探し、`check_all.sh` はファミリーの各リポジトリ自身のチェックを実行して、1 件ごとに PASS、FAIL、SKIP の 1 行を出力します。 `make_glance.py` は各リポジトリのマニフェストと `data/glance.json` から「ひと目で」の表を書きます（`--check` は比較、`--apply` は書き込み）。バージョンを上げた後は `python tools/make_glance.py --apply --repo NAME` でそのリポジトリの表を更新します。`check_claims.py` は、ファミリーの各リポジトリの英語 README を読み、リスクのある語(E-STOP、インターロック、リアルタイム、署名済み、mTLS、FDCAN、YOLO、AI 駆動、自律、認証済みなど)を含む文の隣に状態の印(計画中、未実装、任意、既定で無効、シミュレーション、テスト済みなど)がなく、かつ担当者がコードと突き合わせて読み `data/claims_reviewed.json` に登録した行でもない場合に失敗します。

## 🧩 HYDRA-UMC での役割

HYDRA-UMC-DOCS はエコシステムの記憶です。アーキテクチャ、インターフェース、セキュリティ基準、能力マトリクスがここにあり、すべてのリポジトリを並べて比較するツールもここに置かれています。各リポジトリは自分の README、テスト、契約を持ち続けます。このリポジトリは、それらがどう組み合わさるか、そして実際に何が実証されたかを述べます。

## 🏛️ アーキテクチャ

文書はエコシステムの各ファミリーを説明します。下の図はこのリポジトリ自身です。ツールは兄弟リポジトリのマニフェストと README を読み、カタログ、At a glance の表、バナー、8 つの README を書き、2 つの検査が公開してはならないものを拒否します。

<p align="center">
  <img src="images/architecture.svg" alt="HYDRA-UMC-DOCS architecture" width="100%">
</p>

## 🔒 セキュリティと安全

| 脅威 | 防御 | 場所 |
|---|---|---|
| 非常停止やインターロックなど危険を伴う機能が、どこまで実証されているかを書かずに記述される README | `check_claims.py` は各リポジトリの英語 README を読み、リスク語を含み、状態の印も確認済みの記録も無い文があると失敗します（`data/claims_reviewed.json`） | `tools/check_claims.py` |
| 公開物と一緒に非公開のものが外に出る | `publication_check.py` は公開前に、ファイルと履歴に非公開のものが無いか調べます | `tools/publication_check.py` |
| どのリポジトリにもたどれない記述 | 文書はリポジトリの README、マニフェスト、変更履歴、文書から書かれ、たどれなかった記述はその旨が明記されます | `docs/CAPABILITY_MATRIX.md` |

## 🚀 クイックスタート

**必要なもの：** Python 3.10 以降、テスト用に pytest

```bash
python tools/make_catalog.py --check             # カタログが最新（このリポジトリの隣に他のリポジトリが必要）
python tools/make_brand.py --check               # バナー、アイコン、マップが最新
python tools/make_readmes.py --check             # 8 つの README が最新
python tools/make_glance.py --check              # ファミリー全体の「ひと目で」の表が最新（このリポジトリの隣に他のリポジトリが必要）
python tools/status_lights.py --check            # プロジェクトの状況の表の信号が、マニフェストで許される範囲を超えていない
python tools/publication_check.py                # 公開で非公開のものが外に出ない
python tools/check_claims.py --require-siblings  # どの README も、状態を示さずにリスクのある機能を主張していない(このリポジトリの隣に他のリポジトリが必要)
bash tools/check_all.sh                          # 各リポジトリのチェックを 1 行ずつ
python -m pytest tests -q                        # ツールの単体テスト
```

## 🧪 テスト

`python -m pytest tests -q` で自動テスト 153 件を実行します。 ハードウェアも、このマシンの外にあるものも必要ありません。

CI は `HYDRA_UMC_CI=1 python tools/ci_validate.py` を実行し、マニフェスト、文書、8 つの README、図を検査します。

## 🏗️ ビルドとリリース

`build.sh` / `build.bat` はパッケージをインストールしてテストを実行します。バージョンは変更しません。`build-test.sh` / `build-test.bat` は何も変更せずに検査します。

## 📂 リポジトリの構成

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of HYDRA-UMC-DOCS" width="100%">
</p>

<details>
<summary>ツリーのテキスト版</summary>

```text
HYDRA-UMC-DOCS/
├── docs/                                                                           アーキテクチャ、インターフェース、能力マトリクス、セキュリティ基準、脅威モデル、最初のスライス、生成されたカタログ
├── data/                                                                           確認済みの記述と、「ひと目で」の表のデータ
├── src/                                                                            パッケージとしてのツール（カタログ、ブランド、README、公開前チェック）
├── tools/                                                                          パッケージの上の薄いスクリプト、check_all.sh、エコシステム共通の CI チェック
├── tests/                                                                          ツールの単体テスト
├── images/                                                                         バナーとファミリーマップ
├── brand/                                                                          アイコン
├── .github/                                                                        CI ワークフローと Issue テンプレート
├── build.sh / build.bat / build-test.sh / build-test.bat / run.sh / run.bat        ビルドと検査。バージョンは変更しない
├── hydra-umc.project.json / pyproject.toml / CHANGELOG.md / LICENSE / LICENSE.md   マニフェスト：バージョン、成熟度、ファミリー
├── bump_manifest_version.py                                                        マニフェストのバージョンを同期
├── bump_version.py                                                                 明示的なバージョン更新
└── test.sh                                                                         テストを実行
```

</details>

## 🗺️ ロードマップと既知の制限

**現時点の既知の制限**

このリポジトリは文書と小さなツールでできています。他のリポジトリを読む検査（カタログ、At a glance の表、記述の確認）には、それらのリポジトリをこのリポジトリの隣にチェックアウトしておく必要があります。ハードウェアについては何も証明しません。機能マトリクスが、各機能について、シミュレーションのみか実際に試したかを示します。

## 🌍 言語

この README とリポジトリの文書は、英語・スペイン語・ドイツ語・フランス語・イタリア語・日本語・中国語・ポルトガル語（ポルトガル）の 8 言語で提供されています。8 つのファイルは同時に書かれ、同じ節と同じリンクを持つことを CI が確認します。 このリポジトリには独自の画面もメッセージカタログもないため、翻訳すべきインターフェース文字列はありません。

## 🔗 関連プロジェクト

HYDRA-UMC は独立したリポジトリで構成され、それぞれに固有のバージョン、テスト、README があります。グループ別のファミリーは次のとおりです：

* **Cognitive AI Node:** [HYDRA-UMC-COGNITIVE-NODE](https://github.com/JuanenRac/HYDRA-UMC-COGNITIVE-NODE), [HYDRA-UMC-DOCS-QA](https://github.com/JuanenRac/HYDRA-UMC-DOCS-QA), [HYDRA-UMC-LOCAL-TECHNICIAN](https://github.com/JuanenRac/HYDRA-UMC-LOCAL-TECHNICIAN), [HYDRA-UMC-SEMANTIC-PLANNER](https://github.com/JuanenRac/HYDRA-UMC-SEMANTIC-PLANNER), [HYDRA-UMC-VLA-ENGINE](https://github.com/JuanenRac/HYDRA-UMC-VLA-ENGINE), [HYDRA-UMC-VOICE-UI](https://github.com/JuanenRac/HYDRA-UMC-VOICE-UI)
* **Complementary Tools:** [HYDRA-UMC-DASHBOARD-AI](https://github.com/JuanenRac/HYDRA-UMC-DASHBOARD-AI), [HYDRA-UMC-TOOL-CLI](https://github.com/JuanenRac/HYDRA-UMC-TOOL-CLI), [HYDRA-UMC-WATCH](https://github.com/JuanenRac/HYDRA-UMC-WATCH)
* **Core Backend & Clients:** [HYDRA-UMC-ANDROID-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-ANDROID-CONTROL), [HYDRA-UMC-DSI](https://github.com/JuanenRac/HYDRA-UMC-DSI), [HYDRA-UMC-EDITOR-STL](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-STL), [HYDRA-UMC-EDITOR-URDF](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-URDF), [HYDRA-UMC-IOS-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-IOS-CONTROL), [HYDRA-UMC-SERVER](https://github.com/JuanenRac/HYDRA-UMC-SERVER), [HYDRA-UMC-STUDIO](https://github.com/JuanenRac/HYDRA-UMC-STUDIO), [HYDRA-UMC-SUITE](https://github.com/JuanenRac/HYDRA-UMC-SUITE)
* **Core Hardware:** [HYDRA-UMC](https://github.com/JuanenRac/HYDRA-UMC)
* **Data & Analytics:** [HYDRA-UMC-ANOMALY-DETECTOR](https://github.com/JuanenRac/HYDRA-UMC-ANOMALY-DETECTOR), [HYDRA-UMC-DATALAKE](https://github.com/JuanenRac/HYDRA-UMC-DATALAKE), [HYDRA-UMC-PRODUCTION-REPORTS](https://github.com/JuanenRac/HYDRA-UMC-PRODUCTION-REPORTS), [HYDRA-UMC-TELEMETRY-COLLECTOR](https://github.com/JuanenRac/HYDRA-UMC-TELEMETRY-COLLECTOR)
* **Digital Twin & Simulation:** [HYDRA-UMC-HIL-BRIDGE](https://github.com/JuanenRac/HYDRA-UMC-HIL-BRIDGE), [HYDRA-UMC-PHYSICS-REPLICA](https://github.com/JuanenRac/HYDRA-UMC-PHYSICS-REPLICA), [HYDRA-UMC-SYNTHETIC-DATA-GEN](https://github.com/JuanenRac/HYDRA-UMC-SYNTHETIC-DATA-GEN), [HYDRA-UMC-TWIN](https://github.com/JuanenRac/HYDRA-UMC-TWIN)
* **Ecosystem Operations:** [HYDRA-UMC-DEV-SERVER](https://github.com/JuanenRac/HYDRA-UMC-DEV-SERVER), **HYDRA-UMC-DOCS** (このリポジトリ), [HYDRA-UMC-OPS-AGENT](https://github.com/JuanenRac/HYDRA-UMC-OPS-AGENT), [HYDRA-UMC-OS-REBUILDER](https://github.com/JuanenRac/HYDRA-UMC-OS-REBUILDER), [HYDRA-UMC-UPDATER](https://github.com/JuanenRac/HYDRA-UMC-UPDATER)
* **External Automation Bridges:** [HYDRA-UMC-BRIDGE-CNC](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-CNC), [HYDRA-UMC-BRIDGE-LASER](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-LASER), [HYDRA-UMC-BRIDGE-OPENPNP](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-OPENPNP), [HYDRA-UMC-BRIDGE-PRINTER3D](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-PRINTER3D), [HYDRA-UMC-BRIDGE-ROS2](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-ROS2)
* **Industrial Gateway:** [HYDRA-UMC-GATEWAY-INDUSTRIAL](https://github.com/JuanenRac/HYDRA-UMC-GATEWAY-INDUSTRIAL), [HYDRA-UMC-MQTT-BROKER](https://github.com/JuanenRac/HYDRA-UMC-MQTT-BROKER), [HYDRA-UMC-MTCONNECT-ADAPTER](https://github.com/JuanenRac/HYDRA-UMC-MTCONNECT-ADAPTER), [HYDRA-UMC-OPCUA-SERVER](https://github.com/JuanenRac/HYDRA-UMC-OPCUA-SERVER)
* **Mobile & Autonomous Bridges:** [HYDRA-UMC-BRIDGE-AMR](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-AMR), [HYDRA-UMC-BRIDGE-DROIDS](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-DROIDS), [HYDRA-UMC-BRIDGE-UAV](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-UAV)
* **Orchestration & Swarm:** [HYDRA-UMC-JOB-DISPATCHER](https://github.com/JuanenRac/HYDRA-UMC-JOB-DISPATCHER), [HYDRA-UMC-NODE-HEALING](https://github.com/JuanenRac/HYDRA-UMC-NODE-HEALING), [HYDRA-UMC-ORCHESTRATOR](https://github.com/JuanenRac/HYDRA-UMC-ORCHESTRATOR), [HYDRA-UMC-PATH-PLANNER-3D](https://github.com/JuanenRac/HYDRA-UMC-PATH-PLANNER-3D), [HYDRA-UMC-SWARM-SYNC](https://github.com/JuanenRac/HYDRA-UMC-SWARM-SYNC)
* **Platform Foundation & Contracts:** [HYDRA-UMC-CONNECTOR-HUB](https://github.com/JuanenRac/HYDRA-UMC-CONNECTOR-HUB), [HYDRA-UMC-OS](https://github.com/JuanenRac/HYDRA-UMC-OS), [HYDRA-UMC-SDK](https://github.com/JuanenRac/HYDRA-UMC-SDK)
* **Vision AI Node:** [HYDRA-UMC-DETECTION-HEF](https://github.com/JuanenRac/HYDRA-UMC-DETECTION-HEF), [HYDRA-UMC-SAFETY-ZONES](https://github.com/JuanenRac/HYDRA-UMC-SAFETY-ZONES), [HYDRA-UMC-VISION-NODE](https://github.com/JuanenRac/HYDRA-UMC-VISION-NODE), [HYDRA-UMC-VISION-STREAMER](https://github.com/JuanenRac/HYDRA-UMC-VISION-STREAMER), [HYDRA-UMC-VISUAL-SERVOING-API](https://github.com/JuanenRac/HYDRA-UMC-VISUAL-SERVOING-API)

**HYDRA-UMC の外：**

* **[ARMOR-DOCS](https://github.com/JuanenRac/ARMOR-DOCS)** - A.R.M.O.R. セキュリティエコシステム向けの同じ考え方
* **[URTC](https://github.com/JuanenRac/URTC)** - 汎用ロボットツールコントローラ。SDK 経由で接続される独立した製品
* **[JuanenRac](https://github.com/JuanenRac/JuanenRac)** - すべてのエコシステムのプロフィールとステータスダッシュボード

## 📚 ドキュメント

さらに読むには：

* [能力マトリクス：実証済みのものとそうでないもの](docs/CAPABILITY_MATRIX.md)
* [プロジェクトカタログ：各リポジトリのバージョンと種類](docs/PROJECT_CATALOG.md)
* [エコシステムのセキュリティ基準](https://github.com/JuanenRac/HYDRA-UMC-DOCS/blob/main/docs/SECURITY_BASELINE.md)
* [エコシステムの脅威モデル](https://github.com/JuanenRac/HYDRA-UMC-DOCS/blob/main/docs/THREAT_MODEL.md)
* [このリポジトリの変更履歴](CHANGELOG.md)
* [このリポジトリのライセンス](LICENSE.md)

## 🤝 コントリビュートとコミュニティ

* プルリクエストの前に `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py`（または `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`）を実行してください。`CI_VALIDATION=PASS` と表示される必要があります。この確認に `build.sh` や `build.bat` は使わないでください。ビルドは検査ではありません。
* 8 つの README は HYDRA-UMC-DOCS の 1 つのソースから書かれます。手で編集しないでください。ソースを変更し、`tools/make_readmes.py` で書き直します。
* 実行していないことを README に書かないでください。事実であれば「シミュレーションのみ」「実機では未確認」と書きます。
* [CONTRIBUTING.md](CONTRIBUTING.md)、[行動規範](CODE_OF_CONDUCT.md)、[SECURITY.md](SECURITY.md)、[SUPPORT.md](SUPPORT.md) を参照してください。

## 👤 作者

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 ライセンス

GPL-3.0-or-later - [LICENSE](LICENSE).
