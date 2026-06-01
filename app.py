import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# from IBKR import df, fig
df = pd.read_excel(r"D:\IBKR\Project\df.xlsx")
st.title("Portfolio Dashboard")
st.dataframe(df)

portfolio_total = df["Market_Value_USD"].sum()
fig, ax = plt.subplots()
ax.pie(df["Market_Value_USD"], autopct='%1.1f%%', pctdistance=1.15)
ax.set_title(f"Portfolio Allocation\nTotal: $ {portfolio_total:,.2f}")
ax.legend(df["Ticker"], bbox_to_anchor=(1, 0.9))
st.pyplot(fig)

df_vt = pd.read_excel(r"D:\IBKR\Project\vt.xlsx")
df_vt["Close"] = pd.to_numeric(df_vt["Close"], errors="coerce")
df_vt = df_vt.dropna(how="all") # delete empty rows
st.title("VT Price Since Start of Year 2026")
st.dataframe(df_vt)

fig2, ax2 = plt.subplots(figsize=(12, 6))
ax2.plot(df_vt["Date"], df_vt["Close"])
ax2.set_title("VT Price Since Start of Year 2026")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price USD")
ax2.grid(True)

entry_date = pd.to_datetime("2026-05-15")
entry_price = 154.14
ax2.scatter(entry_date, entry_price, s=30)
ax2.annotate("Entry 154.14 / 15.05", (entry_date, entry_price), textcoords= "offset points", xytext=(10, 10))
ax2.axhline(y=154.14, linestyle='--', color='red')
st.pyplot(fig2)

df_voo = pd.read_excel(r"D:\IBKR\Project\voo.xlsx")
df_voo["Close"] = pd.to_numeric(df_voo["Close"], errors="coerce")
df_voo = df_voo.dropna(how="all") # delete empty rows
st.dataframe(df_voo)

fig3, ax3 = plt.subplots(figsize=(12, 6))
ax3.plot(df_voo["Date"], df_voo["Close"])
ax3.set_title("VOO Price Since Start of Year 2026")
ax3.set_xlabel("Date")
ax3.set_ylabel("Price USD")
ax3.grid(True)
st.pyplot(fig3)

df_iau = pd.read_excel(r"D:\IBKR\Project\iau.xlsx")
df_iau["Close"] = pd.to_numeric(df_iau["Close"], errors="coerce")
df_iau = df_iau.dropna(how="all") # delete empty rows
st.dataframe(df_iau)

fig4, ax4 = plt.subplots(figsize=(12, 6))
ax4.plot(df_iau["Date"], df_iau["Close"])
ax4.set_title("IAU Price Since Start of Year 2026")
ax4.set_xlabel("Date")
ax4.set_ylabel("Price USD")
ax4.grid(True)
st.pyplot(fig4)

df_sgov = pd.read_excel(r"D:\IBKR\Project\sgov.xlsx")
df_sgov["Close"] = pd.to_numeric(df_sgov["Close"], errors="coerce")
df_sgov = df_sgov.dropna(how="all") # delete empty rows
st.dataframe(df_sgov)

fig5, ax5 = plt.subplots(figsize=(12, 6))
ax5.plot(df_sgov["Date"], df_sgov["Close"])
ax5.set_title("SGOV Price Since Start of Year 2024")
ax5.set_xlabel("Date")
ax5.set_ylabel("Price USD")
ax5.grid(True)
st.pyplot(fig5)






