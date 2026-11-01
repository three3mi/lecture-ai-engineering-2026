# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
- 自分で学習を実行したか（`executed_training_myself`）：はい / いいえ（実行できた範囲：　）
- 学習前：`format_rate` =　 / `content_rate` =　
- 学習後：`format_rate` =　 / `content_rate` =　
- 退行した質問：
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：
- 学習で変わったこと・変わらなかったこと：

## 宿題

- 取り組んだレベル：基礎 
- 変えた設定やデータ："lora_r": 80,
- 結果（比較表や数字）：
  修正前"before": {"seconds": 23.3}
  修正後"before": {"seconds": 22.2}
  修正前  "after": {
    "label": "after",
    "n": 21,
    "format_rate": 1.0,
    "content_rate": 0.9047619047619048,
    "both_rate": 0.9047619047619048,
    "seconds": 45.0
  },
  修正後　 "after": {
    "label": "after",
    "n": 21,
    "format_rate": 1.0,
    "content_rate": 0.8571428571428571,
    "both_rate": 0.8571428571428571,
    "seconds": 57.2
  },


- ファインチューニングが向く場面・向かない場面についての考察：
"lora_r": 80　修正前の5倍にしてみました。
出力結果は1件差異があり、処理時間が増えました。
したがって、この21件の評価では、修正によって形式は維持された一方、内容の正答率が下がり、処理も遅くなったようです。ただし、差は正解1件分でした
afterjsonで以下のような結果になり
content_rate：0.9048 → 0.8571
both_rate：0.9048 → 0.8571
の結果の通り正解数が減っています
修正前
    {
      "question": "PDF 以外でも出せますか",
      "raw": "{\"answer\": \"提出形式は PDF 1 ファイルで、ファイル名は 学籍番号_課題番号.pdf です。\", \"needs_review\": false}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": true,
      "both_ok": true,
      "gold_needs_review": false
    },
修正後
    {
      "question": "PDF 以外でも出せますか",
      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",
      "format_ok": true,
      "format_reason": "",
      "content_ok": false,
      "both_ok": false,
      "gold_needs_review": false
    },
