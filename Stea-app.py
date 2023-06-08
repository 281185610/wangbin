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

def ozonPricing(purchaseCost: float) -> (float, str):
     """Ozon定价计算函数"""
     if not isinstance(purchaseCost, float) or purchaseCost <= 0:  
          st.warning('请输入正确的数值类型参数!')
          return  

     # 采购成本加成计算  
     costPlus = purchaseCost * (1 + purchaseMargin/100)   
     
     # 其他费用计算
     totalCost = costPlus + logisticsFee + otherFee + fixedFee  

     # 汇率调整
     totalCost = totalCost * exchangeRate
     
     # 折扣与损耗计算
     price = totalCost / ((1 - promotionDiscount/100) *  
                          (1 - categoryCommission/100) *  
                          (1 - exchangeLoss/100) *  
                          (1 - goodsLoss/100))
     formula = f'定价={totalCost} / (1 - {promotionDiscount}%折扣) / (1 - {categoryCommission}%佣金) / (1-{exchangeLoss}%汇率损失) / (1-{goodsLoss}%货损)'
     return price, formula  

# Streamlit实现可视化 
st.title('Ozon定价计算工具')  

# 获取用户输入
purchaseCost = st.number_input('请输入采购成本', min_value=1, max_value=1000000, value=1) 

# 调用函数进行计算
if purchaseCost: 
     price, formula = ozonPricing(purchaseCost)
     st.write(f'最终定价: ¥{price}')
     st.latex(formula)
else:
     st.warning('请输入采购成本!')     
