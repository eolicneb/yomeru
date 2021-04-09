def new_cell(row, html):
    cell = html.new_tag('td')
    row.append(cell)
    return cell


def new_row(table, html):
    row = html.new_tag('tr')
    table.append(row)
    return row


def insert_tsubu(tsubu, cell, html):
    new_table = html.new_tag('table')
    new_table['imi'] = tsubu.imi
    cell.append(new_table)

    if hasattr(tsubu, '_uchiryuu'):
        row = new_row(new_table, html)
        for shi in tsubu._uchiryuu:
            insert_tsubu(shi, new_cell(row, html), html)

        colspan = len(tsubu._uchiryuu)

    else:
        onsei_row = new_row(new_table, html)
        on_cell = new_cell(onsei_row, html)
        on_cell.string = tsubu.onsei if tsubu.onsei else ""
        on_cell['class'] = "onsei"

        kao_row = new_row(new_table, html)
        kao_cell = new_cell(kao_row, html)
        kao_cell.string = tsubu.kao
        kao_cell['class'] = "kao"

        colspan = 1

    if tsubu.imi:
        imi_row = new_row(new_table, html)
        imi_cell = new_cell(imi_row, html)
        imi_cell.string = tsubu.imi
        imi_cell['class'] = "imi"
        imi_cell['colspan'] = colspan