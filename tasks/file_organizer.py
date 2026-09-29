from pathlib import Path
import shutil
from core.task import Task

class FileOrganizerTask(Task):
    name = "文件整理"

    def __init__(self, target_dir: str, dry_run: bool = True):
        self.target_dir = Path(target_dir)
        self.dry_run = dry_run

    def run(self, context):
        rules = {
            "图片": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
            "文档": [".pdf", ".docx", ".txt", ".md", ".xlsx"],
            "视频": [".mp4", ".mov", ".avi"],
            "音频": [".mp3", ".wav"],
            "压缩包": [".zip", ".rar", ".7z"],
        }
        moved = []
        if not self.target_dir.exists():
            return "文件夹不存在！"
            
        for file in self.target_dir.iterdir():
            if not file.is_file():
                continue
            for folder, exts in rules.items():
                if file.suffix.lower() in exts:
                    dest_dir = self.target_dir / folder
                    dest = dest_dir / file.name
                    if self.dry_run:
                        moved.append(f"[模拟] {file.name} -> {folder}/")
                    else:
                        dest_dir.mkdir(exist_ok=True)
                        shutil.move(str(file), str(dest))
                        moved.append(f"{file.name} -> {folder}/")
                    break
        return "\n".join(moved) if moved else "没有需要整理的文件"