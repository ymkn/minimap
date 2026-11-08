# 現行ケース

編集対象：**`minimap.FCStd`**。本体ケースとウェイトを含む一つの文書で、版番号はファイル・フォルダー名に持たせない。

114.5mm角Choc基板・プレート向けの外寸120.5mm角バスタブケースと、奥端110×14mmの細いウェイト。5°、手前ゴム帯と奥端パッドで支持する。金属タップ版と3DPナット版は代替Bodyで、同時には使用しない。

現行とは別の外観検討案：[`concepts/picture-frame/`](concepts/picture-frame/)（壁厚7.5mm・外周R2・三段の額縁と46本の内周開放目盛り溝、溝幅1mm・端R0.5）。現行CAD・現行STEPの置き換えではない。

## 現行STEP

出力は `STEP/` 内の次の3ファイルだけを使用する。保存済み `minimap.FCStd` の対応形状と、体積・外接寸法・双方向の形状差を照合済み。

| STEP | 対応Body・用途 |
| --- | --- |
| [`STEP/minimap_case.step`](STEP/minimap_case.step) | `Case`：本体ケース |
| [`STEP/minimap_weight_metal.step`](STEP/minimap_weight_metal.step) | `WeightMetal`：金属タップ版ウェイト |
| [`STEP/minimap_weight_print.step`](STEP/minimap_weight_print.step) | `WeightPrint`：3DPナット版ウェイト |

金属版と3DP版は代替案であり、旧版と新版ではない。同時には使用しない。すべてケースの設計座標系で、印刷用に接地面を水平に置き直したデータではない。CADを変更した場合は対応STEPも更新する。

STL一式と、前側ゴム帯の理想化した参考STEPは `../archive/freecad-exports-20261104/` へ退避した。ゴム帯の形状自体はCAD内の `FrontContactStrip` に残る。

寸法・組立・金具・出力・制約は [../doc/case.md](../doc/case.md)。作業時の図・検査記録は `../archive/image/case/`・`../archive/doc/reports/current-case/` に保管する。

旧WeightPlate_v1/v2、BathtubMount_v2、SquareMount_v1、KeyboardCase、TiltBase、MinimapBar、変更前控え・旧プレビューは `../archive/Case/` に退避した。MX/GLP3版に対応した旧ケースも同所で保管し、現行Chocケースと区別する。

**製造未承認・`production_ready=false`。** 「現行CADに一致」は製造適合の認定ではない。実荷重での安定性、ゴム、強度・公差・実金具・USB・全実装部品、スイッチ／プレート着座高さは未確認。今回、CADとSTEPの内容は変更していない。
