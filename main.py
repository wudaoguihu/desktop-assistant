from tasks.file_organizer import FileOrganizerTask

if __name__ == "__main__":
    # 注意：这里指向我们刚刚新建的 test_downloads 文件夹
    task = FileOrganizerTask(target_dir="./test_downloads", dry_run=True)
    print(f"正在执行任务：{task.name}")
    result = task.run({})
    print(result)