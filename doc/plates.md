# プレート編集対象

| 版 | 開くファイル | 外形・開口 |
| --- | --- | --- |
| Choc V2 | `../KiCAD/SwitchPlate/minimap_ChocV2Plate.kicad_pro` | 114.5mm角、35個×14.0mm・R0.5、厚さ1.2mm |
| GLP3 | `../KiCAD/SwitchPlate_GLP/minimap_SwitchPlate.kicad_pro` | 126.25×114.5mm、35個×14.1mm・R0.5、厚さ1.2mm |

Chocは市松銅箔・ロゴ・minimap文字を含む。作業時の図は `../archive/image/choc-plate/`、既存検査記録は `../archive/doc/reports/current-choc-plate/` に保管する。

GLP3版のPCB・プロジェクトは今回変更していない。ライブラリ表の参照パスだけを新構成へ調整した。旧製造ZIP、過去の検査・生成記録・表示設定は `../archive/Plate/` へ退避した。旧ZIPを現行寸法・開口の製造データとして使用しない。

ロゴは `../KiCAD/lib/external/ymknlibs-nonfree/` の非フリーライブラリを参照する。同梱ライセンスに従う。ChocとGLP3で外形・開口・固定構造が異なり、互換性を保証しない。

今回、新しいDRC・ゾーン再充填・製造出力生成は行っていない。**製造未承認・`production_ready=false`。** 保持力・実スイッチ着座高さ・加工適合は未検証。
