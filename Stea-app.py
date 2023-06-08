import streamlit as st
import pandas as pd

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

# Streamlit实现可视化
st.title('Ozon定价计算工具')

# 显示计算公式
st.write('**计算公式:**')
st.latex(r'''
定价 = \frac{总成本}{(1 - \frac{促销折扣}{100}) 
(1 - \frac{类目佣金}{100}) (1 - \frac{汇率损失}{100})
(1 - \frac{货物损失}{100})}
''')

# 显示输入表格
st.write('**请输入商品信息:**')
df = pd.DataFrame(columns=['采购成本', '采购成本利润率%', '物流费用', '其他费用', '固定费用', '汇率',
                           '促销折扣%', '类目佣金%', '汇率损失%', '货物损失%'])
st.write(df)

# 显示计算结果表格
result_df = pd.DataFrame(columns=['采购成本', '最终定价'])
st.write('**计算结果:**')
st.write(result_df)

# 添加商品信息到输入表格
st.write('**添加商品信息:**')
with st.form(key='my_form'):
    col1, col2 = st.columns(2)
    with col1:
        purchase_cost = st.number_input('采购成本', help='请输入商品采购成本价格')
        purchase_margin = st.number_input('采购成本利润率%', 1, 100, 0.0, '%')
        logistics_fee = st.number_input('物流费用', 0.0, None, 0.0, '%')
        other_fee = st.number_input('其他费用', 0.0, None, 0.0, '%')
        fixed_fee = st.number_input('固定费用', 0.0, None, 0.0, '%')
        exchange_rate = st.number_input('汇率', 0.0, None, 0.0, '%')
    with col2:
        promotion_discount = st.number_input('促销折扣%', 0.0, None, 0.0, '%')
        category_commission = st.number_input('类目佣金%', 0.0, None, 0.0, '%')
        exchange_loss = st.number_input('汇率损失%', 0.0, None, 0.0, '%')
        goods_loss = st.number_input('货物损失%', 0.0, None, 0.0, '%')

    submitted = st.form_submit_button('添加')
    if submitted:
        row = {'采购成本': purchase_cost,
               '采购成本利润率%': purchase_margin,
               '物流费用': logistics_fee,
               '其他费用': other_fee,
               '固定费用': fixed_fee,
               '汇率': exchange_rate,
               '促销折扣%': promotion_discount,
               '类目佣金%': category_commission,
               '汇率损失%': exchange_loss,
               '货物损失%': goods_loss}
        df = df.append(row, ignore_index=True)
        st.table(df)

# 计算最终定价并添加到结果表格中
if not df.empty:
    for i, row in df.iterrows():
        price = ozon_pricing(row['采购成本'], row['采购成本利润率%'],
                             row['物流费用'], row['其他费用'], row['固定费用'],
                             row['汇率'], row['促销折扣%'], row['类目佣金%'],
                             row['汇率损失%'], row['货物损失%'])
        result_row = {'采购成本': row['采购成本'], '最终定价': price}
        result_df = result_df.append(result_row, ignore_index=True)

    st.write('**计算结果:**')
    st.table(result_df)
