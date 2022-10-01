from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
split = dt_string.split()
datalista = (split[0].split('/'))
horalista = (split[1].split(':'))
data_atual = [datalista, horalista]