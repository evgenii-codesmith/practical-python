class TableFormatter():

    def heading(self, headers):
        """
        Emit the table headings
        """
        pass

    def row(self, rowdata):
        """
        Emit a single row of table data
        """
        pass


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain text format
    """

    def heading(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format
    """

    def heading(self, headers):
        print('<tr><th>Name</th><th>Shares</th><th>Price</th><th>Change</th></tr>')

    def row(self, rowdata):
        print(
            f'<tr><td>{rowdata[0]}</td><td>{rowdata[1]}</td><td>{rowdata[2]}</td><td>{rowdata[3]}</td></tr>')
