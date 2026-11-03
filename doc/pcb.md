# PCB編集対象

| 版 | 開くファイル | 設計 |
| --- | --- | --- |
| Choc V2 | `../KiCAD/PCB/minimap_PCB.kicad_pro` | 114.5mm角、裏面ナット四点固定 |
| MX/GLP3 | `../KiCAD/PCB_GLP/minimap_PCB.kicad_pro` | 126.25×114.5mm、旧ダンパー取付方式 |

Chocは114.5mm角の裏面ナット固定版。MX/GLP3は旧ダンパー取付方式の別設計であり、同じケースへの互換性は保証しない。

SWD三穴とM2ナットは共通ライブラリ `ymknlib_Various` を参照する。実体は `../KiCAD/lib/external/ymknlibs/Various/ymknlib_Various.pretty/`、ナット公称モデルは同ライブラリの `Various/3dmodels/`。作業リポジトリは `../../ymknlibs`。minimap側はsubmoduleのcommitでライブラリの版を固定する。

ライブラリ整理で変更したのは、基板・回路図のライブラリ識別子、モデルパス、ライブラリ表のみ。配線・部品位置・パッド・ネット・設計ルールは変更していない。旧製造出力・ローカル表示設定・未使用の旧MCUフットプリントはarchiveに保管する。

共通GPIO：ROW0–5＝PA5, PA6, PA7, PB0, PB1, PB2、COL0–5＝PB5, PB4, PB3, PD3, PD1, PA15。COL2ROW、35キー。各版の経路・フットプリントは独立。旧COL0=PA4のChoc基板には共通ファームウェアを使用しない。

旧検査記録は `../archive/PCB/reports/` と `../archive/reports/`。寸法更新後にユーザーがChocのDRCを手修正し、サーマル接続エラーを残す方針だったことが既存記録にある。今回、新しいDRCは実行していないため、過去の件数を現行保存版の再検査結果として扱わない。

ナットのランドは暫定・`board_only`。製造BOMへの統合、実装工程適合、接合強度、全実装部品との干渉は未承認。**`production_ready=false`。**
