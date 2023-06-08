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
     # 参数类型检查......
     #  function body......  

     # 采购成本加成计算
     costPlus = purchaseCost * (1 + purchaseMargin/100)   
     
     # 其他费用计算 
     totalCost = costPlus + logisticsFee + otherFee + fixedFee  

     # 汇率调整
     totalCostAfterExchangeRate = totalCost * exchangeRate
     
     # 折扣因素提取 
     discount = 1 - promotionDiscount/100 
     commission = 1 - categoryCommission/100
     exchangeLossFactor = 1 - exchangeLoss/100
     goodsLossFactor = 1 - goodsLoss/100
     
     # 价格计算
     price = totalCostAfterExchangeRate / (discount * commission * 
                                          exchangeLossFactor *
                                          goodsLossFactor  )
     formula = f'定价={totalCostAfterExchangeRate} / 折扣 / 佣金 / 汇率损失 / 货损'
     return price, formula


# Streamlit实现可视化 
st.title('Ozon定价计算工具')  


# 获取用户输入并转换为float类型   
purchaseCost = st.number_input('请输入采购成本', min_value=1, max_value=1000000,  
                               value=1, step=1.0, format='%f')  


# 调用函数进行计算
if purchaseCost: 
     price, formula = ozonPricing(purchaseCost)
     st.write(f'最终定价: ¥{price}')
     st.latex(formula)
else:
     st.warning('请输入采购成本!')     
