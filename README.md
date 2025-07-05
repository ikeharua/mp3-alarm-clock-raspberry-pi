# ⏰ MP3アラーム時計 for Raspberry Pi Pico W 🎵

このプロジェクトは、Raspberry Pi Pico W を使った**音楽付き目覚まし時計**です。
Wi-Fi接続によるNTP時刻同期、温度表示、MP3再生機能を搭載しています。

---

## 🔧 主な機能

- ⏰ アラーム機能（指定時刻にMP3を再生）
- 🌡️ 内蔵温度センサーによる気温表示（ADC）
- 🖥️ OLEDディスプレイ（SSD1306）による情報表示
- 🎵 DFPlayer Mini によるMP3再生
- 🔘 ボタン操作による制御

---

## 🛠️ 使用部品

| 部品名 | 用途 |
|--------|------|
| Raspberry Pi Pico W | 本体マイコン |
| OLEDディスプレイ（SSD1306） | 時刻・温度・状態表示 |
| DFPlayer Mini | MP3再生 |
| スピーカー | 音声出力 |
| ボタン × 4個 | 操作用（再生・停止など） |

---

## 📂 ファイル構成

| ファイル名 | 説明 |
|------------|------|
| `main.py` | 本体コード（自作） |
| `DFPModule.py` | DFPlayer制御クラス（HandsOn+より引用） |
| `ssd1306.py` | OLEDディスプレイドライバ（MITライセンス） |
| `LICENSE` | MITライセンス文書 |

---

## 🙏 参考にした記事・コード

- [HandsOn+ DFPlayer記事](https://www.handsonplus.com/electronic-works/how-to-use-dfplayer-with-raspipico/)
→ `DFPModule.py` はこの記事のコードをそのまま使用しています（著作権は元の作者に帰属）

- [micropython-ssd1306](https://github.com/stlehmann/micropython-ssd1306)（MIT License）
→ `ssd1306.py` はこのリポジトリのコードを使用

---

## 📜 ライセンス

このプロジェクトは **MITライセンス** のもとで公開されています。
一部のコード（`DFPModule.py` など）は出典を明記し、**著作権は元の作者に帰属**します。
詳しくは [`LICENSE`](./LICENSE) ファイルをご覧ください。

---

## ⚠️ 注意事項

- このプロジェクトは**中学生（ikeharua）による学習目的の作品**です。
- 動作確認は行っていますが、**すべての環境での動作を保証するものではありません。**
- 電子工作や配線ミスによる破損・事故などには十分ご注意ください。
- ご使用は**自己責任でお願いいたします。**

---

## ✍️ 作者

**ikeharua（中学生）**
趣味でマイコンを使った作品を開発・公開しています。
GitHubでの公開は初めてですが、誠実にライセンスと出典を守って活動していくつもりです。
