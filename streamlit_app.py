
import streamlit as st

# 定义定价计算函数    
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
    
    # 采购成本加成计算  
    cost_plus = purchase_cost * (1 + purchase_margin/100)      
    # 其他费用计算
    total_cost = cost_plus + logistics_fee + other_fee + fixed_fee  
    # 汇率调整
    total_cost = total_cost * exchange_rate 
    # 折扣与损耗计算
    price = total_cost / ((1 - promotion_discount/100) * (1 - category_commission/100) *  
                         (1 - exchange_loss/100) * (1 - goods_loss/100))
    return price

# Streamlit实现可视化  
st.title('Ozon定价计算工具')

with st.form(key='product_form'):
    # 参数输入        
    params = {}
    params['purchase_cost'] = st.number_input('采购成本')    
    params['purchase_margin'] = st.number_input('采购成本利润率%') 
    params['logistics_fee'] = st.number_input('物流费用') 
    params['other_fee'] = st.number_input('其他费用')
    params['fixed_fee'] = st.number_input('固定费用')
    params['exchange_rate'] = st.number_input('汇率')      
    # ...其他参数         
    submitted = st.form_submit_button('提交')
    
    if submitted: 
        # 计算结果
        price = ozon_pricing(params)  
        st.write(f'最终定价: ¥{price}') 
