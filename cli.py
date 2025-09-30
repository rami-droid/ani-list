from typing import Annotated
# from rich import print

from requests import head
from rich.console import Console
from rich.table import Table
import typer
import api as api

# importing custom ui elements
from ui_elements import create_base_table
from ui_elements import create_genre_table

# setups for typer and console
app = typer.Typer()

console = Console()


@app.command()
def search(
    query: Annotated[str, typer.Option(help="search query")],
    amnt: Annotated[int, typer.Option(help="amount of anime to show")] = 1,
):
    "Search for an anime by name"
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
    "retrieves the details of an anime"
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
def genres():
    try:
        data = api.get_genres()["data"]
        table = create_genre_table("bold cyan")
        for genre in data[:10]:
            table.add_row(genre["name"], "", str(genre["count"]))
        console.print(table)
    except api.ApiError as err:
        console.print(f"[bold]Error {err.status}[/]: {err.message}")


@app.command()
def top(
    nsfw: Annotated[
        bool, typer.Option(help="disable the flag that hides nsfw results")
    ] = False,
    amount: Annotated[
        int, typer.Option(help="amount of results you want (max 25)")
    ] = 5,
    airing: Annotated[
        bool, typer.Option(help="filter to only currently airing")
    ] = False,
):
    "retrieves most popular anime"
    try:
        data = api.get_top(nsfw, airing)
        table = create_base_table("bold purple")

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
