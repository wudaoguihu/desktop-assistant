import tkinter as tk
from tkinter import filedialog, scrolledtext
from tasks.file_organizer import FileOrganizerTask

class App:
    def __init__(self, root):
        self.root = root
        root.title("桌面自动化助手")
        self.path_var = tk.StringVar()

        # 1. 选择文件夹区域
        tk.Label(root, text="目标文件夹:").pack(pady=5)
        tk.Entry(root, textvariable=self.path_var, width=50).pack(pady=5)
        tk.Button(root, text="选择文件夹", command=self.choose_folder).pack(pady=5)

        # 2. 执行任务区域
        tk.Button(root, text="运行文件整理 (模拟)", command=self.run_task).pack(pady=5)

        # 3. 日志显示区域
        tk.Label(root, text="运行日志:").pack(pady=5)
        self.log = scrolledtext.ScrolledText(root, width=60, height=15)
        self.log.pack(pady=5)

    def choose_folder(self):
        """打开文件夹选择对话框"""
        path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)

    def run_task(self):
        """运行文件整理任务"""
        target_dir = self.path_var.get()
        if not target_dir:
            self.log.insert(tk.END, "⚠️ 请先选择文件夹！\n")
            return

        # 为了安全，先保持 dry_run=True（模拟运行）
        task = FileOrganizerTask(target_dir=target_dir, dry_run=True)
        self.log.insert(tk.END, f"正在执行任务：{task.name}\n")
        
        # 清空之前的结果
        result = task.run({})
        self.log.insert(tk.END, result + "\n\n")
        self.log.see(tk.END) # 自动滚动到底部

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()