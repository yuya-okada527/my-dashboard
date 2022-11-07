from dataclasses import dataclass

from textual.app import App, ComposeResult, RenderResult
from textual.widgets import Static, Header, Footer


COMMANDS = [
    ("CMD-D", "タブを分割"),
    ("CMD-W", "タブを閉じる"),
    ("CMD-R", "コマンドを検索"),
    ("CMD-P", "コマンドパレットを表示")
]


@dataclass
class Command:
    name: str
    description: str


class CommandWidget(Static):

    def __init__(self, name: str, description: str) -> None:
        super().__init__()
        self.command = Command(name=name, description=description)

    def render(self) -> RenderResult:
        return f"{self.command.name}: {self.command.description}"


class Dashboard(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Warp Cheat Sheet")
        for name, description in COMMANDS:
            yield CommandWidget(name=name, description=description)
        yield Footer()


if __name__ == "__main__":
    app = Dashboard()
    app.run()
