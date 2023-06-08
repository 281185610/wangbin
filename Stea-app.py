import streamlit as st

def ozon_pricing(
    purchase_cost,  
    ...  
):  
    if not isinstance(purchase_cost, (int, float)):
        st.warning('请输入数值类型的参数!')
        return
    ...

# Streamlit实现可视化  
st.title('Ozon定价计算工具')  

# 定义参数初值  
purchase_cost = 15  
...  

# 调用函数进行计算  
if isinstance(purchase_cost, (int, float)): 
    price, formula = ozon_pricing(purchase_cost, ...)
    st.write(f'最终定价: ¥{price}')  
    st.latex(formula) 
else:
    st.warning('请输入数值类型的参数!')  

with st.form(key='my_form'):
    ...  
if submitted: 
    purchase_cost = st.number_input('采购成本', value=15)
    purchase_cost = purchase_cost  
    if isinstance(purchase_cost, (int, float)):
        price, formula = ozon_pricing(purchase_cost, ...)  
        st.write(f'最终定价: ¥{price}')
        st.latex(formula)    
    else:  
        st.warning('请输入数值类型的参数!')
