import csv
import io

from textual.app import App, ComposeResult
from textual.widgets import DataTable, Static, Header, Footer

CSV = """コマンド,説明
CMD-D,タブを左に分割
CMD-Shift-D,ダブを下に分割
CMD-W,タブを閉じる
CMD-R,コマンドを検索
CMD-P,コマンドパレットを表示
"""


class Dashboard(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Warp Cheat Sheet")
        yield DataTable()
        yield Footer()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        rows = csv.reader(io.StringIO(CSV))
        table.add_columns(*next(rows))
        table.add_rows(rows)


if __name__ == "__main__":
    app = Dashboard()
    app.run()
