from rich.table import Table


def create_base_table(style: str):
    table = Table(show_header=True, header_style=style)
    table.add_column("Title")
    table.add_column("rating")
    table.add_column("genres")
    return table


def create_details_table(style: str):
    table = Table(show_header=True, header_style=style)
    return
