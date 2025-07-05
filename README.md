# MP3アラーム時計 ⏰🎵

Raspberry Pi Pico W を使った音楽付き目覚まし時計です。
温度表示・NTP時刻同期・MP3再生機能を搭載しています。

## 🔧 機能
- アラーム機能（指定時刻に音楽再生）
- 温度センサーによる気温表示
- OLEDディスプレイ表示
- ボタン操作でMP3再生・一時停止・リピート

## 📂 ファイル構成
- `main.py`：本体コード（自作）
- `DFPModule.py`：DFPlayer制御（HandsOn+より引用）
- `bmp180.py`：温度センサー用（MITライセンス）

## 🙏 参考にした記事
- [HandsOn+ DFPlayer記事](https://www.handsonplus.com/electronic-works/how-to-use-dfplayer-with-raspipico/)

## 📜 ライセンス
このプロジェクトは MIT ライセンスのもとで公開されています。
一部のコードは出典を明記し、著作権は元の作者に帰属します。
