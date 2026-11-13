# =============================================================================
# HYDRA-UMC-DOCS - src/hydra_umc_docs/status_rows.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D) <electrohobby3d@gmail.com>
# GPL-3.0-or-later - see LICENSE
# =============================================================================
"""The extra lines of the "Project status" table, in the eight languages.

Besides Software, Tests, Real hardware and Documentation a repository can carry lines for the parts that
matter to it: its interface, its integration with the rest of the ecosystem, its security, how it is
deployed, how it is operated, how it is updated, its stop path and its languages. Each line is chosen in
``data/glance.json`` (``"rows": {"security": "host_tested", ...}``) from a fixed list of states; every state
has one light and one sentence that says what is true and what has not been shown. Nothing is typed by hand
in a README, and no state is green unless nothing is left to prove (a security line is never green because
nobody outside the project has reviewed it).
"""
from __future__ import annotations

# the order of the lines in the table (after Software, Tests and Real hardware; Documentation stays last)
ORDER = ("interface", "integration", "security", "deployment", "operation", "updates", "stop", "access",
         "protocol", "contracts", "storage", "voice", "planning", "model")

LANGS = ("en", "es", "de", "fr", "it", "ja", "zh", "pt")


def _l(en, es, de, fr, it, ja, zh, pt):
    return dict(zip(LANGS, (en, es, de, fr, it, ja, zh, pt), strict=True))


LABELS = {
    "interface": _l("Interface and protocols", "Interfaz y protocolos", "Schnittstelle und Protokolle", "Interface et protocoles", "Interfaccia e protocolli", "インターフェースとプロトコル", "接口与协议", "Interface e protocolos"),
    "integration": _l("Integration", "Integración", "Integration", "Intégration", "Integrazione", "連携", "集成", "Integração"),
    "security": _l("Security", "Seguridad", "Sicherheit", "Sécurité", "Sicurezza", "セキュリティ", "安全性", "Segurança"),
    "deployment": _l("Deployment", "Despliegue", "Bereitstellung", "Déploiement", "Distribuzione", "デプロイ", "部署", "Implantação"),
    "operation": _l("Operation", "Operación", "Betrieb", "Exploitation", "Esercizio", "運用", "运维", "Operação"),
    "updates": _l("Updates", "Actualizaciones", "Aktualisierungen", "Mises à jour", "Aggiornamenti", "アップデート", "更新", "Atualizações"),
    "stop": _l("Stop and safety", "Parada y seguridad", "Stopp und Sicherheit", "Arrêt et sécurité", "Arresto e sicurezza", "停止と安全", "停止与安全", "Paragem e segurança"),
    "access": _l("Languages and accessibility", "Idiomas y accesibilidad", "Sprachen und Barrierefreiheit", "Langues et accessibilité", "Lingue e accessibilità", "言語とアクセシビリティ", "语言与无障碍", "Idiomas e acessibilidade"),
    "protocol": _l("Equipment protocol", "Protocolo del equipo", "Geräteprotokoll", "Protocole de l'équipement", "Protocollo dell'apparecchiatura", "機器のプロトコル", "设备协议", "Protocolo do equipamento"),
    "contracts": _l("Contracts and clients", "Contratos y clientes", "Verträge und Clients", "Contrats et clients", "Contratti e client", "契約とクライアント", "契约与客户端", "Contratos e clientes"),
    "storage": _l("Data and storage", "Datos y almacenamiento", "Daten und Speicher", "Données et stockage", "Dati e archiviazione", "データと保存", "数据与存储", "Dados e armazenamento"),
    "voice": _l("Voice", "Voz", "Sprache", "Voix", "Voce", "音声", "语音", "Voz"),
    "planning": _l("Planning", "Planificación", "Planung", "Planification", "Pianificazione", "計画", "规划", "Planeamento"),
    "model": _l("Vision model", "Modelo de visión", "Bildmodell", "Modèle de vision", "Modello di visione", "視覚モデル", "视觉模型", "Modelo de visão"),
}

# state -> (light, sentence per language)
STATES: dict[str, dict[str, tuple[str, dict[str, str]]]] = {
    "interface": {
        "documented_tested": ("yellow", _l(
            "The routes or messages it offers are documented and tested with a client; not every client has used them yet",
            "Las rutas o los mensajes que ofrece están documentados y probados con un cliente; aún no los han usado todos los clientes",
            "Die angebotenen Routen oder Nachrichten sind dokumentiert und mit einem Client getestet; noch nicht jeder Client hat sie benutzt",
            "Les routes ou les messages proposés sont documentés et testés avec un client ; tous les clients ne les ont pas encore utilisés",
            "Le rotte o i messaggi offerti sono documentati e provati con un client; non tutti i client li hanno ancora usati",
            "提供するルートやメッセージは文書化され、クライアントで試験済みです。すべてのクライアントがまだ使ったわけではありません",
            "提供的路由或消息已有文档，并用客户端测试过；尚未被所有客户端使用",
            "As rotas ou mensagens que oferece estão documentadas e testadas com um cliente; ainda nem todos os clientes as usaram")),
        "documented": ("orange", _l(
            "The routes or messages are documented; no client has been run against them in a test yet",
            "Las rutas o los mensajes están documentados; todavía ningún cliente se ha probado contra ellos",
            "Die Routen oder Nachrichten sind dokumentiert; noch kein Client wurde in einem Test dagegen betrieben",
            "Les routes ou les messages sont documentés ; aucun client n'a encore été exécuté contre eux dans un test",
            "Le rotte o i messaggi sono documentati; nessun client è ancora stato provato contro di essi in un test",
            "ルートやメッセージは文書化されていますが、クライアントを使った試験はまだありません",
            "路由或消息已有文档；尚未有客户端在测试中对其运行",
            "As rotas ou mensagens estão documentadas; nenhum cliente foi ainda testado contra elas")),
    },
    "integration": {
        "bench": ("yellow", _l(
            "It runs together with the other services on the CM5 test bench and its messages follow the shared contracts of the SDK",
            "Funciona junto con los demás servicios en el banco de pruebas de la CM5 y sus mensajes siguen los contratos compartidos del SDK",
            "Es läuft zusammen mit den anderen Diensten auf dem CM5-Prüfstand, und seine Nachrichten folgen den gemeinsamen Verträgen des SDK",
            "Il fonctionne avec les autres services sur le banc d'essai CM5 et ses messages suivent les contrats partagés du SDK",
            "Funziona insieme agli altri servizi sul banco prova CM5 e i suoi messaggi seguono i contratti condivisi dell'SDK",
            "CM5 のテストベンチで他のサービスと一緒に動作し、メッセージは SDK の共通契約に従います",
            "在 CM5 测试台上与其他服务一起运行，其消息遵循 SDK 的共享契约",
            "Funciona em conjunto com os outros serviços na bancada de testes da CM5 e as suas mensagens seguem os contratos partilhados do SDK")),
        "contract": ("yellow", _l(
            "Its messages and routes are checked against the shared contracts of the SDK; it has not run together with the real equipment",
            "Sus mensajes y rutas se comprueban contra los contratos compartidos del SDK; no ha funcionado junto con el equipo real",
            "Seine Nachrichten und Routen werden gegen die gemeinsamen Verträge des SDK geprüft; es lief noch nicht zusammen mit der echten Ausrüstung",
            "Ses messages et ses routes sont vérifiés par rapport aux contrats partagés du SDK ; il n'a pas fonctionné avec l'équipement réel",
            "I suoi messaggi e le sue rotte sono verificati rispetto ai contratti condivisi dell'SDK; non ha ancora funzionato insieme all'apparecchiatura reale",
            "メッセージとルートは SDK の共通契約に照らして検証されていますが、実機と一緒に動かしたことはありません",
            "其消息和路由已对照 SDK 的共享契约检查；尚未与真实设备一起运行",
            "As suas mensagens e rotas são verificadas contra os contratos partilhados do SDK; ainda não funcionou em conjunto com o equipamento real")),
        "standalone": ("orange", _l(
            "It works on its own; its link with the rest of the ecosystem has not been exercised yet",
            "Funciona por sí solo; su enlace con el resto del ecosistema aún no se ha ejercitado",
            "Es funktioniert für sich allein; die Verbindung zum Rest des Ökosystems wurde noch nicht erprobt",
            "Il fonctionne seul ; son lien avec le reste de l'écosystème n'a pas encore été exercé",
            "Funziona da solo; il collegamento con il resto dell'ecosistema non è ancora stato provato",
            "単独では動作しますが、エコシステムの他の部分との連携はまだ試していません",
            "它可以独立工作；与生态系统其余部分的连接尚未验证",
            "Funciona por si só; a ligação com o resto do ecossistema ainda não foi exercitada")),
    },
    "security": {
        "host_tested": ("yellow", _l(
            "Access control, input limits or signatures are implemented and tested on a computer; nobody outside the project has reviewed them",
            "El control de acceso, los límites de entrada o las firmas están implementados y probados en un ordenador; nadie ajeno al proyecto los ha revisado",
            "Zugriffskontrolle, Eingabegrenzen oder Signaturen sind umgesetzt und auf einem Rechner getestet; niemand außerhalb des Projekts hat sie geprüft",
            "Le contrôle d'accès, les limites d'entrée ou les signatures sont implémentés et testés sur un ordinateur ; personne hors du projet ne les a relus",
            "Il controllo degli accessi, i limiti d'ingresso o le firme sono implementati e provati su un computer; nessuno al di fuori del progetto li ha rivisti",
            "アクセス制御、入力の制限、署名のいずれかは実装されコンピューター上で試験済みですが、プロジェクト外の誰もレビューしていません",
            "访问控制、输入限制或签名已实现并在计算机上测试；项目之外无人审查过",
            "O controlo de acesso, os limites de entrada ou as assinaturas estão implementados e testados num computador; ninguém fora do projeto os reviu")),
        "partial": ("orange", _l(
            "Some protections exist (a token, limits on what it accepts) but they are not all covered by tests; nobody outside the project has reviewed them",
            "Existen algunas protecciones (un token, límites a lo que acepta) pero no todas están cubiertas por pruebas; nadie ajeno al proyecto las ha revisado",
            "Einige Schutzmaßnahmen bestehen (ein Token, Grenzen für das Akzeptierte), sind aber nicht alle durch Tests abgedeckt; niemand außerhalb des Projekts hat sie geprüft",
            "Quelques protections existent (un jeton, des limites sur ce qu'il accepte) mais elles ne sont pas toutes couvertes par des tests ; personne hors du projet ne les a relues",
            "Esistono alcune protezioni (un token, limiti su ciò che accetta) ma non sono tutte coperte da test; nessuno al di fuori del progetto le ha riviste",
            "一部の保護（トークン、受け付ける内容の制限）はありますが、すべてがテストで網羅されているわけではなく、プロジェクト外のレビューもありません",
            "有一些保护措施（令牌、对输入的限制），但并非都有测试覆盖；项目之外无人审查过",
            "Existem algumas proteções (um token, limites ao que aceita) mas nem todas estão cobertas por testes; ninguém fora do projeto as reviu")),
        "none": ("red", _l(
            "No protection is implemented yet",
            "Todavía no hay ninguna protección implementada",
            "Es ist noch kein Schutz umgesetzt",
            "Aucune protection n'est encore implémentée",
            "Non è ancora implementata alcuna protezione",
            "保護はまだ実装されていません",
            "尚未实现任何保护措施",
            "Ainda não há qualquer proteção implementada")),
        "not_applicable": ("white", _l(
            "Nothing to protect here: no network access, no secrets and no stored data",
            "Aquí no hay nada que proteger: sin acceso de red, sin secretos y sin datos almacenados",
            "Hier gibt es nichts zu schützen: kein Netzzugriff, keine Geheimnisse und keine gespeicherten Daten",
            "Rien à protéger ici : pas d'accès réseau, pas de secrets et pas de données stockées",
            "Qui non c'è nulla da proteggere: nessun accesso di rete, nessun segreto e nessun dato memorizzato",
            "保護するものはありません。ネットワークアクセス、秘密情報、保存データがありません",
            "此处无需保护：没有网络访问、没有机密、没有存储数据",
            "Aqui não há nada a proteger: sem acesso à rede, sem segredos e sem dados guardados")),
    },
    "deployment": {
        "cm5_service": ("yellow", _l(
            "Installed as a service on the CM5 test bench with its installer and unit; restarted on every update",
            "Instalado como servicio en el banco de pruebas de la CM5 con su instalador y su unidad; se reinicia en cada actualización",
            "Als Dienst auf dem CM5-Prüfstand mit Installer und Unit installiert; bei jeder Aktualisierung neu gestartet",
            "Installé comme service sur le banc d'essai CM5 avec son installeur et son unité ; redémarré à chaque mise à jour",
            "Installato come servizio sul banco prova CM5 con il suo installatore e la sua unità; riavviato a ogni aggiornamento",
            "CM5 のテストベンチにインストーラーとユニット付きのサービスとして導入され、更新のたびに再起動されます",
            "作为服务安装在 CM5 测试台上，带有安装脚本和单元；每次更新都会重启",
            "Instalado como serviço na bancada de testes da CM5 com o seu instalador e a sua unidade; reiniciado em cada atualização")),
        "installer": ("orange", _l(
            "An installer exists; it has not been run on the CM5 test bench as a service yet",
            "Existe un instalador; todavía no se ha ejecutado en el banco de pruebas de la CM5 como servicio",
            "Ein Installer existiert; er wurde noch nicht als Dienst auf dem CM5-Prüfstand ausgeführt",
            "Un installeur existe ; il n'a pas encore été exécuté comme service sur le banc d'essai CM5",
            "Esiste un installatore; non è ancora stato eseguito come servizio sul banco prova CM5",
            "インストーラーはありますが、CM5 のテストベンチでサービスとして実行したことはまだありません",
            "已有安装脚本；尚未在 CM5 测试台上作为服务运行",
            "Existe um instalador; ainda não foi executado como serviço na bancada de testes da CM5")),
        "release": ("orange", _l(
            "Published as a release; installing it on a clean machine is documented but not recorded",
            "Publicado como release; instalarlo en un equipo limpio está documentado pero no consta",
            "Als Release veröffentlicht; die Installation auf einem frischen Rechner ist dokumentiert, aber nicht vermerkt",
            "Publié comme release ; l'installation sur une machine propre est documentée mais non consignée",
            "Pubblicato come release; l'installazione su una macchina pulita è documentata ma non registrata",
            "リリースとして公開されています。新しい環境へのインストールは文書化されていますが記録はありません",
            "已作为发布版本公开；在干净机器上安装有文档，但没有记录",
            "Publicado como release; instalá-lo numa máquina limpa está documentado mas não registado")),
        "apk": ("orange", _l(
            "A signed APK is published with each release; no installation on a phone or watch is recorded for this version",
            "Con cada release se publica un APK firmado; no consta ninguna instalación en un móvil o reloj para esta versión",
            "Mit jedem Release wird ein signiertes APK veröffentlicht; für diese Version ist keine Installation auf Telefon oder Uhr vermerkt",
            "Un APK signé est publié avec chaque release ; aucune installation sur un téléphone ou une montre n'est consignée pour cette version",
            "Con ogni release viene pubblicato un APK firmato; per questa versione non è registrata alcuna installazione su telefono o orologio",
            "リリースごとに署名付き APK を公開しますが、この版でスマートフォンや時計に入れた記録はありません",
            "每个发布版本都会发布已签名的 APK；此版本没有在手机或手表上安装的记录",
            "É publicado um APK assinado com cada release; não há registo de instalação num telemóvel ou relógio para esta versão")),
    },
    "operation": {
        "metrics": ("yellow", _l(
            "Exposes /metrics in the Prometheus text format with a health summary; it is not wired to a monitoring dashboard yet",
            "Expone /metrics en el formato de texto de Prometheus con un resumen de salud; todavía no está conectado a un panel de supervisión",
            "Stellt /metrics im Prometheus-Textformat mit einer Gesundheitsübersicht bereit; noch nicht an ein Überwachungs-Dashboard angeschlossen",
            "Expose /metrics au format texte de Prometheus avec un résumé de santé ; pas encore relié à un tableau de supervision",
            "Espone /metrics nel formato testo di Prometheus con un riepilogo dello stato; non è ancora collegato a un pannello di monitoraggio",
            "Prometheus テキスト形式の /metrics と健全性の概要を公開しますが、監視ダッシュボードにはまだ接続していません",
            "以 Prometheus 文本格式提供 /metrics 和健康摘要；尚未接入监控面板",
            "Expõe /metrics no formato de texto do Prometheus com um resumo de saúde; ainda não está ligado a um painel de monitorização")),
        "metrics_optin": ("yellow", _l(
            "Offers /metrics in the Prometheus text format with a health summary once the configuration file enables it (off by default); it is not wired to a monitoring dashboard yet",
            "Ofrece /metrics en el formato de texto de Prometheus con un resumen de salud cuando el fichero de configuración lo activa (apagado por defecto); todavía no está conectado a un panel de supervisión",
            "Bietet /metrics im Prometheus-Textformat mit einer Gesundheitsübersicht, sobald die Konfigurationsdatei es aktiviert (standardmäßig aus); noch nicht an ein Überwachungs-Dashboard angeschlossen",
            "Offre /metrics au format texte de Prometheus avec un résumé de santé dès que le fichier de configuration l'active (désactivé par défaut) ; pas encore relié à un tableau de supervision",
            "Offre /metrics nel formato testo di Prometheus con un riepilogo dello stato quando il file di configurazione lo attiva (spento per impostazione predefinita); non è ancora collegato a un pannello di monitoraggio",
            "設定ファイルで有効にすると、Prometheus テキスト形式の /metrics と健全性の概要を提供します（既定では無効）。監視ダッシュボードにはまだ接続していません",
            "在配置文件启用后以 Prometheus 文本格式提供 /metrics 和健康摘要（默认关闭）；尚未接入监控面板",
            "Oferece /metrics no formato de texto do Prometheus com um resumo de saúde quando o ficheiro de configuração o ativa (desligado por predefinição); ainda não está ligado a um painel de monitorização")),
        "logs": ("orange", _l(
            "It writes logs; it has no metrics or health endpoint yet",
            "Escribe registros; todavía no tiene punto de métricas ni de salud",
            "Es schreibt Logs; einen Metrik- oder Gesundheits-Endpunkt hat es noch nicht",
            "Il écrit des journaux ; il n'a pas encore de point de métriques ni de santé",
            "Scrive log; non ha ancora un endpoint di metriche o di stato",
            "ログは出力しますが、メトリクスや健全性のエンドポイントはまだありません",
            "会写日志；尚无指标或健康检查端点",
            "Escreve registos; ainda não tem ponto de métricas nem de saúde")),
    },
    "updates": {
        "trains": ("yellow", _l(
            "Updated through HYDRA-UMC-UPDATER (signed trains, backups and rollback tested on a computer)",
            "Se actualiza con HYDRA-UMC-UPDATER (trenes firmados, copias de seguridad y reversión probadas en un ordenador)",
            "Wird über HYDRA-UMC-UPDATER aktualisiert (signierte Züge, Sicherungen und Rücknahme auf einem Rechner getestet)",
            "Mis à jour par HYDRA-UMC-UPDATER (trains signés, sauvegardes et retour arrière testés sur un ordinateur)",
            "Si aggiorna con HYDRA-UMC-UPDATER (treni firmati, copie di sicurezza e ripristino provati su un computer)",
            "HYDRA-UMC-UPDATER で更新します（署名付きトレイン、バックアップ、ロールバックはコンピューター上で試験済み）",
            "通过 HYDRA-UMC-UPDATER 更新（签名的发布列车、备份和回滚已在计算机上测试）",
            "Atualiza-se através do HYDRA-UMC-UPDATER (comboios assinados, cópias de segurança e reversão testados num computador)")),
        "apk": ("orange", _l(
            "Updated by installing the signed APK of the release; the update of an installed app is not recorded on a device",
            "Se actualiza instalando el APK firmado de la release; la actualización de una app instalada no consta en un dispositivo",
            "Wird durch Installieren des signierten APK des Releases aktualisiert; die Aktualisierung einer installierten App ist auf keinem Gerät vermerkt",
            "Mise à jour en installant l'APK signé de la release ; la mise à jour d'une app installée n'est pas consignée sur un appareil",
            "Si aggiorna installando l'APK firmato della release; l'aggiornamento di un'app installata non è registrato su un dispositivo",
            "リリースの署名付き APK を入れて更新します。インストール済みアプリの更新を実機で行った記録はありません",
            "通过安装发布版本的已签名 APK 来更新；在设备上更新已安装应用没有记录",
            "Atualiza-se instalando o APK assinado da release; a atualização de uma app instalada não está registada num dispositivo")),
        "manual": ("orange", _l(
            "Updated by hand from the release; there is no automatic update or rollback for it yet",
            "Se actualiza a mano desde la release; todavía no tiene actualización ni reversión automáticas",
            "Wird von Hand aus dem Release aktualisiert; eine automatische Aktualisierung oder Rücknahme gibt es noch nicht",
            "Mis à jour à la main depuis la release ; pas encore de mise à jour ni de retour arrière automatiques",
            "Si aggiorna a mano dalla release; non ha ancora aggiornamento né ripristino automatici",
            "リリースから手動で更新します。自動更新やロールバックはまだありません",
            "从发布版本手动更新；尚无自动更新或回滚",
            "Atualiza-se à mão a partir da release; ainda não tem atualização nem reversão automáticas")),
    },
    "stop": {
        "simulated": ("orange", _l(
            "The stop path and its limits are implemented and tested against simulators; they have never run on a real machine, and this is not a certified safety system",
            "El camino de parada y sus límites están implementados y probados con simuladores; nunca han funcionado en una máquina real, y esto no es un sistema de seguridad certificado",
            "Der Stoppweg und seine Grenzen sind umgesetzt und gegen Simulatoren getestet; sie liefen nie an einer echten Maschine, und dies ist kein zertifiziertes Sicherheitssystem",
            "Le chemin d'arrêt et ses limites sont implémentés et testés avec des simulateurs ; ils n'ont jamais fonctionné sur une vraie machine, et ce n'est pas un système de sécurité certifié",
            "Il percorso di arresto e i suoi limiti sono implementati e provati con simulatori; non hanno mai funzionato su una macchina reale e questo non è un sistema di sicurezza certificato",
            "停止経路とその制限は実装されシミュレーターで試験済みですが、実機で動かしたことはなく、認証された安全システムではありません",
            "停止路径及其限制已实现并用模拟器测试；从未在真实机器上运行，这也不是经过认证的安全系统",
            "O caminho de paragem e os seus limites estão implementados e testados com simuladores; nunca funcionaram numa máquina real, e isto não é um sistema de segurança certificado")),
    },
    "access": {
        "languages": ("yellow", _l(
            "The interface and its help are in eight languages; keyboard and screen-reader use has not been tested",
            "La interfaz y su ayuda están en ocho idiomas; el uso con teclado y lector de pantalla no se ha probado",
            "Oberfläche und Hilfe gibt es in acht Sprachen; die Bedienung per Tastatur und Screenreader wurde nicht getestet",
            "L'interface et son aide sont en huit langues ; l'usage au clavier et avec un lecteur d'écran n'a pas été testé",
            "L'interfaccia e la sua guida sono in otto lingue; l'uso con tastiera e screen reader non è stato provato",
            "インターフェースとヘルプは 8 言語ですが、キーボード操作とスクリーンリーダーでの利用は試していません",
            "界面及其帮助有八种语言；键盘和屏幕阅读器的使用尚未测试",
            "A interface e a sua ajuda estão em oito idiomas; a utilização com teclado e leitor de ecrã não foi testada")),
        "partial": ("orange", _l(
            "Some screens are translated; keyboard and screen-reader use has not been tested",
            "Algunas pantallas están traducidas; el uso con teclado y lector de pantalla no se ha probado",
            "Einige Bildschirme sind übersetzt; die Bedienung per Tastatur und Screenreader wurde nicht getestet",
            "Certains écrans sont traduits ; l'usage au clavier et avec un lecteur d'écran n'a pas été testé",
            "Alcune schermate sono tradotte; l'uso con tastiera e screen reader non è stato provato",
            "一部の画面は翻訳済みですが、キーボード操作とスクリーンリーダーでの利用は試していません",
            "部分界面已翻译；键盘和屏幕阅读器的使用尚未测试",
            "Alguns ecrãs estão traduzidos; a utilização com teclado e leitor de ecrã não foi testada")),
    },
    "protocol": {
        "mock": ("orange", _l(
            "Speaks the protocol of its equipment; checked against fakes and simulators only, never against the real machine",
            "Habla el protocolo de su equipo; comprobado solo con dobles de prueba y simuladores, nunca con la máquina real",
            "Spricht das Protokoll seines Geräts; nur gegen Attrappen und Simulatoren geprüft, nie gegen die echte Maschine",
            "Parle le protocole de son équipement ; vérifié seulement avec des doublures et des simulateurs, jamais avec la vraie machine",
            "Parla il protocollo della sua apparecchiatura; verificato solo con simulatori e controfigure, mai con la macchina reale",
            "機器のプロトコルを話しますが、検証は模擬機器とシミュレーターのみで、実機では行っていません",
            "使用其设备的协议；仅用仿真和模拟器检查过，从未对真实机器检查",
            "Fala o protocolo do seu equipamento; verificado só com simuladores e dobles de teste, nunca com a máquina real")),
    },
    "contracts": {
        "verified": ("green", _l(
            "Every closed contract has a valid and an invalid fixture and is validated in Python, Go, Rust and TypeScript against the same schemas",
            "Cada contrato cerrado tiene un ejemplo válido y uno inválido y se valida en Python, Go, Rust y TypeScript contra los mismos esquemas",
            "Jeder geschlossene Vertrag hat ein gültiges und ein ungültiges Beispiel und wird in Python, Go, Rust und TypeScript gegen dieselben Schemas geprüft",
            "Chaque contrat fermé a un exemple valide et un invalide et est validé en Python, Go, Rust et TypeScript par rapport aux mêmes schémas",
            "Ogni contratto chiuso ha un esempio valido e uno non valido ed è convalidato in Python, Go, Rust e TypeScript rispetto agli stessi schemi",
            "閉じた契約にはそれぞれ有効な例と無効な例があり、Python、Go、Rust、TypeScript で同じスキーマに対して検証されます",
            "每个封闭契约都有一个有效和一个无效的示例，并在 Python、Go、Rust 和 TypeScript 中按同一模式验证",
            "Cada contrato fechado tem um exemplo válido e um inválido e é validado em Python, Go, Rust e TypeScript contra os mesmos esquemas")),
    },
    "storage": {
        "host_tested": ("yellow", _l(
            "The store, its downsampling and its retention are tested on a computer and run on the CM5 test bench; not under a sustained load",
            "El almacén, su reducción de muestras y su retención están probados en un ordenador y funcionan en el banco de pruebas de la CM5; no con una carga sostenida",
            "Speicher, Downsampling und Aufbewahrung sind auf einem Rechner getestet und laufen auf dem CM5-Prüfstand; nicht unter Dauerlast",
            "Le stockage, son sous-échantillonnage et sa rétention sont testés sur un ordinateur et fonctionnent sur le banc CM5 ; pas sous charge soutenue",
            "L'archivio, il suo downsampling e la sua conservazione sono provati su un computer e funzionano sul banco prova CM5; non sotto carico prolungato",
            "ストア、ダウンサンプリング、保持期間はコンピューター上で試験済みで CM5 のテストベンチで動作していますが、持続的な負荷下では未検証です",
            "存储、降采样和保留策略已在计算机上测试，并在 CM5 测试台上运行；未做持续负载测试",
            "O armazenamento, a sua redução de amostras e a sua retenção estão testados num computador e funcionam na bancada da CM5; não sob carga contínua")),
    },
    "voice": {
        "synthetic": ("orange", _l(
            "The commands are understood in eight languages and the whole chain is tested with synthetic audio; no microphone or speech engine has been tried",
            "Los comandos se entienden en ocho idiomas y toda la cadena está probada con audio sintético; no se ha probado ningún micrófono ni motor de voz",
            "Die Befehle werden in acht Sprachen verstanden und die ganze Kette ist mit synthetischem Audio getestet; kein Mikrofon und keine Spracherkennung wurde ausprobiert",
            "Les commandes sont comprises en huit langues et toute la chaîne est testée avec de l'audio synthétique ; aucun microphone ni moteur vocal n'a été essayé",
            "I comandi sono compresi in otto lingue e tutta la catena è provata con audio sintetico; non è stato provato alcun microfono né motore vocale",
            "コマンドは 8 言語で理解され、全体の流れは合成音声で試験済みですが、マイクや音声エンジンは試していません",
            "命令可用八种语言理解，整条链路用合成音频测试；尚未试过麦克风或语音引擎",
            "Os comandos são entendidos em oito idiomas e toda a cadeia está testada com áudio sintético; nenhum microfone ou motor de voz foi experimentado")),
    },
    "planning": {
        "simulated": ("orange", _l(
            "The planner works on simulated scenes and scripted goals; it has never planned for a real robot",
            "El planificador funciona con escenas simuladas y objetivos de guion; nunca ha planificado para un robot real",
            "Der Planer arbeitet mit simulierten Szenen und vorgegebenen Zielen; er hat nie für einen echten Roboter geplant",
            "Le planificateur fonctionne sur des scènes simulées et des objectifs scriptés ; il n'a jamais planifié pour un vrai robot",
            "Il pianificatore funziona su scene simulate e obiettivi programmati; non ha mai pianificato per un robot reale",
            "プランナーは模擬シーンと台本どおりの目標で動作しますが、実機ロボットの計画をしたことはありません",
            "规划器在模拟场景和脚本化目标上工作；从未为真实机器人规划过",
            "O planeador funciona com cenas simuladas e objetivos de guião; nunca planeou para um robô real")),
    },
    "model": {
        "none": ("orange", _l(
            "The pipeline works with a stand-in detector; no real model has run on the accelerator yet",
            "La cadena funciona con un detector de sustitución; todavía no ha corrido ningún modelo real en el acelerador",
            "Die Pipeline arbeitet mit einem Ersatzdetektor; auf dem Beschleuniger lief noch kein echtes Modell",
            "La chaîne fonctionne avec un détecteur de remplacement ; aucun vrai modèle n'a encore tourné sur l'accélérateur",
            "La catena funziona con un rilevatore sostitutivo; nessun modello reale è ancora stato eseguito sull'acceleratore",
            "パイプラインは代用の検出器で動作しており、アクセラレーター上で実際のモデルを動かしたことはありません",
            "流水线使用替身检测器工作；尚未在加速器上运行真实模型",
            "A cadeia funciona com um detetor de substituição; ainda nenhum modelo real correu no acelerador")),
    },
}

STATE_KEYS = {key: tuple(states) for key, states in STATES.items()}
