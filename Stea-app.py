import streamlit as st
import pandas as pd


def ozon_pricing(params):
	...  # 参数和函数定义 (与上面代码相同)  


# Streamlit实现可视化界面   
st.title('Ozon定价计算工具')

products = {...}  # 产品参数定义 (与上面代码相同)  

with st.form(key='product_form'):
	cols = st.columns(2)
	data = []
for product_name, product_params in products.items()::
with cols[0]:
	st.write(f'{product_name}定价计算公式:')
	formula = f'# 价格 = 采购成本 x (1+{product_params["采购成本利润率"]}%'
	st.markdown(formula)
	for param in product_params:
		product_params[param] = st.number_input(f'{product_name}{param}', value=product_params[param])
data.append(product_params)
submitted = st.form_submit_button('提交')

if submitted:
	results = []
	for product in data:
		product_name = product.pop('product_name')
		price, profit = ozon_pricing(product)
		product['价格'] = price
		product['利润'] = profit
		product['product_name'] = product_name
		results.append(product)

	st.write('定价与利润计算结果:')
	st.table(pd.DataFrame(results))
