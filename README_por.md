<!-- =============================================================================
HYDRA-UMC-DOCS - Architecture, interfaces, security baseline and what is proven
Copyright (C) JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
GPL-3.0-or-later - see LICENSE
============================================================================= -->

<p align="center">
  <img src="images/HYDRA_UMC_BANNER.svg" alt="HYDRA-UMC-DOCS banner" width="100%">
</p>

# 📚 HYDRA-UMC-DOCS

<p align="center"><a href="README.md">🇺🇸 English</a> | <a href="README_spa.md">🇪🇸 Español</a> | <a href="README_fra.md">🇫🇷 Français</a> | <a href="README_ita.md">🇮🇹 Italiano</a> | <a href="README_deu.md">🇩🇪 Deutsch</a> | <a href="README_zho.md">🇨🇳 简体中文</a> | <a href="README_jpn.md">🇯🇵 日本語</a> | 🇵🇹 <b>Português</b></p>

### Arquitetura, interfaces, base de segurança e a verdade sobre o que está comprovado

<p align="center">
  <img src="https://img.shields.io/badge/License-GPL%203.0--or--later-blue.svg" alt="GPL 3.0 or later">
  <img src="https://img.shields.io/badge/Format-Markdown-083fa1.svg" alt="Format">
  <img src="https://img.shields.io/badge/Languages-8-00E5FF.svg" alt="Languages">
  <img src="https://img.shields.io/badge/Tests-153%20passing-2ea44f.svg" alt="Tests">
  <img src="https://img.shields.io/badge/Version-0.0.5-0f6cbd.svg" alt="Version">
  <img src="https://img.shields.io/badge/Maturity-scaffolding-FFB020.svg" alt="Maturity">
</p>

---

**Verificação de honestidade - o que funciona mesmo hoje:** este repositório contém documentos e pequenas ferramentas. As ferramentas (o gerador do catálogo, o da marca, o dos README, a verificação de publicação e a verificação da família) são reais e têm testes unitários executados na CI; o fluxo noturno executa-as sobre os restantes repositórios da família. Os documentos são escritos a partir dos README, manifestos, registos de alterações e documentos desses repositórios tal como foram lidos para esta versão, e uma afirmação que não se conseguiu rastrear até um repositório fica assinalada como tal. Nada aqui é um teste de hardware: a matriz de capacidades diz, para cada capacidade, se foi apenas simulada, testada num computador ou executada em hardware real, e o repositório do firmware indica que ainda não existe nenhuma placa montada.

---

> **Estado de segurança (safety e security):** este ecossistema não é um sistema de segurança certificado. Ainda não existe um caminho de E-STOP por hardware, nem limites ou interlocks impostos pelo firmware, nem um comando de movimento verificado; as imagens de firmware são verificadas com CRC-32 e uma assinatura Ed25519, e uma compilação de versão recusa as chaves de desenvolvimento publicadas (as cabeças de ferramenta e as placas de expansão atrás do relé ainda usam os bootloaders do URTC, que aceitam um HMAC-SHA256 de chave partilhada em vez de uma assinatura); TLS e TLS mútuo são opcionais e estão desativados por defeito; nenhuma placa própria foi ainda montada ou testada. Leia a [base de segurança](docs/SECURITY_BASELINE.md) e o [modelo de ameaças](docs/THREAT_MODEL.md) antes de confiar em qualquer afirmação aqui para a segurança de uma pessoa.

---

## 📋 Num relance

| | |
|---|---|
| Versão | `0.0.5` |
| Maturidade | Estrutura inicial |
| Testes | 153 (`python -m pytest tests -q`) |
| Tecnologia | Markdown / Mermaid / Python / SVG |
| Destino | O PC de quem o usa |
| Em hardware real | Não aplicável: nada aqui corre em hardware |

**Ir para:** [Visão geral](#-visão-geral) · [Arquitetura](#-arquitetura) · [Segurança e proteção](#-segurança-e-proteção) · [Início rápido](#-início-rápido) · [Testes](#-testes) · [Estrutura do repositório](#-estrutura-do-repositório) · [Projetos relacionados](#-projetos-relacionados)

## 🚦 Estado do projeto

Cada linha é uma parte deste repositório e a luz diz até onde chega hoje. É escrita com o que o repositório consegue demonstrar (testes, compilações, execuções), não com o que está previsto.

🟢 Feito e verificado · 🟡 Funciona, com limites conhecidos · 🟠 Feito a meio ou ainda por verificar · 🔴 Por fazer ou a não funcionar

| Área | Estado | O que significa aqui |
|---|---|---|
| Software | 🟠 | Só estrutura e as primeiras peças; falta a maior parte do trabalho |
| Testes | 🟡 | 153 testes automáticos, executados a cada alteração |
| Hardware real | 🟡 | Não aplicável: nada aqui corre em hardware |
| Documentação | 🟡 | README em oito idiomas, verificado contra o manifesto a cada alteração |

## 🎯 Visão geral

<p align="center">
  <img src="images/HYDRA_UMC_FAMILY.svg" alt="HYDRA-UMC families" width="100%">
</p>

A imagem abaixo mostra as famílias de repositórios e os fluxos que os seus documentos afirmam.

* [Arquitetura](docs/ARCHITECTURE.md): camadas, fluxos de dados, portas e fronteiras de confiança.
* [Interfaces](docs/INTERFACES.md): quem é dono de cada contrato e onde está documentado.
* [Matriz de capacidades](docs/CAPABILITY_MATRIX.md): o que está comprovado em software e o que precisa de hardware, projeto a projeto.
* [Base de segurança](docs/SECURITY_BASELINE.md): o que o código impõe e o que ainda falta; e o [modelo de ameaças](docs/THREAT_MODEL.md).
* [Primeiro corte vertical](docs/FIRST_VERTICAL_SLICE.md): o caminho de ponta a ponta mais pequeno que existe hoje.
* [Catálogo de projetos](docs/PROJECT_CATALOG.md): cada repositório da família, escrito a partir do seu próprio manifesto.
* **Ferramentas:** `make_catalog.py` escreve o catálogo, `make_brand.py` o banner, o ícone e o mapa das famílias, `make_readmes.py` os oito README deste repositório, `publication_check.py` procura qualquer coisa privada antes de uma publicação e `check_all.sh` executa as verificações próprias de cada repositório da família e imprime uma linha PASS, FAIL ou SKIP por cada um. `make_glance.py` escreve a tabela Num relance de cada repositório a partir do seu manifesto e de `data/glance.json` (`--check` compara, `--apply` escreve); depois de subir uma versão, `python tools/make_glance.py --apply --repo NOME` atualiza a tabela desse repositório. `check_claims.py` lê o README em inglês de cada repositório da família e falha quando uma frase tem uma palavra de risco (E-STOP, interlock, tempo real, assinado, mTLS, FDCAN, YOLO, orientado por IA, autónomo, certificado, ...) sem uma marca de estado ao lado (previsto, não implementado, opcional, desativado por defeito, simulado, testado, ...), a menos que uma pessoa tenha lido essa linha junto ao código e a tenha registado em `data/claims_reviewed.json`.

## 🧩 Papel no HYDRA-UMC

O HYDRA-UMC-DOCS é a memória do ecossistema: o lugar onde vivem a arquitetura, as interfaces, a base de segurança e a matriz de capacidades, e onde se guardam as ferramentas que comparam todos os repositórios lado a lado. Cada repositório mantém o seu próprio README, os seus testes e o seu contrato; este explica como encaixam e o que foi realmente comprovado.

## 🏛️ Arquitetura

Os documentos descrevem cada família do ecossistema. A imagem abaixo é este próprio repositório: as ferramentas leem os manifestos e os README dos repositórios irmãos e escrevem o catálogo, as tabelas Num relance, o banner e os oito README, e duas verificações recusam o que não deve ser publicado.

<p align="center">
  <img src="images/architecture.svg" alt="HYDRA-UMC-DOCS architecture" width="100%">
</p>

## 🔒 Segurança e proteção

| Ameaça | Defesa | Onde |
|---|---|---|
| Um README que afirma uma capacidade de risco (uma paragem de emergência, um interbloqueio) sem dizer até onde está provada | `check_claims.py` lê o README em inglês de cada repositório e falha numa frase com uma palavra de risco sem marca de estado e sem revisão (`data/claims_reviewed.json`) | `tools/check_claims.py` |
| Algo privado a sair com uma publicação | `publication_check.py` procura qualquer coisa privada nos ficheiros e no histórico antes de uma publicação | `tools/publication_check.py` |
| Uma afirmação que ninguém consegue ligar a um repositório | Os documentos são escritos a partir dos README, manifestos, registos de alterações e documentos dos repositórios, e uma afirmação que não se conseguiu rastrear é marcada como tal | `docs/CAPABILITY_MATRIX.md` |

## 🚀 Início rápido

**Requisitos:** Python 3.10 ou superior; pytest para os testes

```bash
python tools/make_catalog.py --check             # o catálogo está atualizado (precisa dos repositórios ao lado deste)
python tools/make_brand.py --check               # o banner, o ícone e o mapa estão atualizados
python tools/make_readmes.py --check             # os oito README estão atualizados
python tools/make_glance.py --check              # as tabelas Num relance da família estão atualizadas (precisa dos repositórios ao lado deste)
python tools/status_lights.py --check            # as luzes da tabela Estado do projeto não passam do que o manifesto permite
python tools/publication_check.py                # nada privado sairia com uma publicação
python tools/check_claims.py --require-siblings  # nenhum README afirma uma capacidade de risco sem o seu estado (precisa dos repositórios ao lado deste)
bash tools/check_all.sh                          # as verificações de cada repositório, uma linha por cada um
python -m pytest tests -q                        # os testes unitários das ferramentas
```

## 🧪 Testes

153 testes automáticos correm com `python -m pytest tests -q`. Não precisam de hardware nem de nada fora desta máquina.

A CI executa `HYDRA_UMC_CI=1 python tools/ci_validate.py`, que verifica o manifesto, os documentos, os oito README e as imagens.

## 🏗️ Compilação e publicação

`build.sh` / `build.bat` instalam o pacote e executam os testes; nunca mudam a versão. `build-test.sh` / `build-test.bat` verificam sem alterar nada.

## 📂 Estrutura do repositório

<p align="center">
  <img src="images/repository-structure.svg" alt="Repository structure of HYDRA-UMC-DOCS" width="100%">
</p>

<details>
<summary>Versão em texto da árvore</summary>

```text
HYDRA-UMC-DOCS/
├── docs/                                                                           arquitetura, interfaces, matriz de capacidades, base de segurança, modelo de ameaças, primeiro corte, catálogo gerado
├── data/                                                                           as afirmações revistas e os dados das tabelas Num relance
├── src/                                                                            as ferramentas como pacote (catálogo, marca, README, verificação de publicação)
├── tools/                                                                          scripts finos sobre o pacote, check_all.sh e as verificações de CI partilhadas do ecossistema
├── tests/                                                                          testes unitários das ferramentas
├── images/                                                                         banner e mapa das famílias
├── brand/                                                                          o ícone
├── .github/                                                                        fluxo de CI e modelos de problemas
├── build.sh / build.bat / build-test.sh / build-test.bat / run.sh / run.bat        compila e verifica; nunca muda a versão
├── hydra-umc.project.json / pyproject.toml / CHANGELOG.md / LICENSE / LICENSE.md   manifesto: versão, maturidade, família
├── bump_manifest_version.py                                                        sincroniza a versão do manifesto
├── bump_version.py                                                                 subida de versão explícita
└── test.sh                                                                         executa os testes
```

</details>

## 🗺️ Roteiro e limites conhecidos

**Limites conhecidos hoje**

Este repositório é feito de documentos e pequenas ferramentas. As verificações que leem os outros repositórios (o catálogo, as tabelas Num relance, as afirmações) precisam desses repositórios descarregados ao lado deste. Não prova nada sobre hardware: a matriz de capacidades diz, para cada capacidade, se foi apenas simulada ou testada a sério.

## 🌍 Idiomas

Este README e os documentos do repositório existem em oito idiomas: inglês, espanhol, alemão, francês, italiano, japonês, chinês e português (Portugal). São escritos em conjunto e a CI verifica que os oito ficheiros têm as mesmas secções e as mesmas ligações. Este repositório não tem ecrã nem catálogo de mensagens próprios, por isso não há textos de interface para traduzir.

## 🔗 Projetos relacionados

O HYDRA-UMC é feito de repositórios independentes, cada um com a sua versão, os seus testes e o seu README. Esta é a família, por grupos:

* **Cognitive AI Node:** [HYDRA-UMC-COGNITIVE-NODE](https://github.com/JuanenRac/HYDRA-UMC-COGNITIVE-NODE), [HYDRA-UMC-DOCS-QA](https://github.com/JuanenRac/HYDRA-UMC-DOCS-QA), [HYDRA-UMC-LOCAL-TECHNICIAN](https://github.com/JuanenRac/HYDRA-UMC-LOCAL-TECHNICIAN), [HYDRA-UMC-SEMANTIC-PLANNER](https://github.com/JuanenRac/HYDRA-UMC-SEMANTIC-PLANNER), [HYDRA-UMC-VLA-ENGINE](https://github.com/JuanenRac/HYDRA-UMC-VLA-ENGINE), [HYDRA-UMC-VOICE-UI](https://github.com/JuanenRac/HYDRA-UMC-VOICE-UI)
* **Complementary Tools:** [HYDRA-UMC-DASHBOARD-AI](https://github.com/JuanenRac/HYDRA-UMC-DASHBOARD-AI), [HYDRA-UMC-TOOL-CLI](https://github.com/JuanenRac/HYDRA-UMC-TOOL-CLI), [HYDRA-UMC-WATCH](https://github.com/JuanenRac/HYDRA-UMC-WATCH)
* **Core Backend & Clients:** [HYDRA-UMC-ANDROID-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-ANDROID-CONTROL), [HYDRA-UMC-DSI](https://github.com/JuanenRac/HYDRA-UMC-DSI), [HYDRA-UMC-EDITOR-STL](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-STL), [HYDRA-UMC-EDITOR-URDF](https://github.com/JuanenRac/HYDRA-UMC-EDITOR-URDF), [HYDRA-UMC-IOS-CONTROL](https://github.com/JuanenRac/HYDRA-UMC-IOS-CONTROL), [HYDRA-UMC-SERVER](https://github.com/JuanenRac/HYDRA-UMC-SERVER), [HYDRA-UMC-STUDIO](https://github.com/JuanenRac/HYDRA-UMC-STUDIO), [HYDRA-UMC-SUITE](https://github.com/JuanenRac/HYDRA-UMC-SUITE)
* **Core Hardware:** [HYDRA-UMC](https://github.com/JuanenRac/HYDRA-UMC)
* **Data & Analytics:** [HYDRA-UMC-ANOMALY-DETECTOR](https://github.com/JuanenRac/HYDRA-UMC-ANOMALY-DETECTOR), [HYDRA-UMC-DATALAKE](https://github.com/JuanenRac/HYDRA-UMC-DATALAKE), [HYDRA-UMC-PRODUCTION-REPORTS](https://github.com/JuanenRac/HYDRA-UMC-PRODUCTION-REPORTS), [HYDRA-UMC-TELEMETRY-COLLECTOR](https://github.com/JuanenRac/HYDRA-UMC-TELEMETRY-COLLECTOR)
* **Digital Twin & Simulation:** [HYDRA-UMC-HIL-BRIDGE](https://github.com/JuanenRac/HYDRA-UMC-HIL-BRIDGE), [HYDRA-UMC-PHYSICS-REPLICA](https://github.com/JuanenRac/HYDRA-UMC-PHYSICS-REPLICA), [HYDRA-UMC-SYNTHETIC-DATA-GEN](https://github.com/JuanenRac/HYDRA-UMC-SYNTHETIC-DATA-GEN), [HYDRA-UMC-TWIN](https://github.com/JuanenRac/HYDRA-UMC-TWIN)
* **Ecosystem Operations:** [HYDRA-UMC-DEV-SERVER](https://github.com/JuanenRac/HYDRA-UMC-DEV-SERVER), **HYDRA-UMC-DOCS** (este repositório), [HYDRA-UMC-OPS-AGENT](https://github.com/JuanenRac/HYDRA-UMC-OPS-AGENT), [HYDRA-UMC-OS-REBUILDER](https://github.com/JuanenRac/HYDRA-UMC-OS-REBUILDER), [HYDRA-UMC-UPDATER](https://github.com/JuanenRac/HYDRA-UMC-UPDATER)
* **External Automation Bridges:** [HYDRA-UMC-BRIDGE-CNC](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-CNC), [HYDRA-UMC-BRIDGE-LASER](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-LASER), [HYDRA-UMC-BRIDGE-OPENPNP](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-OPENPNP), [HYDRA-UMC-BRIDGE-PRINTER3D](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-PRINTER3D), [HYDRA-UMC-BRIDGE-ROS2](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-ROS2)
* **Industrial Gateway:** [HYDRA-UMC-GATEWAY-INDUSTRIAL](https://github.com/JuanenRac/HYDRA-UMC-GATEWAY-INDUSTRIAL), [HYDRA-UMC-MQTT-BROKER](https://github.com/JuanenRac/HYDRA-UMC-MQTT-BROKER), [HYDRA-UMC-MTCONNECT-ADAPTER](https://github.com/JuanenRac/HYDRA-UMC-MTCONNECT-ADAPTER), [HYDRA-UMC-OPCUA-SERVER](https://github.com/JuanenRac/HYDRA-UMC-OPCUA-SERVER)
* **Mobile & Autonomous Bridges:** [HYDRA-UMC-BRIDGE-AMR](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-AMR), [HYDRA-UMC-BRIDGE-DROIDS](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-DROIDS), [HYDRA-UMC-BRIDGE-UAV](https://github.com/JuanenRac/HYDRA-UMC-BRIDGE-UAV)
* **Orchestration & Swarm:** [HYDRA-UMC-JOB-DISPATCHER](https://github.com/JuanenRac/HYDRA-UMC-JOB-DISPATCHER), [HYDRA-UMC-NODE-HEALING](https://github.com/JuanenRac/HYDRA-UMC-NODE-HEALING), [HYDRA-UMC-ORCHESTRATOR](https://github.com/JuanenRac/HYDRA-UMC-ORCHESTRATOR), [HYDRA-UMC-PATH-PLANNER-3D](https://github.com/JuanenRac/HYDRA-UMC-PATH-PLANNER-3D), [HYDRA-UMC-SWARM-SYNC](https://github.com/JuanenRac/HYDRA-UMC-SWARM-SYNC)
* **Platform Foundation & Contracts:** [HYDRA-UMC-CONNECTOR-HUB](https://github.com/JuanenRac/HYDRA-UMC-CONNECTOR-HUB), [HYDRA-UMC-OS](https://github.com/JuanenRac/HYDRA-UMC-OS), [HYDRA-UMC-SDK](https://github.com/JuanenRac/HYDRA-UMC-SDK)
* **Vision AI Node:** [HYDRA-UMC-DETECTION-HEF](https://github.com/JuanenRac/HYDRA-UMC-DETECTION-HEF), [HYDRA-UMC-SAFETY-ZONES](https://github.com/JuanenRac/HYDRA-UMC-SAFETY-ZONES), [HYDRA-UMC-VISION-NODE](https://github.com/JuanenRac/HYDRA-UMC-VISION-NODE), [HYDRA-UMC-VISION-STREAMER](https://github.com/JuanenRac/HYDRA-UMC-VISION-STREAMER), [HYDRA-UMC-VISUAL-SERVOING-API](https://github.com/JuanenRac/HYDRA-UMC-VISUAL-SERVOING-API)

**Para além do HYDRA-UMC:**

* **[ARMOR-DOCS](https://github.com/JuanenRac/ARMOR-DOCS)** - a mesma ideia para o ecossistema de segurança A.R.M.O.R.
* **[URTC](https://github.com/JuanenRac/URTC)** - o controlador universal de ferramenta de robô, um produto independente ligado através do SDK
* **[JuanenRac](https://github.com/JuanenRac/JuanenRac)** - o perfil e o painel de estado de todos os ecossistemas

## 📚 Documentação

Onde ler mais:

* [Matriz de capacidades: o que está comprovado e o que não está](docs/CAPABILITY_MATRIX.md)
* [Catálogo de projetos: versões e tipos dos repositórios](docs/PROJECT_CATALOG.md)
* [Base de segurança do ecossistema](https://github.com/JuanenRac/HYDRA-UMC-DOCS/blob/main/docs/SECURITY_BASELINE.md)
* [Modelo de ameaças do ecossistema](https://github.com/JuanenRac/HYDRA-UMC-DOCS/blob/main/docs/THREAT_MODEL.md)
* [Registo de alterações deste repositório](CHANGELOG.md)
* [Licença deste repositório](LICENSE.md)

## 🤝 Contribuir e comunidade

* Antes de um pull request execute `HYDRA_UMC_CI=1 py -3 tools/ci_validate.py` (ou `HYDRA_UMC_CI=1 python3 tools/ci_validate.py`): tem de imprimir `CI_VALIDATION=PASS`. Não execute `build.sh` nem `build.bat` para esta verificação; compilar não é verificar.
* Os oito README são escritos a partir de uma única fonte em HYDRA-UMC-DOCS; não os edite à mão. Altere a fonte e escreva-os de novo com `tools/make_readmes.py`.
* Não afirme num README o que não foi executado: diga «simulado» ou «não testado em hardware» quando for a verdade.
* Consulte [CONTRIBUTING.md](CONTRIBUTING.md), o [código de conduta](CODE_OF_CONDUCT.md), [SECURITY.md](SECURITY.md) e [SUPPORT.md](SUPPORT.md).

## 👤 AUTOR

**JuanenRac (Electro Hobby 3D)** · electrohobby3d@gmail.com

## 📜 LICENÇA

GPL-3.0-or-later - [LICENSE](LICENSE).
