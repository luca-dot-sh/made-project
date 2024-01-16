![AI generated picture of bicycle theft in the rain](images/bt_banner.png)

# The impact of weather and bicycle traffic on bicycle theft in Berlin
Bicycle theft is a huge problem in Berlin, as it has one of [the highest rates of bike theft per inhabitant in Germany](https://www.wsm.eu/en/knowledge/bicycle-theft-in-germany/). This poses the question: How can one keep their bicycle safe in Berlin? Apart from a strong lock and a safe parking spot, there might be other influences on the probability of a bike being stolen, such as place or time of the day. A rather uncommon factor to think of is the weather, though it plays a huge part in mobility and transportation, especially for bicycles. In this project, three datasets from Berlin from 2022 are combined:
one containing bicycle theft data, one containing different weather metrics and one containing bicycle traffic counts, looking for anomalies and correlations in the data. The result can be found in [the report here](https://github.com/luca-dot-sh/made-project/blob/main/project/report.html).

# Overview over research questions
- RC1: Does more bicycle **traffic** lead to more bicycle **thefts**?
- RC2: Are there times where bikes, relative to traffic, are stolen more often?
- RC3: Do higher temperatures lead to more bicycle **traffic**?
- RC4: Do higher temperatures increase the risk of bicycle **theft**?
- RC5: Does more rain lead to less or more bicycle **traffic**?
- RC6: Does more rain increase the risk of bicycle **theft**?
- RC7: Are there significant differences in weather metrics at times when bikes were stolen?

# Data Pipeline
The /project/pipeline.sh script must be run from the root folder after installing the necessary packages:
```
pip install -r project/requirements.txt
bash project/pipeline.sh
```

# Tests
The /project/tests.sh script must be run from the root folder after installing the necessary packages:
```
pip install -r project/requirements.txt
bash project/tests.sh
```

# Archived data in /data
The data/archived_bicycle_theft_2022.csv is a archived version of the [Fahrraddiebstahl in Berlin](https://daten.berlin.de/datensaetze/fahrraddiebstahl-berlin) dataset, which unfortunately is currently no longer available, as it apperently only contains data from the last and current year. It was (and is) published under the [CC BY 3.0 DEED license](https://creativecommons.org/licenses/by/3.0/de/)

# Python Version
This project was tested with Python 3.10.

# License
This project is licensed under [Creative Commons Attribution 4.0 International](https://github.com/luca-dot-sh/made-project/blob/main/LICENSE).

# Banner
The banner was generated using DALL-E and cropped.