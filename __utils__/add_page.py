import os
import re
import pathlib
import shutil


class AddPage:
    def __init__(self, text_dir: str, base_page_path: str):
        assert os.path.isdir(text_dir), f"'{text_dir}' not valid path."
        assert os.path.isfile(base_page_path), \
            f"'{base_page_path}' not valid path."
        self.root = text_dir
        self.page_path = base_page_path

    @staticmethod
    def get_last_page(root_dir):
        last_page = 0
        for (dirpath, dirs, files) in os.walk(root_dir):
            for filename in files:
                match = re.match(r"^p(\d+)\.py$", filename)
                if not match:
                    continue
                this_page = int(match.group(1))
                last_page = max(last_page, this_page)
        return last_page

    def add_base_page(self, page_name: str):
        src = self.page_path
        dst = pathlib.Path(self.root) / page_name
        shutil.copy(src, dst)

    def add_next_page(self):
        last_page = self.get_last_page(self.root)
        new_page_file = f"p{last_page+1}.py"
        self.add_base_page(new_page_file)


if __name__ == "__main__":
    root = pathlib.Path(os.getcwd()).parent
    text_path = root / "text"
    base_page_path = root / "__utils__" / "base_page_model.utils"
    AddPage(str(text_path), str(base_page_path)).add_next_page()
