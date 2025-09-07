# Python チートシート

## 📝 文字列操作

### 基本操作
```python
# 文字列分割（任意の空白文字で分割、連続する空白も処理）
s = "  hello   world  "
words = s.split()  # ['hello', 'world']

# 特定文字で分割
s = "a,b,c"
parts = s.split(',')  # ['a', 'b', 'c']

# リストを文字列に結合
words = ['hello', 'world']
result = ' '.join(words)  # "hello world"
result = ''.join(['a', 'b', 'c'])  # "abc"

# 文字列をリストに変換
s = "hello"
chars = list(s)  # ['h', 'e', 'l', 'l', 'o']
```

### 文字判定・変換
```python
# 文字種判定
c.isalpha()    # アルファベット判定
c.isdigit()    # 数字判定
c.isalnum()    # 英数字判定
c.isspace()    # 空白判定

# 大文字小文字変換
s.lower()      # 小文字変換
s.upper()      # 大文字変換

# 母音チェック
vowels = 'aeiouAEIOU'
if char in vowels:
    # 母音の場合の処理
```

### スライシング
```python
s = "hello"
s[0]       # 'h' (最初の文字)
s[-1]      # 'o' (最後の文字)
s[:3]      # 'hel' (最初から3文字)
s[2:]      # 'llo' (2番目から末尾まで)
s[::-1]    # 'olleh' (逆順)
```

## 🔢 リスト・配列操作

### 基本操作
```python
# 要素追加・削除
lst.append(item)        # 末尾に追加
lst.extend(other_list)  # リスト拡張
lst.insert(index, item) # 指定位置に挿入
lst.pop()              # 末尾削除して返す
lst.pop(index)         # 指定位置削除して返す
lst.remove(item)       # 最初の該当要素を削除

# リスト作成
lst = [0] * n          # 長さnで0で初期化
lst = list(range(n))   # [0, 1, 2, ..., n-1]
```

### イテレーション
```python
# インデックス付きループ
for i, value in enumerate(lst):
    print(f"Index {i}: {value}")

# 2つのリストを同時にループ
for a, b in zip(list1, list2):
    print(a, b)

# 逆順ループ
for item in reversed(lst):
    print(item)
```

### ソート・検索
```python
# ソート
lst.sort()              # in-place昇順ソート
sorted_lst = sorted(lst)  # 新しいソート済みリスト
lst.sort(reverse=True)   # 降順ソート

# 二分探索（要ソート済み）
import bisect
index = bisect.bisect_left(sorted_list, target)
```

## 📚 辞書操作

### 基本操作
```python
# 辞書作成・アクセス
d = {}
d[key] = value
value = d.get(key, default_value)  # 安全なアクセス

# 辞書のループ
for key, value in d.items():
    print(key, value)

# キーのみ、値のみ
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
```

### よく使うパターン
```python
# カウンター
count = {}
for item in items:
    count[item] = count.get(item, 0) + 1

# またはCollectionsを使用
from collections import Counter
count = Counter(items)

# 最大値・最小値のキー取得
max_key = max(d, key=d.get)
min_key = min(d, key=d.get)
```

## 🧮 数学・ビット演算

### 数学関数
```python
from math import gcd, sqrt, ceil, floor

# 最大公約数
result = gcd(a, b)

# 切り上げ・切り下げ
ceil(3.2)   # 4
floor(3.8)  # 3
```

### ビット演算
```python
# 基本演算
a ^ b      # XOR（排他的論理和）
a & b      # AND
a | b      # OR
~a         # NOT
a << 1     # 左シフト（2倍）
a >> 1     # 右シフト（1/2）

# よく使うパターン
result = 0
for num in nums:
    result ^= num  # XORで重複を消去

# 最下位ビット確認
if num & 1:  # 奇数判定
    pass
```

## 🔗 LinkedList操作

### 基本構造
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ダミーノード使用
dummy = ListNode(0)
current = dummy

# リンクリストトラバーサル
while current:
    print(current.val)
    current = current.next
```

## 🎯 アルゴリズムパターン

### Two Pointers（双方向ポインタ）
```python
# 配列の両端から中央に向かう
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        # 値を交換
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    elif other_condition:
        left += 1
    else:
        right -= 1
```

### Sliding Window
```python
# 固定サイズのウィンドウ
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(k, len(arr)):
    window_sum += arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)
```

### Dynamic Programming
```python
# 1次元DP
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = dp[i-1] + dp[i-2]  # フィボナッチ型

# 2次元DP
dp = [[0] * (m + 1) for _ in range(n + 1)]
```

## 📊 データ構造

### スタック・キュー
```python
# スタック（リストで実装）
stack = []
stack.append(item)    # プッシュ
item = stack.pop()    # ポップ

# キュー
from collections import deque
queue = deque()
queue.append(item)    # エンキュー
item = queue.popleft() # デキュー
```

### セット
```python
# セット作成・操作
s = set()
s.add(item)
s.remove(item)
s.discard(item)  # エラーを発生させない削除

# セット演算
set1 & set2  # 積集合
set1 | set2  # 和集合
set1 - set2  # 差集合
```

## 💡 よく使うテクニック

### 値の交換
```python
# Pythonic way
a, b = b, a

# リスト内の要素交換
arr[i], arr[j] = arr[j], arr[i]
```

### 条件分岐の短縮
```python
# 三項演算子
result = value1 if condition else value2

# デフォルト値設定
result = value or default_value

# None チェック
if value is not None:
    pass
```

### リスト内包表記
```python
# 基本形
squares = [x**2 for x in range(10)]

# 条件付き
evens = [x for x in range(10) if x % 2 == 0]

# 2次元配列初期化
matrix = [[0] * cols for _ in range(rows)]  # 正しい
# matrix = [[0] * cols] * rows  # NG: 同じリストを参照
```

## 🚀 パフォーマンス Tips

### 時間計算量
- `list.append()`: O(1)
- `list.insert(0, item)`: O(n) - 先頭挿入は遅い
- `list.pop()`: O(1), `list.pop(0)`: O(n)
- `dict[key]`: O(1)
- `key in dict`: O(1)
- `item in list`: O(n)
- `item in set`: O(1)

### メモリ効率
```python
# ジェネレータ使用（大量データの場合）
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# in-place操作を優先
# nums[:] = sorted(nums)  # in-place
# nums = sorted(nums)     # 新しいリスト作成
```

## 🏃‍♂️ コーディング試験での心得

1. **Edge Casesを忘れずに**
   - 空の配列/文字列
   - 単一要素
   - 重複要素
   - 負の数・0

2. **時間・空間計算量を意識**
   - O(1) < O(log n) < O(n) < O(n log n) < O(n²)

3. **デバッグ用print文**
```python
print(f"Debug: {variable}")  # f-string使用
```

4. **型ヒント（可読性向上）**
```python
def func(nums: List[int]) -> int:
    pass
```
