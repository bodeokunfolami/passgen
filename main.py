import click
import clipboard

from password_generator import PasswordGenerator


@click.command()
@click.option('-l', '--length', default=8, help="Length of password")
@click.option('-n/-nn', '--numbers/--no-numbers', default=True, help='Add or remove numbers from your passowrd')
@click.option('-sm/-nsm', '--symbols/--no-symbols', default=True, help="Add or remove symbols from your password")
@click.option('-s/-ns', '--save/--no-save', default=False, help="Save password to text file")
def main(length, numbers, symbols, save):
    passgen = PasswordGenerator(length, numbers, symbols, save)
    password = passgen.create_password()

    # Copies password to clipboard
    clipboard.copy(password)

    click.echo(f"{click.style('Password:',  fg='blue')} {password}")
    click.secho("Password copied to clipboard", fg='yellow')

    if save:
        click.secho("Password saved to password.txt", fg="green")
        passgen.save_password(password)

if __name__ == '__main__':
    main()