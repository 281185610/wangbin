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
    formula = f'定价={total_cost} / (1 - {promotion_discount}%折扣) / (1 - {category_commission}%佣金) / (1-{exchange_loss}%汇率损失) / (1-{goods_loss}%货损)'
    return price, formula

# Streamlit实现可视化  
st.title('Ozon定价计算工具')  

# 定义参数初值  
purchase_cost = 15  
...  

# 调用函数进行计算  
price, formula = ozon_pricing(purchase_cost, ...)
st.write(f'最终定价: ¥{price}')  
st.latex(formula)  

with st.form(key='my_form'):
    ...
if submitted: 
    price, formula = ozon_pricing(purchase_cost, ...) 
    st.write(f'最终定价: ¥{price}')
    st.latex(formula)     
