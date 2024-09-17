import pandas as pd
import time

# sql
query_06 = '''
select
	sum(l_extendedprice * l_discount) as revenue
from
	lineitem
where
	l_shipdate >= date '1994-01-01'
	and l_shipdate < date '1994-01-01' + interval '1' year
	and l_discount between .06 - 0.01 and .06 + 0.01
	and l_quantity < 24;
'''

# Set pandas display options to show all columns
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_colwidth', None)  # Show full content of each column

column_names = [
    "l_orderkey",
    "l_partkey",
    "l_suppkey",
    "l_linenumber",
    "l_quantity",
    "l_extendedprice",
    "l_discount",
    "l_tax",
    "l_returnflag",
    "l_linestatus",
    "l_shipdate",
    "l_commitdate",
    "l_receiptdate",
    "l_shipinstruct",
    "l_shipmode",
    "l_comment",
    "l_omit"
]

# load dataset
# lineitem = pd.read_csv('./SF-1/data/lineitem_tmp.tbl', sep='|', names=column_names, header=None, parse_dates=['l_shipdate', 'l_commitdate', 'l_receiptdate'])
# lineitem = pd.read_csv('./SF-1/data/lineitem.tbl', sep='|', names=column_names, header=None, parse_dates=['l_shipdate', 'l_commitdate', 'l_receiptdate'])
lineitem = pd.read_csv('./SF-1/data/lineitem.tbl', sep='|', names=column_names, header=None)


# print 10 lines if the data is loaded successfully
# print(lineitem.head(2))

# shipdate, start date and end date
lineitem['l_shipdate'] = pd.to_datetime(lineitem['l_shipdate'])
start_date = pd.to_datetime('1994-01-01')
end_date = start_date + pd.DateOffset(years=1)

# print(f"*** start_date: {start_date}, end_date:, {end_date}")

start_time = time.time()
# filter
filtered_df = lineitem[
    (lineitem['l_shipdate'] >= start_date) &
    (lineitem['l_shipdate'] < end_date) &
    (lineitem['l_discount'].between(0.05, 0.07)) &
    (lineitem['l_quantity'] < 24)
]

# print 10 lines if the data is filtered successfully
# print(filtered_df.head(2))

# calculate revenue
revenue = (filtered_df['l_extendedprice'] * filtered_df['l_discount']).sum()
end_time = time.time()
time_used = end_time - start_time

print(f"Revenue: {revenue}")
print(f"time_used: {time_used}s")