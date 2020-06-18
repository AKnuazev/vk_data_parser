from source.friends import calc_age
from source.graphs import make_age_hist

user_id = 'shaku'  # Mary
ages_quant = calc_age(user_id)
make_age_hist(user_id, ages_quant)
