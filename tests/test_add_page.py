import pytest
import os
import sys
import pathlib

import __utils__.add_page


@pytest.fixture
def root_mode_path() -> pathlib.Path:
    this_dir = __package__
    root_path = pathlib.Path(sys
                             .modules[this_dir.split(".")[0]]
                             .__file__)
    return root_path


@pytest.fixture
def text_path(root_mode_path) -> pathlib.Path:
    text_path_ = root_mode_path.parent / "text"
    assert os.path.exists(str(text_path_))
    return text_path_


@pytest.fixture
def page_path(root_mode_path) -> pathlib.Path:
    page_path_ = (root_mode_path.parent / "__utils__"
                 / "base_page_model.utils")
    assert os.path.exists(str(page_path_))
    return page_path_


def test_last_page(text_path, page_path):
    adder = __utils__.add_page.AddPage(str(text_path), str(page_path))
    last_page = adder.get_last_page()
    assert isinstance(last_page, int)
    assert last_page > 0
