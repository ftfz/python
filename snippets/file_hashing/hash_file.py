import hashlib
import click


@click.command()
@click.argument("filename",type=click.File("rb"))
@click.option("--hash", default="md5", show_default=True,
type=click.Choice(hashlib.algorithms_guaranteed, case_sensitive=False),
help="Hashing algorithm to use")
def get_hash(filename, hash):
    """Returns the hash of FILENAME."""
    if hash.lower() in hashlib.algorithms_guaranteed:
        file_hash = getattr(hashlib,hash.lower())()
    else:
        return

    while True:
        while chunk := filename.read(8192):
            file_hash.update(chunk)
        if not chunk:
            break
    click.echo(file_hash.hexdigest())

if __name__ == '__main__':
    get_hash()
