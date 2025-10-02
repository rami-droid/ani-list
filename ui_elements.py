from rich import table
from rich.table import Table


def create_base_table(style: str):
    table = Table(show_header=True, header_style=style)
    table.add_column("Title")
    table.add_column("rating")
    table.add_column("genres")
    return table


def create_genre_table(style: str):
    table = Table(show_header=True, header_style=style)
    table.add_column("Genre Name")
    table.add_column("", width=12)
    table.add_column("anime with genre")
    return table


def create_details_table(style: str):
    table = Table(show_header=True, header_style=style)
    return


def create_schedule_table(style: str, day: str):
    table = Table(show_header=True, header_style=style)
    table.add_column(day)
    table.add_column("rating")
    table.add_column("genres")
    return table
