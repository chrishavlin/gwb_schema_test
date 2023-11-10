from yt_napari._gui_utilities import translator
from magicgui import type_map, widgets

from gwb_schema_test.wb_pydantic import Model

if __name__ == "__main__":
    data_container = widgets.Container()
    translator.add_pydantic_to_container(
        Model,
        data_container,
        ignore_attrs=['__root__']
    )
    data_container.show(run=True)

