Project in the context of ETL Data Analysis self-learning 

<br>

## &#128295; Used tools
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![API](https://img.shields.io/badge/API-5BC0EB?style=for-the-badge)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Parallels](https://img.shields.io/badge/Parallels-E40046?style=for-the-badge&logo=parallels&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black) 

<br>

## [Subject : Build dashboard serving openweather-API's data]

<br>

## &#x1F4DD; Project graph

<br>

<p align="center">
  <img width="934" height="178" alt="Capture d’écran 2026-04-16 à 10 57 50" 
  src="https://github.com/user-attachments/assets/990fa1d8-357c-4897-8843-7f40347a17bd" />
</p>

<br>

## &#127919; Project steps

<br>

* Retrieve and transform data from the openweather API (`Python`).
* Import cleaned data into (`MySQL`) running on virtual machine (`parallels`).
* Build a dashboard (`Power Bi`) leading to relevant analysis concerning project's data. 

<br>

## &#128640; Project setup and activation

<br>

`Git clone` the project and get inside, to project root.

  ```bash
  git clone <repository-url> openweather-api-etl-dashboard
  cd openweather-api-etl-dashboard
  ```
<br>

Write your personal credentials and settings (which will be needed on the loading phase) into a `.env` file.

  ```bash
  touch .env # (for Mac)
  ```
  ```dotenv
  API_KEY=""
  MYSQL_HOST=""
  MYSQL_USER=""
  MYSQL_PASSWORD=""
  MYSQL_DB_NAME=""
  MYSQL_TABLE=""
  ```
<br>

Run the following file `main.py`, which will activate etl's files (extract-transform-load), in will load api's results into `MySQL`afer creating database and table.

  ``` bash
  python main.py
  ```
<br>

Open the `dashboard/.pbix` file.
<br>

Connect `Power Bi` to your `MySQL` database to use the dashboard.

