# minimap ファームウェアの所在

ファームウェア本体はWSL2 Ubuntu側で旧名 `gs2` のまま管理している。今回のminimapへの改名対象はこの設計リポジトリであり、WSL側のディレクトリ・パッケージ名・成果物は変更していない。このディレクトリには所在案内のみを置き、ソースや成果物を複製していない。

- WSL：`/home/ymkn/rmk-projects/gs2`
- Windows：`\\wsl.localhost\Ubuntu\home\ymkn\rmk-projects\gs2`
- RMK 0.9.0、35キー・1レイヤー、Vial対応。
- 既存成果物：同プロジェクトの `dist/gs2.elf`、`dist/gs2.hex`、`dist/gs2.bin`。

設定・ビルド・書き込みの注意はファームウェア本体の `README.md` を参照。今回、本体や成果物のコピー・移動・変更は行っていない。

MXを正本としてChocもCOL0=PB5へ揃えた共通GPIO版を使用する。**旧COL0=PA4のChoc基板には共通ファームウェアを使用しない。** 物理Escを押しながらUSB接続してROM DFUへ入る操作には、対応ファームウェアの初回書き込みが必要。実機書き込み・DFU列挙・動作確認は未実施。
