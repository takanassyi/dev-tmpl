# Atomic Design 参考資料

- [Atomic Design について調べてみた](https://qiita.com/yoshimo123/items/302fb3f1698a8db3cf23)

## ディレクトリ構成例

```
├── public // コンパイル済み各公開ファイル
│   └── assets
│   └── index.html
└── src
    ├── components // Reduxに依存しないReactのコンポーネントディレクトリ
    │   ├── atoms
    │   └── molecules
    ├── containers // Reduxとコネクトするコンポーネント
    │   ├── organisms
    │   └── pages
    ├── redux // ReduxのAction,Reducer,Storeを扱うディレクトリ
    │   ├── middlewares // 主にAPI処理をまとめたディレクトリ（ReduxでいうとAction発行時にReducerの前でインターセプトする処理）
    │   ├── modules
    │   └── records
    ├── styles // 基本的なスタイルを定義する
    │   ├── core
    │   ├── foundation
    │   └── utility
    └── utils // 汎用的な処理をするUtil用ディレクトリ
```

## 各ディレクトリの説明

Atomic Designとは、以下の5つの構造にページを分け、それぞれの役割を明確にし再利用可能なコンポーネントを作って行くことです。

### Atoms

Atoms(原子)とは、UIを構築する最小単位です。なのでそれ以上に細かく分割することはできません。


- テキストフォーム
- 追加ボタン
- チェックボックス
- テキスト
- チェックボックス
- テキスト
のように分けることができます。

Atomsは、Atomic DesignかつWebサイトを構築する上で基本的なものであり重要な要素です。

### Molecules

Molecules(分子)になると,UIがどんな意味を持ちどのように使われるかが具体性が出てきます。

先ほどのAtoms単体だけを見ると、何をしたらいいかがわかりませんよね？しかしMoleculesになると入力フォームがありボタンがあるので、「何か入力して送信するんだなー」とより具体的なインターフェイスになることがわかります。

Atomsを組み合わせて複雑なMoleculesになってしまうと、他の箇所で注意が必要。

### Organisms

Organisms(有機体)はAtomsやMoleculesが組み合わされて利用されます。AtomsやMoleculesとの大きな違いは再利用性があまり求められてないと言う点です。

Organismsの代表として ヘッダーが挙げられます。

### Templates

Templates(テンプレート)はワイヤフレームと同じで、ページに画像や実際のデータが反映される前の状態です。

### Pages

Pages(ページ)は、Templatesに対してページに画像や実際のデータを反映させたものです。
