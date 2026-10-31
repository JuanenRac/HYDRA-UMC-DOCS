# The screenshots of the READMEs: which images each repository shows (they live in its images/screenshots/), and what each one says, in the eight languages.
# The images are taken at 1920x1080 on a test bench with made-up sample data, never on a real installation.
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""``SHOTS`` maps a repository to ``[(file in images/screenshots/, caption key)]``; ``section(lg, name)`` is the body of its Screenshots section."""
from __future__ import annotations

NOTE = {
    "en": "Captured at 1920×1080 on a test bench, with sample data and no real installation behind them.",
    "es": "Capturadas a 1920×1080 en un banco de pruebas, con datos de ejemplo y sin ninguna instalación real detrás.",
    "fr": "Capturées en 1920×1080 sur un banc d'essai, avec des données d'exemple et sans installation réelle derrière.",
    "it": "Catturate a 1920×1080 su un banco di prova, con dati di esempio e senza alcuna installazione reale dietro.",
    "de": "Aufgenommen mit 1920×1080 auf einem Prüfstand, mit Beispieldaten und ohne eine echte Anlage dahinter.",
    "zh": "在测试台上以 1920×1080 截取，使用示例数据，背后没有真实的安装。",
    "ja": "テストベンチで 1920×1080 で撮影。サンプルデータを使用しており、実際の設備は接続されていません。",
    "pt": "Capturadas a 1920×1080 numa bancada de testes, com dados de exemplo e sem qualquer instalação real por trás.",
}

_ORDER = ("en", "es", "fr", "it", "de", "zh", "ja", "pt")


def _c(*texts: str) -> dict[str, str]:
    return dict(zip(_ORDER, texts, strict=False))


CAPTIONS = {
    "studio_overview": _c(
        "Overview: the eight robot nodes of the micro-factory with their role, model and tooling, and the machine status in the bar below.",
        "Resumen: los ocho nodos robot de la microfábrica con su función, modelo y herramienta, y el estado de la máquina en la barra inferior.",
        "Vue d'ensemble : les huit nœuds robot de la micro-usine avec leur rôle, leur modèle et leur outil, et l'état de la machine dans la barre du bas.",
        "Panoramica: gli otto nodi robot della microfabbrica con ruolo, modello e utensile, e lo stato della macchina nella barra in basso.",
        "Übersicht: die acht Roboterknoten der Mikrofabrik mit Rolle, Modell und Werkzeug und der Maschinenstatus in der unteren Leiste.",
        "概览：微型工厂的八个机器人节点，包含其角色、型号和工具，底部状态栏显示机器状态。",
        "概要：マイクロファクトリーの 8 台のロボットノードと、その役割・モデル・ツール。下のバーにマシンの状態を表示します。",
        "Resumo: os oito nós de robô da microfábrica com a função, o modelo e a ferramenta, e o estado da máquina na barra inferior."),
    "studio_robot_view": _c(
        "Robot view: joint controls, XYZ jog, the 3D model of the arm and the trajectory panel with the recorded points.",
        "Vista de robot: controles de articulaciones, jog XYZ, el modelo 3D del brazo y el panel de trayectorias con los puntos grabados.",
        "Vue robot : commandes des articulations, jog XYZ, le modèle 3D du bras et le panneau des trajectoires avec les points enregistrés.",
        "Vista robot: comandi dei giunti, jog XYZ, il modello 3D del braccio e il pannello delle traiettorie con i punti registrati.",
        "Roboteransicht: Gelenksteuerung, XYZ-Jog, das 3D-Modell des Arms und das Trajektorienfeld mit den aufgezeichneten Punkten.",
        "机器人视图：关节控制、XYZ 点动、机械臂的 3D 模型，以及带有已记录点位的轨迹面板。",
        "ロボットビュー：関節コントロール、XYZ ジョグ、アームの 3D モデル、記録済みポイントを含む軌道パネル。",
        "Vista do robô: controlos das articulações, jog XYZ, o modelo 3D do braço e o painel de trajetórias com os pontos gravados."),
    "studio_xy_table": _c(
        "XY table: the size of the table, the jog buttons with their step and the live 3D view of the axes.",
        "Mesa XY: el tamaño de la mesa, los botones de jog con su paso y la vista 3D en vivo de los ejes.",
        "Table XY : la taille de la table, les boutons de jog avec leur pas et la vue 3D en direct des axes.",
        "Tavola XY: le dimensioni della tavola, i pulsanti di jog con il loro passo e la vista 3D dal vivo degli assi.",
        "XY-Tisch: die Größe des Tisches, die Jog-Tasten mit ihrer Schrittweite und die 3D-Live-Ansicht der Achsen.",
        "XY 工作台：工作台尺寸、带步长的点动按钮和各轴的实时 3D 视图。",
        "XY テーブル：テーブルのサイズ、ステップ付きのジョグボタン、各軸のライブ 3D ビュー。",
        "Mesa XY: o tamanho da mesa, os botões de jog com o seu passo e a vista 3D em direto dos eixos."),
    "studio_flasher": _c(
        "Flasher Studio: pick the board and the robot slot, choose a firmware file and flash it over CAN; here in simulation, so nothing is sent to a board.",
        "Flasher Studio: elige la placa y la ranura del robot, escoge un fichero de firmware y flashéalo por CAN; aquí en simulación, así que no se envía nada a ninguna placa.",
        "Flasher Studio : choisissez la carte et l'emplacement du robot, un fichier de firmware, et flashez-le par CAN ; ici en simulation, donc rien n'est envoyé à une carte.",
        "Flasher Studio: scegli la scheda e lo slot del robot, un file di firmware e flashalo via CAN; qui in simulazione, quindi non viene inviato nulla a nessuna scheda.",
        "Flasher Studio: Platine und Roboterplatz wählen, eine Firmware-Datei auswählen und per CAN flashen; hier in der Simulation, es wird also nichts an eine Platine gesendet.",
        "Flasher Studio：选择开发板和机器人插槽，选择固件文件并通过 CAN 烧录；此处为模拟模式，不会向任何板子发送数据。",
        "Flasher Studio：ボードとロボットスロットを選び、ファームウェアファイルを選んで CAN で書き込みます。ここはシミュレーションで、ボードには何も送信されません。",
        "Flasher Studio: escolha a placa e a ranhura do robô, escolha um ficheiro de firmware e grave-o por CAN; aqui em simulação, por isso nada é enviado a nenhuma placa."),
    "studio_tester": _c(
        "Tester Center: the status LED, the persistence check, the tool telemetry, the self-test and the raw bus monitor of a board.",
        "Tester Center: el LED de estado, la comprobación de persistencia, la telemetría de la herramienta, el autotest y el monitor de bus en bruto de una placa.",
        "Tester Center : la LED d'état, le contrôle de persistance, la télémétrie de l'outil, l'autotest et le moniteur de bus brut d'une carte.",
        "Tester Center: il LED di stato, il controllo di persistenza, la telemetria dell'utensile, l'autotest e il monitor del bus grezzo di una scheda.",
        "Tester Center: die Status-LED, die Persistenzprüfung, die Werkzeugtelemetrie, der Selbsttest und der Rohbus-Monitor einer Platine.",
        "Tester Center：开发板的状态 LED、持久化检查、工具遥测、自检和原始总线监视器。",
        "Tester Center：ボードのステータス LED、永続性チェック、ツールテレメトリ、セルフテスト、生バスモニター。",
        "Tester Center: o LED de estado, a verificação de persistência, a telemetria da ferramenta, o autoteste e o monitor de barramento em bruto de uma placa."),
    "studio_safety_limits": _c(
        "Safety limits: arming of the jog, the reservation rule and the jog and bed-temperature ceilings per robot model, kept in the server.",
        "Límites de seguridad: armado del jog, regla de reservas y los techos de jog y de temperatura de cama por modelo de robot, guardados en el servidor.",
        "Limites de sécurité : armement du jog, règle de réservation et plafonds de jog et de température du plateau par modèle de robot, conservés dans le serveur.",
        "Limiti di sicurezza: armamento del jog, regola delle prenotazioni e i massimi di jog e di temperatura del piano per modello di robot, conservati nel server.",
        "Sicherheitsgrenzen: Scharfschaltung des Jogs, Reservierungsregel und die Jog- und Betttemperatur-Obergrenzen je Robotermodell, im Server gespeichert.",
        "安全限制：点动的启用、预约规则，以及按机器人型号设置的点动和热床温度上限，均保存在服务器中。",
        "安全制限：ジョグの有効化、予約ルール、ロボットモデルごとのジョグとベッド温度の上限。サーバーに保存されます。",
        "Limites de segurança: armação do jog, regra de reservas e os tetos de jog e de temperatura da cama por modelo de robô, guardados no servidor."),
}

CAPTIONS.update({
    "suite_overview": _c(
        "Overview: the active controller, its system metrics and the list of robots with model, role, status and speed.",
        "Resumen: el controlador activo, sus métricas del sistema y la lista de robots con modelo, función, estado y velocidad.",
        "Vue d'ensemble : le contrôleur actif, ses métriques système et la liste des robots avec modèle, rôle, état et vitesse.",
        "Panoramica: il controllore attivo, le sue metriche di sistema e l'elenco dei robot con modello, ruolo, stato e velocità.",
        "Übersicht: der aktive Controller, seine Systemmetriken und die Liste der Roboter mit Modell, Rolle, Status und Geschwindigkeit.",
        "概览：当前控制器、其系统指标，以及包含型号、角色、状态和速度的机器人列表。",
        "概要：アクティブなコントローラー、そのシステムメトリクス、モデル・役割・状態・速度つきのロボット一覧。",
        "Resumo: o controlador ativo, as suas métricas do sistema e a lista de robôs com modelo, função, estado e velocidade."),
    "suite_robot_control": _c(
        "Robot control: live or simulated mode, the reservation buttons, the six joint sliders, playback and the tool accessories.",
        "Control del robot: modo real o simulado, los botones de reserva, los seis deslizadores de articulación, la reproducción y los accesorios de la herramienta.",
        "Contrôle du robot : mode réel ou simulé, les boutons de réservation, les six curseurs d'articulation, la lecture et les accessoires de l'outil.",
        "Controllo del robot: modalità reale o simulata, i pulsanti di prenotazione, i sei cursori dei giunti, la riproduzione e gli accessori dell'utensile.",
        "Robotersteuerung: Live- oder Simulationsmodus, die Reservierungstasten, die sechs Gelenkregler, die Wiedergabe und das Werkzeugzubehör.",
        "机器人控制：实机或模拟模式、预约按钮、六个关节滑块、回放和工具附件。",
        "ロボット制御：実機またはシミュレーションのモード、予約ボタン、6 つの関節スライダー、再生、ツールのアクセサリー。",
        "Controlo do robô: modo real ou simulado, os botões de reserva, os seis cursores das articulações, a reprodução e os acessórios da ferramenta."),
    "suite_flasher": _c(
        "Flasher Studio: pick the board and the robot slot, see the route the update takes, choose a firmware file and flash it over CAN.",
        "Flasher Studio: elige la placa y la ranura del robot, mira la ruta que sigue la actualización, escoge un fichero de firmware y flashéalo por CAN.",
        "Flasher Studio : choisissez la carte et l'emplacement du robot, voyez le chemin de la mise à jour, un fichier de firmware, et flashez-le par CAN.",
        "Flasher Studio: scegli la scheda e lo slot del robot, guarda il percorso dell'aggiornamento, un file di firmware e flashalo via CAN.",
        "Flasher Studio: Platine und Roboterplatz wählen, den Weg des Updates sehen, eine Firmware-Datei auswählen und per CAN flashen.",
        "Flasher Studio：选择开发板和机器人插槽，查看更新经过的路径，选择固件文件并通过 CAN 烧录。",
        "Flasher Studio：ボードとロボットスロットを選び、更新の経路を確認して、ファームウェアファイルを CAN で書き込みます。",
        "Flasher Studio: escolha a placa e a ranhura do robô, veja o caminho que a atualização segue, escolha um ficheiro de firmware e grave-o por CAN."),
    "suite_tester": _c(
        "Tester Center: the status LED, the ring LED, the OLED mode, the persistence check, the self-test and the raw bus monitor of a board.",
        "Tester Center: el LED de estado, el LED en anillo, el modo OLED, la comprobación de persistencia, el autotest y el monitor de bus en bruto de una placa.",
        "Tester Center : la LED d'état, la LED en anneau, le mode OLED, le contrôle de persistance, l'autotest et le moniteur de bus brut d'une carte.",
        "Tester Center: il LED di stato, il LED ad anello, la modalità OLED, il controllo di persistenza, l'autotest e il monitor del bus grezzo di una scheda.",
        "Tester Center: die Status-LED, die Ring-LED, der OLED-Modus, die Persistenzprüfung, der Selbsttest und der Rohbus-Monitor einer Platine.",
        "Tester Center：开发板的状态 LED、环形 LED、OLED 模式、持久化检查、自检和原始总线监视器。",
        "Tester Center：ボードのステータス LED、リング LED、OLED モード、永続性チェック、セルフテスト、生バスモニター。",
        "Tester Center: o LED de estado, o LED em anel, o modo OLED, a verificação de persistência, o autoteste e o monitor de barramento em bruto de uma placa."),
    "suite_safety_limits": _c(
        "Safety limits: arming of the jog, the reservation rule and the jog and bed-temperature ceilings per robot model.",
        "Límites de seguridad: armado del jog, regla de reservas y los techos de jog y de temperatura de cama por modelo de robot.",
        "Limites de sécurité : armement du jog, règle de réservation et plafonds de jog et de température du plateau par modèle de robot.",
        "Limiti di sicurezza: armamento del jog, regola delle prenotazioni e i massimi di jog e di temperatura del piano per modello di robot.",
        "Sicherheitsgrenzen: Scharfschaltung des Jogs, Reservierungsregel und die Jog- und Betttemperatur-Obergrenzen je Robotermodell.",
        "安全限制：点动的启用、预约规则，以及按机器人型号设置的点动和热床温度上限。",
        "安全制限：ジョグの有効化、予約ルール、ロボットモデルごとのジョグとベッド温度の上限。",
        "Limites de segurança: armação do jog, regra de reservas e os tetos de jog e de temperatura da cama por modelo de robô."),
    "rebuilder_overview": _c(
        "The window: the CM5 projects found for the image with their version, role and stack, the build options and the build log.",
        "La ventana: los proyectos de la CM5 encontrados para la imagen con su versión, función y pila, las opciones de construcción y el registro.",
        "La fenêtre : les projets de la CM5 trouvés pour l'image avec leur version, leur rôle et leur pile, les options de construction et le journal.",
        "La finestra: i progetti della CM5 trovati per l'immagine con versione, ruolo e stack, le opzioni di costruzione e il registro.",
        "Das Fenster: die für das Image gefundenen CM5-Projekte mit Version, Rolle und Stack, die Build-Optionen und das Build-Protokoll.",
        "窗口：为镜像找到的 CM5 项目及其版本、角色和技术栈，构建选项和构建日志。",
        "ウィンドウ：イメージ用に見つかった CM5 プロジェクトのバージョン・役割・スタック、ビルドオプション、ビルドログ。",
        "A janela: os projetos da CM5 encontrados para a imagem com a sua versão, função e pilha, as opções de construção e o registo."),
})
CAPTIONS.update({
    "dashboard_ai": _c(
        "The two panels: the trend summary of a vibration series read from the data lake, and the anomaly check that scores its latest window against the fitted baseline.",
        "Los dos paneles: el resumen de tendencia de una serie de vibración leída del lago de datos, y la comprobación de anomalías que puntúa su última ventana contra la línea base ajustada.",
        "Les deux panneaux : le résumé de tendance d'une série de vibrations lue dans le lac de données, et le contrôle d'anomalies qui note sa dernière fenêtre par rapport à la base ajustée.",
        "I due pannelli: il riepilogo di tendenza di una serie di vibrazioni letta dal data lake, e il controllo delle anomalie che valuta l'ultima finestra rispetto alla baseline adattata.",
        "Die zwei Panels: die Trendzusammenfassung einer aus dem Data Lake gelesenen Schwingungsreihe und die Anomalieprüfung, die ihr jüngstes Fenster gegen die angepasste Baseline bewertet.",
        "两个面板：从数据湖读取的振动序列的趋势摘要，以及将其最新窗口与已拟合基线进行评分的异常检查。",
        "2 つのパネル：データレイクから読み取った振動系列のトレンド要約と、最新のウィンドウをフィット済みのベースラインに対して採点する異常チェック。",
        "Os dois painéis: o resumo de tendência de uma série de vibração lida do lago de dados e a verificação de anomalias que pontua a sua última janela contra a linha de base ajustada."),
})
# repository -> [(file in images/screenshots/, caption key)]
SHOTS: dict[str, list[tuple[str, str]]] = {
    "HYDRA-UMC-STUDIO": [("overview", "studio_overview"), ("robot-view", "studio_robot_view"), ("xy-table", "studio_xy_table"),
                         ("flasher-studio", "studio_flasher"), ("tester-center", "studio_tester"), ("safety-limits", "studio_safety_limits")],
    "HYDRA-UMC-SUITE": [("overview", "suite_overview"), ("robot-control", "suite_robot_control"), ("flasher-studio", "suite_flasher"), ("tester-center", "suite_tester"), ("safety-limits", "suite_safety_limits")],
    "HYDRA-UMC-OS-REBUILDER": [("overview", "rebuilder_overview")],
    "HYDRA-UMC-DASHBOARD-AI": [("dashboard", "dashboard_ai")],
}


def section(lg: str, name: str) -> str:
    """The body of the Screenshots section of a repository: the note and a two-column table of pictures with captions."""
    cells = [f'<td width="50%" valign="top"><img src="images/screenshots/{file}.png" alt="{CAPTIONS[key][lg]}" width="100%"><br><sub>{CAPTIONS[key][lg]}</sub></td>'
             for file, key in SHOTS[name]]
    rows = "\n".join("<tr>" + "".join(cells[i:i + 2]) + "</tr>" for i in range(0, len(cells), 2))
    return f"{NOTE[lg]}\n\n<table>\n{rows}\n</table>"
