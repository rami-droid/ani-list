# ani-list

a CLI tool to help you find anime to watch, intended for use with one of the many
anime cli watching programs.
There's also a database to manage the status of your currently watched anime
Since my thing is basically just a few python files you can download [api.py](https://github.com/rami-droid/ani-list/blob/main/api.py)
if you wanna use my jinkan api
implementation. Only requirement is the requests python package.

## Commands

- `search`
  - lets you search by text for an anime.
- `details`
  - lets you see the details of an anime. Search by either myanimeList id, or name.
- `top`
  - retrieves the top anime.
- `genres`
  - retrieves the top genres and lets you add to your database.
- `airing`
  - retrieves the top airing anime.
- `db`
  - manage your database of anime. Delete or edit rows here! You can edit the status of the anime (watching, finished, etc) and change the current episode you're on.

## install/build guide
the package is available on pip, so you can just 
  ```
pip install ani-list
```


## todo


- persistence
  - create sqlite db stuff
  - add episode tracking 

- frontend
  - maybe rewrite frontend for textual or smt idk

- watching anime
  - possibly integrating with ani-cli or another cli anime watcher

## stuff i used

- jinkan api
- rich, and typer and readchar
