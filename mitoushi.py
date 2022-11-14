from language.ryuushi import Kanji


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
    new_table['id'] = tsubu.id
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
        kao_cell['class'] = "kao kanji" if isinstance(tsubu, Kanji) else "kao"

        colspan = 1

    if tsubu.imi:
        imi_row = new_row(new_table, html)
        imi_cell = new_cell(imi_row, html)
        imi_cell.string = tsubu.imi
        imi_cell['class'] = "imi"
        imi_cell['colspan'] = colspan


def insert_bun(tsubu, tag, html):
    table_div = html.new_tag("div")
    table_div['class'] = "bun"
    tag.append(table_div)
    table = html.new_tag("table")
    table_div.append(table)
    bun_row = new_row(table, html)
    bun_cell = new_cell(bun_row, html)
    insert_tsubu(tsubu, bun_cell, html)
