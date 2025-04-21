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
              <li>JResearch Scientist</li>
          </ul>
      </td>
      <td>
          <p> <ins>Tranches d'age<ins></p>
          <ul>
              <li>18 à 29 ans</li>
              <li>30 à 44 ans</li>
              <li>15 à 99 ans</li>
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
              <li>Bachelor</li>
              <li>Master</li>
              <li>Doctoral</li>
          </ul>
      </td>
      <td>
          <p> <ins>Logiciels de reportings<ins></p>
          <ul>
              <li>Matplotlib</li>
              <li>Seaborn</li>
              <li>Plotly</li>
              <li>Ggplot</li>
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
   <img align="center" width="150%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/Screen%20visuel%20dataset%20nettoy%C3%A9.PNG" />
</p>
<br>
<br>



## <ins> METHODOLOGIE </ins> ##

- <ins>**Collecte des données sur le site Kaggle**</ins>
  - Enquête 2018 ***42.56 MB***
  - Enquête 2019 ***22.21 MB*** 
  - Enquête 2020 ***25.48 MB***
  - Enquête 2021 ***35.2 MB***
  - Enquête 2022 ***25.93 MBo***
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


### **<ins>Présentation des compétences nédessaires à chaque métier</ins>**
<p align="center">
   <img align="center" width="85%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/REPORT_PBI/SCREENS_PBI/Skills.PNG" /> 
</p>
<br> 


### **<ins>Evolution des compétences nédessaires à chaque métier</ins>**
<p align="center">
   <img align="center" width="85%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/REPORT_PBI/SCREENS_PBI/Evolution_compt%C3%A9tences.PNG" /> 
</p>
<br> 
<br> 

## <ins> APPLICATION STREAMLIT </ins> ##

Ce projet propose une application interactive dédiée à l'exploration, la visualisation et la prédiction de données professionnelles des acteurs du monde de la data science. 
Elle permet une analyse en profondeurs des rôles de chaque métier, de leurs outils ainsi que des compétences techniques nécessaires à chacun d’eux. 


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





























<br> 
<br> 



## <ins> CONCLUSIONS </ins> ##

À travers cette étude, il apparaît clairement que les différents métiers de la data science partagent un **solide tronc commun de comptétences.**\                           
<br>
Le **Data Analyst** explore et interprète les données afin de comprendre les tendances passées et d’éclairer les prises de décision. Il maîtrise les outils de ***traitement de données (SQL, Python)*** ainsi que les ***solutions de visualisation*** et de ***reporting*** comme ***Tableau ou Power BI.***

Quant à lui, le **Data Scientist** transforme les données complexes en modèles exploitables. Spécialiste en ***modélisation prédictive*** et ***automatisation des décisions***, dispose d’une ***solide expertise en machine learning***, en ***Python, R*** , de même qu’en ***outils cloud.***

Le **Software Engineer** conçoit des applications web et logicielles, tout en intégrant et déployant des modèles de machine learning en production. Il travaille principalement en ***Java, JavaScript*** et maitrise les ***outils DevOps pour l’automatisation des processus.***

Enfin, le **Research Scientist** conçoit des algorithmes complexes et exploite des flux de données en temps réel afin de répondre à des problématiques de recherche appliquée. C’est un expert en ***R, Python, C/C++*** de même qu’en ***calcul de haute performance.***
