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
    return price

def calculate_profit(price, target_profit_margin):
    cost = price / (1 + target_profit_margin/100)
    profit = price - cost
    return profit

# Streamlit实现可视化
st.title('Ozon定价计算工具')

# 显示计算公式
st.write('**计算公式:**')
st.latex(r'''
定价 = \frac{总成本}{(1 - \frac{促销折扣}{100}) 
(1 - \frac{类目佣金}{100}) (1 - \frac{汇率损失}{100})
(1 - \frac{货物损失}{100})}
''')

# 显示输入字段
with st.form(key='my_form'):
    col1, col2 = st.columns(2)
    with col1:
        purchase_cost = st.number_input('采购成本', value=15,
                                        help='请输入商品采购成本价格')
        purchase_margin = st.number_input('采购成本利润率%', value=20)
        logistics_fee = st.number_input('物流费用', value=10)
        other_fee = st.number_input('其他费用', value=5)
        fixed_fee = st.number_input('固定费用', value=100)
        exchange_rate = st.number_input('汇率', value=15)
        # 显示字段值
        st.write('**字段值:**')
        st.write(f'采购成本: {purchase_cost}')
        st.write(f'采购成本利润率%: {purchase_margin}')
        st.write(f'物流费用: {logistics_fee}')
        st.write(f'其他费用: {other_fee}')
        st.write(f'固定费用: {fixed_fee}')
        st.write(f'汇率: {exchange_rate}')
    with col2:
        promotion_discount = st.number_input('促销折扣%', value=10)
        category_commission = st.number_input('类目佣金%', value=8)
        exchange_loss = st.number_input('汇率损失%', value=3)
        goods_loss = st.number_input('货物损失%', value=1)
        target_profit_margin = st.number_input('目标利润率%', value=30)
        # 显示字段值
        st.write('**字段值:**')
        st.write(f'促销折扣%: {promotion_discount}')
        st.write(f'类目佣金%: {category_commission}')
        st.write(f'汇率损失%: {exchange_loss}')
        st.write(f'货物损失%: {goods_loss}')
        st.write(f'目标利润率%: {target_profit_margin}')
    submitted = st.form_submit_button('提交')
    if submitted:
        price = ozon_pricing(purchase_cost, purchase_margin, logistics_fee,
                             other_fee, fixed_fee, exchange_rate,
                             promotion_discount, category_commission,
                             exchange_loss, goods_loss)
        profit = calculate_profit(price, target_profit_margin)
        # 显示计算值
        st.write('**计算值:**')
        st.write(f'最终定价: ¥{price:.2f}')
        st.write(f'利润: ¥{profit:.2f}')
