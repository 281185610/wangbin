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
company_name = 'Ozon中国'   

def ozonPricing(purchaseCost: float):  
     """Ozon定价计算函数"""  
     # function body......
     
# Streamlit实现可视化     
st.latex(f'定价 = {purchaseCost}*(1 + {purchaseMargin}/100)*(1 - {promotionDiscount}/100)*{exchangeRate}*(1 - {exchangeLoss}/100)')
st.title(f'{company_name}定价计算工具')  

# 获取用户输入并转换为float类型
purchaseCost = st.number_input('请输入采购成本', min_value=0.0, max_value=1000000,  
                               step=0.01, format='%f')

# 调用函数进行计算  
if purchaseCost:  
     price = purchaseCost * (1 + purchaseMargin/100)  
     price = price * (1 - promotionDiscount/100)  
     price = price * exchangeRate * (1 - exchangeLoss/100)  
     st.write(f'{company_name}最终定价: ¥{price}')  
     # ......
else:  
     st.warning('请输入采购成本!')
