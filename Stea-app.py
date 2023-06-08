import streamlit as st

# 定义变量
purchaseMargin = 10   

def ozonPricing(purchaseCost):  
     """Ozon定价计算函数"""
     if not isinstance(purchaseCost, (int, float)) or purchaseCost <= 0:  
          st.warning('请输入正确的数值类型参数!')
          return  
     
     # 其他参数也增加类型检查......  
     
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
