import streamlit as st
# 定义变量并添加类型注释
purchaseCost: float
purchaseMargin = 10  # 采购加成,百分数
logisticsFee = 5   # 物流费,元
otherFee = 10       # 其他费用,元
fixedFee = 20        # 固定费用,元
exchangeRate = 6.5   # 汇率,比率
promotionDiscount = 8 # 促销折扣,百分数
categoryCommission = 5 # 产品佣金,百分数
exchangeLoss = 2     # 汇率损失,百分数
goodsLoss = 3        # 货损,百分数

def ozonPricing(purchaseCost: float):  
     """Ozon定价计算函数"""  
     # function body......

# Streamlit实现可视化
st.title('Ozon定价计算工具')  

# 获取用户输入并转换为float类型
purchaseCost = st.number_input('请输入采购成本', min_value=0.0, max_value=1000000,  
                               step=0.01, format='%f')   

# 调用函数进行计算
if purchaseCost:  
     price, formula = ozonPricing(purchaseCost)   
     st.write(f'最终定价: ¥{price}')   
     st.latex(formula)  
else:  
     st.warning('请输入采购成本!')
