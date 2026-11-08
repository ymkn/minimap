# minimap

キーボード設計プロジェクト。KiCad設計、FreeCAD設計、文書、画像、ファームウェアの案内を分離した。現行Choc版とMX/GLP3版を保持し、過去版・試行履歴は `archive/` に保管する。

## 編集対象

| 対象 | 開くファイル | 保存されている設計 |
| --- | --- | --- |
| Choc V2 PCB・回路図 | `KiCAD/PCB/minimap_PCB.kicad_pro` | 114.5mm角、裏面ナット四点固定 |
| Choc V2プレート | `KiCAD/SwitchPlate/minimap_ChocV2Plate.kicad_pro` | 114.5mm角、14.0mm・R0.5の35開口、厚さ1.2mm、市松・ロゴ・minimap文字 |
| 本体ケース・奥端ウェイト | `FreeCAD/minimap.FCStd` | 外寸120.5mm角、110×14mmウェイト、5°、金属／3DP代替Body |
| 額縁ケース検討案 | `FreeCAD/concepts/picture-frame/minimap_frame.FCStd` | 外寸130.5mm角、三段の額縁・46本の目盛り溝。現行ケースとは別の外観検討用 |
| MX/GLP3 PCB・回路図 | `KiCAD/PCB_GLP/minimap_PCB.kicad_pro` | 126.25×114.5mm、旧ダンパー取付構造 |
| GLP3プレート | `KiCAD/SwitchPlate_GLP/minimap_SwitchPlate.kicad_pro` | 126.25×114.5mm、14.1mm・R0.5の35開口、厚さ1.2mm |

MX/GLP3とChocでは外形・固定方式が異なる。**現在のケースをMX/GLP3用として扱わない。** `minimap.FCStd` には本体ケースの `Case` Bodyと、代替ウェイトの `WeightMetal`・`WeightPrint` Bodyが含まれる。ウェイトだけのCADではない。

「現行」は今回残す設計版を意味し、製造承認ではない。全版 `production_ready=false`。実物の安定性・強度・公差・実金具・スイッチ着座高さ・全実装部品・加工適合は未認定。検討用STEPを本番製造・加工発注へ使わない。今回、新たなDRC・CAD再計算・Gerber生成は行っていない。

## ディレクトリ

```text
minimap/
├─ KiCAD/
│  ├─ PCB/                  # Choc V2
│  ├─ PCB_GLP/              # MX/GLP3
│  ├─ SwitchPlate/          # Choc V2プレート
│  ├─ SwitchPlate_GLP/      # GLP3プレート
│  └─ lib/external/         # ymknlibs・非フリーロゴ
├─ FreeCAD/
│  ├─ minimap.FCStd         # 現行の本体ケース・ウェイト
│  ├─ STEP/                 # 現行CADに対応する3点
│  └─ concepts/
│     └─ picture-frame/     # 額縁検討案のCAD・STEP・画像・検査記録
├─ doc/                     # 恒久的な設計説明・input/KLS
├─ image/                   # 公開・説明用の恒久的な画像
├─ firmware/               # WSL側ファームウェアの所在案内
└─ archive/                # 過去版・試行履歴（Git対象外）
```

PCBの詳細は [doc/pcb.md](doc/pcb.md)、プレートは [doc/plates.md](doc/plates.md)、ケースは [doc/case.md](doc/case.md)。設計元のKLSは `doc/input/minimap.kls.json`（レイアウトは維持し、名称のみ更新）。過去の検査・作業報告と一時レビュー画像は `archive/doc/reports/`・`archive/image/` に保管し、`doc/`・`image/` には置かない。

`archive/` は `.gitignore` の `/archive/` で除外する。削除はしていないが、**Gitで取得・復元される対象にはならないため、保管が必要なら別途バックアップする。**

作業履歴は `archive/` に保管する。過去のスクリプト・JSON・CAD内のSourceFile等に残る旧パスは履歴として保持しており、旧スクリプトをそのまま再実行しない。

外観検討案は `FreeCAD/concepts/` 内で案ごとにまとめ、CAD・対応STEP・説明画像・既存検査記録を同じディレクトリに置く。現行設計の出力や恒久画像とは混在させない。詳細は [額縁検討案のREADME](FreeCAD/concepts/picture-frame/README.md) を参照。自動バックアップ・一時ファイルはGit対象外とし、残す必要のある控えは `archive/` に退避する。

## 依存ライブラリと出典

- `KiCAD/lib/external/ymknlibs`：submodule、固定commit `db12e941510b766ef9056fc83638b4f0245368ad`。SWD三穴・暫定M2ナット・公称モデル・出典通知を含む。ライブラリの修正用リポジトリは `../ymknlibs`。
- `KiCAD/lib/external/ymknlibs-nonfree`：submodule、固定commit `4cd0a35976a805284cbc0c04509bade35a44c603`。非フリーのロゴを含むため同梱の `LICENSE` に従う。
- SWDとナットは `ymknlib_Various` に共通化。ナット名の `PROVISIONAL` は維持し、実装工程適合・はんだ接合強度は未承認。出典はライブラリの `licenses/NOTICE-SMTSO2010CTJ.md`。
- 外部ライブラリは `.gitmodules` とsubmoduleのcommitで版を固定し、自動更新しない。標準ライブラリはKiCad 10の環境変数を利用し、既存の `${KICAD8_3RD_PARTY}` 参照も残る。
- ライブラリ・モデル・ロゴ等は、それぞれに同梱されたライセンス・通知に従う。

取得先は `https://github.com/ymkn/minimap.git`。

```sh
git clone --recurse-submodules https://github.com/ymkn/minimap.git
```

通常のclone後は `git submodule update --init --recursive` でライブラリを取得する。ライブラリを更新して共有するときは、ライブラリ側のcommitを先に公開し、そのcommitを参照するminimap側を後から公開する。非フリーライブラリの取得にはアクセス権が必要になる場合がある。

既存U3モデルの欠落と、検査環境で解決できないMXソケットの外部モデル参照は未修正。

## ファームウェア

所在と注意は [firmware/README.md](firmware/README.md)。本体はWSL2 Ubuntu側で管理し、今回コピー・移動していない。
