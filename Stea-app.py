import streamlit as st

# 定义变量并添加类型注释  
purchaseCost: float  
purchaseMargin = 10  
logisticsFee = 5       
otherFee = 10        
fixedFee = 20
exchangeRate = 6.5  
promotionDiscount = 8  
categoryCommission = 5 
exchangeLoss = 2     
goodsLoss = 3    

def ozonPricing(purchaseCost: float):  
     """Ozon定价计算函数"""  
     price = purchaseCost * (1 + purchaseMargin/100)  
     price = price * (1 - promotionDiscount/100)  
     price = price * exchangeRate * (1 - exchangeLoss/100)
     
     profit = price - purchaseCost - logisticsFee - otherFee - fixedFee
     formula = f'利润 = 定价 - 采购成本 - 物流费 - 其他费用 - 固定费用'
     return price, formula  

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
     profit = price - purchaseCost - logisticsFee - otherFee - fixedFee  
     st.write(f'利润: ¥{profit}')
     st.latex('利润 = 定价 - 采购成本 - 物流费 - 其他费用 - 固定费用')
else:  
     st.warning('请输入采购成本!')
