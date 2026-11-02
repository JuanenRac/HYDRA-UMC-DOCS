# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_STUDIO_KIT.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-STUDIO-KIT."""
from __future__ import annotations

from .. import service_kit as S

ICON = '🧰'
COMMENT = 'Shared code of the HYDRA-UMC web clients'
BADGES = [('Stack', 'TypeScript', '3178C6'), ('Feature', 'No%20Runtime%20Dependencies', 'blueviolet')]
NO_UI = True

SPEC = {
    "stack": "node",
    "req": "22",
    "quick": [
        [
            "npm ci",
            "installs the development dependencies (the package itself has none at run time)"
        ],
        [
            "npm run build",
            "compiles src/ to dist/ (./build.sh runs the tests first; build.bat on Windows)"
        ],
        "npm run typecheck && npm run lint && npm test"
    ],
    "quick_after": {
        "en": "Use it from a web client with `import { createSession, createHttpClient } from 'hydra-umc-studio-kit'`; `docs/API.md` has the reference and `docs/MIGRATION.md` the steps a client follows to adopt it.",
        "es": "Úsalo desde un cliente web con `import { createSession, createHttpClient } from 'hydra-umc-studio-kit'`; `docs/API.md` contiene la referencia y `docs/MIGRATION.md` los pasos que sigue un cliente para adoptarlo.",
        "de": "Verwende es in einem Webclient mit `import { createSession, createHttpClient } from 'hydra-umc-studio-kit'`; `docs/API.md` enthält die Referenz und `docs/MIGRATION.md` die Schritte, mit denen ein Client es übernimmt.",
        "fr": "Utilisez-le depuis un client web avec `import { createSession, createHttpClient } from 'hydra-umc-studio-kit'` ; `docs/API.md` contient la référence et `docs/MIGRATION.md` les étapes que suit un client pour l'adopter.",
        "it": "Usalo da un client web con `import { createSession, createHttpClient } from 'hydra-umc-studio-kit'`; `docs/API.md` contiene il riferimento e `docs/MIGRATION.md` i passi che un client segue per adottarlo.",
        "ja": "Web クライアントから `import { createSession, createHttpClient } from 'hydra-umc-studio-kit'` で使います。リファレンスは `docs/API.md`、クライアントが取り込む手順は `docs/MIGRATION.md` にあります。",
        "zh": "在 Web 客户端中通过 `import { createSession, createHttpClient } from 'hydra-umc-studio-kit'` 使用；`docs/API.md` 是参考文档，`docs/MIGRATION.md` 是客户端接入的步骤。",
        "pt": "Use-o a partir de um cliente web com `import { createSession, createHttpClient } from 'hydra-umc-studio-kit'`; `docs/API.md` tem a referência e `docs/MIGRATION.md` os passos que um cliente segue para o adotar."
    },
    "test_cmd": "npm test",
    "alt": "HYDRA-UMC-STUDIO-KIT architecture",
    "role": {
        "en": "**HYDRA-UMC-STUDIO-KIT** is the code that the web clients of the family would otherwise copy from one another: the sign-in session, the HTTP client, the connection history, the local preferences and the guided tours, as a TypeScript package with no framework and no runtime dependencies. HYDRA-UMC-STUDIO is the first client meant to use it and does not consume it yet.",
        "es": "**HYDRA-UMC-STUDIO-KIT** es el código que los clientes web de la familia, si no, se copiarían unos a otros: la sesión, el cliente HTTP, el historial de conexiones, las preferencias locales y los recorridos guiados, como un paquete de TypeScript sin framework y sin dependencias de ejecución. HYDRA-UMC-STUDIO es el primer cliente pensado para usarlo y todavía no lo consume.",
        "de": "**HYDRA-UMC-STUDIO-KIT** ist der Code, den die Webclients der Familie sonst voneinander kopieren würden: die Anmeldesitzung, der HTTP-Client, der Verbindungsverlauf, die lokalen Einstellungen und die geführten Rundgänge, als TypeScript-Paket ohne Framework und ohne Laufzeitabhängigkeiten. HYDRA-UMC-STUDIO ist der erste Client, der es nutzen soll, und nutzt es noch nicht.",
        "fr": "**HYDRA-UMC-STUDIO-KIT** est le code que les clients web de la famille se copieraient sinon les uns aux autres : la session de connexion, le client HTTP, l'historique des connexions, les préférences locales et les visites guidées, sous forme de paquet TypeScript sans framework et sans dépendance d'exécution. HYDRA-UMC-STUDIO est le premier client prévu pour l'utiliser et ne le consomme pas encore.",
        "it": "**HYDRA-UMC-STUDIO-KIT** è il codice che i client web della famiglia altrimenti si copierebbero a vicenda: la sessione di accesso, il client HTTP, la cronologia delle connessioni, le preferenze locali e i tour guidati, come pacchetto TypeScript senza framework e senza dipendenze di esecuzione. HYDRA-UMC-STUDIO è il primo client pensato per usarlo e non lo consuma ancora.",
        "ja": "**HYDRA-UMC-STUDIO-KIT** は、ファミリーの Web クライアントが放っておけば互いにコピーし合うコードです。サインインセッション、HTTP クライアント、接続履歴、ローカル設定、ガイドツアーを、フレームワークにも実行時の依存にも頼らない TypeScript パッケージにまとめています。HYDRA-UMC-STUDIO がこれを使うことを想定した最初のクライアントですが、まだ使っていません。",
        "zh": "**HYDRA-UMC-STUDIO-KIT** 收纳了本系列 Web 客户端否则会互相复制的代码：登录会话、HTTP 客户端、连接历史、本地偏好设置和导览，作为一个不依赖框架、没有运行时依赖的 TypeScript 包。HYDRA-UMC-STUDIO 是第一个打算使用它的客户端，目前尚未使用。",
        "pt": "O **HYDRA-UMC-STUDIO-KIT** é o código que os clientes web da família, de outro modo, copiariam uns dos outros: a sessão de início de sessão, o cliente HTTP, o histórico de ligações, as preferências locais e as visitas guiadas, como um pacote TypeScript sem framework e sem dependências de execução. O HYDRA-UMC-STUDIO é o primeiro cliente pensado para o usar e ainda não o consome."
    },
    "test_note": {
        "en": " They use fakes for `fetch` and for the storage and need no browser and no network.",
        "es": " Usan simulaciones de `fetch` y del almacenamiento y no necesitan navegador ni red.",
        "de": " Sie nutzen Attrappen für `fetch` und den Speicher und brauchen weder Browser noch Netz.",
        "fr": " Ils utilisent des simulations de `fetch` et du stockage et n'ont besoin ni de navigateur ni de réseau.",
        "it": " Usano simulazioni di `fetch` e dell'archivio e non richiedono né browser né rete.",
        "ja": " `fetch` とストレージの代役を使うため、ブラウザーもネットワークも不要です。",
        "zh": " 它们使用 `fetch` 和存储的模拟替身，不需要浏览器，也不需要网络。",
        "pt": " Usam simulações de `fetch` e do armazenamento e não precisam de navegador nem de rede."
    }
}


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    return S.make_body(lg, ctx, SPEC)
