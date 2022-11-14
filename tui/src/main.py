import csv
import io
import os
import json
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import DataTable, Static, Header, Footer

USERDATA_DIR = os.path.join(
    Path(__file__).resolve().parents[1],
    "userdata"
)
CONFIG_PATH = os.path.join(USERDATA_DIR, "config.json")

class Dashboard(App):

    def __init__(self, driver_class = None, css_path = None, watch_css: bool = False):
        super().__init__(driver_class, css_path, watch_css)
        self.config = load_config()
        self.first_screen = self.config["screens"][0]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(self.first_screen["name"])
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        with open(os.path.join(USERDATA_DIR, self.first_screen["data-source"]["path"]), encoding="utf8") as f:
            rows = csv.reader(io.StringIO(f.read()))
            table.add_columns(*next(rows))
            table.add_rows(rows)


def load_config():
    with open(CONFIG_PATH, encoding="utf8") as f:
        return json.loads(f.read())


if __name__ == "__main__":
    config = load_config()
    app = Dashboard()
    app.run()
