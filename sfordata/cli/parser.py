#!/usr/bin/env python

import click
import stevedore


@click.command()
@click.option('-f', '--format', help='File format')
@click.argument('input', type=click.File())
def main(format, input):
    mgr = stevedore.driver.DriverManager(
        namespace='sfordata.parser',
        name=format,
        invoke_on_load=True,
    )
    click.echo(mgr.driver.parse(input))


if __name__ == '__main__':
    main()
