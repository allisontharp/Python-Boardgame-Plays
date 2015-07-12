import json, time, gdata.docs, gdata.gauth, gdata.spreadsheets.client, gdata.docs.service, gdata.spreadsheet.service, gdata.spreadsheet.text_db, re, os, sys
from oauth2client.client import SignedJwtAssertionCredentials
import urlparse
import os, sys


def read_cell(client, key):
        from datetime import datetime
        rows = 0;
        

        sps = client.GetSpreadsheets()

        lf = client.GetListFeed(key, 'od6').entry
        for arow in lf:
            rows += 1
        
        rows += 1
        
        cq = gdata.spreadsheets.client.CellQuery(rows,rows, 1, 1)
        cs = client.GetCells(key,'od6',q=cq)
        cell_ent  = cs.entry[0]
        latest_game = cell_ent.cell.input_value
        latest_game =  datetime.strptime(latest_game,'%m/%d/%Y')
        print latest_game
        return latest_game



def add_scores(username, passwd, doc_name, header, dict, cols):
    [rows, gd_client, spreadsheet_id, worksheet_id] = connect(username, passwd, doc_name)

    for i, header in enumerate(header):
        entry = gd_client.UpdateCell(row=1, col=i+cols, inputValue = header, key=spreadsheet_id, wksht_id = worksheet_id)

    entry = gd_client.InsertRow(dict, spreadsheet_id, worksheet_id)
    if isinstance(entry, gdata.spreadsheet.SpreadsheetsList):
        print "Insert row succeeded."
    else:
        print "Insert row failed."