import typer

from controller.TerminalController import TerminalController

app: typer.Typer = typer.Typer()
controller: TerminalController = TerminalController()

def save():
    controller.save()

@app.command()
def info():
    """Displays information about the program."""
    controller.info()

@app.command()
def add(date: str, course: str, info: str, progress: int):
    """Adds new element to the list."""
    controller.add(date, course, info, progress)
    save()

@app.command()
def edit(index: int, param: str, value):
    """Edits an existing element in the list."""
    controller.edit(index, param, value)
    save()

@app.command()
def delete(index: int):
    """Deletes an element in the list."""
    controller.delete(index)
    save()

@app.command()
def find(param: str, value):
    """Shows elements with the given parameters."""
    controller.find(param, value)

@app.command()
def list():
    """Shows all of the elements."""
    controller.list()

@app.command()
def settings():
    """Shows all the configurations."""
    controller.settings()

@app.command()
def set(var: str, value):
    """Changes a value in the configurations."""
    controller.set(var, value)
    save()

@app.command()
def sort(param: str):
    """Sorts the list by given parameter."""
    controller.sort(param)
    save()

if (__name__ == "__main__"):
    app()