import asyncio
from os import system, waitstatus_to_exitcode
from textual import work
from textual.app import App, ComposeResult
from textual.widgets import Label,Button


class LanguageApp(App[str]):
    
    def compose(self)->ComposeResult:
        yield Label("What is your favorite ide?")
        yield Button("Nano", id="nano")
        yield Button("Vim", id="vi")
        yield Button("Exit", id="exit")
    
    @work
    async def on_button_pressed(self, event: Button.Pressed)->None:
        if event.button.id == "exit":
            self.notify("Thank for use it.", timeout=5)
            await asyncio.sleep(5)
            self.exit(event.button.id)

        with self.suspend():
            raw_status = system(event.button.id)
            exit_code = waitstatus_to_exitcode(raw_status)
        
        if exit_code == 0:
            self.notify(f"Success: {event.button.id} closed normally.")
            
        else:
            self.notify(f"Exit Code: {exit_code}", severity="error")


if __name__ == "__main__":
    app = LanguageApp()
    return_code = app.run()
    print(f"Your favourite ide is: {return_code}")