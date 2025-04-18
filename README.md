<p align="center">
   <img align="center" width="50%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/datajob_logo_rouge.PNG" />
</p>
<br>
<br>
<br>

## <ins> CONTEXT ET OBJECTIF </ins> ##
<br>
Dans le cadre de ma formation de Data Analyst (promotion 2024), un projet collaboratif nous a été proposé.

Souhaitant me reconvertir dans le domaine de la data, il m’a semblé naturel de m’orienter vers un sujet qui me tient particulièrement à cœur : **l’analyse et le profilage des métiers de la data science.**

La réalisation de ce rapport m’a ainsi permis d’explorer de manière plus concrète et technique ce secteur d’activité, et d’en apprécier toute la richesse ainsi que les perspectives qu’il offre.
<br>
<br>

L’objectif consiste à comprendre, à l’aide des données, les différents profils techniques qui composent aujourd’hui l’industrie de la Data. Plus précisément, il s’agit de mener une **analyse approfondie** des ***tâches réalisées*** ainsi que des ***outils utilisés*** pour chaque poste, dans le but d’identifier des ensembles de compétences et de technologies propres à chaque fonction.
<br>

Cette étude a ainsi une **double finalité** : 
- ***cartographier les métiers de la Data*** afin d’en saisir la diversité et la spécificité, présenté sous la forme d'un rapport Power BI
- ***construire un système de recommandation*** capable de suggérer, à un apprenant ou une personne en reconversion, le poste le plus en adéquation avec ses préférences et ses compétences, à travers la mise en place d'une application Streamlit.

Pour cela, nous nous sommes appuyés sur les données issues de **sondages Kaggle**, en nous concentrant sur 4 métiers spécifiques:
- Data Analyst
- Data Scientits
- Sofware Engineer
- Research Scientits
<br>

Lors du travail initial en groupe, notre modèle prédictif avait atteint une accuracy de 0,42, un score améliorable.
**J’ai repris le projet en le consolidant**, notamment par ***l’ajout des sondages de 2018 et 2019*** et en ***affinant la sélection des variables***, ce qui m'a permis d'en ***accroitre les performances.***
<br>
<br>
<br>

## <ins> PRESENTATION DES DONNEES </ins> ##
<br>

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
              </li>Datarobot</li>
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
<br>
<br>


## <ins> METHODOLOGIE </ins> ##

- <ins>**Collection des données sur le site Kaggle**</ins>
  - Enquête 2018 ***42.56 MB***
  - Enquête 2019 ***22.21 MB*** chacune
  - Enquête 2020 ***25.48 MB***
  - Enquête 2021 ***35.2 MB***
  - Enquête 2022 ***25.93 MBo***
<br>

- <ins>**Data cleaning général sur GoogleColab**</ins>
  - Les datasets ont été nettoyés séparement, puis fusionnés
  - Gestion des colonnes, des modalités (renommer, uniformiser, modifications des types de données ...)
  - Suppressions des données non pertinentes à l’étude, les étudiants ainsi que les chômeurs 
  - Filtration 
  - Téléchargement des datasets sur Power BI
<br>

- <ins>**Data cleaning approfondi sur Power BI**</ins>
  - Uniformisations des noms de colonnes, des types, des données numériques
  - Création de tables de fait FACT, afin de lier les différentes tables entre elles
  - Création de visuels (cartes géographiques interractives, treemap, pie charts, …)
  - Mise en place de liens hypertextes, offres d'emploi, présentation des entreprises
  - Création de filtrations dynamiques, de widgets ...
 <br> 
