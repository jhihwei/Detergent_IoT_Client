class Data_Format():

    def __init__(self):
        pass

    def extract_data(self, d):
        total_flow = f'{self.fix_number(d[5])}{self.fix_number(d[4])}{self.fix_number(d[3])}{self.fix_number(d[2])}{self.fix_number(d[1])}'
        gross_income = f'{self.fix_number(d[10])}{self.fix_number(d[9])}{self.fix_number(d[8])}{self.fix_number(d[7])}{self.fix_number(d[6])}'
        flow = f'{self.fix_number(d[15])}{self.fix_number(d[14])}{self.fix_number(d[13])}{self.fix_number(d[12])}{self.fix_number(d[11])}'
        income = f'{self.fix_number(d[20])}{self.fix_number(d[19])}{self.fix_number(d[18])}{self.fix_number(d[17])}{self.fix_number(d[16])}'
        receipt = f'{self.fix_number(d[25])}{self.fix_number(d[24])}{self.fix_number(d[23])}{self.fix_number(d[22])}{self.fix_number(d[21])}'

        return int(total_flow), int(gross_income), int(flow), int(income), int(receipt)

    def fix_number(self, number):
        number = int(number, 16)
        if number == 0:
            return '00'
        elif number < 10:
            return f'0{number}'
        else:
            return number