import streamlit as st
import pandas as pd

def ozon_pricing(params):
    purchase_cost = params['purchase_cost']  
    purchase_margin = params['purchase_margin'] 
    logistics_fee = params['logistics_fee']  
    other_fee = params['other_fee']
    fixed_fee = params['fixed_fee']
    exchange_rate = params['exchange_rate']
    promotion_discount = params['promotion_discount']
    category_commission = params['category_commission'] 
    exchange_loss = params['exchange_loss']
    goods_loss = params['goods_loss']
    profit_margin = params['profit_margin']
    
    # 采购成本加成计算
    cost_plus = purchase_cost * (1 + purchase_margin/100)  
    
    # 其他费用计算 
    total_cost = cost_plus + logistics_fee + other_fee + fixed_fee   
    
    # 汇率调整
    total_cost = total_cost * exchange_rate   
    
    # 折扣与损耗计算
    price = total_cost / ((1 - promotion_discount/100) *  
                         (1 - category_commission/100) * 
                         (1 - exchange_loss/100) *  
                         (1 - goods_loss/100))
                         
    # 利润计算                
    profit = price * profit_margin/100
    return price, profit  

# Streamlit实现可视化
st.title('Ozon定价计算工具')

products = {
    '产品1': {'purchase_cost':15,  'purchase_margin':20,  
              'logistics_fee':10,  'other_fee':5,  
              'fixed_fee':100, 'exchange_rate':15,  
              'promotion_discount':10, 'category_commission':8,   
              'exchange_loss':3,   'goods_loss':1, 'profit_margin':30}, 
    '产品2': {'purchase_cost':25,  'purchase_margin':25,  
              'logistics_fee':15,  'other_fee':8,  
              'fixed_fee':120, 'exchange_rate':18,  
              'promotion_discount':12,'category_commission':10,    
              'exchange_loss':5,   'goods_loss':3, 'profit_margin':35}  
}  

with st.form(key='product_form'): 
    cols = st.columns(2)
    data = []
    for product_name, product_params in products.items():
        with cols[0]:        
            st.write(f'{product_name}定价计算公式:')
            formula = f'价格 = 采购成本 × (1 + 采购成本利润率{product_params["purchase_margin"]}%) '       
            formula += f'+ 物流费用{product_params["logistics_fee"]} + 其他费用{product_params["other_fee"]} '
            formula += f'+ 固定费用{product_params["fixed_fee"]} '
            formula += f'× 汇率{product_params["exchange_rate"]} '  
            formula += f'÷ (1 - 促销折扣{product_params["promotion_discount"]}% - '
            formula += f'类目佣金{product_params["category_commission"]}% - ' 
            formula += f'汇率损失{product_params["exchange_loss"]}% - '
            formula += f'货物损失{product_params["goods_loss"]}%) '
            formula += f'× (1 + 利润率{product_params["profit_margin"]}%)'
            st.latex(formula)  
            
            for param_name in product_params:             
                product_params[param_name] = st.number_input(
                    f'{product_name}{param_name}',
                    value=product_params[param_name], 
                    help=f'请输入{product_name}{param_name}'
                )
        data.append(product_params) 
    submitted = st.form_submit_button('提交')
