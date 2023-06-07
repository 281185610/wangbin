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

# 读取产品信息
product_df = pd.read_csv('products.csv') 

# Streamlit实现可视化  
st.title('Ozon定价计算工具')

for index, row in product_df.iterrows():
    product_name = row['product_name']
    product_link = row['product_link']
    
    with st.form(key=f'product_{index}_form'):
        # 参数输入        
        params = {}
        params['purchase_cost'] = st.number_input(f'{product_name}采购成本', value=row['purchase_cost']) 
        params['purchase_margin'] = st.number_input(f'{product_name}采购成本利润率%',  
                                                  value=row['purchase_margin']) 
        params['logistics_fee'] = st.number_input(f'{product_name}物流费用', value=row['logistics_fee']) 
        params['other_fee'] = st.number_input(f'{product_name}其他费用', value=row['other_fee']) 
        params['fixed_fee'] = st.number_input(f'{product_name}固定费用', value=row['fixed_fee'])
        params['exchange_rate'] = st.number_input(f'{product_name}汇率', 
                                                 value=row['exchange_rate']) 
        # ...其他参数         
        submitted = st.form_submit_button(f'提交{product_name}')
        
        if submitted: 
            # 计算结果
            price = ozon_pricing(params)  
            st.write(f'{product_name}最终定价: ¥{price}')
            st.write(f'{product_name}产品链接: {product_link}')  
