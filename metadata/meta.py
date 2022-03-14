class WsolManage:
    key = {
        "desc"
    }
    meta = {
        "bbg": {
            "meta": {
                "desc": "bloomberg daily data. updated from bloomberg computer every 8:00 AM",
                "freq": "1day",
                "wblanks": True,
            },
            "columns": {
                "date": "VARCHAR(20) NOT NULL",
                "stk_no": "VARCHAR(6) NOT NULL",
                "bbg_no": "VARCHAR(20)",
                "typ": "VARCHAR(20) NOT NULL",
                "val": "FLOAT"
            },
            "keys": [
                "date",
                "stk_no",
                "typ,"
            ],
        },
        "bbgind": {
            "meta": {
                "desc": "bloomberg daily data. updated from bloomberg computer. for monthly report purpose.",
                "freq": "1day",
                "wblanks": True
            },
            "columns": {
                "date": "VARCHAR(20) NOT NULL",
                "ind_name": "VARCHAR(30)",
                "ind_bbg": "VARCHAR(30) NOT NULL",
                "typ": "VARCHAR(20)",
                "value": "FLOAT"
            },
            "keys": [
                "date",
                "ind_bbg"
            ]
        },
        "corpinfo": {
            "meta": {
                "desc": "DART cross sectional data. Updated from DART Open API on demand",
                "freq": None,
                "wblanks": False,
            },
            "columns": {
                "company": "NVARCHAR(100) NOT NULL",
                "reg_no": "VARCHAR(20)",
                "corp_no": "VARCHAR(20)",
                "krx_no": "VARCHAR(20)",
                "stk_no": "VARCHAR(20)",
            },
            "keys": [
                "company"
            ]
        },
        "dartinfo": {
            "meta": {
                "desc": "DART cross sectional data. Updated from DART Open API. Provides connection between dart_code and stk_code",
                "freq": None,
                "wblanks": False,
            },
            "columns": {
                "corp_name": "VARCHAR(100)",
                "dart_code": "VARCHAR(8)",
                "stk_code": "VARCHAR(6) NOT NULL",
                "modified": "VARCHAR(8)",
            },
            "keys": [
                "stk_code"
            ]
        },
        "dateinfo": {
            "meta": {
                "desc": "Record 1st stock market open date, ksat date, and option maturity dates for backtesting purposes",
                "freq": "1day",
                "wblanks": False,
            },
            "columns": {
                "code": "INT NOT NULL",
                "typ": "VARCHAR(20)",
                "date": "VARCHAR(20)",
            },
            "keys": [
                "code"
            ]
        },
        "indcomp": {
            "meta": {
                "desc": "records the composition of a certain index.",
                "freq": "1month",
                "wblanks": False
            },
            "columns": {
                "year": "INT NOT NULL",
                "chg_no": "INT NOT NULL",
                "code": "INT NOT NULL",
                "stk_no": "VARCHAR(6)",
                "ind_": "VARCHAR(20) NOT NULL",
            },
            "keys": [
                "year",
                "chg_no",
                "code",
                "ind_"
            ]
        },
        "sig": {
            "meta": {
                "desc": "signal developed by wooriam quant team. calculate data from RAWborrow",
                "freq": "1day",
                "wblanks": False
            },
            "columns": {
                "date": "VARCHAR(20) NOT NULL",
                "sigstren": "BIGINT",
                "sig": "VARCHAR(20)",
                "stk": "VARCHAR(6)",
                "sigtyp": "VARCHAR(20)",
            },
            "keys": [
                "date",
                "stk",
                "sigtyp"
            ]
        },
        "bbg_gics": {
            "meta": {
                "desc": "get classification from bloomberg",
                "freq": None,
                "wblanks": False
            },
            "columns": {
                "stk_no": "VARCHAR(6) NOT NULL",
                "cls": "VARCHAR(100) NOT NULL",
                "standard": "VARCHAR(100) NOT NULL"
            },
            "keys": [
                "stk_no",
                "cls",
                "standard",
            ]
        },
    }

    raw_meta = {
        "RAWborrow": {
            "meta": {
                "desc": "records raw data of how many stocks are being borrowed. 100 types of stocks. gain from Check Data KOSCOM",
                "freq": '1day',
                "wblanks": False
            },
            "columns": {
                "date": "VARCHAR(8) NOT NULL",
                "borrow": "BIGINT",
                "d_borrow": "BIGINT",
                "r_borrow": "float",
                "stkcode": "VARCHAR(6) NOT NULL"
            },
            "keys": [
                "date",
                "stkcode"
            ]
        },
        "RAWobase": {
            # TBD
        },
        "RAWoprce": {
            # TBD
        },
    }

