import dataclasses

from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget


COMMANDS = [
    ("CMD-D", "Split Pane Right")
]


@dataclasses.dataclass
class Command:
    name: str
    description: str


class CommandWidget(Widget):

    def __init__(self, name: str, description: str) -> None:
        super().__init__()
        self.command = Command(name=name, description=description)

    def render(self) -> RenderResult:
        return f"{self.command.name}: {self.command.description}"


class Dashboard(App):

    def compose(self) -> ComposeResult:
        for name, description in COMMANDS:
            yield CommandWidget(name=name, description=description)


if __name__ == "__main__":
    app = Dashboard()
    app.run()
