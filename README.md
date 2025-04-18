<p align="center">
   <img align="center" width="50%" src="https://github.com/fanny-lamoliatte/DATAJOB/blob/main/datajob_logo_rouge.PNG" />
</p>
<br>
<br>
<br>

## <ins> CONTEXT ET OBJECTIF </ins> ##
Dans le cadre de ma formation de Data Analyst (promotion 2024), un projet collaboratif nous a été proposé.

Souhaitant me reconvertir dans le domaine de la data, il m’a semblé naturel de m’orienter vers un sujet qui me tient particulièrement à cœur : l’analyse et le profilage des métiers du secteur de la data science.

L’objectif de ce projet est de comprendre, à l’aide des données, les différents profils techniques qui composent aujourd’hui l’industrie de la Data. Plus précisément, il s’agit de mener une analyse approfondie des tâches réalisées ainsi que des outils utilisés pour chaque poste, dans le but d’identifier des ensembles de compétences et de technologies propres à chaque fonction.

Cette étude a une finalité double : dans un premier temps, cartographier les métiers de la Data afin d’en saisir la diversité et la spécificité ; dans un second temps, construire un système de recommandation capable de suggérer, à un apprenant ou une personne en reconversion, le poste le plus en adéquation avec ses préférences et ses compétences.

Pour cela, nous nous sommes appuyés sur les données issues des sondages Kaggle, une référence dans le domaine. Ce rapport m’a ainsi permis d’explorer de manière plus concrète et technique un secteur qui m’attire particulièrement, et d’en appréhender la richesse et les perspectives.

Lors du travail initial en groupe, notre modèle prédictif avait atteint une accuracy de 0,42 — un score encore perfectible. J’ai ensuite repris ce projet en autonomie afin de le consolider : ajout des sondages Kaggle de 2018 et 2019, refonte des variables utilisées, enrichissement de la sélection des données… Ces optimisations m’ont permis d’accroître significativement la performance du modèle.
<br>
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
  [https://www.kaggle.com/datasets/shivijaiswal/kaggle-survey-2021](https://www.kaggle.com/datasets/shivijaiswal/kaggle-survey-2021)

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
          <p> <ins>Ages<ins></p>
          <ul>
              <li>18 à 29 ans</li>
              <li>30 à 44 ans</li>
              <li>15 à 99 ans</li>
              <li>+ 60 ans</li>
          </ul>
      </td>

