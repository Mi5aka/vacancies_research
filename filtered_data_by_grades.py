import pandas as pd
import plotly.graph_objects as go


def filter_data_by_grades():
    active_df = pd.read_csv('active_vacancies.csv')
    inactive_df = pd.read_csv('inactive_vacancies.csv')
    vacancies_df = active_df.append(inactive_df)
    vacancies_df['date'] = pd.to_datetime(vacancies_df['date'], errors='coerce')
    vacancies_df = vacancies_df[vacancies_df['date'] > '2018-12-31']
    intern_df = vacancies_df[vacancies_df['skills'].str.contains('Intern', na=False)]
    junior_df = vacancies_df[vacancies_df['skills'].str.contains('Junior', na=False)]
    middle_df = vacancies_df[vacancies_df['skills'].str.contains('Middle', na=False)]
    senior_df = vacancies_df[vacancies_df['skills'].str.contains('Senior', na=False)]
    lead_df = vacancies_df[vacancies_df['skills'].str.contains('Lead', na=False)]
    intern_data = intern_df.set_index('date').groupby(pd.Grouper(freq='M')).count()
    junior_data = junior_df.set_index('date').groupby(pd.Grouper(freq='M')).count()
    middle_data = middle_df.set_index('date').groupby(pd.Grouper(freq='M')).count()
    senior_data = senior_df.set_index('date').groupby(pd.Grouper(freq='M')).count()
    lead_data = lead_df.set_index('date').groupby(pd.Grouper(freq='M')).count()
    figure = go.Figure(
        data=[
            go.Bar(
                y=intern_data['title'],
                x=junior_data.reset_index()['date'],
                name='Intern'
            ),
            go.Bar(
                y=junior_data['title'],
                x=junior_data.reset_index()['date'],
                name='Junior'
            ),
            go.Bar(
                y=middle_data['title'],
                x=middle_data.reset_index()['date'],
                name='Middle'
            ),
            go.Bar(
                y=senior_data['title'],
                x=senior_data.reset_index()['date'],
                name='Senior'
            ),
            go.Bar(
                y=lead_data['title'],
                x=lead_data.reset_index()['date'],
                name='Lead'
            )
        ],
        layout_title_text="Количество вакансий на ресурсе за 2019-2020 года"
    )
    figure.show()


if __name__ == '__main__':
    filter_data_by_grades()
