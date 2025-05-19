
### IMPORTATION DES LIBRAIRIES
import pandas as pd # gestion ttt des données
import numpy as np # gestion ttt des données
import matplotlib.pyplot as plt  # visu data
import seaborn as sns # visu data
from PIL import Image  # gestion des images
import streamlit as st
import os   # gestion des fichiers et répertoire du système exploitation
import joblib  # Pour charger des modèles
import plotly.express as px # visualisations interactives et avancées
import plotly.graph_objects  as  go  # visualisations interactives et avancées
from plotly.subplots import make_subplots  # création de graph multiples dans une mm figure



### FONCTION DE CHARGEMENT DES DATASETS 
# @st.cache_data chargement rapide des datasets car tjrs identiques
st.spinner("Données en cours de chargement ...") 
@st.cache_data
def load_data():
    data=pd.read_csv('dataset.csv')  
    return data 
df_1=load_data()
      

@st.cache_data
def load_data():
    data=pd.read_csv('dataset_pred.csv')  
    return data 
df=load_data()



# Echantillonnage du dataset pour les visualisations plus rapides
df_sampled = df.sample(n=1000) 
df_sampled_1 = df_1.sample(n=1000) 


### FONCTION DE CHARGEMENT DES MODELES ENTRAINES
@st.cache_resource
def load_model(model_name):
    return joblib.load(f'models/{model_name}.joblib')


### MISE EN PAGE DE L'APPLI

st.image("datajob_logo_rouge.PNG", width=600)

st. sidebar.title( " SOMMAIRE " )                                      
pages=[ " **Présentation des données**" , "**DataVisualisation**", "**Modélisation prédictive**"  ]
page=st.sidebar.radio("", pages )
st.write("")
st.write("")
st.write("")
st.write("")  


### PAGE 1 PRESENTATION DATASETS
if page == pages[ 0 ] :     
  st.markdown(
    "<h3 style='text-align:center; font-size: 40px;color: #18009e; font-style: italic;'>Présentation des données</h3>",
    unsafe_allow_html=True)
  st.write("")
  st.write("")

  st.markdown(
    "<h6 style='text-align: left; font-size: 23px; color: #000000; '>Visuel du jeu de données</h6>",unsafe_allow_html=True)
  st.dataframe(df.head( 10 ) )
  st.write("")
  st.write("")
  st.write("")

  st.markdown(
    "<h6 style='text-align: left; font-size: 23px; color: #000000;'>Taille du jeu de données</h6>",unsafe_allow_html=True)
  st.markdown( f"""
    <div style='text-align: left; font-size: 17px; color: #009400;'>
        {df.shape[0]} lignes &nbsp;&nbsp;&nbsp;/&nbsp;&nbsp;&nbsp; {df.shape[1]} colonnes</div>
    """, unsafe_allow_html=True)
  st.write("")
  st.write("")
  st.write("")

  st.markdown(
    "<h6 style='text-align: left; font-size: 23px; color: #000000;'>Description des variables catégorielles</h6>",unsafe_allow_html=True)
  if st.checkbox("Liste des métiers") :
     st.dataframe(df["Current_role"].unique()) 
  if st.checkbox("Liste des compétences") :
     st.dataframe(df.columns[13:])
  if st.checkbox("Liste des niveaux d'études") :
     st.dataframe(df_1["EducationLevel"].unique())
  if st.checkbox("Répartition des tranches d'âges") :
     st.dataframe(df["Age"].value_counts())



### PAGE 2 PRESENTATION VISUELLE DES DATA
if page == pages[ 1 ] : 
    st.markdown(
    "<h3 style='text-align:center; font-size: 40px;color: #18009e; font-style: italic;'>Visualisation des données</h3>",
    unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")



## GRAPH REPARTITION DES POSTES DES SONDES EN PIE CHART

    valeurs = df_sampled['Current_role'].value_counts()  
    class_names = ['Data Scientist', 'Data Analyst', 'Software Engineer', 'Research Scientist']  

# Couleurs des sections
    colors = ['#89AFCB', '#F4A582', '#A6C8A8', '#FFD07B'] 

# Créa pie chart  
    fig = go.Figure(data=[go.Pie(
        labels=class_names,  
        values=valeurs,  
        hole=0.5,  # trou du centre
        hoverinfo='label+percent',  # infos de survol des parts
        textinfo='percent',  # valeur affichage dans les parts
        textfont_size=20,  # taille texte dans les parts
        marker=dict(colors=colors, line=dict(color='#FFFFFF', width=2)))])  # couleurs des parts et bordure blanche de séparation

# Mise en page graph
    fig.update_layout(
        title_text='Répartition des postes des sondés',  # titre
        title_x=0.15,  # position horizontale 
        title_font_size=23,  # taille du titre
        height=400,  # hauteur graph
        showlegend=True,  # affichage légende
        margin=dict(t=50, b=50, l=50, r=50),  # définition des marges autour du graphique (haut, bas, gauche, droite)
        
# Gestion légende
        legend=dict(
            font=dict(size=18, color='black'),  # taille couleur texte
            title=dict(
                text="Postes",  # titre
                font=dict(size=24, color='black')),  # taille couleur titre
            orientation='v',  # orientation 
            x=1.05,  # position horizontale 
            xanchor='left',  # légende à gauche horiz
            y=0.5,  # position verticale 
            yanchor='middle'))  # légende au centre verti

    st.plotly_chart(fig)   
    
    st.write("")
    st.write("")
    st.write("")



## GRAPH REPARTITION DES NIVEAUX DE FORMATION PAR POSTES EN TREEMAPS 

 # Liste des couleurs
    color_map = {
        'Other': '#f0bd37', 
        'Master': '#ffacd0',  
        'Bachelor': '#6fa8dc',  
        'Professional': '#cbdff7',  
        'Doctoral': '#dcedc1', 
        'NotAnswer': '#f60303'} 

# Liste métiers
    roles = ['Data Analyst', 'Data Scientist', 'Software Engineer', 'Research Scientist']

# Créa figure multigraph 2 lignes 2 colonnes
    fig = make_subplots(
        rows=2, cols=2,  
        subplot_titles=roles,  # titre des ss graphes == métiers
        specs=[[{"type": "domain"}, {"type": "domain"}],  # Définit que chaque sous-graphe sera un graphique de type "domain" (treemap)
            [{"type": "domain"}, {"type": "domain"}]],  # domain == graph treemap
        vertical_spacing=0.1,  # espace vertical entre ss graphs
        horizontal_spacing=0.08)  # espace horizontal ss graph

# Position treemaps dans la figure
    positions = [(1, 1), (1, 2), (2, 1), (2, 2)]

# Compter nbre occurence pour chaque métier
    for idx, role in enumerate(roles):
        df_role = df_sampled_1[df_sampled_1['Current_role'] == role]  # comptage par métiers 

# Compter nbre occurence de niveaux de formation pour chaques métiers
        data_counts = df_role['EducationLevel'].value_counts().reset_index() 
        data_counts.columns = ['EducationLevel', 'Count']  # renommer les cols après comptage
        data_counts['Count'] = data_counts['Count'].astype(int)  

# Liste des couleurs choisies pour les niveaux de formation
        colors = [color_map.get(level, '#cccccc') for level in data_counts['EducationLevel']]

# Créa treemap pour chaque modalité
        treemap = go.Treemap(
            labels=data_counts['EducationLevel'],  # labels 
            parents=[""] * len(data_counts),  # aucune hiérarchie dans les niveaux de formations 
            values=data_counts['Count'],  # taille des segments en fonction des quantités
            marker=dict(colors=colors),  # couleurs segments
            textinfo="label+percent entry",  # affichage labels et pourcentage
            textfont=dict(family="Arial", size=14, weight="bold"))  #  labels en gras       

# Position les treemaps dans la figure
        row, col = positions[idx]  #  position du sous-graphe (ligne et colonne)
        fig.add_trace(treemap, row=row, col=col)  # insertion treemap à l'endroit du dessus

# Mettre à jour la mise en page du graphique
    fig.update_layout(
        height=650,  # hauteur figure
        width=1500,  # largeur figure
        title_text="Répartition des niveaux de formations par métiers",  # titre générale
        title_x=0.15,  # position horizontalement du titre 
        title_y=0.95,  # position verticale du titre 
        title_font=dict(size=22),  # taille  du titre
        font=dict(size=20),  # taille  des textes 
        margin=dict(t=100, l=20, r=20, b=20),  # ajuster les marges 
        showlegend=False)
        
    st.plotly_chart(fig) 

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
## GRAPH REPARTITION DES AGES DES SONDES

    # compte nbre de personnes par poste et tranche d'âge
    df_grouped = df_sampled.groupby(['Current_role', 'Age']).size().reset_index(name='Count')

    # Ordonner les ages dans le sens croissant
    ages = ['18-29', '30-44', '45-59', '60+']
    colors = {
        '18-29': '#A1C9E3',  
        '30-44': '#82D66E',  
        '45-59': '#6A8D9A',  
        '60+': '#FFB966' }    

    bars = []

    for age in ages:
        df_age = df_grouped[df_grouped['Age'] == age]
        bars.append(go.Bar(
            y=df_age['Current_role'],
            x=df_age['Count'],
            name=age,
            orientation='h',  
            marker=dict(color=colors[age]),
            # Supprimer les valeurs dans les barres
            textposition='none')) # retirer les vals des barres à l'intérieur


    fig = go.Figure(data=bars)

    # Gestion de la figure
    fig.update_layout(
        barmode='group',
        title='Répartition moyenne des âges par postes occupés',
        title_font_size=21,
        title_x=0.1,
        height=600,
        width=1200,  
        legend_title_text='Tranches d’âge',
        legend_font_size=18,
        legend_title_font_size=20,
        legend=dict(
            x=1.05,  
            xanchor='left',  # légende à gauche
            y=0.5,  
            yanchor='middle'),  
        margin=dict(l=120, r=40, t=80, b=60),
        font=dict(size=18))
  
    # Axe des y
    fig.update_yaxes(
        title=None,
        tickfont_size=18,  
        tickfont_color="black",   
        categoryorder='category descending')  # ordre affichage catégories 

    # Axe des x
    fig.update_xaxes(
        tickfont_size=10,  
        tickfont_color="black",  
        tickfont_weight="bold") 

    st.plotly_chart(fig)




### PAGE 3 MODELISATION ET AUTOMATISATION SUR DATASET PREDICTIF
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

if page == pages[ 2 ] : 
    st.markdown(
    "<h3 style='text-align:center; font-size: 40px;color: #18009e; font-style: italic;'>Modélisations prédictives</h3>",
    unsafe_allow_html=True)
    st.write("")
    st.write("")

    st.write('##### CORRESPONDANCE CLASSES / METIERS')
    correspondance={'Classe n° 0':'Data Scientist',
                            'Classe n° 1':'Data Analyst',
                            'Classe n°2':'Software Engineer',
                            'Classe n°3':'Research Scientist'}
    st.image("correspondance_classes.PNG")

    class_names=['Data Scientist','Data Analyst',
                    'Software Engineer','Research Scientist']
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")


# MISE EN PLACE ENTRAINEMENT DES MODELES

# Séparation des features et de la cible
    feats = df.drop('Current_role', axis=1)
    target = df['Current_role']

# Séparation Train / Test 20%
    X_train,X_test,y_train,y_test=train_test_split(feats, target, test_size=0.2, random_state=42)

# Sépa vars nums et catés
    num_cols = X_train.select_dtypes(include=['int64', 'float64'])
    cat_cols = X_train.select_dtypes(include=['object'])

# Entrainement vars nums
    num_train=X_train.select_dtypes(include='int64')
    num_test=X_test.select_dtypes(include='int64')

# Entrainement vars catés
    cat_train=X_train.select_dtypes(include='object')
    cat_test=X_test.select_dtypes(include='object')

# encodage de target
    label=LabelEncoder()
    y_train=label.fit_transform(y_train)
    y_test=label.transform(y_test)

# encodage feats nums
    scaler=StandardScaler()
    num_train=scaler.fit_transform(num_train)
    num_test=scaler.transform(num_test)

# encodage feats catés
    cat_train=pd.get_dummies(cat_train)
    cat_test=pd.get_dummies(cat_test)

# Alignement des cols (pour éviter ttes erreurs de taille entre les datasets train et test)
    cat_train, cat_test = cat_train.align(cat_test, join='left', axis=1, fill_value=0)

# reconstitution des datasets encodé
    X_train=np.concatenate([num_train,cat_train],axis=1)
    X_test=np.concatenate([num_test,cat_test],axis=1)


# CREA DES LISTES DE MODELES SCORES 
    model_name_list = ['RandomForestClassifier', 'LogisticRegression', 'KNeighborsClassifier', 'DecisionTreeClassifier']
    metric_choice = ['Accuracy', 'Matrice de confusion', 'Rapport de classification']
    class_names = ["Classe 0", "Classe 1","Classe 2", "Classe 3"]  

# MISE EN PLACE SELECTBOX MODELES ET HYPERPARAMS
# Affichage titre choix du modèle
    st.sidebar.subheader('Choix du modèle')
    model_select = st.sidebar.selectbox("Modèle choisi", model_name_list)
    metric_select= st.sidebar.selectbox('Métrique choisi',metric_choice)

# Affichage titre choix du métrique 
    st.sidebar.subheader("Hyperparamètres du modèle")
    params = {}

    if model_select == 'RandomForestClassifier':
        params['n_estimators'] = st.sidebar.slider('n_estimators', 100, 1000, 300, step=50)
        params['max_depth'] = st.sidebar.slider('max_depth', 1, 50, 10)
    elif model_select == 'LogisticRegression':
        params['C'] = st.sidebar.slider('C (régularisation)', 0.01, 10.0, 1.0, step=0.1)
        params['max_iter'] = st.sidebar.slider('max_iter', 100, 1000, 300, step=50)
    elif model_select == 'DecisionTreeClassifier':
        params['max_depth'] = st.sidebar.slider('max_depth', 1, 50, 5)
        params['min_samples_split'] = st.sidebar.slider('min_samples_split', 2, 20, 4)
    elif model_select == 'KNeighborsClassifier':
        params['n_neighbors'] = st.sidebar.slider('n_neighbors', 1, 20, 7)
        params['metric'] = st.sidebar.radio('Distance metric', ('euclidean', 'manhattan', 'minkowski'))

# Créa f° d'affichage des modèles avec leurs hyperparams
    def create_model(name, params):
        if name == 'RandomForestClassifier':
            return RandomForestClassifier(n_estimators=params['n_estimators'],
                                        max_depth=params['max_depth'],
                                        random_state=42)
        elif name == 'LogisticRegression':
            return LogisticRegression(C=params['C'], max_iter=params['max_iter'])
        elif name == 'DecisionTreeClassifier':
            return DecisionTreeClassifier(max_depth=params['max_depth'],
                                        min_samples_split=params['min_samples_split'])
        elif name == 'KNeighborsClassifier':
            return KNeighborsClassifier(n_neighbors=params['n_neighbors'],
                                        metric=params['metric'])
        

# Créa f° de hachage des hyperparams (pour bien personnaliser les retours de résultats, sinon résults tjrs les mms)
    import hashlib

    def get_model_filename(model_name, params):
        os.makedirs("models", exist_ok=True)
        param_str = str(sorted(params.items()))
        hash_str = hashlib.md5(param_str.encode()).hexdigest()
        return f"models/{model_name}_{hash_str}.joblib"

    def load_or_train_model(model_name, params, X_train, y_train):
        model_path = get_model_filename(model_name, params)

        if os.path.exists(model_path):
            model = joblib.load(model_path)
        else:
            model = create_model(model_name, params)
            model.fit(X_train, y_train)
            joblib.dump(model, model_path)
        return model


# Créa f° de sauvegarde des modèles dans un répertoire "models"  
    def save_model(model, model_name, params):
        os.makedirs("models", exist_ok=True)
        param_str = str(sorted(params.items()))
        hash_str = hashlib.md5(param_str.encode()).hexdigest()
        joblib.dump(model, f"models/{model_name}_{hash_str}.joblib", compress=3)


# Créa f° de sauvegarde des matrices de confusion dans un répertoire "images"  
    def save_matrix(y_true, y_pred, model_name, params, class_names):
        os.makedirs("images", exist_ok=True)
        param_str = str(sorted(params.items()))
        hash_str = hashlib.md5(param_str.encode()).hexdigest()
        cm = confusion_matrix(y_true, y_pred)
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                    xticklabels=class_names, yticklabels=class_names)
        plt.title(f"Matrice de confusion - {model_name}")
        plt.xlabel("Prédictions")
        plt.ylabel("Réalité")
        plt.tight_layout()
        plt.savefig(f"images/{model_name}_{hash_str}_confusion_matrix.png")
        plt.close()

# Créa f° de sauvegarde des scores dans un répertoire "scores"  
    def save_scores(scores, model_name, params, folder="metrics"):
        os.makedirs(folder, exist_ok=True)
        param_str = str(sorted(params.items()))
        hash_str = hashlib.md5(param_str.encode()).hexdigest()
        file_path = os.path.join(folder, f"{model_name}_{hash_str}_scores.joblib")
        joblib.dump(scores, file_path)
        print(f"Scores sauvegardés dans : {file_path}")

# Entraînement du modele lorsque bouton est cliqué
    if st.sidebar.button("Entraîner le modèle"):
        with st.spinner("Modèle en cours d'entraînement..."):
            model = load_or_train_model(model_select, params, X_train, y_train)
            y_pred = model.predict(X_test)

# Sauvegarde des modèles
            save_model(model, model_select, params)
          
            save_matrix(y_test, y_pred, model_select, params, class_names)
# Calcul des scores           
            scores = {
                "Accuracy": accuracy_score(y_test, y_pred),
                "Classification report": classification_report(y_test, y_pred, target_names=class_names, output_dict=True),
                "Confusion matrix": confusion_matrix(y_test, y_pred)}
# Sauvegarde des scores             
            save_scores(scores, model_select, params)

# Affichage dynamique selon la métrique choisie
        if metric_select == 'Accuracy':
            accuracy = scores['Accuracy']
            st.write("**ACCURACY** = Mesure de l'exactitude globale des prédictions d'un modèle en calculant le rapport entre les échantillons correctement classés et le nombre total d'échantillons.")
            st.markdown(f"""
                <h2 style='text-align: left; color: green; font-size: 25px;'>
                {accuracy:.4f}
                </h2>""", unsafe_allow_html=True)

        elif metric_select == 'Matrice de confusion':
            st.subheader("_Matrice de confusion_")
            st.write("La matrice de confusion est un outil de mesure de la performance des modèles de classification. Elle résume ici de manière graphique les valeurs absolues des données prédictives et réelles")
            st.write(" ")
            st.write(" ")   
            cm = scores["Confusion matrix"]
            fig, ax = plt.subplots(figsize=(5, 3))
            sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                        xticklabels=class_names, yticklabels=class_names,
                        annot_kws={"fontsize": 8})
            ax.tick_params(axis='both', labelsize=5)
            plt.xlabel("Prédiction", color="red", fontsize=10)
            plt.ylabel("Réalité", color="red", fontsize=10)
            st.pyplot(fig)

        elif metric_select == 'Rapport de classification':
            st.subheader("_Rapport de classification_")
            st.write(" ")
            st.write(" ")  
            st.markdown("""
                Le **rapport de classification** est un outil utilisé dans l'apprentissage automatique pour évaluer les performances d'un modèle de classification.  
                Il présente les métriques suivantes pour chaque classe :
                - **Recall** : Taux de vrais positifs (sensibilité)
                - **Precision** : Précision des prédictions positives
                - **F1-score** : Moyenne harmonique de la précision et du rappel
                - **Support** : Nombre réel d'échantillons par classe""")
            st.write(" ") 
            st.write(" ")     
            st.write(" ")    

# Transfo du rapport de classification en df
            report_dict = scores["Classification report"]
            df_report = pd.DataFrame(report_dict).transpose()

# Ne concerver que lignes des classes et accuracy et affichage          
            rows_to_keep = list(class_names) + ['accuracy']
            df_report_filtered = df_report[df_report.index.isin(rows_to_keep)]
            st.dataframe(df_report_filtered[['precision', 'recall', 'f1-score', 'support']])







