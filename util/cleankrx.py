import pandas as pd


class KRXClean:
    def __init__(self, file_loc:str, file_name:str, index_name:str):
        # IMMUTABLE CONSTANT
        COLUMN = ['stkcode', 'stkname', 'c_prc', 'wrt', 'updown', 'tv']

        # PROCESS DATE
        y, m = self.clean_date(file_name)

        # IMPORT DATA
        self.data = pd.read_csv(f"{file_loc}{file_name}",
                                encoding='euc-kr')
        self.data.columns = COLUMN

        self.result = self.run(year=y, month=m, index_name=index_name)

    @staticmethod
    def clean_stkcode(val:int, std:int=6) -> str:
        if str(val) == 6:
            return str(val)
        else:
            stk = ['0' * (std - len(str(val))), str(val)]
            return ''.join(stk)

    @staticmethod
    def clean_date(date_source:str) -> (int, int):
        # date format is YYYYMMDD
        year = int(date_source[:4])
        month = int(date_source[4:6])
        return year, month

    def run(self, year:int, month:int, index_name:str):
        self.data['stkcode'] = self.data['stkcode'].apply(self.clean_stkcode)

        # DataFrame Cleaning
        use = self.data['stkcode']
        yd = pd.Series([year] * len(use))
        md = pd.Series([month] * len(use))
        idn = pd.Series([index_name] * len(use))
        cod = pd.Series([i for i in range(1, len(use) + 1)])

        return pd.concat([yd, md, cod, use, idn], axis=1)


if __name__ == "__main__":

    p = 'C:/Users/Wooriam/PycharmProjects/krxCrawler/download/'
    fn = '20100101.csv'

    kc = KRXClean(
        file_loc=p,
        file_name=fn,
        index_name="ksbig"
    )
    print([tuple(r) for r in kc.result.to_numpy()])

