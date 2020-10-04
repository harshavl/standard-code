

import click

def logic(name):
    if name == "harsha":
        return "vardhana"
    else:
        return "No Match"


@click.command()
@click.option("--name")
def harsha(name):
    ''' This is a harsha vardhana function '''
    
    result = logic(name)
    click.echo( click.style('Checking harsha argument', fg='green' ) )
    if result == "vardhana":
        click.echo( click.style(f'{result}', bg='blue', fg='red' ) )
    else:
        click.echo( click.style(f'ATTENTION! Wrong Name: {result}', blink=True, bold=True ) )


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    harsha()


