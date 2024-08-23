from textual import on
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Button
from textual_slider import Slider


class CustomApp(App):
    CSS = """
    Screen {
        align: center middle;
        layout: horizontal;
    }

    Container {
        width: 33%;
        align: center middle;
    }

    #sliders {
        layout: vertical;
        align: center middle;
    }

    #latch-buttons {
        layout: vertical;
    }

    #momentary-buttons {
        layout: vertical;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        # Sliders Container
        with Container(id="sliders"):
            for i in range(6):
                yield Slider(min=-1, max=1, step=0.1, id=f"slider-{i+1}")

        # Latch Buttons Container
        with Container(id="latch-buttons"):
            for i in range(6):
                yield Button(f"Latch {i+1}", id=f"latch-button-{i+1}")

        # Momentary Buttons Container
        with Container(id="momentary-buttons"):
            for i in range(6):
                yield Button(f"Momentary {i+1}", id=f"momentary-button-{i+1}")

    @on(Slider.Changed)
    def on_slider_change(self, event: Slider.Changed) -> None:
        slider_id = event.slider.id
        value = event.value
        self.log(f"{slider_id} changed to {value:.1f}")

    @on(Button.Pressed)
    def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if "latch" in button_id:
            self.log(f"{button_id} latched")
        elif "momentary" in button_id:
            self.log(f"{button_id} momentarily pressed")


if __name__ == "__main__":
    app = CustomApp()
    app.run()
