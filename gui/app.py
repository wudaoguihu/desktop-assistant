import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
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

        # 2. 执行任务区域（模拟 + 真实整理）
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)
        # 模拟运行按钮（蓝色文字，安全）
        tk.Button(btn_frame, text="模拟运行 (Dry Run)", command=lambda: self.run_task(dry_run=True)).pack(side=tk.LEFT, padx=10)
        # 真实整理按钮（红色文字，警告）
        tk.Button(btn_frame, text="真实整理", command=lambda: self.run_task(dry_run=False), fg="red").pack(side=tk.LEFT, padx=10)

        # 3. 日志显示区域
        tk.Label(root, text="运行日志:").pack(pady=5)
        self.log = scrolledtext.ScrolledText(root, width=60, height=15)
        self.log.pack(pady=5)

    def choose_folder(self):
        """打开文件夹选择对话框"""
        path = filedialog.askdirectory()
        if path:
            self.path_var.set(path)

    def run_task(self, dry_run=True):
        """运行文件整理任务，根据 dry_run 参数决定是模拟还是真实移动"""
        target_dir = self.path_var.get()
        if not target_dir:
            self.log.insert(tk.END, "⚠️ 请先选择文件夹！\n")
            return

        # 如果是真实整理，弹出警告窗口让用户二次确认
        if not dry_run:
            confirm = messagebox.askyesno(
                "安全警告", 
                f"你确定要真实整理文件夹吗？\n\n路径：{target_dir}\n\n此操作会真实移动文件，无法撤销！"
            )
            if not confirm:
                self.log.insert(tk.END, "🚫 已取消真实整理操作。\n")
                return

        task = FileOrganizerTask(target_dir=target_dir, dry_run=dry_run)
        mode = "模拟" if dry_run else "真实"
        self.log.insert(tk.END, f"正在执行任务：{task.name} ({mode})\n")
        
        result = task.run({})
        self.log.insert(tk.END, result + "\n\n")
        self.log.see(tk.END) # 自动滚动到底部

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()