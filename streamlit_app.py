python
import streamlit as st

def ozon_pricing(
    purchase_cost,  
    purchase_margin,  
    logistics_fee,  
    other_fee,
    fixed_fee,
    exchange_rate,
    promotion_discount,
    category_commission,
    exchange_loss,
    goods_loss    
):
    # 采购成本加成计算
    cost_plus = purchase_cost * (1 + purchase_margin)  
    
    # 其他费用计算
    total_cost = cost_plus + logistics_fee + other_fee + fixed_fee
    
    # 汇率调整
    total_cost = total_cost * exchange_rate
    
    # 折扣与损耗计算
    price = total_cost / ((1 - promotion_discount) * (1 - category_commission) * 
                         (1 - exchange_loss) * (1 - goods_loss))
    return price

# Streamlit实现可视化  
st.title('Ozon定价计算工具')

with st.form(key='my_form'):
    col1, col2 = st.columns(2)
    
    with col1:
        purchase_cost = st.number_input('采购成本', value=15)
        purchase_margin = st.number_input('采购成本利润率', value=0.2) 
        logistics_fee = st.number_input('物流费用', value=10)
        other_fee = st.number_input('其他费用', value=5)  
        fixed_fee = st.number_input('固定费用', value=100)
        exchange_rate = st.number_input('汇率', value=0.15)      
    with col2:
        promotion_discount = st.number_input('促销折扣', value=0.1)
        category_commission = st.number_input('类目佣金', value=0.08)
        exchange_loss = st.number_input('汇率损失', value=0.03)
        goods_loss = st.number_input('货物损失', value=0.01)
        
    submitted = st.form_submit_button('提交')
    
    if submitted:
        price = ozon_pricing(purchase_cost, purchase_margin, logistics_fee, 
                             other_fee, fixed_fee, exchange_rate, promotion_discount,
                             category_commission, exchange_loss, goods_loss)
        st.write(f'Ozon定价结果: {price}') 
