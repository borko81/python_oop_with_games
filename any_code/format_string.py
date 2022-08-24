from typing import List, Tuple

current_data = [
    (1000, 10, 11),
    (2000, 17),
    (2500, 170),
    (2500, -170),
]


class ReadData:

    def __init__(self, data: List[Tuple]):
        self.data = data

    def fetch_data(self):
        for row in self.data:
            yield row


class FormatData:
    TEMPLATE = "{r:>7,} | {p:>+6} | {percent:>7.2f}%"

    def __init__(self, outside_data: ReadData):
        self.rows = outside_data
        print("REVENUE | PROFIT | PERCENT")

    def stock_row(self):
        for row in self.rows.fetch_data():
            revenue, profit, *_ = row
            percent = revenue / profit
            print(self.TEMPLATE.format(r=revenue, p=profit, percent=percent))


if __name__ == '__main__':
    f = ReadData(current_data)
    result = FormatData(f)
    result.stock_row()
