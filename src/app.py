from flask import Flask, render_template, request
import pandas as pd
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# Carregar apenas 2% dos dados
df_ratings = pd.read_csv(r'C:\Users\peuja\OneDrive\Documentos\sis_recomenda\src\data\ratings.csv').sample(frac=0.02, random_state=42)
df_books = pd.read_csv(r'C:\Users\peuja\OneDrive\Documentos\sis_recomenda\src\data\books.csv')

# Inicializar o modelo KNN
knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
user_item_matrix = df_ratings.pivot_table(index='user_id', columns='ISBN', values='Book_Rating').fillna(0)
knn_model.fit(user_item_matrix)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    try:
        # Verificar se o campo 'book_rating' foi enviado no formulário
        if 'book_rating' not in request.form:
            return render_template('error.html', message="Book rating not provided")

        # Obter a classificação do livro do formulário
        rating = int(request.form['book_rating'])

        # Verificar se a classificação está dentro do intervalo válido
        if rating < 1 or rating > 10:
            return render_template('error.html', message="Invalid book rating")

        # Obter os 10 livros mais próximos com base na classificação inserida pelo usuário
        distances, indices = knn_model.kneighbors(user_item_matrix, n_neighbors=10+1)
        top_books_indices = indices[rating]  # Obter os índices dos livros recomendados com base na classificação
        top_books_info = df_books.iloc[top_books_indices]  # Obter as informações dos livros recomendados

        # Retornar as recomendações como um dicionário para a página output.html
        return render_template('output.html', recommendations=top_books_info.to_dict(orient='records'))

    except Exception as e:
        return render_template('error.html', message=str(e))


if __name__ == '__main__':
    app.run(debug=True)
