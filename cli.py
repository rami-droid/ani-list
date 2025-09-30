from typing import Annotated

# from requests import head
# from rich import print

from rich.console import Console
from rich.table import Table
import typer
import api as api

# setups for typer and console
app = typer.Typer()

console = Console()


def create_base_table():
    table = Table(show_header=True, header_style="bold purple")
    table.add_column("Title")
    table.add_column("rating")
    table.add_column("genres")
    return table


@app.command()
def search(query: str, amnt: int = 1):
    data = api.search_anime(query)["data"]
    table = create_base_table()
    genres = []
    for anime in data[:amnt]:
        for genre in anime["genres"]:
            genres.append(genre["name"])
        table.add_row(anime["title"], str(anime["score"]), ", ".join(genres))
    console.print(table)


@app.command()
def details(query: str = "", id: int = 0):
    if id == 0:
        data = api.search_anime(query)["data"]
        anime_id = data[0]["mal_id"]
        full_anime = api.search_anime_full(anime_id)
        console.print(full_anime)
    else:
        full_anime = api.search_anime_full(str(id))
        console.print(full_anime)


@app.command()
def top_airing(
    nsfw: Annotated[
        bool, typer.Option(help="disable the flag that hides nsfw results")
    ] = False,
    amount: Annotated[
        int, typer.Option(help="amount of results you want (max 25)")
    ] = 5,
):
    data = api.get_airing(nsfw)["data"]
    table = create_base_table()

    for anime in data[:amount]:
        genres = []
        for genre in anime["genres"]:
            genres.append(genre["name"])
        table.add_row(anime["title"], str(anime["score"]), ", ".join(genres))
    console.print(table)


def main():
    pass


if __name__ == "__main__":
    app()
