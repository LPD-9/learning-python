import json

from files_exercises import (
    count_lines,
    file_extension,
    list_python_files,
    organise_by_extension,
    read_csv_totals,
    update_json_counter,
    write_lines,
)


def make_file(path, text=""):
    path.write_text(text, encoding="utf-8")
    return path


class TestFileExtension:
    def test_lowercases(self):
        assert file_extension("Report.PDF") == "pdf"

    def test_only_the_last_extension(self):
        assert file_extension("archive.tar.gz") == "gz"

    def test_no_extension(self):
        assert file_extension("README") == ""

    def test_with_folders(self):
        assert file_extension("docs/guide.md") == "md"


class TestCountLines:
    def test_three_lines(self, tmp_path):
        file = make_file(tmp_path / "a.txt", "one\ntwo\nthree\n")
        assert count_lines(file) == 3

    def test_last_line_without_a_line_ending(self, tmp_path):
        file = make_file(tmp_path / "a.txt", "one\ntwo")
        assert count_lines(file) == 2

    def test_empty_file(self, tmp_path):
        assert count_lines(make_file(tmp_path / "a.txt")) == 0


class TestWriteLines:
    def test_writes_each_line(self, tmp_path):
        file = tmp_path / "out.txt"
        write_lines(file, ["one", "two"])
        assert file.read_text(encoding="utf-8") == "one\ntwo\n"

    def test_returns_the_count(self, tmp_path):
        assert write_lines(tmp_path / "out.txt", ["a", "b", "c"]) == 3

    def test_replaces_old_contents(self, tmp_path):
        file = make_file(tmp_path / "out.txt", "old stuff\n")
        write_lines(file, ["new"])
        assert file.read_text(encoding="utf-8") == "new\n"

    def test_no_lines(self, tmp_path):
        file = tmp_path / "out.txt"
        assert write_lines(file, []) == 0
        assert file.read_text(encoding="utf-8") == ""


class TestListPythonFiles:
    def test_finds_and_sorts(self, tmp_path):
        for name in ["b.py", "a.py", "notes.txt"]:
            make_file(tmp_path / name)
        assert list_python_files(tmp_path) == ["a.py", "b.py"]

    def test_subfolders_are_not_searched(self, tmp_path):
        make_file(tmp_path / "top.py")
        (tmp_path / "sub").mkdir()
        make_file(tmp_path / "sub" / "deep.py")
        assert list_python_files(tmp_path) == ["top.py"]

    def test_none(self, tmp_path):
        assert list_python_files(tmp_path) == []


class TestReadCsvTotals:
    def test_adds_up_each_name(self, tmp_path):
        file = make_file(
            tmp_path / "payments.csv",
            "name,amount\nada,10\nbob,4.5\nada,2.5\n",
        )
        assert read_csv_totals(file) == {"ada": 12.5, "bob": 4.5}

    def test_header_only(self, tmp_path):
        file = make_file(tmp_path / "payments.csv", "name,amount\n")
        assert read_csv_totals(file) == {}

    def test_quoted_name_containing_a_comma(self, tmp_path):
        file = make_file(tmp_path / "payments.csv", 'name,amount\n"Lovelace, Ada",3\n')
        assert read_csv_totals(file) == {"Lovelace, Ada": 3.0}


class TestUpdateJsonCounter:
    def test_creates_the_file(self, tmp_path):
        file = tmp_path / "counts.json"
        assert update_json_counter(file, "visits") == 1
        assert json.loads(file.read_text(encoding="utf-8")) == {"visits": 1}

    def test_counts_up(self, tmp_path):
        file = tmp_path / "counts.json"
        update_json_counter(file, "visits")
        assert update_json_counter(file, "visits") == 2

    def test_other_keys_are_kept(self, tmp_path):
        file = make_file(tmp_path / "counts.json", '{"errors": 7}')
        assert update_json_counter(file, "visits") == 1
        saved = json.loads(file.read_text(encoding="utf-8"))
        assert saved == {"errors": 7, "visits": 1}


class TestOrganiseByExtension:
    def test_moves_files_into_subfolders(self, tmp_path):
        for name in ["a.txt", "b.txt", "photo.JPG", "README"]:
            make_file(tmp_path / name, name)
        organise_by_extension(tmp_path)
        assert (tmp_path / "txt" / "a.txt").read_text(encoding="utf-8") == "a.txt"
        assert (tmp_path / "txt" / "b.txt").exists()
        assert (tmp_path / "jpg" / "photo.JPG").exists()
        assert (tmp_path / "other" / "README").exists()

    def test_nothing_is_left_behind(self, tmp_path):
        for name in ["a.txt", "photo.JPG"]:
            make_file(tmp_path / name)
        organise_by_extension(tmp_path)
        assert sorted(path.name for path in tmp_path.iterdir()) == ["jpg", "txt"]

    def test_returns_counts(self, tmp_path):
        for name in ["a.txt", "b.txt", "photo.JPG", "README"]:
            make_file(tmp_path / name)
        assert organise_by_extension(tmp_path) == {"txt": 2, "jpg": 1, "other": 1}

    def test_existing_subfolders_are_left_alone(self, tmp_path):
        (tmp_path / "archive").mkdir()
        make_file(tmp_path / "archive" / "old.txt")
        make_file(tmp_path / "new.txt")
        assert organise_by_extension(tmp_path) == {"txt": 1}
        assert (tmp_path / "archive" / "old.txt").exists()

    def test_empty_folder(self, tmp_path):
        assert organise_by_extension(tmp_path) == {}
