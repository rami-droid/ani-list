from typing import Annotated

# from requests import head
# from rich import print

from requests import head
from rich.console import Console
from rich.table import Table
import typer
import api as api

# importing custom ui elements
from ui_elements import create_base_table

# setups for typer and console
app = typer.Typer()

console = Console()


@app.command()
def search(query: str, amnt: int = 1):
    table = create_base_table("bold purple")
    genres = []
    try:
        data = api.search_anime(query)["data"]
        for anime in data[:amnt]:
            for genre in anime["genres"]:
                genres.append(genre["name"])
            table.add_row(anime["title"], str(anime["score"]), ", ".join(genres))
        console.print(table)

    except api.ApiError as err:
        console.print(f"[bold]Error {err.status}[/]: {err.message}")


@app.command()
def details(query: str = "", id: int = 0):
    try:
        if id == 0:
            data = api.search_anime(query)["data"]
            full_anime = data[0]
            # full_anime = api.search_anime_full(anime_id)
            table = Table(show_footer=True, header_style="bold red italic")
            # table.add_row("[bold]FULL INFO[/]")
            table.add_column("Title")
            table.add_column("Synopsis")
            table.add_column("background")
            table.add_row(
                full_anime["title"], full_anime["synopsis"], full_anime["background"]
            )
            console.print(table)
        else:
            full_anime = api.search_anime_full(str(id))["data"]
            table = Table(show_footer=True, header_style="bold red italic")
            # table.add_row("[bold]FULL INFO[/]")
            table.add_column("Title")
            table.add_column("Synopsis")
            table.add_column("background")
            table.add_row(
                full_anime["title"], full_anime["synopsis"], full_anime["background"]
            )
            console.print(table)
    except api.ApiError as err:
        console.print(f"[bold]Error {err.status}[/]: {err.message}")


@app.command()
def top_airing(
    nsfw: Annotated[
        bool, typer.Option(help="disable the flag that hides nsfw results")
    ] = False,
    amount: Annotated[
        int, typer.Option(help="amount of results you want (max 25)")
    ] = 5,
):
    "retrieves most popular anime currently airing"
    try:
        data = api.get_airing(nsfw)["data"]
        table = create_base_table()

        for anime in data[:amount]:
            genres = []
            for genre in anime["genres"]:
                genres.append(genre["name"])
            table.add_row(anime["title"], str(anime["score"]), ", ".join(genres))
        console.print(table)
    except api.ApiError as err:
        console.print(f"[bold]Error {err.status}[/]: {err.message}")


if __name__ == "__main__":
    app()
