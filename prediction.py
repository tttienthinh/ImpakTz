import pandas as pd
import numpy as np
import six
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Données des ventes de véhicules neufs en France de 2009 à 2022
data = {
    'Annee': np.arange(2009, 2023),
    'Ventes': [
        2268671, 2251669, 2204229, 1898760, 1790456, 1795885, 1917226,
        2015177, 2110748, 2173481, 2214279, 1650118, 1659003, 1529035
    ]
}

df = pd.DataFrame(data)

# Séparation des données en deux périodes
df_pre_2020 = df[(df['Annee'] >= 2010) & (df['Annee'] <= 2019)]
df_post_2019 = df[(df['Annee'] >= 2020) & (df['Annee'] <= 2021)]

# Années futures
future_years = np.arange(2023, 2033).reshape(-1, 1)

# Initialisation des modèles de régression linéaire pour chaque période
model_pre_2020 = LinearRegression()
model_post_2019 = LinearRegression()

# Entraînement des modèles sur les périodes respectives
X_pre_2020 = df_pre_2020['Annee'].values.reshape(-1, 1)
y_pre_2020 = df_pre_2020['Ventes'].values
model_pre_2020.fit(X_pre_2020, y_pre_2020)

X_post_2019 = df_post_2019['Annee'].values.reshape(-1, 1)
y_post_2019 = df_post_2019['Ventes'].values
model_post_2019.fit(X_post_2019, y_post_2019)

# Création des lignes de tendance pour les deux périodes
X_all_years = df['Annee'].values.reshape(-1, 1)
trend_pre_2020 = model_pre_2020.predict(X_all_years)
trend_post_2019 = model_post_2019.predict(X_all_years)

# Prédictions futures pour les deux périodes
future_trend_pre_2020 = model_pre_2020.predict(future_years)
future_trend_post_2019 = model_post_2019.predict(future_years)

# Affichage des résultats avec les deux lignes de tendance
plt.figure(figsize=(12, 6))
plt.scatter(df['Annee'], df['Ventes'], color='blue', label='Données historiques')
plt.plot(X_all_years, trend_pre_2020, color='green', linestyle='-', label='2014-2019 Trend')
plt.plot(X_all_years, trend_post_2019, color='purple', linestyle='-', label='2020-2022 Trend')
plt.plot(future_years, future_trend_pre_2020, color='green', linestyle='--', label='Prédiction future 2014-2019 Trend')
plt.plot(future_years, future_trend_post_2019, color='purple', linestyle='--', label='Prédiction future 2020-2022 Trend')
plt.xlabel('Année')
plt.ylabel('Nouvelles ventes de véhicules')
plt.title('Prédiction des nouvelles ventes de voitures en France')
plt.legend()
plt.show()



### Calcul de la rentabilité espérée selon les trois scénarios d'adoption

# Prix par NFT
prix_nft = 39.90

# Taux d'adoption pour chaque scénario
taux_adoption = {
    'Défavorable (1%)': 0.01,
    'Neutre (20%)': 0.20,
    'Favorable (70%)': 0.70
}

# Calcul de la rentabilité pour chaque année et pour chaque scénario
predictions = model_post_2019.predict(future_years.reshape(-1, 1))
rentabilite = {}
for scenario, taux in taux_adoption.items():
    rentabilite[scenario] = predictions * taux * prix_nft

# Création d'un DataFrame pour présenter les résultats
rentabilite_df = pd.DataFrame(rentabilite, index=np.arange(2023, 2033))
rentabilite_df.round(2)

# Fonction pour afficher un DataFrame en tant que tableau avec un format comptable
def render_mpl_table(data, col_width=4.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
        ax.set_title("Chiffre d'affaire prévu pour la vente de NFT", fontsize=16, weight='bold')

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors)])
            if k[0] != 0 and "202" != cell.get_text().get_text()[:3] and "203" != cell.get_text().get_text()[:3]:  # Change the display format for non-header cells.
                cell.get_text().set_text(f"{int(cell.get_text().get_text()):,} €".replace(',', ' '))
    return ax

# Arrondir les valeurs du DataFrame et appliquer le format comptable
rentabilite_df_rounded = rentabilite_df.round(0).astype(int)

# Création du tableau formaté
selection = [2,5,7]
render_mpl_table(rentabilite_df_rounded.iloc[selection].reset_index(), header_columns=0, col_width=2.5)
