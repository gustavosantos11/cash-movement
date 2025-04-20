import shutil
from pathlib import Path


def move_to_desktop():
    origin_archive = "Movimento_de_caixa.xlsx"

    current_path = Path.cwd()
    parent_path = current_path.parent

    tables_folder = parent_path / "Tables"
    tables_folder.mkdir(exist_ok=True)

    def get_unique_filename(base_folder, filename):
        file_path = base_folder / filename
        i = 1
        while file_path.exists():
            name = f"Movimento_de_caixa_{i}.xlsx"
            file_path = base_folder / name
            i += 1
        return file_path

    destiny_archive = get_unique_filename(tables_folder, origin_archive)

    shutil.move(origin_archive, destiny_archive)
    print(f"Arquivo movido para: {destiny_archive}")
