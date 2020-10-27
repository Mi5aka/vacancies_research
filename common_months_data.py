import pandas as pd
import plotly.graph_objects as go


def filter_data_by_months():
    active_df = pd.read_csv('active_vacancies.csv')
    inactive_df = pd.read_csv('inactive_vacancies.csv')
    vacancies_df = active_df.append(inactive_df)
    vacancies_df['date'] = pd.to_datetime(vacancies_df['date'], errors='coerce')
    data = vacancies_df.set_index('date').groupby(pd.Grouper(freq='M')).count()
    figure = go.Figure(
        data=[
            go.Bar(
                y=data['title'],
                x=data.reset_index()['date'],
                name='Intern'
            )
        ],
        layout_title_text="Количество вакансий на ресурсе за 2015-2020 года"
    )
    figure.show()


if __name__ == '__main__':
    filter_data_by_months()
