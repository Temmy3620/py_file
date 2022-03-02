# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk

# rootメインウィンドウの設定
root = tk.Tk()
root.title("news App")
root.geometry("300x300")

# Notebookウィジェットの作成
notebook = ttk.Notebook(root)

# ボタンの作成
btn = tk.Button(root, text='ボタン') # ボタンの設定(text=ボタンに表示するテキスト)
btn.place(x=250, y=5) #ボタンを配置する位置の設定

# タブの作成
tab_one = tk.Frame(notebook, bg='white')
tab_two = tk.Frame(notebook, bg='white')
tab_three = tk.Frame(notebook, bg='white')

# notebookにタブを追加
notebook.add(tab_one, text="today", underline=0)
notebook.add(tab_two, text="IT")
notebook.add(tab_three, text="world")

# tab_oneに配置するウィジェットの作成
label = ttk.Label(tab_one, text="今日のニュース", background='white')
# ウィジェットの配置
notebook.pack(expand=True, fill='both', padx=10, pady=10)
label.pack()

# tab_oneに配置するウィジェットの作成
label_it = ttk.Label(tab_two, text="今日のITニュース", background='white')
# ウィジェットの配置
notebook.pack(expand=True, fill='both', padx=10, pady=10)
label_it.pack()

# tab_oneに配置するウィジェットの作成
label_world = ttk.Label(tab_three, text="今日の国際ニュース", background='white')
# ウィジェットの配置
notebook.pack(expand=True, fill='both', padx=10, pady=10)
label_world.pack()

root.mainloop()