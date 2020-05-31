import os
import pandas as pd
import click
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpmax

# input constants
(SIGMA, NUMBER_OF_TRANSACTIONS, MIN_FREQUENT_ITEMSET_SIZE) = (4, 25000, 3)

MIN_SUPPORT = SIGMA/NUMBER_OF_TRANSACTIONS


@click.command()
@click.argument('filename', default=os.path.join(os.getcwd(), 'retail_25k.dat'), type=click.Path(exists=True))
def generate_frequent_itemsets(filename):
	"""Function implementing FP-Max to extract frequent_itemsets of
	MAX_FREQUENT_ITEMSET_SIZE that appears at least as often as the
	minimum support value SIGMA
	"""
	data = pd.read_csv(filename, header=None)

	# Transform data into right format
	transactions = [tuple(row) for row in data[0].str.split()]
	te = TransactionEncoder()
	te_ary = te.fit(transactions).transform(transactions)
	df = pd.DataFrame(te_ary, columns=te.columns_)

	# extract columns support, items/itemsets that appear
	# at least as often as the SIGMA
	frequent_itemsets = fpmax(df, min_support=MIN_SUPPORT, use_colnames=True)

	frequent_itemsets['length'] = frequent_itemsets['itemsets']\
		.apply(lambda itemset: len(itemset))
	# filter dataframe to get frequent itemsets of size 3 or more
	frequent_itemsets = frequent_itemsets[
		frequent_itemsets['length'] >= MIN_FREQUENT_ITEMSET_SIZE]
	frequent_itemsets['co-occurrence frequency'] = frequent_itemsets['support']\
		.apply(lambda value: NUMBER_OF_TRANSACTIONS*value)

	frequent_itemsets.drop('support', axis=1, inplace=True)
	frequent_itemsets = frequent_itemsets.join(
		frequent_itemsets['itemsets']
		.apply(lambda itemset: ', '.join(itemset)).str.split(', ', expand=True))
	frequent_itemsets.drop('itemsets', axis=1, inplace=True)

	frequent_itemsets.to_csv(
		'frequently_purchased_items.csv',
		index=False, header=False, sep=",", na_rep="")


if __name__ == '__main__':
	generate_frequent_itemsets()
