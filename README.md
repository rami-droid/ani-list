# ani-list

a CLI tool to help you find anime to watch, intended for use with one of the many
anime cli watching programs.
Since my thing is basically just 2 python files you can download [api.py](https://github.com/rami-droid/ani-list/blob/main/api.py)
if you wanna use my jinkan api
implementation. Only requirement is the requests python package.

## Commands

- `search`
  - lets you search by text for an anime.
- `details`
  - lets you see the details of an anime. Search by either myanimelist ID, or name.
- `top`
  - retrieves the top anime, optionally include  `--airing` to see the top currently airing.

## TODO


- persistence
  - create SQLite db stuff
  - add episode tracking 

- frontend
  - maybe rewrite frontend for textual or smt idk

- watching anime
  - possibly integrating with ani-cli or another cli anime watcher

## stuff I used

- jinkan api
- rich, and Typer and readchar
