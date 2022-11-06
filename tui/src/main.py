from textual.app import App, ComposeResult, RenderResult
from textual.widget import Widget


class CommandWidget(Widget):

    def render(self) -> RenderResult:
        return "CMD-D: Split Split Pane Right"


class Dashboard(App):

    def compose(self) -> ComposeResult:
        yield CommandWidget()


if __name__ == "__main__":
    app = Dashboard()
    app.run()
