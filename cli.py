from requests import head
from rich import print
from rich.console import Console
from rich.table import Table
import typer
import api as api

# setups for typer and console
app = typer.Typer()

console = Console()


@app.command()
def search(query: str, amnt: int = 1):
    data = api.search_anime(query)["data"]
    table = Table(show_header=True, header_style="bold purple")
    table.add_column("Title")
    table.add_column("rating")
    table.add_column("genres")

    for anime in data[:amnt]:
        table.add_row(anime["title"], str(anime["score"]), "temp")
    console.print(table)


@app.command()
def top_airing():
    api.get_airing()


def main():
    pass


if __name__ == "__main__":
    app()
