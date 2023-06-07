python
import streamlit as st

def ozon_pricing(params):
    purchase_cost = params['purchase_cost']  
    purchase_margin = params['purchase_margin']  
    # ...定价计算逻辑...
    return price   

# Streamlit实现可视化  
st.title('Ozon定价计算工具')

products = {'产品1':{'purchase_cost':15, 'purchase_margin':20, ...}, 
            '产品2':{'purchase_cost':20, 'purchase_margin':25, ...},
            '产品3':{'purchase_cost':25, 'purchase_margin':30, ...}}

with st.form(key='my_form'):
    cols = st.columns(len(products))
    data = []
    for i, (product_name, product_params) in enumerate(products.items()): 
        with cols[i]:        
            for param_name in product_params:                
                product_params[param_name] = st.number_input(
                    f'{product_name}{param_name}', 
                    value=product_params[param_name], 
                    help=f'请输入{product_name}{param_name}'
                )
        data.append(product_params)          
    submitted = st.form_submit_button('提交')  
    
    if submitted:
        for product in data:  
            product['product_name'] = product_name
            price = ozon_pricing(product)    
            st.write(f'{product_name}最终定价: ¥{price}') 
