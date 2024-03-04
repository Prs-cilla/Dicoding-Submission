import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# membaca file all_data.csv
all_df = pd.read_csv("all_data.csv")

# membuat judul
st.title('Bike Sharing Dataset')

# membuat header 1
st.header('Question 1')

# menulis penjelasan bar chart
st.write(
    """
    # Pada jam berapa terdapat peminjam sepeda casual dengan jumlah tertinggi?
    Casual biker terbanyak terdapat pada pukul 14. Selain itu, dapat terlihat juga bahwa pukul 4 jumlah casual biker terendah di antara pukul lainnya.
    """
)

# visualisasi jumlah pengendara sepeda casual tiap jamnya
fig, ax = plt.subplots(nrows=1)
 
colors = [ "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="hr", y="casual_x", data=all_df, estimator=sum, palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Highest Casual Biker in Each Hour", loc="center", fontsize=15)
ax.tick_params(axis='y', labelsize=12)

st.pyplot(fig)

# membuat header 2
st.header('Question 2')

# menjelaskan penjelasan bar chart
st.write(
    """
    # Bagaimana pengaruh season terhadap total peminjam sepeda setiap harinya?
    Total biker terbanyak terdapat pada musim 3. Di mana musim 3 merupakan musim gugur dan biker terendah terdapat pada musim 1 atau musim semi.
    """
)

# visualisasi total peminjam sepeda untuk tiap musim
fig, ax = plt.subplots(nrows=1)
 
colors = [ "#D3D3D3", "#72BCD4", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="season_x", y="cnt_x", data=all_df, estimator=sum, palette=colors, ax=ax)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.set_title("Highest Total Biker in Every Season", loc="center", fontsize=15)
ax.tick_params(axis='y', labelsize=12)

st.pyplot(fig)