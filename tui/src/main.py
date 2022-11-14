import csv
import io
import os
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import DataTable, Static, Header, Footer

USERDATA_DIR = os.path.join(
    Path(__file__).resolve().parents[1],
    "userdata"
)

class Dashboard(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Warp Cheat Sheet")
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        with open(os.path.join(USERDATA_DIR, "warp-command.csv"), encoding="utf8") as f:
            rows = csv.reader(io.StringIO(f.read()))
            table.add_columns(*next(rows))
            table.add_rows(rows)


if __name__ == "__main__":
    app = Dashboard()
    app.run()
