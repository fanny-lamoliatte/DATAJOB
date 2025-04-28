
METTRE ENVOI FORMAT PBIX



















<p align="center">
   <img align="center" width="50%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/datajob_logo_rouge.PNG" />
</p>
<br>
<br>


## <ins> CONTEXT </ins> ##
Dans le cadre de ma formation de Data Analyst (promotion 2024), un projet collaboratif nous a été proposé.

Souhaitant me reconvertir dans le domaine de la data, il m’a semblé naturel de m’orienter vers un sujet qui me tient particulièrement à cœur : **l’analyse et le profilage des métiers de la data science.**

La réalisation de ce rapport m’a ainsi permis d’explorer de manière plus concrète et technique ce secteur d’activité, et d’en apprécier toute la richesse ainsi que les perspectives qu’il offre.
<br>
<br>


## <ins> OBJECTIF </ins> ##
L’objectif consiste à comprendre, à l’aide des données, les différents profils techniques qui composent aujourd’hui l’industrie de la Data. Plus précisément, il s’agit de mener une **analyse approfondie** des ***tâches réalisées*** ainsi que des ***outils utilisés*** pour chaque poste, dans le but d’identifier des ensembles de compétences et de technologies propres à chaque fonction.
<br>

Cette étude a ainsi une **double finalité** : 
- ***cartographier les métiers de la Data*** afin d’en saisir la diversité et la spécificité, présenté sous la forme d'un rapport Power BI
- ***créer une application interactive*** permettant de visualiser et d’analyser les données liées aux métiers de la data, tels que Data Scientist ou Data Analyst. Elle intègre également des modèles prédictifs pour anticiper les tendances et l’évolution de ces rôles.

Pour cela, nous nous sommes appuyés sur les données issues de **sondages Kaggle**, en nous concentrant sur 4 métiers spécifiques:
- Data Analyst
- Data Scientits
- Sofware Engineer
- Research Scientits
<br>

Lors du travail initial en groupe, notre modèle prédictif avait atteint une accuracy de 0,42, un score améliorable.\
**J’ai repris le projet en le consolidant**, notamment par ***l’ajout des sondages de 2018 et 2019*** ainsi qu'en ***affinant la sélection des variables***, ce qui m'a permis d'en ***accroitre les performances.***
<br>
<br>


## <ins> PRESENTATION DES DONNEES </ins> ##

<h3><ins>Datasets</ins>
  <img src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/logo_kaggle.PNG?raw=true" width="60" style="vertical-align: middle; margin-left: 10px;" />
</h3>

- **Enquête Kaggle 2018** :  
  [https://www.kaggle.com/datasets/kaggle/kaggle-survey-2018?select=multipleChoiceResponses.csv](https://www.kaggle.com/datasets/kaggle/kaggle-survey-2018?select=multipleChoiceResponses.csv)

- **Enquête Kaggle 2019** :  
  [https://www.kaggle.com/datasets/paultimothymooney/public-dataset-for-2019-kaggle-survey-data](https://www.kaggle.com/datasets/paultimothymooney/public-dataset-for-2019-kaggle-survey-data)

- **Enquête Kaggle 2020** :  
  [https://www.kaggle.com/datasets/allyloreno/kagglesurvey2020?select=2020_kaggle_ds_and_ml_survey_responses_only.csv](https://www.kaggle.com/datasets/allyloreno/kagglesurvey2020?select=2020_kaggle_ds_and_ml_survey_responses_only.csv)

- **Enquête Kaggle 2021** :  
  [https://www.kaggle.com/datasets/dhirajkumar612/kagglesurvey2021responses)

- **Enquête Kaggle 2022** :  
  [https://www.kaggle.com/datasets/monikagarg02/kaggle-survey-2022-responses](https://www.kaggle.com/datasets/monikagarg02/kaggle-survey-2022-responses)
<br>

### **<ins>Présentation des variables**

<table>
   <tr> 
      <td>
          <p> <ins>Postes occupés<ins></p>
          <ul>
              <li>Data Analyst</li>
              <li>Data Scientist</li>
              <li>Software Engineer</li>
              <li>Research Scientist</li>
          </ul>
      </td>
      <td>
          <p> <ins>Tranches d'age<ins></p>
          <ul>
              <li>18 à 29 ans</li>
              <li>30 à 44 ans</li>
              <li>45 à 59 ans</li>
              <li>+ 60 ans</li>
          </ul>
      </td>
      <td>
          <p> <ins>Niveaux de formation<ins></p>
          <ul>
              <li>Bachelor</li>
              <li>Master</li>
              <li>Doctoral</li>
          </ul>
      </td>
      <td>
          <p> <ins>Sexes<ins></p>
          <ul>
              <li>Male</li>
              <li>Female</li>
          </ul>
      </td>
   </tr>        
</table>
<br>



<table>
   <tr> 
      <td>
          <p> <ins>Langages de programmation<ins></p>
          <ul>
              <li>SQL</li>
              <li>Java</li>
              <li>R</li>
              <li>C</li>
          </ul>
      </td>
      <td>
          <p> <ins>Notebooks<ins></p> 
          <ul>
              <li>Kaggle</li>
              <li>GoogleColab</li>
              <li>Jupyter</li>
              <li>Azure</li>
          </ul>
      </td>
      <td>
          <p> <ins>Librairies de visualisations<ins></p>
          <ul>
              <li>Matplotlib</li>
              <li>Seaborn</li>
              <li>Plotly</li>
              <li>Ggplot</li>
          </ul>
      </td>
      <td>
          <p> <ins>Logiciels de reportings<ins></p>
          <ul/>
              <li>Tableau</li>
              <li>Power BI</li>
              <li>DataStudio</li>
              <li>QuickSight</li>
          </ul>
      </td>
   </tr>              
</table>
<p><strong><em>Langages en plus de Python (langage de base en programmation)</em></strong></p>
<br>
             
<table>
   <tr> 
      <td>
          <p> <ins>Algorithmes de Machine Learning<ins></p>
          <ul>
              <li>Méthodes de régression</li>
              <li>Méthodes de classification</li>
              <li>Arbres/Forêts de décisions</li>
              <li>Réseaux Neuronaux</li>
              <li>Gradient Boosting</li>
          </ul>
      </td>
      <td>
          <p> <ins>Plateformse de ML automatisé</ins><ins></p> 
          <ul>
              <li>GoogleCLoud</li>
              <li>Datarobot</li>
              <li>Sagemaker</li>
              <li>Azure</li>
              <li>H2O</li>
              <li>Databriks</li>
          </ul>
      </td>
      <td>
          <p> <ins>Environnements de développement<ins></p>
          <ul>
              <li>Jupyter</li>
              <li>RStudio</li>
              <li>VSCode</li>
              <li>PyCharm</li>
              <li>SublimText</li>
          </ul>
      </td>
      <td>
          <p> <ins>Outils d'analyse visuelle<ins></p>
          <ul>
              <li>Classification d'images</li>
              <li>Segmentation d'images</li>
              <li>Détection d'objets</li>
              <li>Images vidéo</li>
              <li>Réseaux neuronaux</li>
          </ul>
      </td>
   </tr>        
</table>
<br>


### **<ins>Extrait du dataset nettoyé</ins>**

<p align="center">
   <img align="center" width="90%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/Screen%20visuel%20dataset%20nettoy%C3%A9.PNG" />
</p>
<br>
<br>



## <ins> METHODOLOGIE </ins> ##

- <ins>**Collecte des données sur le site Kaggle**</ins>
  - Enquête 2018 ***42.56 MB***
  - Enquête 2019 ***22.21 MB*** 
  - Enquête 2020 ***25.48 MB***
  - Enquête 2021 ***35.2 MB***
  - Enquête 2022 ***25.93 MB***
<br>

- <ins>**Data cleaning général sur GoogleColab**</ins>
  - Les datasets ont été nettoyés séparement, puis fusionnés
  - Restriction du nombre de colonnes (350) de moitié par choix des compétences ciblées préalablement
  - Gestion des colonnes, des modalités (uniformisation, modifications des types, données numériques ...)
  - Filtration sur les 4 métiers qui nous interessent
  - Suppression des données non pertinentes à l’étude, les étudiants ainsi que les chômeurs
  - Regroupement des modalités, notamment sur la variable "Age" (de 11 à 4 valeurs)
  - Normalisation des données en vue de l'étude prédictive qui va suivre
  - Conception de visuels tests pour sélectionner les plus efficaces 
  - Téléchargement des datasets sur Power BI
<br>

- <ins>**Data cleaning approfondi sur Power BI**</ins>
  - Affinage de la gestion des noms de colonnes, des types, des données numériques ...
  - Création d'indicateurs d'évolution des compétences et outils (treemap, pie charts, …)
  - Mise en place de filtrations dynamiques sur les postes occupés, les années, les aptitudes ..., de widgets
 <br>
 <br>

## <ins> RAPPORT POWER BI</ins> ##

### **<ins>Présentation du jeu de données</ins>**
<p align="center">
   <img align="center" width="85%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/REPORT_PBI/SCREENS_PBI/Pr%C3%A9sentation_datasets.PNG" /> 
</p>
<br> 


### **<ins>Présentation d'une page de glossaire</ins>**
<p align="center">
   <img align="center" width="85%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/REPORT_PBI/SCREENS_PBI/Glossaire.PNG" /> 
</p>
<br> 


### **<ins>Présentation des compétences nécessaires à chaque métier</ins>**
<p align="center">
   <img align="center" width="85%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/REPORT_PBI/SCREENS_PBI/Skills.PNG" /> 
</p>
<br> 


### **<ins>Evolution des compétences métier dans le temps</ins>**
<p align="center">
   <img align="center" width="85%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/REPORT_PBI/SCREENS_PBI/Evolution_compt%C3%A9tences.PNG" /> 
</p>
<br> 
<br> 

## <ins> APPLICATION STREAMLIT </ins> ##

Ce projet propose une application interactive dédiée à l'exploration, la visualisation et la prédiction de données professionnelles des acteurs du monde de la data science. 
Elle permet une analyse en profondeur des rôles de chaque métier, de leurs outils ainsi que des compétences techniques nécessaires à chacun d’eux. 

Voici le lien de connection à mon application: http://170.39.216.234:8501
<br> 
<br> 

```
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
```

<p align="center">
   <img align="center" width="50%" src="https://github.com/fanny-lamoliatte/DATAJOB/raw/main/STREAMLIT_APP/STREAMLIT_SCREENS/Page%20pr%C3%A9sentation%20des%20donn%C3%A9es.PNG" /> 
</p>



```
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
```

<p align="center">
   <img align="center" width="50%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/STREAMLIT_APP/STREAMLIT_SCREENS/Page%20visualisation%20des%20donn%C3%A9es.PNG" /> 
</p>




```
# MISE EN PLACE ENTRAINEMENT DES MODELES
# Création des répertoires pour sauvegarder les modèles, images, et scores
    import os
    os.makedirs("models.joblib", exist_ok=True)
    os.makedirs("images.joblib", exist_ok=True)
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
```

<p align="center">
   <img align="center" width="50%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/STREAMLIT_APP/STREAMLIT_SCREENS/Page%20mod%C3%A9lisation%20des%20donn%C3%A9es.PNG" /> 
</p>



```
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
# Créa f° de sauvegarde des modèles entrainés pour éviter le recalcul des résultats == gain de temps affichage
    @st.cache_resource
    def train_model(_model, X_train, y_train): 
        _model.fit(X_train, y_train)
        return _model
# Entraînement du modele lorsque bouton est cliqué
    if st.sidebar.button("Entraîner le modèle"):
        with st.spinner("Modèle en cours d'entraînement..."):
            model = train_model(create_model(model_select, params), X_train, y_train)
            y_pred = model.predict(X_test)
            # Sauvegarde du modèle
            os.makedirs("models", exist_ok=True)
            joblib.dump(model, f"models/{model_select}.joblib",compress=3)
            # Sauvegarde matrice 
            def save_matrix(y_true, y_pred, model_name):
                cm = confusion_matrix(y_true, y_pred)
                plt.figure(figsize=(8, 6))
                sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                            xticklabels=class_names, yticklabels=class_names)
                plt.title(f"Matrice de confusion - {model_name}")
                plt.xlabel("Prédictions")
                plt.ylabel("Réalité")
                plt.tight_layout()
                os.makedirs("images", exist_ok=True)
                plt.savefig(f"images/{model_name}_confusion_matrix.png")
                plt.close()
            save_matrix(y_test, y_pred, model_select)
            # Affichage des métriques
            if metric_select == 'Accuracy':
                accuracy = accuracy_score(y_test, y_pred)
                st.write("**ACCURACY** = Mesure de l'exactitude globale des prédictions d'un modèle en calculant le rapport entre les échantillons correctement classés et le nombre total d'échantillons.")
                st.markdown(f"""
                            <h2 style='text-align: left; color: green; font-size: 25px;'>
                            {accuracy:.4f}
                         </h2>""", unsafe_allow_html=True)
            elif metric_select == 'Matrice de confusion':
                st.subheader(" _Matrice de confusion_")
                st.write("La matrice de confusion est un outil de mesure de la performance des modèles de classification. Elle résume ici de manière graphique les valeurs absolues des données prédictives et réelles")
                st.write(" ")
                st.write(" ")              
                cm = confusion_matrix(y_test, y_pred)
                fig, ax = plt.subplots(figsize=(5, 3))
                sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                            xticklabels=class_names, yticklabels=class_names,
                            annot_kws={"fontsize": 8})
                ax.tick_params(axis='both', labelsize=5) 
                plt.xlabel("Prédiction",color="red",fontsize=10)
                plt.ylabel("Réalité",color="red",fontsize=10)
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
                # Transfo du rapport en df
                report_dict = classification_report(y_test, y_pred, target_names=class_names, output_dict=True)
                df_report = pd.DataFrame(report_dict).transpose()
                # Que lignes des classes et accuracy
                rows_to_keep = list(class_names) + ['accuracy']
                df_report_filtered = df_report[df_report.index.isin(rows_to_keep)]
                st.dataframe(df_report_filtered[['precision', 'recall', 'f1-score', 'support']])
```

<p align="center">
   <img align="center" width="30%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/STREAMLIT_APP/STREAMLIT_SCREENS/Console%20de%20mod%C3%A9lisation.PNG" /> 
</p>
<br> 
<br> 



## <ins> CONCLUSIONS </ins> ##

À travers cette étude, il apparaît clairement que les différents métiers de la data science partagent un **solide tronc commun de comptétences.**                           
<br>
Le **Data Analyst** explore et interprète les données afin de comprendre les tendances passées et d’éclairer les prises de décision. Il maîtrise les outils de ***traitement de données (SQL, Python)*** ainsi que les ***solutions de visualisation*** et de ***reporting*** comme ***Tableau ou Power BI.***

Le **Data Scientist**, quant à lui, transforme les données complexes en modèles exploitables. Spécialiste en ***modélisation prédictive*** et ***automatisation des décisions***, il dispose d’une ***solide expertise en machine learning***, en ***Python, R*** , de même qu’en ***outils cloud.***

Le **Software Engineer** conçoit des applications web et logicielles, tout en intégrant et déployant des modèles de machine learning en production. Il travaille principalement en ***Java, JavaScript*** et maitrise les ***outils DevOps pour l’automatisation des processus.***

Enfin, le **Research Scientist** conçoit des algorithmes complexes et exploite des flux de données en temps réel afin de répondre à des problématiques de recherche appliquée. C’est un expert en ***R, Python, C/C++*** de même qu’en ***calcul de haute performance.***
<br>
<br>

Notons aussi que le **monde de la data est en perpétuel mouvement.**

Afin de répondre aux demandes "clients" de plus en plus spécifiques, dans un but de ***simplification et valorisation des performances***, de nombreux ***outils, méthodes sont conçus et mis régulièrement à la disposition des codeurs, développeurs.***

D’où une faculté nécessaire des acteurs de la Data à l’***adaptation ainsi à la formation en continue.***
<br>
<br>

Enfin, il est important de relever une **spécialisation des métiers de data science**, dans un souci de ***gain de temps***, de ***valorisation*** et ***d'accessibilité aux données***, mais aussi et surtout afin de ***pousser de plus en plus loin le champ des possibles*** en totale adaptation aux nécessités entreprises, comportementales, sociétales.



