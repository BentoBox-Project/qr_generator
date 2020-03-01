import click
import util


@click.command()
@click.option('--email', prompt='Email', help='The email for the QR code')
@click.option('--name', prompt='Name', help='The name for the QR code')
def single_qr(email, name):
    """Simple program that greets NAME for a total of COUNT times."""
    image = util.get_qr_from_single_json({
        "name": name,
        "email": email
    })

    print(type(image))

    click.echo('QR Generated for %s!' % name)


@click.command()
@click.option('--file', default=None,
              help='a CSV file containing the information of '
                   'multiple people that would be stored on QR codes')
def multiple_qr(file_name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('%s Loaded!' % file_name)


if __name__ == '__main__':
    single_qr()
