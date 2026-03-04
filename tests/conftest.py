import os
import tarfile

from pytest import fixture


def untar(abspath: str, target_dir: str):
    with tarfile.open(abspath, "r:gz") as f:
        f.extractall(target_dir)

    return target_dir


@fixture(scope="function")
def extract_data(tmp_path):
    target_dir = tmp_path / "data"
    target_dir.mkdir()
    data_abspath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

    def get_tar(path: str):
        save_dir = untar(os.path.join(data_abspath, f"{path}.tar.gz"), target_dir)
        return os.path.join(save_dir, path)

    yield get_tar
