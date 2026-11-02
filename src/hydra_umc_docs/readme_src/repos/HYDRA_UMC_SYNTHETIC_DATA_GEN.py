# HYDRA-UMC-DOCS - readme_src/repos/HYDRA_UMC_SYNTHETIC_DATA_GEN.py
# Copyright (C) 2026 JuanenRac (Electro Hobby 3D). GPL-3.0-or-later.
"""What is specific to the README of HYDRA-UMC-SYNTHETIC-DATA-GEN."""
from __future__ import annotations

from typing import Any

from .. import service_kit as S

ICON = '📸'
COMMENT = 'Procedural training datasets with exact labels'
BADGES = [('Format', 'YOLO%20%2F%20COCO', 'FF6F00'), ('Target', 'Vision%20AI%20Node', 'green')]
NO_UI = True

SPEC = {
    "stack": "python",
    "req": "3.10",
    "quick": [
        [
            "./build.sh",
            "Linux, macOS (build.bat on Windows)"
        ],
        "./run.sh generate --out ./out --count 10 --seed 42",
        "./run.sh generate --out ./out --format yolo --defect-rate 0.3"
    ],
    "test_cmd": "python -m pytest -q tests",
    "alt": "HYDRA-UMC-SYNTHETIC-DATA-GEN architecture",
    "role": {
        "en": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** writes small training datasets for the vision nodes: random scenes of components, with the bounding boxes taken from the same coordinates that drew them, exported as YOLO or COCO together with a manifest of how the set was made. Today the scenes are flat 2D shapes; rendering through the Digital Twin is planned.",
        "es": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** escribe pequeños conjuntos de entrenamiento para los nodos de visión: escenas aleatorias de componentes, con las cajas delimitadoras tomadas de las mismas coordenadas que las dibujaron, exportadas como YOLO o COCO junto con un manifiesto de cómo se hizo el conjunto. Hoy las escenas son formas 2D planas; el renderizado con el Digital Twin está previsto.",
        "de": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** schreibt kleine Trainingsdatensätze für die Vision-Knoten: zufällige Szenen aus Bauteilen, deren Begrenzungsrahmen aus denselben Koordinaten stammen, mit denen sie gezeichnet wurden, exportiert als YOLO oder COCO zusammen mit einem Manifest, wie der Satz entstand. Heute sind die Szenen flache 2D-Formen; das Rendern über den Digital Twin ist geplant.",
        "fr": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** écrit de petits jeux d'entraînement pour les nœuds de vision : des scènes aléatoires de composants, dont les boîtes englobantes viennent des mêmes coordonnées que celles qui les ont dessinées, exportées en YOLO ou COCO avec un manifeste de la façon dont le jeu a été fait. Aujourd'hui les scènes sont des formes 2D plates ; le rendu via le Digital Twin est prévu.",
        "it": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** scrive piccoli insiemi di addestramento per i nodi di visione: scene casuali di componenti, con i riquadri presi dalle stesse coordinate che le hanno disegnate, esportati come YOLO o COCO insieme a un manifesto di come è stato fatto l'insieme. Oggi le scene sono forme 2D piatte; il rendering tramite il Digital Twin è previsto.",
        "ja": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** はビジョンノード向けの小さな学習データセットを書き出します。部品のランダムな場面で、バウンディングボックスは描画に使った同じ座標から取られ、YOLO または COCO 形式で、作り方を記録したマニフェストとともに出力されます。現在の場面は平面の 2D 図形で、Digital Twin 経由のレンダリングは計画中です。",
        "zh": "**HYDRA-UMC-SYNTHETIC-DATA-GEN** 为视觉节点写出小型训练数据集：随机的元件场景，边界框取自绘制它们的同一组坐标，以 YOLO 或 COCO 导出，并附带说明数据集如何生成的清单。目前场景是平面的 2D 形状；通过 Digital Twin 渲染还在计划中。",
        "pt": "O **HYDRA-UMC-SYNTHETIC-DATA-GEN** escreve pequenos conjuntos de treino para os nós de visão: cenas aleatórias de componentes, com as caixas delimitadoras tiradas das mesmas coordenadas que as desenharam, exportadas como YOLO ou COCO com um manifesto de como o conjunto foi feito. Hoje as cenas são formas 2D planas; a renderização através do Digital Twin está prevista."
    }
}


from ... import readme_kit as K

EXTRAS: Any = {}


def EXTRA(lg):
    out = {}
    sec = EXTRAS.get("security")
    if sec:
        out["security"] = K.table(lg, "threat", sec["rows"]) + ("\n\n" + K.pick(sec["never"], lg) if sec.get("never") else "")
    cfg = EXTRAS.get("configuration")
    if cfg:
        out["configuration"] = (K.pick(cfg["intro"], lg) + "\n\n" if cfg.get("intro") else "") + K.table(lg, "config", cfg["rows"])
    trb = EXTRAS.get("troubleshooting")
    if trb:
        out["troubleshooting"] = K.table(lg, "trouble", trb)
    itf = EXTRAS.get("interfaces")
    if itf:
        out["interfaces"] = K.table(lg, itf["head"], itf["rows"]) if isinstance(itf["head"], str) else K.table(lg, [K.pick(h, lg) for h in itf["head"]], itf["rows"])
    return out


def DOCS(lg, ctx):
    return S.docs_items(lg, ctx)


def BODY(lg, ctx):
    body = S.make_body(lg, ctx, SPEC)
    body.update(EXTRA(lg))
    return body


# Optional scenarios of `generate` (all off unless their option is given), described in the configuration section.
_SCENARIOS = {
    "en": "Classes and parts from outside (all off unless the option is given): `generate --classes-from REGISTRY --model NAME` takes the classes, in the order of the model (which is the class id), and the size of the input from a registry of HYDRA-UMC-DETECTION-HEF, and draws no defect when the model has no `defect` class; only the name, version, size and classes reach the manifest, never a path. `--catalog FILE` draws the objects with the outline of the real parts of a catalogue of STL and URDF files (a convex outline seen from above, files inside the folder of the catalogue only) instead of rectangles. `--servoing-config FILE` (needs a catalogue; `configs/servoing.json`) places parts at sampled 6-DOF poses in front of a pinhole camera and writes `poses.json` with the intrinsics and, per image, the translation, quaternion and angles of each part. `--safety-config FILE` (`configs/safety_zones.json`) adds stylised people in and out of rectangular zones and writes `zones.json` with the zones, the boxes and the action a safety system should take (`stop`, `slow` or `clear`); a file whose `enabled` is not `true` changes nothing, and `verify` checks both files against the manifest.",
    "es": "Clases y piezas de fuera (todo apagado salvo que se dé la opción): `generate --classes-from REGISTRO --model NOMBRE` toma las clases, en el orden del modelo (que es el id de clase), y el tamaño de la entrada de un registro de HYDRA-UMC-DETECTION-HEF, y no dibuja defectos si el modelo no tiene clase `defect`; al manifiesto solo llegan el nombre, la versión, el tamaño y las clases, nunca una ruta. `--catalog FICHERO` dibuja los objetos con la silueta de las piezas reales de un catálogo de ficheros STL y URDF (silueta convexa vista desde arriba, solo ficheros dentro de la carpeta del catálogo) en lugar de rectángulos. `--servoing-config FICHERO` (necesita catálogo; `configs/servoing.json`) coloca piezas con poses 6-DOF muestreadas ante una cámara estenopeica y escribe `poses.json` con los intrínsecos y, por imagen, la traslación, el cuaternión y los ángulos de cada pieza. `--safety-config FICHERO` (`configs/safety_zones.json`) añade personas estilizadas dentro y fuera de zonas rectangulares y escribe `zones.json` con las zonas, las cajas y la acción que debería tomar un sistema de seguridad (`stop`, `slow` o `clear`); un fichero cuyo `enabled` no es `true` no cambia nada, y `verify` comprueba ambos ficheros contra el manifiesto.",
    "de": "Klassen und Teile von außen (alles aus, sofern die Option nicht gegeben wird): `generate --classes-from REGISTER --model NAME` übernimmt die Klassen in der Reihenfolge des Modells (sie ist die Klassen-ID) und die Eingabegröße aus einem Register von HYDRA-UMC-DETECTION-HEF und zeichnet keinen Defekt, wenn das Modell keine Klasse `defect` hat; ins Manifest gelangen nur Name, Version, Größe und Klassen, nie ein Pfad. `--catalog DATEI` zeichnet die Objekte mit dem Umriss der echten Teile eines Katalogs aus STL- und URDF-Dateien (ein konvexer Umriss von oben, nur Dateien im Ordner des Katalogs) statt mit Rechtecken. `--servoing-config DATEI` (braucht einen Katalog; `configs/servoing.json`) platziert Teile in gesampelten 6-DOF-Posen vor einer Lochkamera und schreibt `poses.json` mit den Intrinsics und je Bild Translation, Quaternion und Winkeln jedes Teils. `--safety-config DATEI` (`configs/safety_zones.json`) fügt stilisierte Personen in und außerhalb rechteckiger Zonen hinzu und schreibt `zones.json` mit den Zonen, den Rahmen und der Aktion, die ein Sicherheitssystem wählen sollte (`stop`, `slow` oder `clear`); eine Datei, deren `enabled` nicht `true` ist, ändert nichts, und `verify` prüft beide Dateien gegen das Manifest.",
    "fr": "Classes et pièces venues de l'extérieur (tout est désactivé sauf si l'option est donnée) : `generate --classes-from REGISTRE --model NOM` prend les classes, dans l'ordre du modèle (qui est l'identifiant de classe), et la taille de l'entrée dans un registre de HYDRA-UMC-DETECTION-HEF, et ne dessine aucun défaut si le modèle n'a pas de classe `defect` ; seuls le nom, la version, la taille et les classes arrivent dans le manifeste, jamais un chemin. `--catalog FICHIER` dessine les objets avec la silhouette des vraies pièces d'un catalogue de fichiers STL et URDF (silhouette convexe vue de dessus, uniquement des fichiers dans le dossier du catalogue) au lieu de rectangles. `--servoing-config FICHIER` (demande un catalogue ; `configs/servoing.json`) place des pièces à des poses 6-DOF échantillonnées devant une caméra sténopé et écrit `poses.json` avec les intrinsèques et, par image, la translation, le quaternion et les angles de chaque pièce. `--safety-config FICHIER` (`configs/safety_zones.json`) ajoute des personnes stylisées dans et hors de zones rectangulaires et écrit `zones.json` avec les zones, les boîtes et l'action qu'un système de sécurité devrait prendre (`stop`, `slow` ou `clear`) ; un fichier dont `enabled` n'est pas `true` ne change rien, et `verify` contrôle les deux fichiers par rapport au manifeste.",
    "it": "Classi e pezzi dall'esterno (tutto spento salvo che si dia l'opzione): `generate --classes-from REGISTRO --model NOME` prende le classi, nell'ordine del modello (che è l'id di classe), e la dimensione dell'ingresso da un registro di HYDRA-UMC-DETECTION-HEF, e non disegna difetti se il modello non ha la classe `defect`; nel manifesto arrivano solo nome, versione, dimensione e classi, mai un percorso. `--catalog FILE` disegna gli oggetti con la sagoma dei pezzi reali di un catalogo di file STL e URDF (sagoma convessa vista dall'alto, solo file dentro la cartella del catalogo) invece di rettangoli. `--servoing-config FILE` (richiede un catalogo; `configs/servoing.json`) colloca pezzi in pose 6-DOF campionate davanti a una camera stenopeica e scrive `poses.json` con gli intrinseci e, per immagine, traslazione, quaternione e angoli di ogni pezzo. `--safety-config FILE` (`configs/safety_zones.json`) aggiunge persone stilizzate dentro e fuori da zone rettangolari e scrive `zones.json` con le zone, i riquadri e l'azione che un sistema di sicurezza dovrebbe prendere (`stop`, `slow` o `clear`); un file il cui `enabled` non è `true` non cambia nulla, e `verify` controlla entrambi i file rispetto al manifesto.",
    "ja": "外部からのクラスと部品（オプションを指定しない限りすべてオフ）：`generate --classes-from REGISTRY --model NAME` は、HYDRA-UMC-DETECTION-HEF のレジストリからモデルの順序どおりのクラス（その順序がクラス ID）と入力サイズを取り込み、モデルに `defect` クラスがなければ欠陥を描きません。マニフェストに入るのは名前、バージョン、サイズ、クラスだけで、パスは決して入りません。`--catalog FILE` は、長方形の代わりに、STL と URDF ファイルのカタログにある実際の部品の輪郭（上から見た凸の輪郭。カタログのフォルダ内のファイルのみ）で物体を描きます。`--servoing-config FILE`（カタログが必要。`configs/servoing.json`）は、サンプリングした 6 自由度の姿勢でピンホールカメラの前に部品を置き、内部パラメータと、画像ごとに各部品の並進・クォータニオン・角度を記した `poses.json` を書きます。`--safety-config FILE`（`configs/safety_zones.json`）は、長方形のゾーンの内外に様式化した人物を加え、ゾーン、ボックス、安全システムが取るべき動作（`stop`、`slow`、`clear`）を記した `zones.json` を書きます。`enabled` が `true` でないファイルは何も変えず、`verify` は両ファイルをマニフェストと照合します。",
    "zh": "来自外部的类别与零件（除非给出选项，否则全部关闭）：`generate --classes-from 注册表 --model 名称` 从 HYDRA-UMC-DETECTION-HEF 的注册表中取得按模型顺序排列的类别（该顺序即类别 id）和输入尺寸，若模型没有 `defect` 类则不绘制缺陷；清单中只会出现名称、版本、尺寸和类别，绝不会出现路径。`--catalog 文件` 用 STL 和 URDF 文件目录中真实零件的轮廓（从上方看的凸轮廓，仅限目录文件夹内的文件）代替矩形来绘制物体。`--servoing-config 文件`（需要目录；`configs/servoing.json`）把零件按采样的 6 自由度位姿放在针孔相机前，并写出 `poses.json`，其中有内参以及每张图像中每个零件的平移、四元数和角度。`--safety-config 文件`（`configs/safety_zones.json`）在矩形区域内外加入风格化的人物，并写出 `zones.json`，包含区域、边界框以及安全系统应采取的动作（`stop`、`slow` 或 `clear`）；`enabled` 不是 `true` 的文件不会改变任何东西，`verify` 会对照清单检查这两个文件。",
    "pt": "Classes e peças vindas de fora (tudo desligado a menos que a opção seja dada): `generate --classes-from REGISTO --model NOME` toma as classes, pela ordem do modelo (que é o id da classe), e o tamanho da entrada de um registo do HYDRA-UMC-DETECTION-HEF, e não desenha defeitos se o modelo não tiver a classe `defect`; ao manifesto chegam apenas o nome, a versão, o tamanho e as classes, nunca um caminho. `--catalog FICHEIRO` desenha os objetos com o contorno das peças reais de um catálogo de ficheiros STL e URDF (contorno convexo visto de cima, só ficheiros dentro da pasta do catálogo) em vez de retângulos. `--servoing-config FICHEIRO` (precisa de catálogo; `configs/servoing.json`) coloca peças em poses 6-DOF amostradas diante de uma câmara pinhole e escreve `poses.json` com os intrínsecos e, por imagem, a translação, o quaternião e os ângulos de cada peça. `--safety-config FICHEIRO` (`configs/safety_zones.json`) acrescenta pessoas estilizadas dentro e fora de zonas retangulares e escreve `zones.json` com as zonas, as caixas e a ação que um sistema de segurança deve tomar (`stop`, `slow` ou `clear`); um ficheiro cujo `enabled` não seja `true` não muda nada, e `verify` confere ambos os ficheiros com o manifesto.",
}
ADDENDA = {"configuration": _SCENARIOS}

_BODY_BASE = BODY


def BODY(lg, ctx):  # type: ignore[no-redef]
    from ... import readme_kit as _K

    return _K.apply_addenda(_BODY_BASE(lg, ctx), ADDENDA, lg)
