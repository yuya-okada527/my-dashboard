# my-dashboard

自分自身の日々の生活・活動をモニタリングするためのパーソナルダッシュボードツール

## 要求

![要求](docs/images/requirements.png)

## 設計

### 基本方針

- 1st リリースでは、TUI アプリケーションとして実装する

### 起動フロー

```mermaid
flowchart LR
  A["アプリケーション起動"] --> B["設定ファイル読み込み"]
  B --> C["データロード"]
  C --> D["画面表示"]
```

### 設定ファイル形式例

```yml
screens:
  - name: Warp Short Cut
    view-type: table
    data-source:
      type: file
      path: ./data/warp-short-cut.csv
```
