# KiCad設計

各基板・プレートを独立したプロジェクトディレクトリに置く。

| ディレクトリ | 対象 |
| --- | --- |
| `PCB/` | 現行114.5mm角Choc V2基板・回路図 |
| `PCB_GLP/` | 126.25×114.5mmのMX/GLP3基板・回路図 |
| `SwitchPlate/` | 現行114.5mm角Choc V2プレート |
| `SwitchPlate_GLP/` | 126.25×114.5mmのGLP3プレート |
| `lib/external/` | 共通のymknlibsと非フリーロゴのGit submodule |

設計の寸法・制約は [../doc/pcb.md](../doc/pcb.md) と [../doc/plates.md](../doc/plates.md)。SWD三穴と暫定M2ナットは `ymknlib_Various` に共通化し、旧プロジェクト専用ライブラリと未使用MCUはarchiveへ退避した。外部ライブラリはsubmoduleのcommitで版を固定し、自動更新しない。ライセンスは各ライブラリに同梱されたLICENSE・通知を参照。

**製造未承認。** この配置変更では新規DRC・Gerber生成を行っていない。
