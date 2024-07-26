from shiny import App, Inputs, ui
from shiny.module import resolve_id
from pathlib import Path
from shiny.render.renderer import Renderer, Jsonifiable
from htmltools import HTMLDependency

cm6_dep = HTMLDependency(
    "cm6.bundle.min",
    "6.0.0",
    source={"subdir": "cm6"},
    script={"src": "SQLeditor.js", "type": "module"},
    all_files=True,
)

def output_sqleditor(id, height="500px"):
    return ui.div(
        cm6_dep,
        # Use resolve_id so that our component will work in a module
        id=resolve_id(id),
        class_="shiny-sql-editor",
        style=f"height: {height}",
    )
    
    


class render_sqleditor(Renderer[str]):
    def auto_output_ui(self):
        return ui.output_sqleditor(self.output_name)


app_ui = ui.page_fluid(
    ui.input_text_area("ta", "SQL Editor", value=''),
    output_sqleditor("editor"),
)


def server(input: Inputs):
    @render_sqleditor
    def sqlEditor():
        return input.ta()


app = App(app_ui, server)








