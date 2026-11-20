import streamlit as st

st.set_page_config(
    page_title="第五降临者 · 内功练习场",
    page_icon=":taoist:",
)

st.title("第五降临者 · 内功练习场")

st.write(
    """
    这里是第五降临者的内功练习场。

    修行不在招式华丽，而在日复一日的扎马步——
    写代码、调 bug、读文档，然后重来一遍。

    场中三戒：
    - **静心**：先看清问题，再动手落子。
    - **持恒**：每日精进一寸，胜过一时猛进。
    - **复盘**：每次提交都是一回小结，留下成长的印记。

    内功非一日之功，愿此处见证每一次精进。
    """
)

st.divider()

# ---- 修炼计数器 ----
st.subheader("打坐计数")

# session_state 的值在脚本重跑时不会丢失
if "count" not in st.session_state:
    st.session_state.count = 0

# 用两个按钮包住，点击后分别加减
col1, col2 = st.columns(2)
with col1:
    if st.button("打坐一次", use_container_width=True):
        st.session_state.count += 1
with col2:
    if st.button("重置", use_container_width=True):
        st.session_state.count = 0

# 显示当前次数
st.metric("累计修炼次数", st.session_state.count)

# 根据次数显示不同的境界
if st.session_state.count == 0:
    st.caption("当前境界：初入江湖 · 尚未开始")
elif st.session_state.count < 5:
    st.caption("当前境界：初入江湖 · 持续修炼中")
elif st.session_state.count < 15:
    st.caption("当前境界：小有所成 · 气沉丹田")
elif st.session_state.count < 30:
    st.caption("当前境界：渐入佳境 · 心如止水")
else:
    st.caption("当前境界：登峰造极 · 返璞归真")
