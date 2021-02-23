import hashlib
import click


@click.command()
@click.argument("filename",type=click.File("rb"))
@click.option("--algorithm", default="md5", show_default=True,
type=click.Choice(['MD5', 'SHA1', 'SHA256'], case_sensitive=False),
help="Hashing algorithm to use")
def get_hash(filename, algorithm):
    """Returns the hash of FILENAME."""
    if algorithm.upper() == 'MD%':
        hashing = hashlib.md5()
    elif algorithm.upper() == 'SHA1':
        hashing = hashlib.sha1()
    elif algorithm.upper() == 'SHA256':
        hashing = hashlib.sha256()
    else:
        return

    file_hash = hashing

    while True:
        while chunk := filename.read(1048576):
            file_hash.update(chunk)
        if not chunk:
            break
    click.echo(file_hash.hexdigest())

if __name__ == '__main__':
    get_hash()
